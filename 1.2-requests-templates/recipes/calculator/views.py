from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet_view(request):
    omlet = DATA["omlet"]
    servings = int(request.GET.get("servings", 1))
    new_omlet = {}
    for key, val in omlet.items():
        new_omlet.setdefault(key, val * servings)
    context = {
        'recipe': new_omlet
    }
    return render(request, 'calculator/index.html', context=context)


def pasta_view(request):
    pasta = DATA["pasta"]
    servings = int(request.GET.get("servings", 1))
    new_pasta = {}
    for key, val in pasta.items():
        new_pasta.setdefault(key,val*servings)
    context = {
        'recipe': new_pasta
    }
    return render(request, 'calculator/index.html', context=context)


def buter_view(request):
    buter = DATA["buter"]
    servings = int(request.GET.get("servings", 1))
    new_buter = {}
    for key, val in buter.items():
        new_buter.setdefault(key, val * servings)
    context = {
        'recipe': new_buter
    }
    return render(request, 'calculator/index.html', context=context)


def menu_view(request):
    menu = DATA
    context = {
        'recipe': menu
    }
    return render(request, 'calculator/index.html', context=context)


def dish_view(request, dish):
    dish = DATA[dish]
    servings = int(request.GET.get("servings", 1))
    new_dish = {}
    for key, val in dish.items():
        new_dish.setdefault(key, val * servings)
    context = {
        'recipe': new_dish
    }
    return render(request, 'calculator/index.html', context=context)