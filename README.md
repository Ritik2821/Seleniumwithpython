# Selenium With Python Basic Operations

This repository contains examples of basic operations in Selenium WebDriver, such as interacting with checkboxes, radio buttons, links, and handling alert windows.

## Prerequisites

Before running the code, ensure that you have the following installed:

- Python (version 3.x)
- Selenium WebDriver (`pip install selenium`)
- ChromeDriver (Download and install from [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/))

## Selenium Operations

### 1. Open Website and Maximize Window

The following code snippet opens the URL and maximizes the browser window:

```python
from selenium import webdriver

# Initialize WebDriver and maximize the window
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
