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
        objects = ColorExcerpt.objects.filter(is_color=True)
        view_type = 'verified'
    else:
        objects = ColorExcerpt.objects.all()
        view_type = 'all'
    objects.select_related('case')
    objects.prefetch_related('colors')

    context = {'objects': list(objects), 'view_type': view_type}
    return render(request, "colors.html", context)


def check_color(request):
    """
    Serving up random colors for two checks each
    If color, create ColorCase instance, hide PendingColorCase
    If not color, do nothing, hide PendingColorCase
    If no consensus, do nothing, hide PendingColorCase
    """
    if request.method == 'POST':
        pending_case = ColorExcerpt.objects.get(id=request.POST.get('case_id'))
        is_color = "True" if request.POST.get('is_color') == 'color' else "False"

        pending_case.votes.append(is_color)
        if len(pending_case.votes) >= 2:
            # switch checking off
            pending_case.to_check = False

            if "False" not in pending_case.votes:
                # consensus reached! IS color
                pending_case.is_color = True
            else:
                # either consensus is not reached
                # or is not color
                # either way, mark as not color, hide
                pending_case.is_color = False

        pending_case.save()
        # check if any pending cases left

    # find all pending check
    all_pending = ColorExcerpt.objects.filter(to_check=True)
    # if none found, serve up everything
    if all_pending.count() == 0:
        return render(request, "colors.html", {
            'cases': list(ColorExcerpt.objects.all()),
        })

    # serve up random numbered excerpt
    randnum = random.randrange(all_pending.count())
    pending_case = all_pending[randnum]

    context = {'case': pending_case}

    return render(request, 'color_check.html', context)

