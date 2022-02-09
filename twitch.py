
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Watcher:
	def __init__(self):
		chrome_options = Options()
		#chrome_options.add_argument("--headless")
		chrome_options.add_argument("log-level=3")
		self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

	def watch(self,channelname,timeout):
		#login
		self.driver.get(f"https://twitch.tv/{channelname}")
		self.driver.implicitly_wait(100)
		self.driver.find_element(By.CSS_SELECTOR, ".kJZgbi .Layout-sc-nxg1ff-0").click()
		self.driver.implicitly_wait(100)
		self.driver.find_element(By.ID, "login-username").send_keys("JCMSimon")
		self.driver.implicitly_wait(100)
		self.driver.find_element(By.ID, "password-input").send_keys("password")
		self.driver.implicitly_wait(100)
		self.driver.find_element(By.ID, "login-username").send_keys(Keys.ENTER)
		
		#how to get email code

		time.sleep(timeout)
		self.watch(channelname,timeout)

if __name__ == "__main__":
	Watcher = Watcher()
	Watcher.watch("pong_blog",3600)