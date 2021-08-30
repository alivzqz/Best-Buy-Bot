from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import datetime
#import time
import info

# make sure this path is correct
PATH = "C:\\Users\\Ali\\Downloads\\chromedriver.exe"

## Test Links
##
## Legend of Zelda Skyward Sword HD $59.99
## https://www.bestbuy.com/site/the-legend-of-zelda-skyward-sword-hd-nintendo-switch-nintendo-switch-lite/6414119.p?skuId=6414119
##
## Pokemon 1-3 Blu-Ray $18.99
## https://www.bestbuy.com/site/pokemon-movies-1-3-blu-ray/6332747.p?skuId=6332747
##
## Metroid Dread Special Edition $89.99
## https://www.bestbuy.com/site/metroid-dread-special-edition-nintendo-switch-nintendo-switch-lite/6464104.p?skuId=6464104

link = input("Link: ")
chrome_options = Options()
driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
driver.get(link)

isComplete = False
print(info.email)
print("Refreshing every 5 seconds until 'Add to Cart' Button is found")

#driver.get("https://www.bestbuy.com/identity/global/signin")
#time.sleep(3)

while not isComplete:
    # find add to cart button
    try:
        atcBtn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        driver.refresh()
        continue
    
    print("Add to Cart button found")

    try:
        # add to cart
        atcBtn.click()

        # go to cart and begin checkout as guest
        driver.get("https://www.bestbuy.com/cart")

        checkoutBtn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button'))
        )
        checkoutBtn.click()
        print("Successfully added to cart - beginning check out")

        # fill in email and password
        emailField = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        print("Email Username filled")

        emailField.send_keys(info.email)

        pwField = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        print("Email Password filled")
        
        pwField.send_keys(info.password)

        # click sign in button
        signInBtn = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cia-form__controls__submit'))
        )
        signInBtn.click()
        print("Sign In Successful")


##        # fill in card cvv
##        # comment this section out if the "Place Order" page does not contain a CVV Field usually under $100 items  
##        cvvField = WebDriverWait(driver, 3).until(
##            EC.presence_of_element_located((By.ID, "credit-card-cvv"))
##        )
##        cvvField.send_keys(info.cvv)
##        print("CVV Key Filled")
##        
##        # place order - Fast Track Button
        
        placeOrderBtn = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
        )
        placeOrderBtn.click()

##        # Secondary Payment Screen Check
##        continueBtn = WebDriverWait(driver, 3).until(
##            EC.presence_of_element_located((By.XPATH, '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button/span'))
##            )
##        continueBtn.click()
##        print ("Secondary Payment Information Screen")
##
##        # place order on secondary screen
##        primaryBtn = WebDriverWait(driver, 7).until(
##            EC.presence_of_element_located((By.XPATH, '//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[3]/div[2]/button'))
##            )
##        primaryBtn.click()
        
        print("Attempting to place order...")

        isComplete = True
        
    except:
        # make sure this link is the same as the link passed to driver.get() before looping
        driver.get(link)
        print("Error - restarting bot")
        datetime_object = datetime.datetime.now()
        print(datetime_object)
        continue

print("Order successfully placed")

