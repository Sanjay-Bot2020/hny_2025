"""
Test

Test
"""

# string = "tomorrow is sankranti"
#
# conv_str = string.split(" ")
# print(conv_str)
# length = len(conv_str)
#
# output = conv_str[0].lower()
#
# def conv_camel(text):
#     return text[0].upper() + text[1:].lower()

# for i in range(1, length):
#     output = output + conv_camel(conv_str[i])
#
# print(output)
#

# x = 50000000
# for x in range(1, x):
#     cube = 0
#     temp = x
#     while (x > 0):
#         r =  x % 10
#         x = x // 10
#         cube = cube + (r*r*r)
#     if (cube == temp):
#         print(temp)

# import time
# from selenium import webdriver
# option = webdriver.ChromeOptions()
# option.add_argument("--incognito")
# # option.add_argument("--headless")
# driver = webdriver.Chrome(options=option)
# driver.maximize_window()
# time.sleep(10)

# import pytest
# class Test_1():
#
#     @pytest.mark.parametrize("Names, Ages", [("Sanjay", 44), ("Divya", 37)])
#     def test_method(self, Names, Ages):
#         print(Names, end=' ')
#         print(Ages)

# string = "zNeedN to count the numbers in the stringz"
#
# char_count = {}
#
# for char in string:
#     if char == ' ':
#         continue
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

# print(char_count)
# from datetime import date
# bd, bm, by = input("Enter your DOB in dd//mm/yyyy format").split("/")
# born = date(year=int(by), month=int(bm), day=int(bd))
# today = date.today()
#
# age = today - born
#
# age_in_years = age/365
#
# print(age_in_years)

#
# from hny_2025.Utilities.TestStatus import TestStatus
#
# class Passing_Result():
#     def __init__(self):
#         self.ts = TestStatus()
#
#     def first(self):
#         self.ts.mark("True", "Login Passed")
#
#     def second(self):
#         self.ts.mark("True", "Login Failed")
#
#     def third(self):
#         self.ts.mark("True", "Product page opened")
#
#     def fourth(self):
#         self.ts.mark_final("True", "logged out successfully")
#
# obj = Passing_Result()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()
# import unittest
#
# from hny_2025.Utilities.get_csv_data import read_csv_file
# from ddt import ddt, data, unpack
# import pytest
#
# @ddt
# # @pytest.mark.usefixtures("setup")
# class Test_data_driven_testing(unittest.TestCase):
#
#     @data(*read_csv_file("C:\\Users\\Sanjay Joshi\\workspace_python\\Jan2025\\hny_2025\\Utilities\\family.csv"))
#     @unpack
#     def test_data_driven_testing(self, name, age, sex):
#         print("Your name is %s Age is %s Sex is %s" %(name, age, sex))
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from hny_2025.Utilities.TestStatus import TestStatus
baseurl = "https://sarathi.parivahan.gov.in/sarathiservice/stateSelection.do"

_dropdown_select_state_name = "#stfNameId"

_button_complete_pending_appln_xpath = "//p[text()='Complete your Pending Application']"

_popup_close_css = "button[class='close popupclose']"
_textbox_appln_number_css = "#applNum"
_textbox_captcha_css = "#entcaptxt"
_date_dob_css = "#dateOfBirth"
_button_submit_css= "#submit"
_appl_number = 4363577524
_dob = "04-06-1980"

_label_current_status_xpath = "//legend[contains(text(),'Current Status')]"


driver = webdriver.Chrome()
driver.maximize_window()
obj = TestStatus(driver)
driver.get(baseurl)
# time.sleep(2)
obj.explicit_wait(5,1,"css", _dropdown_select_state_name)
select_state_dropdown = driver.find_element(By.CSS_SELECTOR, _dropdown_select_state_name)
select = Select(select_state_dropdown)
select.select_by_value("KA")

# time.sleep(10)
obj.explicit_wait(15,1,"css", _popup_close_css)
driver.find_element(By.CSS_SELECTOR, _popup_close_css).click()

# time.sleep(2)
obj.explicit_wait(15,1,"xpath", _button_complete_pending_appln_xpath)
driver.find_element(By.XPATH, _button_complete_pending_appln_xpath).click()

# time.sleep(6)
obj.explicit_wait(15,1,"css", _textbox_appln_number_css)
driver.find_element(By.CSS_SELECTOR, _textbox_appln_number_css).send_keys(_appl_number)
driver.find_element(By.CSS_SELECTOR, _date_dob_css).send_keys(_dob)
captcha = input("Enter Captcha")
driver.find_element(By.CSS_SELECTOR, _textbox_captcha_css).send_keys(captcha)
# time.sleep(3)
driver.find_element(By.CSS_SELECTOR, _button_submit_css).click()
# time.sleep(4)

# driver.execute_script("window.scrollBy(0,400);")
obj.explicit_wait(15,1,"xpath", _label_current_status_xpath)
current_status = driver.find_element(By.XPATH, _label_current_status_xpath)

driver.execute_script("arguments[0].scrollIntoView();", current_status)

time.sleep(10)
# test123456789,10,11,13,14,pb14
abc

123
sanjay

















