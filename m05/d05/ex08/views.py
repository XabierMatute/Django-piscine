import csv
import io
from pathlib import Path

import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.utils.html import escape


def _get_connection():
    return psycopg2.connect(
        dbname=settings.DATABASES["default"]["NAME"],
        user=settings.DATABASES["default"]["USER"],
        password=settings.DATABASES["default"]["PASSWORD"],
        host=settings.DATABASES["default"]["HOST"],
        port=settings.DATABASES["default"]["PORT"],
    )


def init(request):
    create_planets_sql = """
    CREATE TABLE IF NOT EXISTS ex08_planets (
        id SERIAL PRIMARY KEY,
        name VARCHAR(64) UNIQUE NOT NULL,
        climate VARCHAR,
        diameter INTEGER,
        orbital_period INTEGER,
        population BIGINT,
        rotation_period INTEGER,
        surface_water REAL,
        terrain VARCHAR(128)
    );
    """

    create_people_sql = """
    CREATE TABLE IF NOT EXISTS ex08_people (
        id SERIAL PRIMARY KEY,
        name VARCHAR(64) UNIQUE NOT NULL,
        birth_year VARCHAR(32),
        gender VARCHAR(32),
        eye_color VARCHAR(32),
        hair_color VARCHAR(32),
        height INTEGER,
        mass REAL,
        homeworld VARCHAR(64) REFERENCES ex08_planets(name)
    );
    """

    try:
        conn = _get_connection()
        cur = conn.cursor()
        cur.execute(create_planets_sql)
        cur.execute(create_people_sql)
        conn.commit()
        cur.close()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def populate(request):
    base_dir = Path(__file__).resolve().parent
    planets_csv = base_dir / "planets.csv"
    people_csv = base_dir / "people.csv"

    if not planets_csv.exists() or not people_csv.exists():
        return HttpResponse("Error: people.csv or planets.csv not found")

    results = []

    try:
        conn = _get_connection()
        cur = conn.cursor()

        try:
            with planets_csv.open() as f:
                cur.copy_expert(
                    """
                    COPY ex08_planets (name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
                    FROM STDIN WITH (FORMAT csv, DELIMITER E'\t', NULL 'NULL');
                    """,
                    f,
                )
            conn.commit()
            results.append("OK")
        except Exception as e:
            conn.rollback()
            results.append(f"Error: {str(e)}")

        try:
            with people_csv.open() as f:
                cur.copy_expert(
                    """
                    COPY ex08_people (name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
                    FROM STDIN WITH (FORMAT csv, DELIMITER E'\t', NULL 'NULL');
                    """,
                    f,
                )
            conn.commit()
            results.append("OK")
        except Exception as e:
            conn.rollback()
            results.append(f"Error: {str(e)}")

        cur.close()
        conn.close()
        return HttpResponse("<br>".join(results))

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def display(request):
    try:
        conn = _get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT pe.name, pe.homeworld, pl.climate
            FROM ex08_people pe
            JOIN ex08_planets pl ON pe.homeworld = pl.name
            WHERE pl.climate ILIKE %s OR pl.climate ILIKE %s
            ORDER BY pe.name ASC;
            """,
            ("%windy%", "%moderately windy%"),
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()

        if not rows:
            return HttpResponse("No data available")

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>ex08 display</title>
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

        for name, homeworld, climate in rows:
            html += (
                "<tr>"
                f"<td>{escape(name) if name is not None else ''}</td>"
                f"<td>{escape(homeworld) if homeworld is not None else ''}</td>"
                f"<td>{escape(climate) if climate is not None else ''}</td>"
                "</tr>"
            )

        html += """
                </tbody>
            </table>
        </body>
        </html>
        """
        return HttpResponse(html)

    except Exception:
        return HttpResponse("No data available")