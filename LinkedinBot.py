from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from linkedinpassword import password

options = Options()
options.add_experimental_option('detach', True)

chrome_driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(options=options)

driver.get("https://www.linkedin.com/jobs/search/?alertAction=viewjobs&currentJobId=3568519432&f_AL=true&f_E=2&f_TPR=r2592000&f_WT=1%2C2%2C3&geoId=103644278&keywords=software%20engineer&location=United%20States&sortBy=R")
signin_button = driver.find_element(By.LINK_TEXT, "Sign in")
signin_button.click()
time.sleep(2)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys("clintonnmereole@gmail.com")
time.sleep(2)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)
time.sleep(2)
password_field.send_keys(Keys.ENTER)
time.sleep(2)

all_listings = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        if apply_button:
            apply_button.click()
            time.sleep(2)
            next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
            if next_button:
                while next_button:
                    next_button.click()
                    time.sleep(2)
                review_button = driver.find_element(By.CLASS_NAME, "artdeco-button artdeco-button--2 artdeco-button--primary ember-view")
                if review_button:
                    review_button.click()
                    time.sleep(2)
                submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button artdeco-button--2 artdeco-button--primary ember-view")
                submit_button.click()
                time.sleep(2)
                done_button = driver.find_element(By.CLASS_NAME, "artdeco-button artdeco-button--2 artdeco-button--primary ember-view mlA block")
                done_button.click()
            else:
                submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button artdeco-button--2 artdeco-button--primary ember-view")
                if submit_button:
                    submit_button.click()
                    time.sleep(2)
                    done_button = driver.find_element(By.CLASS_NAME, "artdeco-button artdeco-button--2 artdeco-button--primary ember-view mlA block")
                    done_button.click()
                else:
                    continue
        else:
            continue
    except NoSuchElementException:
        print("No application button, skipped")
        continue
   

#driver.close()
