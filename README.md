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
```
### 2. Interact with Checkboxes
The script clicks on a checkbox using the ID locator.
```python
checkbutton = driver.find_element(By.ID, "checkBoxOption1")
checkbutton.click()
```

### 3. Interact with Radio Buttons
```python
radioButton = driver.find_element(By.XPATH, "//input[@value='radio2']")
radioButton.click()
```

### 4. Click a Link
The script clicks a link using the LINK_TEXT locator.

```python
driver.find_element(By.LINK_TEXT, "QA Meetup with Rahul Shetty @Bangalore - Limited Seats! Book Now!")
```
### 5. Dropdown Selection
The script selects an option from a dropdown using the ID locator and Select class.

```python
dropdown = driver.find_element(By.ID, "dropdown-class-example")
select = Select(dropdown)
select.select_by_visible_text("Option2")
```
### 6. Handle Alerts
The script triggers and handles an alert. It waits for the alert to appear, retrieves the alert's text, and accepts it.

```python
alertTextField = driver.find_element(By.NAME, "enter-name")
driver.find_element(By.ID, "alertbtn").click()

# Wait for the alert to be present (Explicit Wait)
wait = WebDriverWait(driver, 10)
wait.until(EC.alert_is_present())

# Switch to the alert
alert = driver.switch_to.alert
alert_text = alert.text
print(f"Alert Text: {alert_text}")
alert.accept()
```
### 7. Switch Between Multiple Windows
The script opens a new window, switches to the new window, and closes it after completing operations.

```python
mainwindow = driver.current_window_handle
driver.find_element(By.XPATH, "//button[contains(text(), 'Open Window')]").click()
allwindows = driver.window_handles

# Iterate through all windows and close the ones that aren't the main window
for window in allwindows:
    if window != mainwindow:
        driver.switch_to.window(window)
        driver.maximize_window()
        driver.close()

# Switch back to the main window
driver.switch_to.window(mainwindow)
8. Action on Main Window
After switching back to the main window, the script interacts with an input field by typing "India" into it.

python
Copy code
inputText = driver.find_element(By.XPATH, "//input[@placeholder='Type to Select Countries']")
inputText.send_keys("India")
```
### 8 Close the Browser
Finally, the script closes the browser.
```python
driver.quit()
```