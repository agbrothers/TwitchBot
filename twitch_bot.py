import sys
import otp
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class WebBot():
    """
    
    Fundamental Bot Superclass
    -------
     : Contains basic webdriver methods for chrome browser access with selenium
               
    """
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        
    def relaunch(self):
        self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        
    def back(self):
        self.driver.execute_script("window.history.go(-1)")

    def go(self, url, wait=5):
        """ 
        Smarter nav + optional delay to avoid bot detection 
        """
        if self.driver.current_url != url:
            self.driver.get(url)
            time.sleep(wait)    
            

class TwitchBot(WebBot):
    """
    
    Twitch Point Optimizing Bot
    -------
     : Used to farm Twitch points for a given list of channels
     
     : Contains Methods for automated interactions with twitch.tv
          
    -------
    Assumptions
    
     : A gmail account is linked to the Twitch account (Necessary for automating login process)
        
    -------    
    Parameters
    
        username : twitch.tv account username
        
        password : twitch.tv account password
        
        gmail : the google email linked to the twitch account
        
        channels : a list of the channel names to be watched
        
        time interval : (optional) the number of minutes each channel is 
                        watched for prior to cycling to the next
                        
    -------
    Things to Add
     : Open multiple channels in different tabs & simultaneously collect points
     
     : Participate in raids
     
     : 
    
    """
    
    def __init__(self, username, password, gmail, channels, time_interval=15):
        WebBot.__init__(self)
        self.un = username
        self.pw = password
        self.gmail = gmail
        self.channels = channels
        self.time_interval = time_interval*60
        self.base_url = 'https://www.twitch.tv/'
        self.main()
        

    def main(self):
        self.login()
        for channel in self.channels:
            self.watch(channel)
        
        
    def login(self):
        """
        
        Logs in to the ESPN account using the credentials provided
        -------

        """
        self.go(self.base_url+'login')
        try:
            # Enter the username and password
            un_element = self.driver.find_element_by_xpath('//input[@id="login-username"]')
            un_element.send_keys(un)
            time.sleep(2.3)
            pw_element = self.driver.find_element_by_xpath('//input[@id="password-input"]')
            pw_element.send_keys(pw) 
            time.sleep(0.75)
            pw_element.send_keys(Keys.ENTER)
                

            # Get the One Time Password from the given gmail account to login
            try:
                time.sleep(20)
                one_time_passcode = otp.get_twitch('greysonbrothers@gmail.com')
                # one_time_passcode = input(f'Please enter the one-time-passcode sent to {self.un}')
                input_elements = self.driver.find_elements_by_xpath('//input[@type="text"]')
                for i,num in enumerate(one_time_passcode):
                    input_elements[i].send_keys(num)
                    time.sleep(0.5)
                time.sleep(3)
            except Exception:
                return
            
        except Exception:
            sys.exit(f'Error: There was an issue logging in to {self.login_url}.  Please check the credentials provided and retry.')
                
        
    def collect_pts(self):
        """

        Collects accumulated channel points if possible (the cyan button in chat)
        -------

        """        
        buttons = self.driver.find_elements_by_xpath('//button[@class="tw-button tw-button--success"]')
        if len(buttons):
            buttons[0].click()
            
            
    def is_live(self):
        """

        Returns bool with respect to the channel's live status
        -------

        """
        offline_element = self.driver.find_elements_by_xpath('//div[@class="channel-status-info channel-status-info--offline tw-border-radius-medium tw-inline-block"]')
        status = not bool(len(offline_element))
        return status
    
    
    def is_mature(self):
        """
        
        Check if content is set to mature and press 'Start Watching' button if true
        -------

        """
        mature_element = self.driver.find_elements_by_xpath("//button[@data-a-target='player-overlay-mature-accept']")
        if len(mature_element):
            mature_element[0].click()        


    def watch(self, channel):
        """
        
        Calls all methods necessary to watch a channel while maximizing points earned
        -------
         : Navigates to channel
         
         : Checks if Live
         
         : Checks if Mature
         
         : Collects points at most every 15 minutes until the time interval ends
        
        """
        self.go(self.base_url + channel)        
        self.is_mature()   
        time_left = self.time_interval
        collection_interval = 15*60 # Number of seconds needed for points to accumulate
        self.collect_pts()
        
        while time_left:
            if not self.is_live():
                return
            if time_left < collection_interval:
                time.sleep(time_left)
                time_left = 0
            else:
                time.sleep(time_left)
                time_left -= collection_interval
            self.collect_pts()
            
            
        
        
if __name__ == '__main__':
        
    un = 'gaymingming'
    pw = 'manbearpiggayfishfrog'
    email = 'greysonbrothers@gmail.com'
    channels = ['Mizkif','hJune','ludwig','KristoferYee','Myth','SwaggerSouls']
    t = 0.25
    
    bot = TwitchBot(un, pw, email, channels, t)
    
    
    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
    # ActionChains(driver).key_down(Keys.COMMAND).send_keys("t").key_up(Keys.COMMAND).perform()



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    