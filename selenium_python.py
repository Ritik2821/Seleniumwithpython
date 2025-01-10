from tabnanny import check
from time import thread_time

from selenium import webdriver
from selenium.webdriver.common.by import By

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

print("ritik")
