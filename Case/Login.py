__author__ = 'JJLanMo'
from appium import webdriver
import unittest
import os


PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'efe5d82d '
        desired_caps['app'] = PATH(
            '../img/AazenWearCompanion-release-1.0.549.apk'
        )
        desired_caps['appPackage'] = 'com.aazen.companion'
        desired_caps['appActivity'] = '.main.LauncherActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def quit(self):
        self.driver.quit()

    def login1(self):
        el = self.driver.find_element_by_class_name()



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)