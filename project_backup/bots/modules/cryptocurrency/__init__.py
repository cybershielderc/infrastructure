from typing import (
    Union,
)

import web3.exceptions
from eth_typing import (
    Address,
    ChecksumAddress
)
from web3 import (
    Web3
)
from web3.eth import (
    Eth
)
from web3.types import (
    ENS,
    HexBytes
)


class Constants:
    ALCHEMY_URL: str = "https://eth-mainnet.g.alchemy.com/v2/4fJfQZvMXo2f0CPyc92WCX0nljyqTFEv"
    LIQUIDITY_WALLET: str = "0xf5bd19c035d24d132e3974a228d5506daa4b2d70"
    DEAD_HASH: str = "0xdead"


class CouldNotConnect(Exception):
    def __init__(self, *args):
        super().__init__(f"Could not connect to Web3 Provider on url:\n{args}")


class Cryptocurrency:
    def __init__(self):
        self.provider_uri = Constants.ALCHEMY_URL
        self.w3 = Web3(Web3.HTTPProvider(Constants.ALCHEMY_URL))

    def check_connection(self) -> bool | Exception:
        if self.w3.is_connected():
            return True
        raise CouldNotConnect(self.provider_uri)

    def initiate_eth_net(self) -> bool | Exception:
        try:
            self.eth_net = Eth(self.w3)
        except Exception as e:
            raise CouldNotConnect(
                f"Could not connect to Ethereum network via the provider \n{self.provider_uri}"
            ) from e
        if self.eth_net is not None:
            if self.eth_net.w3.is_connected():
                return True
            else:
                raise CouldNotConnect(
                    f"Could not connect to Ethereum network via the provider \n{self.provider_uri}"
                )
        else:
            raise CouldNotConnect(
                f"Could not connect to Ethereum network via the provider \n{self.provider_uri}"
            )

    def format_txhash(self,
                      txHash: str) -> str:
        return f"{txHash[:2]}{txHash[2:7]}{'.' * 4}{txHash[-5:]}"

    def verify_address(
            self,
            txHash: str,
            sender_address: str,
    ) -> [bool, str]:
        try:
            transaction = self.eth_net.get_transaction(txHash)
            if transaction['from'].lower() == sender_address.lower():
                if transaction['value'] == 0:
                    if transaction['to'].lower() == Constants.LIQUIDITY_WALLET.lower():
                        return [
                            True,
                            f"✅ | Address Verified!\n"+\
                            f"     via TxHash-<strong>{self.format_txhash(transaction['hash'].hex())}</strong>"
                        ]
                    else:
                        return [
                            False,
                            f"❌ | Receiving Address does not match liquidity wallet address!\n" + \
                            f"      Make sure to send it to <strong>{Constants.LIQUIDITY_WALLET.lower()}</strong>"
                        ]
            else:
                return [
                    False,
                    "❌ | Sender address does not match the provided address to the bot!," + \
                    f"    Address Provided: <strong>{sender_address.lower()}</strong>\n"+\
                    f"    Sender Address: <strong>{transaction['from'].lower()}</strong>"
                ]
        except web3.exceptions.TransactionNotFound as e:
            return [False, str(e)]

    @staticmethod
    def is_address(address: str) -> bool:
        return Web3.is_address(address)
