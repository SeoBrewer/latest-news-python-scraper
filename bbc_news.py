import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_bbc_news():
    current_date = datetime.now().strftime("%d-%m-%y")
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = soup.find_all("div", {"class": "gs-c-promo-body"})
    print(f"Found {len(articles)} articles on BBC News")


    
    saved_links = set()

    try:
        with open("bbc_news.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                _, _, link = row
                saved_links.add(link)
    except FileNotFoundError:
        pass 

    new_articles_count = 0

    with open("bbc_news.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for story in articles:
            headline = story.find("h3", {"class": "gs-c-promo-heading__title"})
            link = story.find("a", {"class": "gs-c-promo-heading"})
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


