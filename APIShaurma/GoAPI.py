from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import undetected_chromedriver
import time

def GetData():
    online_players = ""
    try:
        driver = undetected_chromedriver.Chrome()
        driver.get("https://mgr.veroid.net/auth/login")
        time.sleep(10)
        driver.find_element(By.NAME, "username").send_keys("agat515@mail.ru")  
        time.sleep(3)
        driver.find_element(By.NAME, "password").send_keys("F5212711009!")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "#app > div.App___StyledDiv-sc-2l91w7-0.fnfeQw" +
        "> div > div > form > div > div.LoginFormContainer___StyledDiv3-sc-cyh04c-6.kOFLMG" + 
        "> div.LoginContainer___StyledDiv2-sc-qtrnpk-2.klHVdZ > button").click()
        time.sleep(5)
        driver.get("https://mgr.veroid.net/server/892c9e11/minecraft/players")
        time.sleep(5)
        online_players = driver.find_element(By.CSS_SELECTOR, "body > div.App___StyledDiv-sc-2l91w7-0.fnfeQw >" + 
        " div.Fade__Container-sc-1p0gm8n-0.hcgQjy > section > div.ContentContainer-sc-x3r2dw-" + 
        "0.PageContentBlock___StyledContentContainer-sc-kbxq2g-0.jyeSuy.HeRWk.fade-appear-don" + 
        "e.fade-enter-done > div > div.w-full.mb-8.flex.flex-col > div > h1.text-sm.text-neutral-400").text
        time.sleep(3)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        return online_players

print(GetData())