# pip3 install cosmpy
# pip3 install sentinel-protobuf

from cosmpy.aerial.client import LedgerClient, NetworkConfig
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey
from sentinel_protobuf.sentinel.subscription.v1.msg_pb2 import MsgCancelRequest, MsgCancelResponse
from cosmpy.aerial.tx import Transaction
from cosmpy.aerial.client.utils import prepare_and_broadcast_basic_transaction

cfg = NetworkConfig(
    chain_id="sentinelhub-2",
    url="grpc+http://aimokoivunen.mathnodes.com:9090/",
    fee_minimum_gas_price=0.4,
    fee_denomination="udvpn",
    staking_denomination="udvpn",
)

client = LedgerClient(cfg)


mnemonic = "maximum merge ..."

seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
bip44_def_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.COSMOS).DeriveDefaultPath()
wallet = LocalWallet(PrivateKey(bip44_def_ctx.PrivateKey().Raw().ToBytes()), prefix="sent")


address = wallet.address()
print(f"Address: {address}")


tx = Transaction()
tx.add_message(MsgCancelRequest(id=1255))

tx = prepare_and_broadcast_basic_transaction(client, tx, wallet)
tx.wait_to_complete()
print(tx)



