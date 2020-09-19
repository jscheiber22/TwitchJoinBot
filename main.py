from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# A bot to automatically join a twitch stream upon seeing it go live.
# Very nice to do for small channels you want to support
# Written by James Scheiber, 4am 9/19/2020 :)

class TwitchJoinBot:

    # Current default set to chkn.ngts
    def __init__(self, url = "https://www.twitch.tv/chknngts"):
        self.url = url

        # Adding the headless option allows the browser to open without a GUI. This makes the program far more user friendly.
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

        # COMMENT OUT THE ABOVE THREE LINES AND UNCOMMENT THIS ONE IF YOU WANT TO SEE THE BROWSER WINDOW
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # Does the actual checking to see if the account is live
    def checkLive(self):
        self.driver.get(self.url)
        try:
            offline = self.driver.find_element_by_xpath("//p[contains(text(), 'Offline')]")
            print("Streamer is offline, closing window.")
            return False
        except NoSuchElementException:
            print("Streamer is online, leaving window open.")
            return True

    def quit(self):
        self.driver.quit() # Closes all windows associated with the driver, .close() would close just the current window
