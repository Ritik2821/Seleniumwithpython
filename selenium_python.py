'''
tabnanny is a Python module used to check for inconsistent indentation in Python files.
It does not serve any purpose in your script.
'''
from tabnanny import check
from time import thread_time, time

import drive
# import EC
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# CLICK CHECK OPTION USING ID LOCATOR
checkbutton=driver.find_element(By.ID, "checkBoxOption1")
checkbutton.click()

# CLICK CHECK OPTION USING XPATH LOCATOR
radioButton = driver.find_element(By.XPATH, "//input[@value='radio2']")
radioButton.click()

#CLICK LINK TEXT USING LOCATOR LINK TEXT
driver.find_element(By.LINK_TEXT, "QA Meetup with Rahul Shetty @Bangalore - Limited Seats! Book Now!").click()



#  DROP DOWWN
dropdown=driver.find_element(By.ID,"dropdown-class-example")
select=Select(dropdown)
select.select_by_visible_text("Option2")
print("Checking that select is working")


#ALERT HANDLE
alertTextField=driver.find_element(By.NAME,"enter-name")
# alertTextField.send_keys("Ritik Sharma")
driver.find_element(By.ID,"alertbtn").click()

# Wait for the alert to be present (Explicit Wait)
wait = WebDriverWait(driver, 10)
wait.until(EC.alert_is_present())  # Wait until the alert is present

# Switch to the alert
alert = driver.switch_to.alert

# Get the alert's text
alert_text = alert.text
print(f"Alert Text: {alert_text}")

# Accept the alert after waiting
alert.accept()

# WINDOW HANDLE

#STORE THE MAIN WINDOW
mainwindow=driver.current_window_handle

# Click on the button to open the new window
driver.find_element(By.XPATH, "//button[contains(text(), 'Open Window')]").click()

# Get all window handles
allwindows = driver.window_handles

#PRINT ALL WINDOW IDS
for i in allwindows:
    print(i)


# Iterate through all windows
for window in allwindows:
    if window != mainwindow:  # Skip the main window
        # Switch to the new window
        driver.switch_to.window(window)
        driver.maximize_window()
        print("Window opened")

        # Close the current window after your operations
        driver.close()

#SWITCHING TO MAIN WINDOW
driver.switch_to.window(mainwindow)

#ACTION ON MAIN WINDOW
inputText=driver.find_element(By.XPATH,"//input[@placeholder='Type to Select Countries']")
inputText.send_keys("India")

driver.quit()