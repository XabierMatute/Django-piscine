import psycopg2
from django.http import HttpResponse
from django.conf import settings

def init(request):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS ex00_movies (
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