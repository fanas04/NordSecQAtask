import unittest
import page
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from locators import *


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://palaikykalu.lt/QA_Task.html")

    def test_correct_grid_size(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "Page title doesn't match."
        grid_size = main_page.random_correct_number()
        if grid_size >= '3' or grid_size <= '9':
            main_page.grid_size_4_x_4_perimeter()
            main_page.alert(grid_size)
            assert main_page.count_grid_boxes() == int(grid_size) * int(grid_size)
            print("Grid size given = ", grid_size, "Test passed")
        else:
            print("Given incorrect grid size")

    def test_incorrect_grid_size_numbers(self):
        main_page = page.MainPage(self.driver)
        grid_size = main_page.random_incorrect_number()
        main_page.grid_size_4_x_4_perimeter()
        obj = self.driver.switch_to.alert
        assert obj.text == main_page.dialog_notification(), "Wrong notification text"
        obj.send_keys(grid_size)
        obj.accept()
        assert obj.text == main_page.dialog_notification_second(), "Wrong notification text"
        obj.accept()
        print("Grid size given = ", grid_size, "Test passed")

    def test_incorrect_grid_size_symbols(self):
        main_page = page.MainPage(self.driver)
        grid_size = main_page.random_incorrect_symbol()
        main_page.grid_size_4_x_4_perimeter()
        try:
            obj = self.driver.switch_to.alert
            assert obj.text == main_page.dialog_notification(), "Wrong notification text"
            obj.send_keys(grid_size)
            obj.accept()
            print("Grid size given = ", grid_size, "Test passed")
        except NoSuchElementException:
            sleep(1)

    def test_all_button_clicked(self):
        main_page = page.MainPage(self.driver)
        main_page.grid_size_4_x_4_perimeter()
        main_page.alert('3')
        main_page.grid_size_3_x_3()
        assert self.driver.find_element(*GridIconLocators.Button1_1).get_attribute("active") == "true"
        assert self.driver.find_element(*GridIconLocators.Button1_2).get_attribute("active") == "true"
        assert self.driver.find_element(*GridIconLocators.Button1_3).get_attribute("active") == "true"
        assert self.driver.find_element(*GridIconLocators.Button2_1).get_attribute("active") == "true"
        assert self.driver.find_element(*GridIconLocators.Button2_2).get_attribute("active") == "true"
        assert self.driver.find_element(*GridIconLocators.Button2_3).get_attribute("active") == "true"
        assert self.driver.find_element(*GridIconLocators.Button3_1).get_attribute("active") == "true"
        assert self.driver.find_element(*GridIconLocators.Button3_2).get_attribute("active") == "true"
        assert self.driver.find_element(*GridIconLocators.Button3_3).get_attribute("active") == "true"
        print("All button at grid 3x3 was clicked")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

