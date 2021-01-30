# TwitchBot
  TwitchBot

# SETUP
  The bot utilizes chromedriver to connect and interact with espn.com. Downloads for chromedriver can be found here:
  https://sites.google.com/a/chromium.org/chromedriver/downloads
  
  To get personal credentials for the gmail API and to authorize this program to access gmail, follow the steps at the following link:
  https://developers.google.com/gmail/api/quickstart/python
  
  Following the instructions there will generate a "credentials.json" file which you should place in the same directory as the files in this repository.

  Alternatively, if you don't want to give the program gmail access, if you have trouble getting the gmail API setup, or if your ESPN account 
  isn't linked to a gmail account, you can modify the code to enable manual logins within FantasyBasketballBot.py > Eyes class > _login method

  To do this you can remove the line: 

          one_time_passcode = otp.get_espn(user_id=self.un)

  and replace it with:

          one_time_passcode = input(f'Please enter the one-time-passcode sent to {self.un}')

  enabling you to manually input the passcode into the console to log in.  This line is already commented out in the code for convenience.  



# FUTURE FEATURES 
  • Open multiple tabs and rotate between them
