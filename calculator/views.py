from django.core import paginator
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render

def get_omlet(request):
    num_portions = int(request.GET.get('servings', 1))
    context = {
        'omlet': {
            'яйца, шт': 2 * num_portions,
            'молоко, л': 0.1 * num_portions,
            'соль, ч.л.': 0.5 * num_portions,
            }
    }
    return render(request, 'calculator/index.html', context)


def get_pasta(request):
    num_portions = int(request.GET.get('servings', 1))
    context = {
        'pasta': {
            'макароны, г': 0.3 * num_portions,
            'сыр, г': 0.05 * num_portions,
            }
    }
    return render(request, 'calculator/index.html', context)


def get_buter(request):
    num_portions = int(request.GET.get('servings', 1))
    context = {
        'buter': {
            'хлеб, ломтик': 1 * num_portions,
            'колбаса, ломтик': 1 * num_portions,
            'сыр, ломтик': 1 * num_portions,
            'помидор, ломтик': 1 * num_portions,
            }
    }
    return render(request, 'calculator/index.html', context)
