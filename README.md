# Description

Python custom automation framework using unittest and Selenium Python bindings. For reporting, a custom version of Wai Yip Tung's HTMLTestRunner is used:
* https://github.com/airosu/HTMLTestRunner_dex

### Unittest:
* https://docs.python.org/3.6/library/unittest.html

### Selenium Python Bindings:
* Code: https://github.com/SeleniumHQ/selenium/wiki/Python-Bindings
* Documentation: https://selenium-python.readthedocs.io/

### Webdriver for chrome:
* http://chromedriver.chromium.org/

### Other useful libraries
* requests: https://realpython.com/python-requests/
* pyautogui: https://pyautogui.readthedocs.io/en/latest/

![pyautogui cheat sheet](/pyautogui_key_cheatsheet.png)

# Installation

* Install python. Version 3.6 or higher is required. pip will be included by default.
* Download preferred webdrivers for selenium (desktop / mobile). For the initial tests, chromedriver is recommended.
* Add the following folders in paths: /Python36-32, /Python36-32/Scripts, /webdrivers. See see below section for details.

#### Install required libraries:
```
pip install selenium
```

#### Install optional libraries:
```
pip install requests
pip install pyautogui

```

# Set-up guide

### For Windows
> Install python
* Version 3.6 or higher from: https://www.python.org/downloads/

> Install webdriver
* Get latest chromedriver from: http://chromedriver.chromium.org/
* Copy chromedriver.exe in a local folder (e.g. in C:\webdrivers)

> Add paths
* System Properties → Advanced → Environment Variables → System Variables → Path
* New path for python folder (e.g. C:\Users\........\Python36-32)
* New path for scripts folder (e.g. C:\Users\........\Python36-32\Scripts)
* New: path for webdrivers folder (e.g. C:\webdrivers)
* Restart PC
* In order to test if python is properly installed open CMD and type “python --version”

### For MAC
> Install homebrew:
* Open terminal
* Enter the following command into a single line of the terminal:
* /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
* Full guide can be found here, only points 1 and 2 are needed (http://osxdaily.com/2018/03/07/how-install-homebrew-mac-os/)

> Install python:
* https://docs.python.org/3/using/mac.html
* Using homebrew: https://www.chrisjmendez.com/2017/08/03/installing-multiple-versions-of-python-on-your-mac-using-homebrew/
* In order to check if python is correctly installed, in terminal type “python --version”

> Webdrivers
* Copy your webdriver (e.g. "chromedriver.exe") in a local folder
* One option is: “brew cask install chromedriver” (if this returns an error, you may need to input “brew tap homebrew/cask” before)
* Add the folder to path: https://www.kenst.com/2015/03/including-the-chromedriver-location-in-macos-system-path/

