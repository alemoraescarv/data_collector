
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart


class scraper():

    def __init__(self, url) -> None:
        self.url = url

    def dates(self):
        #_date = input("Please give me dates in the format DD/MM/YYYY")
        _date="02/03/2023"
        return date(_date)
    
    def search_holliday(self):
        return None

if __name__=="__main__":
    # Change this to your own chromedriver path!
    chromedriver_path = 'chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path) 