# ProjectThetaV2-Free

## INSTALL THE FONT FILE FIRST OR NOTHING WILL LOOK RIGHT
## Before first run of the script run the following command : pip3 install pyqt5 requests flask python_anticaptcha lxml bs4

## Captcha Harvester
The captcha harvester starts a web server on port 5000 using your local IP address. You can view this webpage by going to http://127.0.0.1:5000/solve however it's likely you will get the error 'localhost is not a supported domain' or something of the sort. To fix this you need to append your hosts file. On windows, this file is located in the directory 'C:\Windows\System32\drivers\etc\hosts'. On linux or osx, this file is located in the directory '/etc/hosts'. To append this file you will open your hosts file and add '127.0.0.1    dev.adidas.com' for adidas to the end of the file (and if you're harvesting for a different website just follow that format, for example supremenewyork would be '127.0.0.1    dev.supremenewyork.com'). After you've done this, the webpage you added to your hosts will now take place of 127.0.0.1 in the previous url EG: http://dev.adidas.com:5000/solve. After solving tokens, the successfully created tokens will be stored in the webpage http://127.0.0.1:5000/tokens. All tokens expire after 110 seconds because recaptcha tokens are only valid for 2 minutes. 

## Captcha Engine
The captcha engine fetches tokens simultaneously from anti-captcha and 2captcha upon request. The text boxes are for your API key's from the respective services. The engine is multithreaded so if you need 10 captcha tokens asap you can change the 'Tasks per Service' number to 10 which will yield 10 tokens being requested from both 2captcha and anti-captcha. If you don't want to use one of these two services, simply select the off radio button and the engine will not fetch a token from that service. These tokens are posted to the captcha harvester so make sure the harvester is running before requesting tokens from the engine. If you need to use these tokens they can be found at the web address http://127.0.0.1:5000/tokens.

## Account Creator
Update: Changed account creation to be done on the .co.uk domain for adidas. All accounts are universal but when being created on the US server the minimum age requirement was causing issues with other domains, this was fixed by switching the sign up to the GB locale. Thanks!

The adidas account creator creates a list of email address(s) depending on the email creation style. If using gmail you will enter the normal gmail address. If using catch-all you will just enter the domain of the email server. After this is done, the script will create the accounts and test them by signing into adidas once. Each account needs a captcha token that the script pulls from the captcha harvester's successful tokens which are stored for 110 seconds @ http://127.0.0.1:5000/tokens. The sitekey for account creation can be found on the page : https://cp.adidas.co.uk/web/eCom/en_GB/loadcreateaccount

## Adidas Carter
Proxies must be saved in a file with only one proxy per line. Proxies must be in the format STYLEOFPROXIES://USERNAME:PASSWORD@IPADDRESS:PORT. If your proxies do not have usernames and passwords just remove the username:password@. Your proxy would only need to be STYLEOFPROXY://IPADDRESS:PORT. So, for example a socks5 proxy with the username of cosmo and password of coolpass @ the ipaddress of 8.8.8.8 using the port 8080 the format would be: socks5://cosmo:coolpass@8.8.8.8:8080. The program does not currently support adidas accounts for logging into the carted items. You can however do this manually with the browsers that open up. Im not sure but I don't think the timer currently works either, if someone can test that and get back to me that would be great. Thanks.
