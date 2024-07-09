from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
# driver.get("https://google.com")
driver.get("https://kasirdemo.belajarqa.com")
# driver.quit()