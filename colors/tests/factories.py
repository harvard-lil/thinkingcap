import factory
import random

from django.conf import settings
from django.template.defaultfilters import slugify

from colors.resources import create_colors
from colors.models import *


def setup_colors(**kwargs):
    create_colors(settings.COLOR_LIST)


def setup_color_case():
    randnum = random.randrange(Color.objects.count())
    case = ColorCaseFactory()
    case.colors.add(Color.objects.all()[randnum])
    case.save()
    return case


class ColorCaseFactory(factory.DjangoModelFactory):
    class Meta:
        model = ColorCase

    name = factory.Faker('sentence', nb_words=5)
    name_abbreviation = factory.Faker('sentence', nb_words=2)
    slug = factory.LazyAttribute(lambda o: '%s' % slugify(o.name))
    decision_date = factory.Faker("date_this_century", before_today=True, after_today=False)