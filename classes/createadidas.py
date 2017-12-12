import requests
from bs4 import BeautifulSoup as bs
from classes.fetchtoken import main as fetchtoken

def createv2(first, last, email, password):
    try:
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-US,en;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Content-Length':'580',
            'Content-Type':'application/x-www-form-urlencoded',
            'DNT':'1',
            'Host':'shop.miteam.adidas.us',
            'Origin':'https://shop.miteam.adidas.us',
            'Referer':'https://shop.miteam.adidas.us/miadidas-miteam/Logout.action',
            'Upgrade-Insecure-Requests':'1'
        }
        res = s.get('http://www.miteam.adidas.us/on/demandware.store/Sites-miTeam-Site/en_US/Home-Show')
        res = s.get('https://shop.miteam.adidas.us/miadidas-miteam/Logout.action')
        soup = bs(res.text, 'lxml')
        payload = {
            'registerUser' : soup.find('input', {'name':'registerUser'})['value'],
            'sourcePath' : soup.find('input', {'name':'sourcePath'})['value'],
            'recipeIdent' : soup.find('input', {'name':'recipeIdent'})['value'],
            'orderId' : soup.find('input', {'name':'orderId'})['value'],
            'minAge' : soup.find('input', {'name':'minAge'})['value'],
            'userVO.userAuthentication.regFirstName' : first,
            'userVO.userAuthentication.regLastName' : last,
            'userVO.userAuthentication.regLogin' : email,
            'userVO.userAuthentication.regPassword' : password,
            'userVO.userAuthentication.confrmPassword' : password,
            'userVO.newsUpdate' : 'false',
            'agree' : 'true',
            'userVO.dateVO.day' : '1',
            'userVO.dateVO.month' : '1',
            'userVO.dateVO.year' : '1953',
            '_sourcePage' : soup.find('input', {'name':'_sourcePage'})['value'],
            '__fp' : soup.find('input', {'name':'__fp'})['value']
        }
        res = s.post('https://shop.miteam.adidas.us/miadidas-miteam/Login.action', data = payload, headers = headers)
        if login(email, password):
            return(True)
        else:
            print('Error : Failed Logging In')
            return(False)
    except Exception as f:
        print('Error : ' + f)
        return(False)


def createaccount(first, last, email, password):
    try:
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-US,en;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Content-Length':'549',
            'Content-Type':'application/x-www-form-urlencoded',
            'DNT':'1',
            'Host':'cp.adidas.com',
            'Origin':'https://cp.adidas.com',
            'Referer':'https://cp.adidas.com/web/eCom/en_US/accountcreate',
            'Upgrade-Insecure-Requests':'1'
        }
        res = s.get('https://cp.adidas.com/web/eCom/en_US/loadcreateaccount')
        soup = bs(res.text, 'lxml')
        recaptoken = fetchtoken()
        payload = {
            'firstName' : first,
            'lastName' : last,
            'minAgeCheck' : 'true',
            '_minAgeCheck' : 'on',
            'email' : email,
            'password' : password,
            'confirmPassword' : password,
            '_amf' : 'on',
            'terms' : 'true',
            '_terms' : 'on',
            'g-recaptcha-response' : recaptoken,
            'metaAttrs[pageLoadedEarlier]':'true',
            'app':'eCom',
            'locale':'en_US',
            'domain':'',
            'consentData1':'Sign me up for adidas emails, featuring exclusive offers, latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Privacy Policy</a> for details.',
            'consentData2':'',
            'consentData3':'',
            'CSRFToken': soup.find('input', {'name':'CSRFToken'})['value']
        }
        res = s.post('https://cp.adidas.com/web/eCom/en_US/accountcreate', data = payload, headers = headers)
        if 'spsessionauthnadapterid' not in res.text.lower():
            return(False)
        soup = bs(res.text, 'lxml')
        payload = {
            "IdpAdapterId" : soup.find('input', {'name':'IdpAdapterId'})['value'],
            "PartnerSpId" : soup.find('input', {'name':'PartnerSpId'})['value'],
            "SpSessionAuthnAdapterId" : soup.find('input', {'name':'SpSessionAuthnAdapterId'})['value'],
            "TargetResource" : soup.find('input', {'name':'TargetResource'})['value'],
            "InErrorResource" : soup.find('input', {'name':'InErrorResource'})['value'],
            "loginUrl" : soup.find('input', {'name':'loginUrl'})['value'],
            "cd" : soup.find('input', {'name':'cd'})['value'],
            "username" : soup.find('input', {'name':'username'})['value'],
            "password" : soup.find('input', {'name':'password'})['value'],
            "validator_id" : soup.find('input', {'name':'validator_id'})['value'],
            "app" : soup.find('input', {'name':'app'})['value']
        }
        res = s.post('https://cp.adidas.com/idp/startSSO.ping', data = payload, headers = headers)
        resumeurl = res.text[res.text.find('cp.adidas.com/idp')+13:res.text.find('resumeSAML20')+30]
        resumeurldata = res.text[res.text.find('cp.adidas.com/idp')+13:res.text.find('resumeSAML20')+30].replace('/','%2f')
        resumeurldata2 = 'eCom|en_US|cp.adidas.com|null'.replace('|', '%7C')
        geturl = res.text[res.text.find('https://cp.adidasspecialty'):res.text.find('ssoiniturl')+32].replace('amp;','')
        res = s.get('https://cp.adidas.com/web/ssoCookieCreate?' + resumeurldata + '&' + resumeurldata2, headers = headers)
        return(True)
    except Exception as f:
        print('Error : ' + f)
        return(False)

def login(email, passw):
    try:
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
        headers = {
          'Origin':'https://cp.adidas.com',
          'Referer':'https://cp.adidas.com',
          'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        }
        res = s.get('https://cp.adidas.com/web/eCom/en_US/loadsignin?target=account', headers = headers)
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
        res = s.post('https://cp.adidas.com/idp/startSSO.ping', data = payload, headers = headers)
        sub = res.text[res.text.find('/idp/')+5:]
        firststring = sub[:sub.find('/idp/')]
        secondstring = sub[sub.find('/idp/')+5:sub.find("'")]
        url = '/idp/' + firststring + '/idp/' + secondstring
        res = s.get('https://cp.adidas.com/web/ssoCookieCreate?resume={}&cd={}|{}|{}|null'.format(url.replace(' ', '%7C'), payload['cd'].replace(' ', '%7C'), payload['locale'].replace(' ', '%7C'), payload['domain'].replace(' ', '%7C')), headers = headers)
        #soup = bs(res.text, 'lxml')
        #nexturl = soup.find('img')['src']
        #self.s.get(nexturl)
        res = s.get('https://cp.adidas.com' + url, headers = headers)
        soup = bs(res.text, 'lxml')
        payload = {
            'RelayState':soup.find('input', {'name':'RelayState'})['value'],
            'SAMLResponse':soup.find('input', {'name': 'SAMLResponse'})['value']
        }
        res = s.post('https://cp.adidas.com/sp/ACS.saml2', data = payload, headers = headers)
        soup = bs(res.text, 'lxml')
        payload = {
            'REF':soup.find('input', {'name':'REF'})['value'],
            'TargetResource':soup.find('input', {'name':'TargetResource'})['value']
        }
        res = s.post('https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MyAccount-ResumeLogin', headers = headers, data = payload)
        return(True)
    except:
        return(False)
