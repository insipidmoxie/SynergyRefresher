#Synergy Refresher by Reece Griffith
#Future updates to include a GUI with pause&resume buttons and windows notification on record detection.
#Future update where it refreshes as soon as the button appears is also easily possible but it's set to click every 2 seconds for now.
#Currently the script logs into synergy and CTAS and constantly checks for cases. When a case is detected the script will play a sound and stop.




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import winsound


synergy_username = "replace this text with your synergy username" #PLEASE ENTER YOUR SYNERGY USERNAME BETWEEN THESE QUOTATION MARKS
synergy_password = "replace this text with your synergy password" #PLEASE ENTER YOUR SYNERGY PASSWORD BETWEEN THESE QUOTATION MARKS
ctas_userame = "replace this text with your ctas username"        #PLEASE ENTER YOUR CTAS USERNAME BETWEEN THESE QUOTATION MARKS
ctas_password = "replace this text with your ctas password"       #PLEASE ENTER YOUR CTAS PASSWORD BETWEEN THESE QUOTATION MARKS









#main code below here. Do NOT edit below here unless you want to change how many times the alert sound plays.


ctas_url = "https://contact-tracing-staff.phe.gov.uk/staff/sign_in"
synergy_url = "https://ttt3.callscripter.com/"


def open_CTAS_tab():                                                #opens a tab for CTAS
    driver.execute_script("window.open('{}')".format(ctas_url))
    return

def focus_synergy_tab():                                            #switches to the synergy tab
    driver.switch_to.window(driver.window_handles[0])
    return

def alert():                                                        #plays the alert.wav sound thrice. 
    winsound.PlaySound('alert.wav', winsound.SND_FILENAME)          #To change to once or twice delete two or one of these lines, respectively.
    winsound.PlaySound('alert.wav', winsound.SND_FILENAME)
    winsound.PlaySound('alert.wav', winsound.SND_FILENAME)
    return

def Login_to_Synergy(username, password):
    driver.find_element(By.CSS_SELECTOR,"#txtUsername").send_keys(username + Keys.TAB)      #enters username
    driver.find_element(By.CSS_SELECTOR,"#txtPassword").send_keys(password)                 #enters password
    WebDriverWait(driver, timeout=1)                                                        
    driver.find_element(By.CSS_SELECTOR,".btn").click()                                     #clicks login
    return

def Login_to_CTAS(username, password):
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.CSS_SELECTOR, "#staff-member-email-field").send_keys(username + Keys.TAB)       #enters username
    driver.find_element(By.CSS_SELECTOR, "#staff-member-password-field").send_keys(password + Keys.ENTER)  #enters password
    return

def start_tracing():
    iframe = driver.find_element(By.CSS_SELECTOR, "#ifFrontpage")                           
    driver.switch_to.frame(iframe)
    iframe3 = driver.find_element(By.CSS_SELECTOR, ".stack-fill > iframe:nth-child(1)")
    driver.switch_to.frame(iframe3)
    driver.find_element(By.TAG_NAME, "button").click()                                          #clicks start tracing
    driver.switch_to.default_content()
    return


def back():
    iframe = driver.find_element(By.CSS_SELECTOR, "#ifFrontpage")
    driver.switch_to.frame(iframe)                                                              #focuses on frame so it can see the page
    records_text = driver.find_element(By.CSS_SELECTOR, "div.CSGroup:nth-child(3)").text
    if "no available records for you" in records_text:                                          #checks if there are no records
        driver.find_element(By.CSS_SELECTOR, "#backToCampaignsBtn").click()                     #if no records click back
        driver.switch_to.default_content()
        return
    else:
        alert()
        sys.exit("You probably have a record.")                                                 #if a record is there the script plays a sound and stops

if __name__ == "__main__":                                  #main loop
    
    driver = webdriver.Firefox()                            #starts a browser for synergy
    driver.get(synergy_url)                                 #loads synergy   
    Login_to_Synergy(synergy_username, synergy_password)    #logs into synergy
    open_CTAS_tab()                                         #opens tab for ctas
    time.sleep(1)
    Login_to_CTAS(ctas_userame, ctas_password)              #logs into ctas
    time.sleep(1)
    focus_synergy_tab()                                     #switches back to synergy tab
    time.sleep(2)
    
    
    while(1):                                               #repeats the following until stopped:
        start_tracing()                                     #hits start tracing
        time.sleep(2)                                       #waits 2 seconds
        back()                                              #hits back if no case
        time.sleep(2)                                       #waits 2 seconds
        








