import requests, time

class TwoCaptchaCosmo:
    def __init__(self, apikey, sitekey, url):
        self.s = requests.Session()
        self.apikey = apikey
        self.sitekey = sitekey
        self.url = url
    def Solve(self):
        postpayload = {
            'key' : self.apikey,
            'method' : 'userrecaptcha',
            'googlekey' : self.sitekey,
            'pageurl' : self.url,
            'json' : '1'
        }

        res = self.s.post('http://2captcha.com/in.php', data = postpayload)
        capid = res.json()['request']

        if capid == 'ERROR_ZERO_BALANCE':
            return('ERROR_ZERO_BALANCE')

        while True:
            getpayload = {
                'action' : 'get',
                'key' : self.apikey,
                'id' : capid
            }

            res = self.s.post('http://2captcha.com/res.php', data = getpayload)

            while 'NOT_READY' in res.text:
                time.sleep(5)
                res = self.s.post('http://2captcha.com/res.php', data = getpayload)

            return(res.text[res.text.find('|')+1:])
