import random
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class SearchTextElement(BasePage):
    page_title = 'Clickity Click Tech Skill Task'


class MainPage(BasePage):

    def is_title_matches(self):
        return SearchTextElement.page_title in self.driver.title

    def grid_size_3_x_3(self):
        wait = WebDriverWait(self.driver, 40)
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button1_1)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button1_2)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button1_3)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button2_1)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button2_2)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button2_3)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button3_1)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button3_2)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button3_3)))).click()

    def grid_size_4_x_4_perimeter(self):
        wait = WebDriverWait(self.driver, 40)
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button1_1)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button1_2)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button1_3)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button1_4)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button2_1)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button3_1)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button3_4)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button2_4)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button4_1)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button4_2)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button4_3)))).click()
        wait.until(EC.visibility_of((self.driver.find_element(*GridIconLocators.Button4_4)))).click()

    def alert(self, text):
        obj = self.driver.switch_to.alert
        obj.send_keys(text)
        obj.accept()

    def count_grid_boxes(self):
        value = len(self.driver.find_elements_by_css_selector("div.mainGrid > div.row > div.icon"))
        return int(value)

    @staticmethod
    def random_incorrect_symbol():
        randomInt = ['*', '%', '/', '+']
        grid_size = random.choice(randomInt)
        return grid_size

    @staticmethod
    def random_correct_number():
        randomInt = ['3', '4', '5', '6', '7', '8', '9']
        grid_size = random.choice(randomInt)
        return grid_size

    @staticmethod
    def random_incorrect_number():
        randomInt = ['1', '2', '10', '999999']
        grid_size = random.choice(randomInt)
        return grid_size

    @staticmethod
    def dialog_notification():
        text = "Done! Ready for the next try? Give me a size [3-9]:"
        return text

    @staticmethod
    def dialog_notification_second():
        text = "Not a good size!"
        return text


