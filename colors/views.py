from django.shortcuts import render
from colors.models import *


def color_pixel(request):
    cases = ColorCase.objects.all()
    cases.prefetch_related('colors')
    color_count = 0
    for case in cases:
        color_count += case.colors.count()
    context = {
        'cases': list(cases),
        'color_count': color_count
    }
    return render(request, "colors.html", context)

