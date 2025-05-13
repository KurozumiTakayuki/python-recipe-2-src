from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 要素が見つかるまで最大5秒待機するように設定
driver.implicitly_wait(5)

driver.get("file:///C:/・・・・/341.sample.html")

# 要素が見つかるまで、最大でimplicitly_waitで指定した5秒間待機
element = driver.find_element(By.ID, "new-id")

print(element.text)

driver.quit()
