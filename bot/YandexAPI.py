import subprocess
import requests
import json

class YandexAPI:

    def __init__ (self, instanceId):
        self.instanceId = instanceId
        self.url = 'https://compute.api.cloud.yandex.net/compute/v1/instances/'

    def get_token(self):
        token = subprocess.Popen(['yc iam create-token'],shell=True,
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE).communicate()
        if str(token[1].decode()) == '':
            self.token = 'Bearer ' + str(token[0])[2:-3]
        else:
            self.token = None

    def request(self, method, action):
        if self.token:
            if method == 'POST':
                r = requests.post(self.url + self.instanceId + action, headers={'Authorization' : self.token })
                try:
                    status = json.loads(r.text)["done"]
                    return True 
                except:
                    return False
            elif method == 'GET':
                r = requests.get(self.url + self.instanceId + action, headers={'Authorization' : self.token })
                return r.text
            else:
                return 'Method is not supported'
            print(r.text)
            
        else:
            return('Token required!')


    def start(self):
        return self.request('POST', ':start')

    def stop(self):
        return self.request('POST', ':stop')

    def status(self):
        return json.loads(self.request('GET', ''))['status']