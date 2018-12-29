Written in Python 3.7 with Selenium for interfacing with the website via chromedriver.exe and Tkinter for GUI.
Compiled as a standalone with Pyinstaller.

----- COMPILING -----

Before trying this out, please make sure you have Python 3.x. In Python 2.x the Tkinter commands are a bit different.
You also need Selenium to be installed installed and to make sure that chromedirver is installed.

This piece of code pulls variables from an external .py file (LoginInfo.py).
I had to trick Pyinstaller in order to keep the file external and not have it compiled. If it compiles, we won't be able to change the login info because it will be part of the .exe.
If you decide to compile, make sure that the LoginInfo.py file is not in the the same folder as the code (TW Logger.py).
After compiling, move the LoginInfo.py file back to the same root as the compiled software and you will still be able to pull from it.

----- INSTALLING -----

In order for this to work properly, you will need to input your login details.
To do so, please edit the LoginInfo.py file found in the root of the installation path and fill in the fields respectively.

On the first run you will be prompted with a Windows Firewall message asking to allow the connection. TW Logger is connecting to the TimeWatch website (http://checkin.timewatch.co.il/punch/punch.php). You can safely allow this connection.
