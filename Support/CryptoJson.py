import json
from Logic.Transaction import Transaction
from Logic.Block import Block
from Logic.BlockChain import BlockChain
from Logic.Header import Header

TYPE_FIELD = '_type'


class CryptoEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Transaction):
            return {TYPE_FIELD: Transaction.__name__,
                    "sender": o.get_sender(),
                    "receiver": o.get_receiver(),
                    "amount": o.get_amount(),
                    "time": o.get_time(),
                    "singature": o.get_signature()
                    }
        elif isinstance(o, Header):
            return {TYPE_FIELD: Header.__name__,
                    "prev_hash": o.get_prev_hash(),
                    "root_hash": o.get_root_hash(),
                    "transactions": o.get_nonce(),
                    "nonce": o.get_nonce(),
                    "miner": o.get_miner(),
                    "n_bits": o.get_n_bits()
                    }
        elif isinstance(o, Block):
            return {TYPE_FIELD: Block.__name__,
                    "header": o.header(),
                    "receiver": o.get_receiver(),
                    "amount": o.get_amount(),
                    "time": o.get_time(),
                    "singature": o.get_signature()
                    }
        elif isinstance(o, BlockChain):
            return {TYPE_FIELD: BlockChain.__name__,
                    "sender": o.get_sender(),
                    "receiver": o.get_receiver(),
                    "amount": o.get_amount(),
                    "time": o.get_time(),
                    "singature": o.get_signature()
                    }


1


class CryptoDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args,
                                  **kwargs)

    def object_hook(self, o):
        if TYPE_FIELD in o:
            if o[TYPE_FIELD] == Transaction.__name__:
                pass
            if o[TYPE_FIELD] == Block.__name__:
                pass
            if o[TYPE_FIELD] == BlockChain.__name__:
                pass

        return o
