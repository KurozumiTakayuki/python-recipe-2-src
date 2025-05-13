from selenium import webdriver
import time

# Google Chromeを起動
driver = webdriver.Chrome()

time.sleep(3)

# ブラウザを閉じる
driver.quit()
