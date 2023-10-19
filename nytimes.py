#BROKEN
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


# Configure the Selenium browser
driver = webdriver.Chrome()
url = "https://www.nytimes.com/"
driver.get(url)

# Wait for the elements you need to appear
wait = WebDriverWait(driver, 10)
articles_loaded = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "article")))

# Get the updated content after JavaScript has loaded it

page_source = driver.page_source

# Close the browser
driver.quit()

# Analyze the HTML source code with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

articles = soup.find_all("article", class_="css-uuu4k4")
print(f"Found {len(articles)} articles on the page")

with open("nytimes_news.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Headline", "Link"])
    for article in articles:
        headline = article.find("h2", class_="css-1gb49n4")
        link = article.find("a")
        if headline and link and "href" in link.attrs:
            writer.writerow([headline.text.strip(), link["href"]])
