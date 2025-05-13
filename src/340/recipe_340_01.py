from selenium import webdriver

driver = webdriver.Chrome()

# https://gihyo.jp/に遷移
driver.get("https://gihyo.jp/")

# ページのスクリーンショットをカレントディレクトリに保存
driver.save_screenshot("myimage.png")

# ブラウザを閉じる
driver.quit()
