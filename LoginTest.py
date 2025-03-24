import time
from selenium.webdriver.common.by import By

def test(username,Passwd,driver):


    Username = driver.find_element(By.ID, "id_username")
    Username.send_keys(username)

    Password = driver.find_element(By.ID, "id_password")
    Password.send_keys(Passwd)

    Submit = driver.find_element(By.XPATH, "(//button)")
    Submit.click()






