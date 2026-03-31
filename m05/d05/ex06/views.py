import psycopg2
from django.http import HttpResponse
from django.conf import settings
from django.middleware.csrf import get_token
from django.utils.html import escape

def init(request):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS ex06_movies (
        title VARCHAR(64) NOT NULL UNIQUE,
        episode_nb INTEGER PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """

    trigger_sql = """
    CREATE OR REPLACE FUNCTION update_changetimestamp_column()
    RETURNS TRIGGER AS $$
    BEGIN
    NEW.updated = now();
    NEW.created = OLD.created;
    RETURN NEW;
    END;
    $$ language 'plpgsql';
    
    DROP TRIGGER IF EXISTS update_films_changetimestamp ON ex06_movies;
    CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
    ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
    update_changetimestamp_column();
    """

    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        cur = conn.cursor()
        cur.execute(create_table_sql)
        conn.commit()
        cur.execute(trigger_sql)
        conn.commit()
        cur.close()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
    

def populate(request):
    movies_data = [
        (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
        (2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
        (3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
        (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
        (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
    ]

    results = []

    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        cur = conn.cursor()

        for ep_nb, title, director, producer, release_date in movies_data:
            try:
                cur.execute("""
                    INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s);
                """, (ep_nb, title, director, producer, release_date))
            except Exception as e:
                conn.rollback()
                results.append(f"Error inserting {title}: {str(e)}")
            else:
                conn.commit()
                results.append("OK")


        cur.close()
        conn.close()
        return HttpResponse("<br>".join(results))

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        cur = conn.cursor()

        cur.execute("""
            SELECT episode_nb, title, director, producer, release_date, opening_crawl, created, updated
            FROM ex06_movies
            ORDER BY episode_nb;
        """)
        
        movies = cur.fetchall()
        cur.close()
        conn.close()
        
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
                <td>{movie[0]}</td>
                <td>{movie[1]}</td>
                <td>{movie[2]}</td>
                <td>{movie[3]}</td>
                <td>{movie[4]}</td>
                <td>{movie[5] if movie[5] is not None else ''}</td>
                <td>{movie[6]}</td>
                <td>{movie[7]}</td>
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

def update(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        cur = conn.cursor()

        if request.method == "POST":
            movie_title = request.POST.get("movie")
            opening_crawl = request.POST.get("opening_crawl")

            if not movie_title or opening_crawl is None:
                cur.close()
                conn.close()
                return HttpResponse("No data available")

            cur.execute(
                """
                UPDATE ex06_movies
                SET opening_crawl = %s
                WHERE title = %s;
                """,
                (opening_crawl, movie_title),
            )

            if cur.rowcount != 1:
                conn.rollback()
                cur.close()
                conn.close()
                return HttpResponse("No data available")

            conn.commit()

        cur.execute("SELECT title FROM ex06_movies ORDER BY episode_nb;")
        movies = cur.fetchall()
        cur.close()
        conn.close()

        if not movies:
            return HttpResponse("No data available")

        csrf_token = get_token(request)
        options = "".join(
            f'<option value="{title}">{title}</option>'
            for (title,) in movies
        )

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Update opening crawl</title>
        </head>
        <body>
            <form method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                <label for="movie">Movie:</label>
                <select id="movie" name="movie">
                    {options}
                </select>
                <br><br>
                <label for="opening_crawl">Opening crawl:</label>
                <textarea id="opening_crawl" name="opening_crawl" rows="8" cols="60"></textarea>
                <br><br>
                <input type="submit" value="Update">
            </form>
        </body>
        </html>
        """
        return HttpResponse(html_content)

    except Exception:
        return HttpResponse("No data available")