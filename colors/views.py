import random

from django.shortcuts import render
from colors.models import *


def color_pixel(request):
    """
    Serving all colors unless asked for verified specifically
    TODO: This should be reversed in the future with more data
    but it's more fun to play with more colors right now
    """
    if request.GET.get('type', '') == 'verified':
        cases = ColorCase.objects.all()
        cases.prefetch_related('colors')
        view_type = 'verified'
    else:
        cases = PendingColorCase.objects.all()
        view_type = 'all'
    context = {'cases': list(cases), 'view_type': view_type}
    return render(request, "colors.html", context)


def check_color(request):
    """
    Serving up random colors for two checks each
    If color, create ColorCase instance, hide PendingColorCase
    If not color, do nothing, hide PendingColorCase
    If no consensus, do nothing, hide PendingColorCase
    """
    all_pending = PendingColorCase.objects.filter(hide=False)
    if all_pending.count() == 0:
        return render(request, "colors.html", {
            'cases': list(ColorCase.objects.all()),
        })

    randnum = random.randrange(all_pending.count())
    pending_case = all_pending[randnum]

    context = {'case': pending_case}

    if request.method == 'POST':
        pending_case = PendingColorCase.objects.get(id=request.POST.get('case_id'))
        is_color = "True" if request.POST.get('is_color') == 'color' else "False"

        pending_case.votes.append(is_color)
        if len(pending_case.votes) >= 2:
            if "False" not in pending_case.votes:
                # consensus reached! IS color
                pending_case.consensus = True
                case, created = ColorCase.objects.get_or_create(
                    slug=pending_case.slug,
                    name=pending_case.name,
                    name_abbreviation=pending_case.name_abbreviation,
                    url=pending_case.url,
                    decision_date=pending_case.decision_date
                )
                case.colors.add(pending_case.color)
                case.save()
            elif "True" not in pending_case.votes:
                # consensus reached! Is NOT color
                pending_case.consensus = True
            else:
                # no consensus reached
                pending_case.consensus = False

            pending_case.hide = True

        pending_case.save()

    return render(request, 'color_check.html', context)

