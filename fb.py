import undetected_chromedriver as uc
#from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
import openpyxl
import keyboard
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
options = Options()
driver = uc.Chrome(options=options)

email= "chadchadlun@yahoo.com.tw"
password= "sheep7111034607"

url= "https://www.facebook.com/welikea/posts/pfbid0exM9stvhUULVyEs9uNgLXVdhVY8G9JHvy7yK9PGqh8qH3vLyBobW5NTnnyaEeUYKl"
driver= uc.Chrome(use_subprocess= True)
driver.get(url)

time.sleep(3)
try:
    Email= driver.find_element(By.ID,"email")
    Password= driver.find_element(By.ID,"pass")
    Email.send_keys(email)
    Password.send_keys(password)
    Login= driver.find_element(By.ID,"loginbutton")
    driver.execute_script("arguments[0].click();", Login)
except:
    print("already login")

time.sleep(5)

ActionChains(driver).move_by_offset(600,500).click().perform()
time.sleep(4)
form= driver.find_elements(By.CSS_SELECTOR,"div.x1jx94hy.x12nagc")

span= form[-1].find_elements(By.CSS_SELECTOR,"span.x193iq5w")
#form_click= driver.find_element(By.CSS_SELECTOR,".x78zum5> span")


driver.execute_script("arguments[0].click();", span[0])
time.sleep(2)
List= driver.find_elements(By.CSS_SELECTOR,"div.xb57i2i.x1q594ok.x5lxg6s.x6ikm8r.x1ja2u2z > div")
find_all= List[3].find_elements(By.CSS_SELECTOR,"span")
driver.execute_script("arguments[0].click();",find_all[-1])

time.sleep(3)

new_comment= driver.find_elements(By.CLASS_NAME,"x1y1aw1k")

flag= 0
while flag!= 1:
    flag= 1
    time.sleep(5)
    more= driver.find_elements(By.CLASS_NAME,"x1i10hfl.xjbqb8w")
    for i in range(0,len(more)):
        print(more[i].text)
        if "檢視另" in more[i].text or "則回覆" in more[i].text or "顯示更多" in more[i].text:
            driver.execute_script("arguments[0].click();",more[i])
            time.sleep(1)
            flag= 0
            print("yes")
    more.clear

time.sleep(3)
comment= driver.find_elements(By.CSS_SELECTOR,"div.x1y1aw1k.xn6708d > div")

for i in range(0,len(comment)):
    if comment[i].text!= "作者":
        print(comment[i].text)

input()
