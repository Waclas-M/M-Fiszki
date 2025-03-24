from selenium.webdriver.common.by import By
import time
def test(driver,file_path,name):
    driver.get("http://mfiszki.pl")


    RedirectToStworz = driver.find_element(By.XPATH, "//nav//div[2]//a[1]")
    RedirectToStworz.click()

    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(file_path)

    time.sleep(1.5)
    save_tab = driver.find_element(By.ID, "Zapis_danych_wpisanych")
    save_tab.click()

    title = driver.find_element(By.ID, "id_title")
    title.send_keys(name)

    save_zestwaw = driver.find_element(By.ID, "make_button")
    save_zestwaw.click()