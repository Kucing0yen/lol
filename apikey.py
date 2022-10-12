import re
from urllib import response
from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from fake_useragent import UserAgent
import os,requests,json,random,string,time

app=Flask(__name__)
api=Api(app)

CORS(app)

class Unli(Resource):
    def post(self):
        useragent=UserAgent()
        ua=useragent.random
        #apikey="5ubR3k4mm@RExCut3Dj18YUauHaooa9w82i"
        nomor=request.form.get('nomor')
        #apikey=request.form.get('apikey')
        #if "5ubR3k4mm@RExCut3Dj18YUauHaooa9w82i" in apikey:
        head={    'authority': 'www.oto.com',    'accept': 'application/json, text/javascript, */*; q=0.01',    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',    'origin': 'https://www.oto.com',    'referer': 'https://www.oto.com/ovb/user-login',    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',    'sec-ch-ua-mobile': '?0',    'sec-ch-ua-platform': '"Linux"',    'sec-fetch-dest': 'empty',    'sec-fetch-mode': 'cors',    'sec-fetch-site': 'same-origin',    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',    'x-requested-with': 'XMLHttpRequest',}
        response = requests.post('https://www.oto.com/ovb/send-otp', params={    'lang': 'id',}, cookies={    'primary_utm_campaign': 'organic',    'primary_utm_medium': 'organic',    'primary_utm_source': 'yahoo',    'utm_campaign': 'organic',    'utm_medium': 'organic',    'utm_source': 'yahoo',    'landing_url': 'https%3A%2F%2Fwww.oto.com%2F',    '_csrf': 'aG2nJALlO7VyltTb-atrM-_EXaThOQri',    'GCLB': 'CPH61KyGt9yB2wE',    '_gcl_au': '1.1.60394401.1662191705',    '_pbjs_userid_consent_data': '3524755945110770',    'pbjs-pubCommonId': '0c3d7536-4c41-4e8c-8078-ede03a294dfe',    '_ga': 'GA1.2.1220515766.1662191705',    '_gid': 'GA1.2.525526430.1662191705',    '_gat': '1',    '_co_session_active': '1',    '_CO_anonymousId': '65ad5b8b-31fe-0728-c3ce-e208c717c122',    '_CO_type': 'connecto',    '_fbp': 'fb.1.1662191705704.1893770966',    '_dc_gtm_UA-58094033-8': '1',    '_lr_retry_request': 'true',    '_lr_env_src_ats': 'false',    '__gads': 'ID=0d3fa2b6107a5244:T=1662191707:S=ALNI_MbMDDAdViTY4nYB086vSjMp8axBUw',    '__gpi': 'UID=0000096baa896e74:T=1662191707:RT=1662191707:S=ALNI_MbpMPTZyUO8x5wnAh3T1Qq5rVKPDw',    'pubmatic-unifiedid': '%7B%22TDID%22%3A%22b8d808f8-e3d6-4b01-bfb5-34a077fe952a%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-08-03T07%3A55%3A08%22%7D',    'panoramaId_expiry': '1662796507670',    '_cc_id': 'a270b7341af8c173e8f2aa3f71b7accd',    'panoramaId': '3cc178a793a7f2c651c73fe7475c16d53938dce698845cc3fb7fea782d2fbcf3',    'pbjs_debug': '0',    'page_view': '1',    'cto_bidid': 'ilf0CV9KN1ZCRzExY1NYMXNqVmclMkJlZ3k4azlIem9NbHhaa1pXYWlCQlhmJTJCVjdCMGhwOUhkRWV4UTNoOFhMbjVLaXpUT2JiN24yNEhCOER6RDZuVFVpSWpYdVElM0QlM0Q',    'cto_bundle': 'yx0Sy185U09IckR1WW4waUNkSmpoY1VFMGdVa2dZSk1VdEYlMkY2bSUyQmhDSG0lMkJ2ZFRUR0FPaG5nTHFrY1ZiQ2IzSGtodmE5dWExeDVNdllUcW1tMXFmMnQ2WUQwZVc1dEREaGJjZ1ZhVzlDZmpzWlQzayUzRA',}, headers=head, data={    'mobile': nomor,    'bookingId': '0',    'businessUnit': 'mobil',}).text
        if "true" in response:
            return (
            {
                "mssg":"success",
                "user-agent":ua,
                "code":200
            }
        )
        else:
            return (
            {
                "mssg":"access denied",
                "user-agent":ua,
                "code":200
            }
        )

api.add_resource(Unli, "/api/smsunli")
if __name__ == "__main__":
    app.run(debug=True,port=3000)
