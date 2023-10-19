import schedule
import time
from elpais import scrape_elpais
from elmundo import scrape_elmundo
from bbc_news import scrape_bbc_news

# Define tu función de scraping aquí (el código de scraping que ya tienes)

# Programa la ejecución del script cada hora
schedule.every().minute.at(":05").do(scrape_elpais)
schedule.every().minute.at(":15").do(scrape_elmundo)  # Ejecución a los 15 minutos de cada hora
schedule.every().minute.at(":30").do(scrape_bbc_news)

while True:
    schedule.run_pending()
    time.sleep(1)
