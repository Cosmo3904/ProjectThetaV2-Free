import requests, random, json, re, time
import classes.fetchtoken as recaptchafetch
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class adidas:
    def __init__(self, region, proxy):
        if proxy == '':
            self.proxy = ''
        else:
            self.proxy = {
                'http': proxy,
                'https': proxy.replace('http://', 'https://')
            }
        self.directproxy = proxy[:proxy.find('://')+3] + proxy[proxy.find('@')+1:]
        self.s = requests.Session()
        self.s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        self.region = region.upper()
        if self.region == 'US':
            self.atcurl = 'http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct'
            self.checkstockurl = 'https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Product-Show?pid=%08{}'
            self.loginurlbase = 'https://cp.adidas.com'
            self.loginurlgetdata = 'https://cp.adidas.com/web/eCom/en_US/loadsignin?target=account'
            self.loginurlpost = 'https://cp.adidas.com/idp/startSSO.ping'
            self.loginurlposttwo = 'https://cp.adidas.com/sp/ACS.saml2'
            self.loginurlcreatecookie = 'https://cp.adidas.com/web/ssoCookieCreate?resume={}&cd={}|{}|{}|null'
            self.loginurlmyaccount = 'https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MyAccount-ResumeLogin'
            self.myaccheaders = {
                  'Origin':self.loginurlbase,
                  'Referer':self.loginurlbase,
                  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
        elif self.region == 'AU':
            self.atcurl = 'http://www.adidas.com.au/on/demandware.store/Sites-adidas-AU-Site/en_AU/Cart-MiniAddProduct'
            self.checkstockurl = 'https://www.adidas.com.au/on/demandware.store/Sites-adidas-AU-Site/en_AU/Product-Show?pid=%08{}'
            self.loginurlbase = 'https://cp.adidas.com.au'
            self.loginurlgetdata = 'https://cp.adidas.com.au/web/eCom/en_AU/loadsignin?target=account'
            self.loginurlpost = 'https://cp.adidas.com.au/idp/startSSO.ping'
            self.loginurlposttwo = 'https://cp.adidas.com.au/sp/ACS.saml2'
            self.loginurlcreatecookie = 'https://cp.adidas.com.au/web/ssoCookieCreate?resume={}&cd={}|{}|{}|null'
            self.loginurlmyaccount = 'https://www.adidas.com.au/on/demandware.store/Sites-adidas-AU-Site/en_AU/MyAccount-ResumeLogin'
            self.myaccheaders = {
                  'Origin':self.loginurlbase,
                  'Referer':self.loginurlbase,
                  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
        elif self.region == 'GB':
            self.atcurl = 'http://www.adidas.co.uk/on/demandware.store/Sites-adidas-GB-Site/en_GB/Cart-MiniAddProduct'
            self.checkstockurl = 'https://www.adidas.co.uk/on/demandware.store/Sites-adidas-GB-Site/en_GB/Product-Show?pid=%08{}'
            self.loginurlbase = 'https://cp.adidas.co.uk'
            self.loginurlgetdata = 'https://cp.adidas.co.uk/web/eCom/en_GB/loadsignin?target=account'
            self.loginurlpost = 'https://cp.adidas.co.uk/idp/startSSO.ping'
            self.loginurlposttwo = 'https://cp.adidas.co.uk/sp/ACS.saml2'
            self.loginurlcreatecookie = 'https://cp.adidas.co.uk/web/ssoCookieCreate?resume={}&cd={}|{}|{}|null'
            self.loginurlmyaccount = 'https://www.adidas.co.uk/on/demandware.store/Sites-adidas-GB-Site/en_GB/MyAccount-ResumeLogin'
            self.myaccheaders = {
                  'Origin':self.loginurlbase,
                  'Referer':self.loginurlbase,
                  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
        elif self.region == 'CA':
            self.atcurl = 'http://www.adidas.ca/on/demandware.store/Sites-adidas-CA-Site/en_CA/Cart-MiniAddProduct'
            self.checkstockurl = 'https://www.adidas.ca/on/demandware.store/Sites-adidas-CA-Site/en_CA/Product-Show?pid=%08{}'
            self.loginurlbase = 'https://cp.adidas.ca'
            self.loginurlgetdata = 'https://cp.adidas.ca/web/eCom/en_CA/loadsignin?target=account'
            self.loginurlpost = 'https://cp.adidas.ca/idp/startSSO.ping'
            self.loginurlposttwo = 'https://cp.adidas.ca/sp/ACS.saml2'
            self.loginurlcreatecookie = 'https://cp.adidas.ca/web/ssoCookieCreate?resume={}&cd={}|{}|{}|null'
            self.loginurlmyaccount = 'https://www.adidas.ca/on/demandware.store/Sites-adidas-CA-Site/en_CA/MyAccount-ResumeLogin'
            self.myaccheaders = {
                  'Origin':self.loginurlbase,
                  'Referer':self.loginurlbase,
                  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
    def login(self, email, passw):
        try:
            res = self.s.get(self.loginurlgetdata, headers = self.myaccheaders, proxies = self.proxy)
            soup = bs(res.text, 'lxml')
            payload = {
                'username': email,
                'password': passw,
                'signinSubmit': 'Sign in'
            }
            payload['IdpAdapterId'] = soup.find('input', {'name':'IdpAdapterId'})['value']
            payload['SpSessionAuthnAdapterId'] = soup.find('input', {'name':'SpSessionAuthnAdapterId'})['value']
            payload['PartnerSpId'] = soup.find('input', {'name':'PartnerSpId'})['value']
            payload['remembermeParam'] = soup.find('input', {'name':'remembermeParam'})['value']
            payload['validator_id'] = soup.find('input', {'name':'validator_id'})['value']
            payload['TargetResource'] = soup.find('input', {'name':'TargetResource'})['value']
            payload['InErrorResource'] = soup.find('input', {'name':'InErrorResource'})['value']
            payload['loginUrl'] = soup.find('input', {'name':'loginUrl'})['value']
            payload['cd'] = soup.find('input', {'name':'cd'})['value']
            payload['app'] = soup.find('input', {'name':'app'})['value']
            payload['locale'] = soup.find('input', {'name':'locale'})['value']
            payload['domain'] = soup.find('input', {'name':'domain'})['value']
            payload['email'] = soup.find('input', {'name':'email'})['value']
            payload['pfRedirectBaseURL_test'] = soup.find('input', {'name':'pfRedirectBaseURL_test'})['value']
            payload['pfStartSSOURL_test'] = soup.find('input', {'name':'pfStartSSOURL_test'})['value']
            payload['resumeURL_test'] = soup.find('input', {'name':'resumeURL_test'})['value']
            payload['FromFinishRegistraion'] = soup.find('input', {'name':'FromFinishRegistraion'})['value']
            payload['CSRFToken'] = soup.find('input', {'name':'CSRFToken'})['value']
            res = self.s.post(self.loginurlpost, data = payload, headers = self.myaccheaders, proxies = self.proxy)
            sub = res.text[res.text.find('/idp/')+5:]
            firststring = sub[:sub.find('/idp/')]
            secondstring = sub[sub.find('/idp/')+5:sub.find("'")]
            url = '/idp/' + firststring + '/idp/' + secondstring
            res = self.s.get(self.loginurlcreatecookie.format(url.replace(' ', '%7C'), payload['cd'].replace(' ', '%7C'), payload['locale'].replace(' ', '%7C'), payload['domain'].replace(' ', '%7C')), headers = self.myaccheaders, proxies = self.proxy)
            #soup = bs(res.text, 'lxml')
            #nexturl = soup.find('img')['src']
            #self.s.get(nexturl)
            res = self.s.get(self.loginurlbase + url, headers = self.myaccheaders, proxies = self.proxy)
            soup = bs(res.text, 'lxml')
            payload = {
                'RelayState':soup.find('input', {'name':'RelayState'})['value'],
                'SAMLResponse':soup.find('input', {'name': 'SAMLResponse'})['value']
            }
            res = self.s.post(self.loginurlposttwo, data = payload, headers = self.myaccheaders, proxies = self.proxy)
            soup = bs(res.text, 'lxml')
            payload = {
                'REF':soup.find('input', {'name':'REF'})['value'],
                'TargetResource':soup.find('input', {'name':'TargetResource'})['value']
            }
            res = self.s.post(self.loginurlmyaccount, headers = self.myaccheaders, data = payload, proxies = self.proxy)
            return(True)
        except:
            return(False)


    def sizetocode(self, size):
        size = float(size)
        if size >= 4 and size <= 13:
            temp = 20 * (size - 4) + 530
            return(str(int(temp)))

    def setupatc(self, sku):
        if self.region == 'US':
            self.atcheaders = {
                'Origin':'http://www.adidas.com',
                'Referer':'http://www.adidas.com/us/' + sku + '.html',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
        elif self.region == 'AU':
            self.atcheaders = {
                'Origin':'https://www.adidas.com.au',
                'Referer':'http://www.adidas.com.au/' + sku + '.html',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
        elif self.region == 'GB':
            self.atcheaders = {
                'Origin':'https://www.adidas.co.uk',
                'Referer':'https://www.adidas.co.uk/' + sku + '.html',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
        elif self.region == 'CA':
            self.atcheaders = {
                'Origin':'https://www.adidas.ca',
                'Referer':'http://www.adidas.ca/en/' + sku + '.html',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }

    def atcupdated(self, sku, size, method):
        if type(size) is not str:
            size = random.choice(size)
        sc = self.sizetocode(size)
        if method == 'captcha':
            payload = {
                'clientCaptchaResponse' : recaptchafetch.main(),
                'invalidFields' : '[]',
                'isValidating' : 'false',
                'product_id' : sku.upper(),
                'product_variation_sku' : sku.upper() + '_' + sc,
                'quantity' : '1',
                'recipe' : '',
                'size' : size
            }

        elif method == 'basic':
            payload = {
                'clientCaptchaResponse' : '',
                'invalidFields' : '[]',
                'isValidating' : 'false',
                'product_id' : sku.upper(),
                'product_variation_sku' : sku.upper() + '_' + sc,
                'quantity' : '1',
                'recipe' : '',
                'size' : size
            }


        if self.region == 'US':
            posturl = 'https://www.adidas.com/api/cart_items?sitePath=us'
        elif self.region == 'AU':
            posturl = 'https://www.adidas.com.au/api/cart_items'
        elif self.region == 'CA':
            posturl = 'https://www.adidas.ca/api/cart_items?sitePath=en'
        elif self.region == 'GB':
            posturl = 'https://www.adidas.co.uk/api/cart_items'

        if self.proxy == '':
            res = self.s.post(posturl, headers = self.atcheaders, data = payload)
        else:
            res = self.s.post(posturl, headers = self.atcheaders, data = payload, proxies = self.proxy)

        print(res.text)

        if 'error' in res.text.lower() or 'failed' in res.text.lower() or 'out-of-stock' in res.text.lower() or 'invalid-captcha' in res.text.lower():
            return(False)
        else:
            return(True)

    def checkstock(self, sku, size):
        res = self.s.get(self.checkstockurl.format(sku.upper()))
        if 'UNFORTUNATELY WE ARE UNABLE TO GIVE YOU ACCESS TO OUR SITE AT THIS TIME' in res.text.upper():
            print('Banned Waiting 60')
            time.sleep(60)
            return(False)
        soup = bs(res.text, 'lxml')
        button = soup.find('button', {'name':'add-to-cart-button'})
        sizelist = []
        try:
            if '' in button.text:
                pass
        except:
            return(False)
        container = soup.find('select', {'name':'pid'})
        for item in container.find_all('ispagecontextset'):
            if '.' not in item['value']:
                sizelist.append(item['value'] + '.0')
            else:
                sizelist.append(item['value'])
        if size in sizelist:
            return(True)
        else:
            return(False)

    def atcbasic(self, sku, size):
        if type(size) is not str:
            size = random.choice(size)
        sc = self.sizetocode(size)
        payload = {
            'layer':'Add To Bag overlay',
            'pid':sku.upper()+'_'+sc,
            'Quantity':'1',
            'masterPid':sku.upper(),
            'sessionSelectedStoreID':'null',
            'ajax':'true',
            'responseformat':'json'
        }
        res = self.s.post(self.atcurl, headers = self.atcheaders, data = payload)
        try:
            if res.json()['result'].lower() == 'success':
                return(True)
            else:
                return(False)
        except:
            if res.json()['success'].lower() == 'true':
                return(True)
            else:
                return(False)

    def atcwrecaptcha(self, sku, size):
        if type(size) is not str:
            size = random.choice(size)
        sc = self.sizetocode(size)
        payload = {
            'layer':'Add To Bag overlay',
            'pid':sku.upper()+'_'+sc,
            'Quantity':'1',
            'g-recaptcha-response':recaptchafetch.main(),
            'masterPid':sku.upper(),
            'sessionSelectedStoreID':'null',
            'ajax':'true',
            'responseformat':'json'
        }
        res = self.s.post(self.atcurl, headers = self.atcheaders, data = payload)
        print(str(res.text))
        try:
            if res.json()['result'].lower() == 'success':
                return(True)
            else:
                return(False)
        except:
            if res.json()['success'].lower() == 'true':
                return(True)
            else:
                return(False)

    def atcdupcap(self, dupcap, clientid, sku, size):
        if type(size) is not str:
            size = random.choice(size)
        sc = self.sizetocode(size)
        recaptoken = recaptchafetch.main()
        payload = {
            'clientId':clientid,
            dupcap:recaptoken,
            'pid':sku.upper()+'_'+sc,
            'Quantity':'1',
            'g-recaptcha-response':recaptoken,
            'sessionSelectedStoreID':'null',
            'ajax':'true',
            'responseformat':'json'
        }
        res = self.s.post(self.atcurl, headers = self.atcheaders, data = payload)
        try:
            if res.json()['result'].lower() == 'success':
                return(True)
            else:
                return(False)
        except:
            if res.json()['success'].lower() == 'true':
                return(True)
            else:
                return(False)

    def opencart(self):
        chrome_options = Options()
        if self.region == 'US':
            self.chrome = webdriver.Chrome(chrome_options=chrome_options)
            self.chrome.get('https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-Show')
            for c in self.s.cookies:
                self.chrome.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires})
        elif self.region == 'AU':
            self.chrome = webdriver.Chrome(chrome_options=chrome_options)
            self.chrome.get('https://www.adidas.com.au/on/demandware.store/Sites-adidas-AU-Site/en_AU/Cart-Show')
            for c in self.s.cookies:
                self.chrome.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires})
        elif self.region == 'GB':
            self.chrome = webdriver.Chrome(chrome_options=chrome_options)
            self.chrome.get('https://www.adidas.co.uk/on/demandware.store/Sites-adidas-GB-Site/en_GB/Cart-Show')
            for c in self.s.cookies:
                self.chrome.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires})
        elif self.region == 'CA':
            self.chrome = webdriver.Chrome(chrome_options=chrome_options)
            self.chrome.get('https://www.adidas.ca/on/demandware.store/Sites-adidas-CA-Site/en_CA/Cart-Show')
            for c in self.s.cookies:
                self.chrome.add_cookie({'name': c.name, 'value': c.value, 'path': c.path, 'expiry': c.expires})
