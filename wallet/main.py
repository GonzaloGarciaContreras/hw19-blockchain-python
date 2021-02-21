import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

w3.eth.getBalance("0xf0bba0e8bb3fdfdee1d0aac3e7009fb17421dcb5")

private_key = os.getenv("PRIVATE_KEY")

print(w3.eth.getBalance("0xf0bba0e8bb3fdfdee1d0aac3e7009fb17421dcb5"))
print(private_key)
