
from Package.scraper import start, dates, driver
from datetime import datetime
from Package.bot import main



#if __name__ == '__main__':
main()
while True:
    #driver()
    if str(datetime.now().time())[:-10] in dates:
        start()
    else:
        continue
