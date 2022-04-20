from hashlib import sha256
from urllib.parse import urlparse
from time import time
from json import dumps

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_block_transactions = []
        self.nodes = set()

        self.add_block(proof=1203, previous_hash="1")

        self.leading_zeroes = 4

    def add_block(self, proof, previous_hash=None):
        new_block = {
            'index'         :   len(self.chain),
            'timestamp'     :   time(),
            'transactions'  :   self.current_block_transactions,
            'proof'         :   proof,
            'previous_hash' :   previous_hash or self.hash(self.chain[-1]),
        }
        self.current_block_transactions = []
        self.chain.append(new_block)
        
        return new_block

    def hash(self, block):
        block_to_str = dumps(block, sort_keys=True).encode()
        return sha256(block_to_str).hexdigest()

    def add_transaction(self, sender, recipient, amount):
        self.current_block_transactions.append(
            {
                'sender'    :   sender,
                'recipient' :   recipient,
                'amount'    :   amount,
            }
        )

    def add_node(self, address):
        url = urlparse(address)

        # adds the node if not present already
        self.nodes.add(url.netloc)

    @property
    def latest_block(self):
        return self.chain[-1]
    
    def proof_is_valid(self, proof, prev_proof):
        """
        Validates proof when appended to prev_proof.
        """
        byte_repr = f"{prev_proof}{proof}".encode()
        hashed = sha256(byte_repr).hexdigest()

        if hashed[0 : self.leading_zeroes] == "0"*self.leading_zeroes:
            return True
        
        return False

    def proof_of_work(self):
        proof = 0
        prev_proof = self.latest_block['proof']
        while not self.proof_is_valid(proof, prev_proof):
            proof += 1
            print(f"Testing {proof}")
        return proof


    def verify_chain(self, start_index=0):
        for block in self.chain[max(1, start_index):]:
            prev_block = self.chain[block['index'] - 1]
            if not self.proof_is_valid(block['proof'], prev_block['proof']):
                return False
            if self.hash(prev_block) != block['previous_hash']:
                return False

            return True