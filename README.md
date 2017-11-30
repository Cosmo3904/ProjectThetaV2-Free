# ProjectThetaV2-Free

## INSTALL THE FONT FILE FIRST OR NOTHING WILL LOOK RIGHT
## Before first run of the script run the following command : pip3 install pyqt5, requests, flask, threading, python_anticaptcha

## Captcha Harvester
The captcha harvester starts a web server on port 5000 using your local IP address. You can view this webpage by going to http://127.0.0.1:5000/solve however it's likely you will get the error 'localhost is not a supported domain' or something of the sort. To fix this you need to append your hosts file. On windows, this file is located in the directory 'C:\Windows\System32\drivers\etc\hosts'. On linux or osx, this file is located in the directory '/etc/hosts'. To append this file you will open your hosts file and add '127.0.0.1    dev.adidas.com' for adidas to the end of the file (and if you're harvesting for a different website just follow that format, for example supremenewyork would be '127.0.0.1    dev.supremenewyork.com'). After you've done this, the webpage you added to your hosts will now take place of 127.0.0.1 in the previous url EG: http://dev.adidas.com:5000/solve. After solving tokens, the successfully created tokens will be stored in the webpage http://127.0.0.1:5000/tokens. All tokens expire after 110 seconds because recaptcha tokens are only valid for 2 minutes. 

## Captcha Engine
The captcha engine fetches tokens simultaneously from anti-captcha and 2captcha upon request. The text boxes are for your API key's from the respective services. The engine is multithreaded so if you need 10 captcha tokens asap you can change the 'Tasks per Service' number to 10 which will yield 10 tokens being requested from both 2captcha and anti-captcha. If you don't want to use one of these two services, simply select the off radio button and the engine will not fetch a token from that service. These tokens are posted to the captcha harvester so make sure the harvester is running before requesting tokens from the engine. If you need to use these tokens they can be found at the web address http://127.0.0.1:5000/tokens.

## Account Creator
The adidas account creator uses tokens from the captcha harvester to create multiple adidas accounts. If you need to create accounts using a gmail address, make sure the 'creation style' is set to gmail. If you need to create accounts using a catch-all domain, make sure the 'creation style' is set to 'catch all'. The account creator will then create a list of email addresses and use this list to create adidas accounts. If you start the creator and it looks as though it isn't doing anything, be sure to remember to solve captchas. Sometimes if you only solve one captcha it can't find it, after solving two though it will use both tokens. The successfully created accounts will be stored in the file 'accounts.txt' in the same directory as your 'main.py'. PS: the sitekey for account creation is found at the url : https://cp.adidas.com/web/eCom/en_US/loadcreateaccount. 

## Adidas Carter
Not working.
