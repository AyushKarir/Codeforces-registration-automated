
#import webdriver from selenium package 
from selenium import webdriver 
#Take input from user on command line
handle = input('Enter handle: ')
email = input('Enter email: ')
password = input('Enter password: ')
passwordConfirm = input('enter password to confirm: ')

url = 'https://codeforces.com/register'

#fetch url 
driver = webdriver.Chrome("C:/.../Downloads/chromedriver_win32/chromedriver.exe") #path to chromedriver given to a driver variable
driver.get(url)
#send input values to input form field 
driver.find_element_by_name('handle').send_keys(handle)
driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_name('passwordConfirmation').send_keys(passwordConfirm)

#mimics clicking a button
driver.find_element_by_class_name('submit').click()