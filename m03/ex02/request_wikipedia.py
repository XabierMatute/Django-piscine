# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    request_wikipedia.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/06 15:09:14 by xmatute-          #+#    #+#              #
#    Updated: 2024/11/14 09:49:49 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import sys
from dewiki import from_string


def get_wikipedia_content(title):
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "explaintext": True  # texto plano
    }
    
    response = requests.get(api_url, params=params)
    if response.status_code != 200:
        print("Error: Failed to connect to the Wikipedia API.")
        return None

    data = response.json()
    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()), None)

    if not page or "extract" not in page:
        print("Error: No information found for the given query.")
        return None
    
    return page["extract"]


def get_wikipedia_title(query):
    api_url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srinfo": "suggestion"
    }
    
    response = requests.get(api_url, params=params)
    if response.status_code != 200:
        print("Error: Failed to connect to the Wikipedia API.")
        return None

    data = response.json()
    results = data.get("query", {}).get("search", [])
    suggestion = data.get("query", {}).get("searchinfo", {}).get("suggestion", None)
    
    if not results:
        print(f"Error: No information found for {query}.")
        if suggestion:
            print(f"Did you mean: {suggestion}?")
            return get_wikipedia_title(suggestion)
        return None
    
    if len(results) > 0:
        return results[0]["title"]
    return None


def save_content_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(from_string(content))
        print(f"Request saved at {filename}")


def request_wikipedia(query):
    title = get_wikipedia_title(query)
    if not title:
        print("Error: No page found for the given query.")
        return
    print(f"Extracting content for {title}...")
    content = get_wikipedia_content(title)
    if content:
        print("Saving...")
        save_content_to_file(query.replace(" ", "_") + ".wiki", content)
    else:
        print("Error: Failed to extract content.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 request_wikipedia.py <query>")
        return
    request_wikipedia(sys.argv[1])


if __name__ == "__main__":
    main()
