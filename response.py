from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get('http://www.lemfix.com/')
driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[3]/a').click()
sleep(1.5)

driver.find_element_by_id('name').send_keys('pipiguai')

driver.find_element_by_id('pass').send_keys('sui1218')

sleep(1)

driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/form/div[3]/input').click()

sleep(1.5)

driver.get('http://www.lemfix.com/topic/5991483bc4d08bdf0d6d2637')

js = "document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(3)


a = '$(".CodeMirror-code pre").text("222222")'
driver.execute_script(a)