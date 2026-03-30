from django.shortcuts import render

def index(request):
    numbers = range(50)
    noir = generate_shades((0, 0, 0))
    rouge = generate_shades((255, 0, 0))
    bleu = generate_shades((0, 0, 255))
    vert = generate_shades((0, 255, 0))
    columns = [
        {'name': 'noir', 'shades': noir},
        {'name': 'rouge', 'shades': rouge},
        {'name': 'bleu', 'shades': bleu},
        {'name': 'vert', 'shades': vert},
    ]
    return render(request, 'ex03/index.html', {'numbers': numbers, 'columns': columns})   


def generate_shades(base_rgb, count=50):
    shades = []
    for i in range(count):
        r = int(base_rgb[0] * (i / count))
        g = int(base_rgb[1] * (i / count))
        b = int(base_rgb[2] * (i / count))
        shades.append(f"rgb({r},{g},{b})")
    return shades   