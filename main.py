from selenium import webdriver
import time

class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
       bot = self.bot
       bot.get("https://instagram.com/accounts/login")
       time.sleep(3)
       bot.find_element_by_name("username").send_keys(self.username)
       bot.find_element_by_name("password").send_keys(self.password)
       time.sleep(3)

    def searchHashtag(self,hashtag):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/" + hashtag)



insta = InstagramBot("Enter your username ","Enter your password")#Anna
insta.login()
insta.searchHashtag("Python")


