# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    roads_to_philosophy.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: xmatute- <xmatute-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/14 10:03:08 by xmatute-          #+#    #+#              #
#    Updated: 2024/11/14 11:24:47 by xmatute-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import requests
from bs4 import BeautifulSoup
import time



def get_first_link(soup):
    content = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content.find_all("p", recursive=False):
        for link in element.find_all("a", recursive=False):
            if link.get("href").startswith("/wiki/") and "Help:" not in link.get("href"):  # ignore invalid links and help pages
                return link.get("href")
    for ul in content.find_all("ul", recursive=False):
        for element in ul.find_all("li", recursive=False):
            for link in element.find_all("a", recursive=False):
                if link.get("href").startswith("/wiki/") and "Help:" not in link.get("href"):
                    return link.get("href")
    return None


def roads_to_philosophy(start_article):
    wikipedia_url = "https://en.wikipedia.org"
    roads = []
    article = f"/wiki/{start_article.replace(' ', '_')}"

    while True:
        url = wikipedia_url + article
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error: Failed to connect to {url}: {e}")
            return
        
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find(id="firstHeading").text
        print(title)
        
        if title in roads:
            print("It leads to an infinite loop!")
            return
        elif title.lower() == "philosophy":
            print(f"{len(roads) + 1} roads from {start_article} to philosophy")
            return
        
        roads.append(title)
        time.sleep(0.1)
        article = get_first_link(soup)
        if not article:
            print("It leads to a dead end!")
            return


def main():
    if len(sys.argv) != 2:
        print("Usage: python roads_to_philosophy.py '<search_term>'")
        sys.exit(1)
    
    roads_to_philosophy(sys.argv[1])


if __name__ == "__main__":
    main()
