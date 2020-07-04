# SynergyRefresher
Refreshes the synergy page to check for cases

Feel free to give suggestions as to how to improve the script.

Read below to learn how to set up and use the script.

https://www.python.org/downloads/windows/

https://www.mozilla.org/en-GB/firefox/new/

You'll need these 2 things in addition to the script: Python to run the script and Firefox to open synergy.

The python version to download will be 3.8.3 (the latest one) and you'll want to download the 64 bit executable installer.

To download the script, press the green Clone button above. Then press Download Zip and extract the Zip file once it's downloaded. To extract simply right click on the downloaded file and press extract.

Once you have extracted the folder, run the setPath.bat file.


1) 
First download the python installer and run it. At the start of the installer there will be an option to add python to PATH. MAKE SURE TO ENABLE IT then continue installing python. After that install Firefox if you haven't already.

2) 
Now open command prompt by pressing windowskey+x and clicking windows powershell or by searching cmd in the bottom left and opening it. Once its open type 

pip install selenium

into it and press enter

It should install the selenium module. If it works go straight to step 3. You might get a warning about pip version but ignore it. 

If you get an error alone the lines of "no such command as pip" you should find where python is installed (default is usually C:\Python38\)
Then open command prompt and type 

setx PATH "%PATH%;C:\Path\To\Python"  

For example, the default would be 

setx PATH "%PATH%;C:\Python38\Scripts"

You will only have to do this if you forgot to enable adding python to PATH during installation. Alteratively reinstall python and make sure to enable the setting.

3)
Almost there!

Right click on the synergy_refresher_public.py file and click Edit with IDLE.

Near the top (lines 18-21) there will be text that says 'replace this text with your synergy username' and the same with the password. Replace it with your username and password (the username is the intelling email), LEAVING THE QUATATION MARKS INTACT.

After this you should be good to press run -> run module and you are DONE! Easy peasy.

NOTE:

Do NOT minimise the browser as it will stop the script. You can, however, do whatever you want over the top of it as long as it's not minimised.

Once a record is found the script will stop, display a message and play an alert thrice. After the call is completed press the back button and resume the script.



Enjoy!!

-Reece

PS. Any issues post them on the issues section or email me and I'll do my best
