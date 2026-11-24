#from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get("https://web.app")

#input("Нажмите Enter в консоли, чтобы закрыть браузер...")
#driver.quit()


from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://telranedu.pages.dev/login")

#input("Press Enter to close the browser...")
driver.quit()
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://telranedu.pages.dev/login")
#https://demowebshop.tricentis.com/ for ds

input("Press Enter to close the browser...")
driver.quit()


#by tag name
div = driver.find_element(By.TAG_NAME,"div")
div_1 = driver.find_element(By.CSS_SELECTOR,"div")

h1 = driver.find_element(By.TAG_NAME,"h1")
h1_1 = driver.find_element(By.CSS_SELECTOR,"h1")

input = driver.find_element(By.TAG_NAME,"input")
input_1 = driver.find_element(By.CSS_SELECTOR,"input")

a_list = driver.find_elements(By.TAG_NAME,"a")
a_1 = driver.find_elements(By.CSS_SELECTOR,"a")
print(len(a_list))
