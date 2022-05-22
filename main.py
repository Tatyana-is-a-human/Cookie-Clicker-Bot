from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Have a great day! :D

def main():

    timeToBuy=time.time()+5
    timeToDie=time.time()+300
    timeInterval=6

    chrome_driver_path = "C:/Development/chromedriver.exe"
    ser = Service(chrome_driver_path)
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    driver.get("http://orteil.dashnet.org/experiments/cookie/")

    cookie = driver.find_element(By.ID, "cookie")

    purchases=driver.find_elements(By.CLASS_NAME, "grayed")
    purchases.pop()
    buyables=["buy"+x.text.split(" - ")[0] for x in purchases]

    inPlay=True
    while inPlay:

        for _ in range(5):
            cookie.click()

        now=time.time()
        if now>=timeToBuy:
            money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

            costsList=[]
            for x in buyables:
                costsList.append(int(driver.find_element(By.ID, x).text.split(" - ")[1].replace(",", "").split("\n")[0]))

            toBuyIndex=0
            for i in range(len(costsList)):
                if money>=costsList[i]:
                    toBuyIndex=i

            driver.find_element(By.ID, buyables[toBuyIndex]).click()

            timeToBuy=time.time()+timeInterval
            timeInterval+=0.45


        if now>=timeToDie:
            inPlay=False


    money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
    cps=driver.find_element(By.ID, "cps").text.split(" : ")[1].replace(",", "")
    driver.close()
    print(f"You got {money} cookies! and were baking {cps} cookies per second!")

if __name__=="__main__":
    main()
