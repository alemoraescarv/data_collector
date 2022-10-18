from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


class Scrapper():

    def __init__(self, url:str = 'https://www.kayak.co.uk') -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)

    def accept_privacy(self):
        """Accepting the privacy pop up in the page when it loads. Waits it appears and click
        """
        try:
            accept_privacy = WebDriverWait(bot.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Accept"]')))
            accept_privacy.click()
        except Exception as error:
            print("Accepting privacy settings error: {}".format(error))

    

    
        
        
