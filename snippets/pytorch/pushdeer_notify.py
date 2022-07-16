import requests as re

def notify(msg):
    url = 'https://sctapi.ftqq.com/SCT160821TEnYN0KqYnj7ngDlN6euZD7H6.send'

    data ={
        'title': 'ViT-STR Training on 10142',
        'content': msg,
    }
    re.post(url, data=data)

msg = 'Iteration [1/300000] TraLos=0.2342423 ValLos=0.24242 CurAcc=9.2324 BesAcc=12.4244'
notify(msg)
