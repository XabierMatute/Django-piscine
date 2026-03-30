import psycopg2
from django.http import HttpResponse
from django.conf import settings

def init(request):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS ex02_movies (
        title VARCHAR(64) NOT NULL UNIQUE,
        episode_nb INTEGER PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL
    );
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
                    INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
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
            SELECT episode_nb, title, director, producer, release_date, opening_crawl
            FROM ex02_movies
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