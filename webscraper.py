
#Author
"""
Author: Christopher Cintron
"""
#Description
"""
Selenium script that logs into banking website
and retrieves banking information
"""




#__Start_script__#
from selenium import webdriver
import time


#Load and open chrome with cookies/data
url = "https://secure07a.chase.com/"
#chase bank info
username = ''#Username
password = ''#password


class Account(object):
    def __init__(self,url,username,password,):
        self.url = url
        self.username = username
        self.password = password
        self.balance = None

    def results(self):
        print("Account_Holder: {}".format(self.username))
        print("Balance: {}".format(self.balance))

class Scraper():
    def __init__(self):
        self.driver = None

    def driver_setup(self):
        options = webdriver.ChromeOptions()
        #Note: Change the next line of code if another user other than Author
        #How to: If using chrome, copy and paste "chrome://version/" into browser
        #and find the appdata path of your machine
        options.add_argument("user-data-dir=C:/Users/Chris/AppData/Local/Google/Chrome/User Data'")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://secure07a.chase.com/web/auth/dashboard#/dashboard/accounts/summary/dda;params=dda,379901328")


    def login(self):
        self.driver.switch_to.frame("logonbox")
        self.driver.find_element_by_name('userId').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('signin-button').click()

    def fetch_balance(self):
        #Fetch balance
        account_balance = self.driver.find_element_by_class_name("balance").text
        return(account_balance)



#__End_script__#
if __name__ == "__main__":
    chase_account = Account(url,username,password)
    chase_scraper = Scraper()
    chase_scraper.driver_setup()
    time.sleep(5)
    chase_scraper.login()
    time.sleep(5)
    chase_account.balance = chase_scraper.fetch_balance()
    chase_account.results()
