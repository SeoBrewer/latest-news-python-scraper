import schedule
import time
from elpais import scrape_elpais
from elmundo import scrape_elmundo
from bbc_news import scrape_bbc_news




schedule.every().hour.at(":05").do(scrape_elpais)
schedule.every().hour.at(":15").do(scrape_elmundo)
schedule.every().hour.at(":30").do(scrape_bbc_news)

while True:
    schedule.run_pending()
    time.sleep(1)
