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
        return(True)
    except:
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
            'g-recaptcha-response' : fetchtoken(),
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
        res = s.get(geturl)
        res = s.get('https://cp.adidas.com' + resumeurl)
        return(True)
    except:
        return(False)
