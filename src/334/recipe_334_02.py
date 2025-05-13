from selenium import webdriver

try:
    driver = webdriver.Chrome()
    # :
    # 何らかの処理
    # :
finally:
    driver.quit()
