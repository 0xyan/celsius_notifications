import requests
import time
import json

SUBSCAN_API = ''

DOT_ADDRESSES = ["1RYwPb3Fhe4NTDDWzBz8LjtKhiUShWVR2UPPPPZRMo4o9VK",
                 "16iEyc4j5hxeSk7v64cfu2URdsxJBrgurKfzaD8BLgJ1Bmmu"]

token = ''
id_tg = ''

def send_bot(text):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id_tg}&text={text}'
    resp = requests.get(url)
    r = resp.json()
    return

def check_dot_transfer():
    last_block = 14700000
    while True:
        for address in DOT_ADDRESSES:
            response = requests.get(f"https://polkadot.api.subscan.io/api/scan/transfers", params={"row": 100, "address": address}, headers={"X-API-Key": SUBSCAN_API})
            response_json = response.json()
            print(response_json)

            for tx in response_json['data']['transfers']:
                if int(tx['block_num']) > last_block:
                    last_block = int(tx['block_num'])
                    send_bot(f"New DOT transaction in address {address}:\nAmount: {tx['amount']} DOT\nhttps://polkadot.subscan.io/extrinsic/{tx['hash']}")

        time.sleep(60)

check_dot_transfer()
