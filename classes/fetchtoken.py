import requests, json

tokens = []

def main():
    global Tokens
    s = requests.Session()
    while True:
        try:
            res = s.get('127.0.0.1:5000/json')
            break
        except:
            pass
    json_dict = res.json()
    index = 0
    capToken = 'temp'
    while True:
        try:
            capToken = json_dict['tokens'][index]
        except IndexError:
            index = 0
            while True:
                try:
                    res = s.get('127.0.0.1:5000/json')
                    break
                except:
                    pass
            json_dict = res.json()
            pass
        if capToken in tokens:
            index = index + 1
        elif capToken == 'temp':
            pass
        elif capToken == '':
            index = index + 1
        else:
            tokens.append(capToken)
            return(capToken)
