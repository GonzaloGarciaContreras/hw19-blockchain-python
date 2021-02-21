import os
from dotenv import load_dotenv
load_dotenv()
from web3 import Web3

key = os.getenv("PRIVATE_KEY")
# print(key)

# conn represents CONNECTION to the ethereum network running on our local machine
conn = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

address2 = Web3.toChecksumAddress('0x6E02eD14fd20A4f7A42197D0C0134f015E3e16Bb')
balance = conn.eth.getBalance(address2)

#print(balance)
