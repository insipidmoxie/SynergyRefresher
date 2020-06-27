# SynergyRefresher
Refreshes the synergy page to check for cases

Read below to learn how to set up and use the script.

https://www.python.org/downloads/windows/

https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip

https://www.mozilla.org/en-GB/firefox/new/

You'll need these 3 things in addition to the scrip:, Python to run the script, Firefox to open synergy and geckodriver to let firefox work with the script.
The python version to download will be 3.8.3 (the latest one) and you'll want to download the 64 bit executable installer.

1) 
First install python and toward the end of the installer there will be an option to add python to PATH. MAKE SURE TO ENABLE IT

2) 
Now open command prompt by pressing windowskey+x and clicking windows powershell or by searching cmd in the bottom left
once its open type 
"pip install selenium"
into it (without the quotation marks) and press enter

It should install the selenium module. You might get a warning about pip version but ignore it. 
If you get an error alone the lines of "no such command as pip" you should find where python is installed (default is usually C:\Python38\)
Then open command prompt and type 
setx PATH "%PATH%;C:\Path\To\Python"  For example, the default would be setx PATH "%PATH%;C:\Python38\Scripts"
You will only have to do this if you forgot to enable adding python to PATH during installation. Alteratively reinstall python and make sure to enable the setting

3) 
Next find the path to where you downloaded the geckodriver file, for example to C:\Users\YourName\Downloads\SynergyRefresher

There are two options for this next step
Option1:
Open command prompt again and write 
setx PATH "%PATH%;C:\Users\YourName\Downloads\SynergyRefresher"
Option2:
In the search bar in the bottom left type "edit the system environment variables" and hit enter.
In the bottom right of the window that comes up, just above the apply button there will be an "Environment Variables" button. Click it
A new window will come up.
In "User variables for YourName" (the top one) there will be a "Path" variable. Click it and click Edit.
A list of folders will come up, press new and put in the folder in which the geckodriver.exe file is, for example C:\Users\YourName\Downloads
Press okay



4) 
Almost there!
Right click on the synergy_refresher_2.py file and click Edit with IDLE
At the top there will be text that says 'replace this text with your synergy username' and the same with the password
Replace it with your username and password (the username is the intelling email), leaving the quotation marks intact
After this you should be good to press run -> run module and you are DONE!

NOTE:
Do NOT minimise the browser as it will stop the script. You can, however, do whatever you want over the top of it as long as
it's not minimised.
When you get a case it'll just stop and print a message saying "You probably have a record". You can either open a new tab
and log into CTAS and do it that way or log into synergy and CTAS on your preferred browser. Really doesn't matter.
If you each time you stop and start the script it'll open a new firefox window. Just close the previous one.

Future updates will probably included a sound playing and a notification when a record is found and a graphical interface to
enter your synergy details into to avoid editing the script.

Enjoy!!

-Reece
