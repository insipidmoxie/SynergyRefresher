#Synergy Refresher by Reece Griffith
#The capabilities for the script to log into CTAS also exist, but they are commented out because it's not as useful.
#Future updates to include a GUI, sound play on record detection, system notification on record detection.
#Future update where it refreshes as soon as the button appears is also easily possible but it's set to click every 2 seconds for now.





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys


synergy_url = "https://ttt3.callscripter.com/"
synergy_username = "replace this text with your synergy username"
synergy_password = "replace this text with your synergy password"
#ctas_userame = "replace this text with your ctas username"
#ctas_password = "replace this text with your ctas password"
#ctas_url = "https://contact-tracing-staff.phe.gov.uk/staff/sign_in"


def Login_to_Synergy(username, password):
    synergy_driver.find_element(By.CSS_SELECTOR,"#txtUsername").send_keys(username + Keys.TAB)      #enters username
    synergy_driver.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys(password)                 #enters password
    WebDriverWait(synergy_driver, timeout=1)                                                        
    synergy_driver.find_element(By.CSS_SELECTOR,".btn").click()                                     #clicks login
    return

def Login_to_CTAS(username, password):
    ctas_driver.find_element(By.CSS_SELECTOR, "#staff-member-email-field").send_keys(username + Keys.TAB)       #enters username
    ctas_driver.find_element(By.CSS_SELECTOR, "#staff-member-password-field").send_keys(password + Keys.ENTER)  #enters password
    return

def start_tracing():
    iframe = synergy_driver.find_element(By.CSS_SELECTOR, "#ifFrontpage")                           
    synergy_driver.switch_to.frame(iframe)
    iframe3 = synergy_driver.find_element(By.CSS_SELECTOR, ".stack-fill > iframe:nth-child(1)")
    synergy_driver.switch_to.frame(iframe3)
    synergy_driver.find_element(By.TAG_NAME, "button").click()                                          #clicks start tracing
    synergy_driver.switch_to.default_content()
    return


def back():
    #synergy_driver.find_element_by_css_selector("#backToCampaignsBtn").click()  #clicks back
    iframe = synergy_driver.find_element(By.CSS_SELECTOR, "#ifFrontpage")
    synergy_driver.switch_to.frame(iframe)
    records_text = synergy_driver.find_element(By.CSS_SELECTOR, "div.CSGroup:nth-child(3)").text
    if "no available records for you" in records_text:                                                  #checks if there are no records
        synergy_driver.find_element(By.CSS_SELECTOR, "#backToCampaignsBtn").click()                     #if no records click back
        synergy_driver.switch_to.default_content()
        return
    else:
        sys.exit("You probably have a record.")                                                         #if a record is there the script stops

if __name__ == "__main__":
    synergy_driver = webdriver.Firefox()    #starts a browser for synergy
    #ctas_driver = webdriver.Firefox()       #starts a browser for ctas (disabled for now. no real use for it)
    
    synergy_driver.get(synergy_url)         #loads synergy
    #ctas_driver.get(ctas_url)               #loads ctas (disabled for now. no real use for it)
    
    Login_to_Synergy(synergy_username, synergy_password)    #logs into synergy
    #Login_to_CTAS(ctas_userame, ctas_password)              #logs into ctas (disabled for now. no real use for it)
    time.sleep(2)
    
    
    while(1):                   #repeats the following until stopped:
        start_tracing()         #hits start tracing
        time.sleep(2)           #waits 2 seconds
        back()                  #hits back if no case
        time.sleep(2)           #waits 2 seconds
        








