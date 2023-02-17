import os
import time
import requests
from dotenv import load_dotenv
from typing import Tuple, Optional

load_dotenv()

def get_ip() -> Tuple[str, Optional[str]]:
    data_v4 = requests.get('https://api.ipify.org?format=json')
    v4 = data_v4.json()['ip']
    data_v6 = requests.get('https://api64.ipify.org?format=json')
    if data_v6.json()['ip'] == v4:
        v6 = None
    else:
        v6 = data_v6.json()['ip']
    return v4, v6

if __name__ == '__main__':
    v4, v6 = None, None
    while True:
        v4_, v6_ = get_ip()
        if os.getenv("ALWAYS_REPORT", 'False') == 'True' or v4_ != v4 or v6_ != v6:
            v4, v6 = v4_, v6_
            requests.post(os.getenv("WEBHOOK_URL", ''), json={"v4": v4, "v6": v6})
        time.sleep(float(os.getenv("FETCH_INTERVAL", '60')))