from selenium.webdriver.common.by import By

def test(driver):
    RedirectToProfil = driver.find_element(By.XPATH, "//nav//div[2]//a[3]")
    RedirectToProfil.click()

    ModalBtnToUsun = driver.find_element(By.XPATH, "//button[@data-bs-toggle='modal']")
    ModalBtnToUsun.click()


    inputAccept = driver.find_element(By.ID, "akcept")
    inputAccept.send_keys("USUWAM")

    UsunUseraBTN = driver.find_element(By.ID, "usun_usera")
    UsunUseraBTN.click()