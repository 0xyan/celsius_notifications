ETHERSCAN_API_KEY = ""
MATIC_CONTRACT = "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0"
SNX_CONTRACT = "0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F"

MATIC_ADDRESS_1 = "0x9477242c59fadf137ea8a1d8be46ee7cf3b3c614"
MATIC_ADDRESS_2 = "0xC131701Ea649AFc0BfCc085dc13304Dc0153dc2e"

SNX_ADDRESS_1 = "0xDb31651967684A40A05c4aB8Ec56FC32f060998d"
SNX_ADDRESS_2 = "0x41318419CFa25396b47A94896FfA2C77c6434040"

DECIMALS = 18

CONTRACTS_ADDRESSES = {
    MATIC_CONTRACT: [MATIC_ADDRESS_1, MATIC_ADDRESS_2],
    SNX_CONTRACT: [SNX_ADDRESS_1, SNX_ADDRESS_2],
}

#telegram API
token = ''
id_tg = ''

def send_bot(text):
    url = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+id_tg+'&text='+text+''
    resp = requests.get(url)
    r = resp.json()
    return

  
def check_token_transfer():
    last_block = 17497063
    while True:
        for contract, addresses in CONTRACTS_ADDRESSES.items():
            for address in addresses:
                response = requests.get(f"https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={contract}&address={address}&startblock={last_block}&endblock=999999999&sort=asc&apikey={ETHERSCAN_API_KEY}")
                response_json = response.json()

                if response_json['status'] == "1":
                    for tx in response_json['result']:
                        if int(tx['blockNumber']) > last_block:
                            last_block = int(tx['blockNumber'])
                            value = int(tx['value']) / (10 ** DECIMALS)
                            send_bot(text=f"New token transfer: {value} {tx['tokenSymbol']}\nhttps://etherscan.io/tx/{tx['hash']}")

        time.sleep(60)

  
 
