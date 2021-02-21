from constants import *
import subprocess
import json
import pandas as pd

import os
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware             #only when working with PoA proof of authority 
from eth_account import Account

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)    #only when working with PoA proof of authority
private_key = os.getenv("PRIVATE_KEY")
account_one = Account.from_key(private_key)
account_one = Account.privateKeyToAccount(private_key)


#command = './derive -g --mnemonic="capable present used warfare pepper popular session ranch head differ fee open spoil dinner affair" --cols=path,address,privkey,pubkey --format=json'
#mnemonic = os.getenv('MNEMONIC', 'capable present used warfare pepper popular session ranch head differ fee open spoil dinner affair’)

my_mnemonic = "capable present used warfare pepper popular session ranch head differ fee open spoil dinner affair"

# --------- Derive BTC 
def derive_btc(my_mnemonic):
    command = './derive -g --mnemonic=my_mnemonic --coin=BTC --cols=path,address,privkey,pubkey --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    #print(keys)
    df = pd.DataFrame(keys)
    #print(df)
    
    return keys, df

# --------- Derive ETH 
def derive_eth(my_mnemonic):
    command = './derive -g --mnemonic=my_mnemonic --coin=ETH --cols=path,address,privkey,pubkey --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    #print(keys)
    df = pd.DataFrame(keys)
    #print(df)
    
    return keys, df

# ---------  ETH 
def xxx_eth(my_mnemonic):
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    w3.eth.getBalance("0x06297Fe891046c0Bfaaf3577259CEc070E66103a")
    private_key = os.getenv("PRIVATE_KEY")
    print(w3.eth.getBalance("0x06297Fe891046c0Bfaaf3577259CEc070E66103a"))
    print(private_key)

# ---------  
def create_raw_tx(account, recipient, amount):  
    """
        Args:
            sender - a w3 account object
            recipient - a string of an address
            amount - an integer to send
    """
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }


def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    print("signed",signed.rawTransaction)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()


# --------- Main 
def main():

    #Derive BTC
    keys_btc, df_btc = derive_btc(my_mnemonic)
    print("\n"); print("BTC keys"); print("\n")
    print(keys_btc)
    print("\n"); print("Derive BTC in df"); print("\n")
    print(df_btc)

    #Derive ETH
    keys_eth, df_eth = derive_eth(my_mnemonic)
    print("\n"); print("ETH keys"); print("\n")
    print(keys_eth)
    print("\n"); print("Derive ETH in df"); print("\n")
    print(df_eth)

    #private_key = os.getenv("PRIVATE_KEY")
    #print(Account.privateKeyToAccount(private_key))

    #send 
    address2 = Web3.toChecksumAddress('0xf0bba0e8bb3fdfdee1d0aac3e7009fb17421dcb5')
    send_tx(account_one, address2 , 5)


if __name__== "__main__":
  main()
  g = input("End Program .... Press any key : "); print (g)

  










