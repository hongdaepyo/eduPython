from selenium import webdriver

driver = webdriver.Chrome("c://Users/kaoni_dev2/chromedriver")

driver.get('https://asp.kaoni.com')

driver.find_element_by_id("TextUserID").send_keys('아이디')
driver.find_element_by_id("TextPassword").send_keys('비밀번호')

driver.find_element_by_id("LoginButton").click()

driver.switch_to.frame("mainFrame")
driver.switch_to.frame(0)
driver.find_element_by_id("disIN").click()