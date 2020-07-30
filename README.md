# SynergyRefresher
Refreshes the synergy page to check for cases

Feel free to give suggestions as to how to improve the script.

Read below to learn how to set up and use the script.

https://www.python.org/downloads/windows/

https://www.mozilla.org/en-GB/firefox/new/

You'll need these 2 things in addition to the script: Python to run the script and Firefox to open synergy.

The python version to download will be 3.8.3 (the latest one) and you'll want to download the 64 bit executable installer.

To download the script, press the green Code button above. Then press Download Zip and extract the Zip file once it's downloaded. To extract simply right click on the downloaded file and press extract.


1) 
First download the python installer and run it. At the start of the installer there will be an option to add python to PATH. MAKE SURE TO ENABLE IT then continue installing python. After that install Firefox if you haven't already.

2) 

Run the InstallSeleniumandSetPath.bat file to install selenium and set PATH to geckodriver. You cannot do this before installing python and enabling python being added to PATH or you will get an error.

3)
Almost there!

Right click on the synergy_refresher_public.pyw file and click Edit with IDLE.

Near the top (lines 18-21) there will be text that says 'replace this text with your synergy username' and the same with the password. Replace it with your username and password (the usernames are the intelling email), LEAVING THE QUATATION MARKS INTACT.

After this you should be good to press run -> run module and you are DONE! Easy peasy.






NOTE:

Do NOT minimise the browser when it is refreshing as it will stop the script. You can, however, do whatever you want over the top of it as long as it's not minimised.

Once a record is found the script will stop, display a message and play an alert thrice. After the call is completed press the back button and resume the script.

To change the amount of time to elapse between clicks change the "seconds_between_clicks" variable.

If you do not trust the .exe file in the download you can download it directly from Mozilla instead at https://github.com/mozilla/geckodriver/releases and place it in the synergy refresher download folder. The exe was included directly in this download to simplify installation

If you do not trust the .bat file in this download you can instead run the "pip install selenium" command yourself and add the geckodriver path to windows searchpath yourself. The .bat file was included to simplify and speed up installation.

Enjoy!!

-Reece

PS. Any issues post them on the issues section or email me and I'll do my best
