from selenium import webdriver

from random import randint

import unittest
import io
from unittest import TextTestRunner

from RegisterTest import test as Register_test
from LoginTest import test as Login_test
from StworzManualTest import test as ManualStworzTest
from StworzFileTest import test as FileStworzTest
from ZestawyManualTEST import test as ManualGameTest
from ZestawyFiszkiTest import test as FiszkiGameTest
from Raport import SendRaport
from ProfilUsunZestawTEST import test as UsunZestawTEST
from ProfilEdytujZestawTest import test as EdytujZestawTEST
from UsunUzytkownikaTEST import test as UsunUzytkownikaTEST

class TestWeb(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.implicitly_wait(5)
        cls.driver.get("http://mfiszki.pl")
        cls.liczba = randint(1, 100000)

        cls.erros = []

        cls.username = "TEST00" + str(cls.liczba)
        cls.Mail = f"{cls.username}@test.com"
        cls.passwd = "!QAZ2wsx#EDC"

        cls.zestaw1 = {'a': 'b', 'c': 'd'}
        cls.zestaw2 = {'Dog': 'pies', 'Smile': 'usmiech','Cup':'kubek','till':'kasa','cake':'ciasto'}
        cls.zestaw3 = {'Cat': 'Kot', 'Dog': 'Pies','Horse':'Koń'}

        cls.url1 = "A:/DjangoServerTestScrpit/Test.png"
        cls.url2 = "A:/DjangoServerTestScrpit/test.txt"

        cls.ZestawName1 = "Test1"
        cls.ZestawName2 = "Test2"
        cls.ZestawName3 = "Test3"

        cls.Zestawy = {
            cls.ZestawName1: cls.zestaw1,
            cls.ZestawName2: cls.zestaw2,
            cls.ZestawName3: cls.zestaw3,
        }

    @classmethod
    def tearDownClass(cls):
        # Wyślij raport
        SendRaport(cls.erros)
        cls.driver.quit()



    def test_01_Register(self):
        try:
            Register_test(self.username, self.passwd, self.Mail, self.driver)
        except Exception as e:
            self.driver.save_screenshot("errors_screen/screenshot_error_Register.png")
            self.erros.append("RegisterTEST\n" + str(e) + str(self.driver.current_url) +'\n')
            raise


    def test_02_login(self):
        try:
            Login_test(self.username, self.passwd, self.driver)
        except Exception as e:
            self.driver.save_screenshot("errors_screen/screenshot_error_Login.png")
            self.erros.append("LoginTEST\n" + str(e) + str(self.driver.current_url)+'\n')
            raise  # Rzuca błąd dalej, aby unittest oznaczył test jako nieuda



    def test_03_Stworz(self):
        try:
            ManualStworzTest(self.driver, self.Zestawy, self.ZestawName1)
            FileStworzTest(self.driver, self.url1, self.ZestawName2)
            FileStworzTest(self.driver, self.url2, self.ZestawName3)

        except Exception as e:
            self.driver.save_screenshot("errors_screen/screenshot_error_Stworz.png")
            self.erros.append("StworzTEST\n" + str(e) + str(self.driver.current_url)+'\n')
            raise  # Rzuca błąd dalej, aby unittest oznaczył test jako nieuda




    def test_04_Game(self):
        try:
            ManualGameTest(self.driver, self.Zestawy, self.ZestawName2)
            FiszkiGameTest(self.driver, self.Zestawy, self.ZestawName2)
        except Exception as e:
            self.driver.save_screenshot("errors_screen/screenshot_error_Game.png")
            self.erros.append("GameTEST\n" + str(e) + str(self.driver.current_url)+'\n')

            raise  # Rzuca błąd dalej, aby unittest oznaczył test jako nieuda

    def test_05_UsunZestaw(self):
        try:
            self.assertEqual(UsunZestawTEST(self.driver,self.Zestawy),2)
        except Exception as e:
            self.driver.save_screenshot("errors_screen/screenshot_error_UsunZestaw.png")
            self.erros.append("UsunZestawTEST\n" + str(e) + str(self.driver.current_url)+'\n')

            raise  # Rzuca błąd dalej, aby unittest oznaczył test jako nieuda

    def test_06_EdytujZestaw(self):
        try:
            EdytujZestawTEST(self.driver,self.Zestawy,self.ZestawName2)
            ManualGameTest(self.driver, self.Zestawy, self.ZestawName2)
        except Exception as e:
            self.driver.save_screenshot("errors_screen/screenshot_error_EdytujZestaw.png")
            self.erros.append("EdytujZestawTEST\n" + str(e) + str(self.driver.current_url)+'\n')

            raise  # Rzuca błąd dalej, aby unittest oznaczył test jako nieuda

    def test_07_UsunUzytkownika(self):
        try:
            UsunUzytkownikaTEST(self.driver)
            self.driver.get('https://mfiszki.pl/Logowanie/')
            Login_test(self.username, self.passwd, self.driver)
            self.assertEqual(self.driver.current_url,'https://mfiszki.pl/Logowanie/')

        except Exception as e:
            self.driver.save_screenshot("errors_screen/screenshot_error_UsunUzytkownika.png")
            self.erros.append("UsunUzytkownikaTEST\n" + str(e) + str(self.driver.current_url) + '\n')

            raise  # Rzuca błąd dalej, aby unittest oznaczył test jako nieuda


if __name__ == '__main__':
    unittest.main()