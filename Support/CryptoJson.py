import json
from Logic.Transaction import Transaction
from Logic.User import User
import base64
from Logic.Block import Block
from Logic.BlockChain import BlockChain
from Logic.Header import Header

TYPE_FIELD = '_type'


class CryptoEncoder(json.JSONEncoder):
    def default(self, o):
        cls_name = o.__class__.__name__
        if cls_name == Transaction.__name__:
            return {TYPE_FIELD: Transaction.__name__,
                    "sender": bytes_to_string(o.get_sender()),
                    "receiver": bytes_to_string(o.get_receiver()),
                    "amount": o.get_amount(),
                    "time": o.get_time(),
                    "signature": bytes_to_string(o.get_signature())
                    }
        elif cls_name == Header.__name__:
            return {TYPE_FIELD: Header.__name__,
                    "prev_hash": bytes_to_string(o.get_prev_hash()),
                    "root_hash": bytes_to_string(o.get_root_hash()),
                    "nonce": o.get_nonce(),
                    "miner": o.get_nonce(),
                    "time_stamp": o.get_miner(),
                    "n_bits": o.get_n_bits()
                    }
        elif cls_name == Block.__name__:
            return {TYPE_FIELD: Block.__name__,
                    "header": o.get_header(),
                    "transactions": o.get_transactions(),
                    }
        elif cls_name == BlockChain.__name__:
            return {TYPE_FIELD: BlockChain.__name__,
                    "blocks": o.get_blocks(),
                    }
        return super(CryptoEncoder, self).default(o)


class CryptoDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args,
                                  **kwargs)

    def object_hook(self, o):
        if TYPE_FIELD in o:
            if o[TYPE_FIELD] == Transaction.__name__:
                return Transaction(o['sender'],o['receiver'],o['amount'],o['time'],o['signature'])
            if o[TYPE_FIELD] == Header.__name__:
                return Header(o['prev_hash'], o['root_hash'], o['nonce'], o['miner'], time_stamp=o['time_stamp'],n_bits=o['n_bits'])
            if o[TYPE_FIELD] == Block.__name__:
                return Block(o['header'], o['transactions'])
            if o[TYPE_FIELD] == BlockChain.__name__:
                return BlockChain(o['blocks'])

        return o

def bytes_to_string(data):
    return base64.b64encode(data).decode("ascii")

def string_to_bytes(data):
    return base64.b64decode(data)

if __name__ == "__main__":
    pass
