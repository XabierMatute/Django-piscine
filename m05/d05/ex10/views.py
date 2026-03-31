from django.http import HttpResponse
from django.utils.html import escape
from django.middleware.csrf import get_token

from .models import Movies, People


def index(request):
    genders_qs = (
        People.objects.exclude(gender__isnull=True)
        .exclude(gender__exact="")
        .values_list("gender", flat=True)
        .distinct()
        .order_by("gender")
    )
    genders = list(genders_qs)

    results = []
    searched = False

    if request.method == "POST":
        searched = True
        min_date = request.POST.get("min_date")
        max_date = request.POST.get("max_date")
        min_diameter = request.POST.get("min_diameter")
        gender = request.POST.get("gender")

        if min_date and max_date and min_diameter and gender:
            try:
                min_diameter = int(min_diameter)

                results = (
                    Movies.objects.filter(
                        release_date__range=[min_date, max_date],
                        characters__gender=gender,
                        characters__homeworld__diameter__gte=min_diameter,
                    )
                    .values_list(
                        "title",
                        "characters__name",
                        "characters__gender",
                        "characters__homeworld__name",
                        "characters__homeworld__diameter",
                    )
                    .distinct()
                    .order_by("characters__name", "title")
                )
            except ValueError:
                results = []

    gender_options = "".join(
        f'<option value="{escape(g)}">{escape(g)}</option>' for g in genders
    )

    csrf_token = get_token(request)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>ex10</title>
    </head>
    <body>
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            <label for="min_date">Movies minimum release date :</label>
            <input type="date" id="min_date" name="min_date" required>
            <br><br>

            <label for="max_date">Movies maximum release date :</label>
            <input type="date" id="max_date" name="max_date" required>
            <br><br>

            <label for="min_diameter">Planet diameter greater than :</label>
            <input type="number" id="min_diameter" name="min_diameter" required>
            <br><br>

            <label for="gender">Character gender :</label>
            <select id="gender" name="gender" required>
                {gender_options}
            </select>
            <br><br>

            <button type="submit">Search</button>
        </form>
        <hr>
    """

    if searched:
        if results:
            for title, char_name, char_gender, world_name, world_diameter in results:
                html += (
                    f"{escape(title)} - {escape(char_name)} - {escape(char_gender)} - "
                    f"{escape(world_name)} - {world_diameter}<br>"
                )
        else:
            html += "Nothing corresponding to your research"

    html += """
    </body>
    </html>
    """

    return HttpResponse(html)