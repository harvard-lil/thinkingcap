import os
import cgi
import requests
import json
import zipfile
import re

from django.conf import settings
from colors.models import *

base_dir = 'colors/tmp/'
if not os.path.exists(base_dir):
    os.mkdir(base_dir)


def create_API_settings():
    # TODO: rethink logic
    new_settings = APISettings.objects.create(limit=settings.API_LIMIT_COLORS)
    new_settings.save()
    return new_settings


def get_next_batch():
    """
    Ugly method, yuck.
    TODO: Fix writing gzipped data to disk and then decompressing

    This method makes a call to the api, gets back data, writes data to disk, decompresses
    finds if there are any colors in the text, creates ColorCase objects if colors exist
    removes all files it created
    """
    last_api_settings = APISettings.objects.last()
    if not last_api_settings:
        last_api_settings = create_API_settings()

    url = os.path.join(settings.API_BASE_URL, 'cases/?limit=%s&offset=%s&type=download' % (last_api_settings.limit, last_api_settings.offset))
    response = requests.get(url, headers={'AUTHORIZATION': 'Token {}'.format(settings.API_TOKEN_COLORS)})
    if response.status_code == 200:
        filename = cgi.parse_header(response.headers['Content-Disposition'])[1]['filename']
        gzipped_filename = base_dir + filename
        open(gzipped_filename, 'a+').close()
        with open(gzipped_filename, 'wb+') as f:
            f.write(response.content)

        zip_ref = zipfile.ZipFile(gzipped_filename, 'r')
        zip_ref.extractall(base_dir)
        zip_ref.close()
        iterate_and_create(base_dir)
        os.remove(gzipped_filename)

        # create new settings entry for debugging purposes
        APISettings.create_with_update(last_api_settings)
    else:
        print("Something happened, got %s status code:" % response.status_code, "reason:", response.reason)
        return


def iterate_and_create(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for name in files:
            if '.json' in name:
                json_filename = os.path.join(root, name)
                with open(json_filename) as fr:
                    json_obj = json.loads(fr.read())
                    create_pending(json_obj)
                os.remove(json_filename)


def xml_to_list(xml_str):
    # remove all tags
    text = re.sub('<[^<]+?>', '', xml_str)

    # remove any nonalphanumeric characters
    text = re.sub(r'\W+', ' ', text)
    # text = re.sub(r'(?!-)\W+', ' ', text)

    return text.lower().split(' ')


def create_pending(json_case):
    text = re.sub('<[^<]+?>', '', str(json_case['casebody']))
    split_text = text.split()
    colors_list = list(Color.objects.values_list('value', flat=True))
    for idx, entity in enumerate(split_text):
        if entity[0] == entity[0].upper():
            # if uppercase, if not following a period
            # most likely a name. continue
            if not idx == 0 and idx > 1 and not split_text[idx-2] == '.':
                continue
        word = re.sub(r'(?!-)\W+', ' ', entity).lower()

        if word in colors_list:
            case, created = Case.objects.get_or_create(
                slug=json_case['slug'],
                name=json_case['name'],
                name_abbreviation=json_case['name_abbreviation'],
                decision_date=json_case['decision_date'],
                url=json_case['url'],
            )
            pending_case = ColorExcerpt(
                color=Color.objects.get(value=word),
                original_word=entity,
                case=case,
            )

            # capture context before and after
            try:
                pending_case.context_before = ' '.join(split_text[idx-5:idx])
            except IndexError:
                pending_case.context_before = ' '.join(split_text[0:idx])
            try:
                pending_case.context_after = ' '.join(split_text[idx + 1::idx+5])
            except IndexError:
                pending_case.context_after = ' '.join(split_text[idx + 1::])
            # check each entity against a list of colors
            # if entity in colors, create
            pending_case.votes = []
            pending_case.save()


def create_if_colors_in_case(json_case):
    colors = list(Color.objects.values_list('value', flat=True))
    case_text_list = xml_to_list(str(json_case['casebody']))
    available_colors = set(case_text_list) & set(colors)
    if len(available_colors):
        case, created = ColorCase.objects.get_or_create(
            slug=json_case['slug'],
            name=json_case['name'],
            url=json_case['url'],
            name_abbreviation=json_case['name_abbreviation'],
            decision_date=json_case['decision_date'])

        for color in available_colors:
            case.colors.add(Color.objects.get(value=color))


def create_colors(color_list):
    for color_name in color_list:
        color, created = Color.objects.get_or_create(value=color_name.lower())
        color.save()
