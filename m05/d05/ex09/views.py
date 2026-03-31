from django.db.models import Q
from django.http import HttpResponse
from django.utils.html import escape

from .models import People

def display(request):
    try:
        people = (
            People.objects.select_related("homeworld")
            .filter(
                Q(homeworld__climate__icontains="windy")
                | Q(homeworld__climate__icontains="moderately windy")
            )
            .order_by("name")
        )

        if not people.exists():
            return HttpResponse(f"No data available, please use the following command line before use:<br>python3 manage.py loaddata ex09/ex09_initial_data.json")

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>ex09 display</title>
            <style>
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Homeworld</th>
                        <th>Climate</th>
                    </tr>
                </thead>
                <tbody>
        """

        for person in people:
            homeworld_name = person.homeworld.name if person.homeworld else ""
            climate = person.homeworld.climate if person.homeworld else ""
            html += (
                "<tr>"
                f"<td>{escape(person.name)}</td>"
                f"<td>{escape(homeworld_name)}</td>"
                f"<td>{escape(climate or '')}</td>"
                "</tr>"
            )

        html += """
                </tbody>
            </table>
        </body>
        </html>
        """
        return HttpResponse(html)

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")