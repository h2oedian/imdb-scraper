from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def imdb_collector():
  driver.get('https://www.imdb.com/chart/top/')
  movies = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'ipc-metadata-list-summary-item')))
  data=[]
  for movie in movies:
    title = movie.find_element(By.CSS_SELECTOR, 'h3').text
    year = movie.find_element(By.CSS_SELECTOR, "span.sc-86fea7d1-8.JTbpG.cli-title-metadata-item").text
    data.append({
      "Movie": title,
      "year": year
    })
    with open("imdb.json", "w", encoding="utf-8") as f:
     json.dump(data, f, ensure_ascii=False, indent=4)
  driver.quit()



imdb_collector()





    

    
