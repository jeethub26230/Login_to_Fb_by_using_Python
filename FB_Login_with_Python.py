from selenium import webdriver
from getpass import getpass

usr = input("Enter your username :")
pwd = getpass("Enter your password :")

driver = webdriver.Chrome(executable_path = 'C:/Users/jeet2/Downloads/chromedriver.exe')
driver.get('https://www.facebook.com/')

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_btn = driver.find.element_by_id('loginbutton')

login_btn.click()

