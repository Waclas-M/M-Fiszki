
from selenium.webdriver.common.by import By


def test(Nazwa,Passwd,Mail,driver):


    ### Testy

    RedirectToLogin = driver.find_element(By.XPATH, "(//nav//div//a)[last()]")
    RedirectToLogin.click()

    RedirectToRegister = driver.find_element(By.XPATH, "(//div//div//a)")
    RedirectToRegister.click()

    Username = driver.find_element(By.ID , "id_username")
    Username.send_keys(Nazwa)

    Email = driver.find_element(By.ID, "id_email")
    Email.send_keys(Mail)

    Password1 = driver.find_element(By.ID, "id_password1")
    Password1.send_keys(Passwd)

    Password2 = driver.find_element(By.ID, "id_password2")
    Password2.send_keys(Passwd)

    Submit = driver.find_element(By.XPATH, "(//button)" )
    Submit.click()




