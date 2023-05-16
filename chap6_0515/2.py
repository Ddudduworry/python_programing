#pip install selenium
#pip install webdriver_manager

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


#options = webdriver.Chrome(options=Option)

#chrome_options = Option()
#chrome_options.add_experimental_option("detach", True)
#chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.naver.com")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(1)
newstitle = driver.find_element(By.XPATH,"/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div").text
print(newstitle)

driver.get("https://m.land.naver.com/search")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("우성꿈동산")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i").click()
time.sleep(1)
rent = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd").text
print(rent)

driver.get("https://finance.naver.com")
time.sleep(1)
subject = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th/a").text
print(subject)
subject = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[1]").text
print(subject)
subject = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]").text
print(subject)
subject = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[3]").text
print(subject)

lst = []
for i in range(3) :
    subject = driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[{i+1}]").text
    lst.append(subject)

print(lst)