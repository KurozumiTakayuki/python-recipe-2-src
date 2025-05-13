from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("file:///C:/・・・・/341.sample.html")

# id=new-idの要素が表示されるまで最大5秒待機する
element = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "new-id"))
)
print(element.text)

driver.quit()
