# Codeforces Automated Registration

This app/program is to automated registration on Codeforces (an online coding competition website) using python and selenium package. Selenium is package or a framework is generally used to automate the web browser.
<img src='https://github.com/AyushKarir/Codeforces-registration-automated/blob/master/automate_reg.gif' style="display:table; margin-left: auto; margin-right: auto;">

## Steps

1.  Create a python (.py) file on VScode (or any IDE/Editor of choice) and from command prompt run command - pip install selenium
2.  After it is installed, download a web-driver for Firefox/Chrome according to your preference. Here, I have used Chrome Web driver which can be installed from [here](https://chromedriver.chromium.org/downloads).
    To check your chrome version, click on the vertical ellipsis icon in chrome (the right-most icon which on hover shows "Customize and control Google Chrome"). Then goto Help ---> About Google Chrome, it will show you the version.
3.  Extract the downloaded folder in the Downloads folder itself and get the path of the chromedriver executable file i.e, chromedriver.exe file (In Windows, it should be something like C:/.../Downloads/chromedriver_win32/chromedriver.exe
4.  Now get the URL of the [registration site of Codeforces](https://codeforces.com/register).
5.  In the .py file, import from selenium webdriver. Next, declare some variable to take input from user, like
    `handle = input('Enter handle-name: ')`.

6.  Set a driver variable value to `webdriver.Chrome("C:/.../Downloads/chromedriver_win32/chromedriver.exe")`.
7.  Fetch the url using `driver.get('url-of-registration-page')`, and go to the registration page.
8.  Now, hover over the input component of the website and right click to open Developer Options/Inspect (Shortcut --- Ctrl +Shift+i ). For the input element HTML tag, select a unique attribute, it could be id, name or an unrepeated class-name and send to it the input value take from the user, like `driver.find_element_by_name('handle').send_keys(handle)`
9.  Similar to the `.send_keys()` function, which is used to send the input value to the website input form field, to register you have to mimic click effect which can be using `.click()` function
10. Run the program.

Voila! We have automated the registration to Codeforces,
Confirm your mail and get on to solve some cool coding problems!

<img src='https://github.com/AyushKarir/Codeforces-registration-automated/blob/master/pic.PNG' style="display:table; margin-left: auto; margin-right: auto;">
