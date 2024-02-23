from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def main():
    driveroptions = Options()
    driveroptions.binary_location = r"C:\Users\TAMANG\Downloads\Win_1216615_chrome-win\chrome-win\chrome.exe"

    driver = webdriver.Chrome(options = driveroptions)
    driver.get("https://www.iimjobs.com/search/IT-0-0-0-1.html")
    
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    results = soup.find("div", class_="listing")

    job_elems = results.find_all('div', class_=['col-lg-9 col-md-9 col-sm-8 container pdmobr5', 'col-lg-3 col-md-3 col-sm-4 pdlr0 mtb2 hidden-xs', 'pull-left col-lg-9new col-md-9new col-sm-9new pdlr0 pdmobl5 mtb2'])
    print(results)
    print("\n THIS IS THE THING \n")
    print(job_elems)
    time.sleep(5)

    print(len(job_elems))

    for jobs in job_elems:
        
        # title
        jobs.find('div', '')
main()