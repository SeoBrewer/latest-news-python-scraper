import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_elmundo():
    current_date = datetime.now().strftime("%d-%m-%y")

    url = "https://elmundo.es/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = soup.find_all("article")
    print(f"Found {len(articles)} articles on El Mundo")

    # Crear un conjunto de enlaces ya guardados
    saved_links = set()

    try:
        with open("elmundo_news.csv", "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Salta la primera fila (encabezado)
            for row in reader:
                _, _, link = row
                saved_links.add(link)
    except FileNotFoundError:
        pass  # El archivo no existe, lo crearemos más tarde

    new_articles_count = 0

    with open("elmundo_news.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for article in articles:
            headline = article.find("h2")
            link = article.find("a")
            if headline and link and "href" in link.attrs:
                article_link = link["href"]
                if article_link not in saved_links:
                    writer.writerow([current_date, headline.text.strip(), article_link])
                    saved_links.add(article_link)
                    new_articles_count += 1

    if new_articles_count > 0:
        print(f"Added {new_articles_count} new articles.")
    else:
        print("No new articles found.")


