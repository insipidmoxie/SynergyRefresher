#Synergy Refresher by Reece Griffith
#Future update where it refreshes as soon as the button appears is also easily possible but it's set to click every 2 seconds for now.
#Currently the script logs into synergy and CTAS and constantly checks for cases. When a case is detected the script will play a sound, give a notification and stop.
#Feel free to email or message improvement suggestions.
#Next improvement will probably be a dropdown to change how many times the alert plays.



import tkinter as tk    
from tkinter import messagebox
import threading  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
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
    driver.switch_to.window(driver.window_handles[1])
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
    global switch
    iframe = driver.find_element(By.CSS_SELECTOR, "#ifFrontpage")
    driver.switch_to.frame(iframe)                                                              #focuses on frame so it can see the page
    records_text = driver.find_element(By.CSS_SELECTOR, "div.CSGroup:nth-child(3)").text
    if "no available records for you" in records_text:                                          #checks if there are no records
        driver.find_element(By.CSS_SELECTOR, "#backToCampaignsBtn").click()                     #if no records click back
        driver.switch_to.default_content()
        return
    else:
        switchoff()
        alert()
        messagebox.showinfo("Synergy Refresher", "A record has been detected. Hopefully.")      #if a record is there the script plays a sound and stops
        

def run():  
     def refresh():
         print('Preparing to refresh')
         while (switch == True):  
            start_tracing()                                     #hits start tracing
            time.sleep(2)                                       #waits 2 seconds
            back()                                              #hits back if no case
            time.sleep(2)                                       #waits 2 seconds  
            if switch == False:  
                 break
     thread = threading.Thread(target=refresh)                  #initialises another thread to run refresh function concurrently with GUI mainloop
     thread.start()  
     
def switchon():                                                 #function governing the Resume switch functionality
     global switch  
     global onbutton
     global offbutton
     switch = True  
     print('Starting')
     onbutton["state"] = "disabled"                              #greys out the on button once its pressed
     offbutton["state"] = "active"                               #makes the off button available to be pressed
     run()                                                       #calls the main run/refresh functions.

def switchoff():    
     print('Pausing')
     global onbutton
     global offbutton
     global switch  
     onbutton["state"] = "active"                               #greys out the off button once its pressed
     offbutton["state"] = "disabled"                            #makes the on button available to be pressed      
     switch = False                                             #sets switch variable to off

def kill():    
     print('Exiting program.')
     root.destroy()
     driver.quit()

if __name__ == "__main__":                                  #main loop
    switch = True                                   
    root = tk.Tk()                                          #initialises GUI
    print('Initialising')
    
    driver = webdriver.Firefox()                            #starts a browser for synergy
    driver.get(synergy_url)                                 #loads synergy   
    Login_to_Synergy(synergy_username, synergy_password)    #logs into synergy
    open_CTAS_tab()                                         #opens tab for ctas
    time.sleep(1)
    Login_to_CTAS(ctas_userame, ctas_password)              #logs into ctas
    focus_synergy_tab()                                     #switches back to synergy tab
    
    onbutton = tk.Button(root, text = "Start/Resume", command = switchon)       #lines 138-146 initialise the GUI buttons
    onbutton.config(height = 2, width = 10)  
    onbutton.pack(padx = 50, pady=12)    
    offbutton =  tk.Button(root, text = "Stop/Pause", command = switchoff)    
    offbutton.config(height = 2, width =10)
    offbutton.pack(padx = 50)    
    killbutton = tk.Button(root, text = "EXIT", command = kill, fg="red")    
    killbutton.config(height = 2, width=10)
    killbutton.pack(padx=50,pady=12)    
    
    root.mainloop()                                                             #opens GUI to run main program
        








