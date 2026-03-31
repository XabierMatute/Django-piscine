from django.http import HttpResponse
from .models import Movies
from django.middleware.csrf import get_token
from django.utils.html import escape

def populate(request):
    movies = [
        Movies(episode_nb=1, title="The Phantom Menace", director="George Lucas", producer="Rick McCallum", release_date="1999-05-19"),
        Movies(episode_nb=2, title="Attack of the Clones", director="George Lucas", producer="Rick McCallum", release_date="2002-05-16"),
        Movies(episode_nb=3, title="Revenge of the Sith", director="George Lucas", producer="Rick McCallum", release_date="2005-05-19"),
        Movies(episode_nb=4, title="A New Hope", director="George Lucas", producer="Gary Kurtz, Rick McCallum", release_date="1977-05-25"),
        Movies(episode_nb=5, title="The Empire Strikes Back", director="Irvin Kershner", producer="Gary Kurtz, Rick McCallum", release_date="1980-05-17"),
        Movies(episode_nb=6, title="Return of the Jedi", director="Richard Marquand", producer="Howard G. Kazanjian, George Lucas, Rick McCallum", release_date="1983-05-25"),
        Movies(episode_nb=7, title="The Force Awakens", director="J. J. Abrams", producer="Kathleen Kennedy, J. J. Abrams, Bryan Burk", release_date="2015-12-11"),
    ]

    results = []
    for movie in movies:
        try:
            movie.save()
        except Exception as e:
            results.append(f"Error inserting {movie.title}: {str(e)}")
        else:
            results.append("OK")
    return HttpResponse("<br>".join(results))

def display(request):
    try:
        movies = Movies.objects.all()
        if not movies:
            return HttpResponse("No data available")
        
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                    font-weight: bold;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
            </style>
        </head>
        <body>
            <table>
                <thead>
                    <tr>
                        <th>Episode NB</th>
                        <th>Title</th>
                        <th>Director</th>
                        <th>Producer</th>
                        <th>Release Date</th>
                        <th>Opening Crawl</th>
                        <th>Created</th>
                        <th>Updated</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        for movie in movies:
            html_content += f"""
            <tr>
                <td>{movie.episode_nb}</td>
                <td>{movie.title}</td>
                <td>{movie.director}</td>
                <td>{movie.producer}</td>
                <td>{movie.release_date}</td>
                <td>{movie.opening_crawl or ''}</td>
                <td>{movie.created}</td>
                <td>{movie.updated}</td>
            </tr>
            """
        
        html_content += """
                </tbody>
            </table>
        </body>
        </html>
        """
        return HttpResponse(html_content)
        
    except Exception as e:
        return HttpResponse("No data available")

def remove(request):
    if request.method == "POST" and "remove" in request.POST:
        selected_title = request.POST.get("title")
        if selected_title:
            Movies.objects.filter(title=selected_title).delete()

    movies = Movies.objects.order_by("episode_nb")
    if not movies.exists():
        return HttpResponse("No data available")

    csrf_token = get_token(request)
    options = "".join(
        f'<option value="{movie.title}">{movie.title}</option>'
        for movie in movies
    )

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Remove movie</title>
    </head>
    <body>
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            <select name="title">
                {options}
            </select>
            <button type="submit" name="remove">remove</button>
        </form>
    </body>
    </html>
    """
    return HttpResponse(html)

def update(request):
    try:
        if request.method == "POST":
            selected_title = request.POST.get("title")
            opening_crawl = request.POST.get("opening_crawl")

            if not selected_title or opening_crawl is None:
                return HttpResponse("No data available")

            movie = Movies.objects.filter(title=selected_title).first()
            if movie is None:
                return HttpResponse("No data available")

            movie.opening_crawl = opening_crawl
            movie.save()

        movies = Movies.objects.order_by("episode_nb")
        if not movies.exists():
            return HttpResponse("No data available")

        csrf_token = get_token(request)
        options = "".join(
            f'<option value="{movie.title}">{movie.title}</option>'
            for movie in movies
        )

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Update movie opening crawl</title>
        </head>
        <body>
            <form method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                <label for="title">Movie:</label>
                <select id="title" name="title">
                    {options}
                </select>
                <br><br>
                <label for="opening_crawl">Opening crawl:</label>
                <textarea id="opening_crawl" name="opening_crawl" rows="8" cols="60"></textarea>
                <br><br>
                <button type="submit">Update</button>
            </form>
        </body>
        </html>
        """
        return HttpResponse(html)
    except Exception:
        return HttpResponse("No data available")