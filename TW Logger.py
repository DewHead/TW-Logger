import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import LoginInfo
 
window = Tk()
window.title("TimeWatch hour logger")
window.configure(background="#ffffff")
window.iconbitmap(r'favicon.ico')
#center window
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
 
# gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
 
# positions the window in the center of the page.
window.geometry("+{}+{}".format(positionRight, positionDown))

class timeWatch(): 
    def setUp(self):
        #call Chrome webdriver in order to open login site
        self.browser = webdriver.Chrome()
        self.browser.get(('http://checkin.timewatch.co.il/punch/punch.php'))
            
    def login(self):
        #set variables for user information
        cmpnyStr = LoginInfo.cmpnyStr
        emplyStr = LoginInfo.emplyStr
        passwdStr = LoginInfo.passwdStr
      
        #tell selenium to find the relevant fields and input info respectively
        companyNumber = self.browser.find_element_by_id('compKeyboard')
        companyNumber.send_keys(cmpnyStr)

        employeeNumber = self.browser.find_element_by_id('nameKeyboard')
        employeeNumber.send_keys(emplyStr)

        password = self.browser.find_element_by_id('pwKeyboard')
        password.send_keys(passwdStr)

        #click the entrance button
        enterButton = self.browser.find_element_by_name('B1')
        enterButton.click()

    def come(self):
        #click the IN button
        tw.setUp()
        tw.login()
        inButton = self.browser.find_element_by_id('inButton')
        inButton.click()
        tw.exit()
        
        
    def go(self):
        #click the OUT button
        tw.setUp()
        tw.login()
        outButton = self.browser.find_element_by_id('outButton')
        outButton.click()
        tw.exit()

    def exit(self):
        #ex = exit()
        self.browser.quit()
        messagebox.showinfo('All done', 'Attendance has been logged')
        sys.exit()

tw = timeWatch()
label = tk.Label(window, text="Welcome to TW Logger\nPlease choose your option", font=("Verdana", 12), bg="#ffffff", fg="#616161")
label.grid(column=1, row=0, pady=10, padx=10)
btn1 = ttk.Button(window, text="Comming in", command=tw.come)
btn2 = ttk.Button(window, text="Done for today", command=tw.go)
btn3 = ttk.Button(window, text="Exit app", command=sys.exit)
btn1.grid(column=1, row=1, pady=10)
btn2.grid(column=1, row=2, pady=10)
btn3.grid(column=1, row=3, pady=10)

window.mainloop()
