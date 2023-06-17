import requests
import time

BLOCKFROST_API_KEY = ''
ADA_ADDRESSES = ['addr1q80wuctzysklh29970et89lzhwr7lcxwma6f23j938alsupvh5wzne6hk7v8fp264p27hl9f6r6v9zh3gk02u8u3f7tq8ujrdn', 
                 'addr1q862vgjrjezhh6zwd2ezpct42fky3xlk4v3ft0y2al65fwyk4pqfglhusay52ym4mnhqrp82ntwmf760s5affjzmpthsgcxqtj']
TOKEN_DECIMALS = 6

#telegram API
token = ''
id_tg = ''

def send_bot(text):
    url = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+id_tg+'&text='+text+''
    resp = requests.get(url)
    r = resp.json()
    return

def check_ada_transfer():
    last_height = 8840848
    while True:
        for address in ADA_ADDRESSES:
            response = requests.get(f"https://cardano-mainnet.blockfrost.io/api/v0/addresses/{address}/transactions", headers={"project_id": BLOCKFROST_API_KEY})
            response_json = response.json()

            for tx in response_json:
                if int(tx['block_height']) > last_height:
                    last_height = int(tx['block_height'])
                    send_bot(f"New ADA transaction in address {address}: https://cardanoscan.io/transaction/{tx['tx_hash']}")

        time.sleep(60)
 
check_ada_transfer()
