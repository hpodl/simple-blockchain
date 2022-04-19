from hashlib import sha256

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_block_transactions = []
        self.nodes = set()

        self.leading_zeroes = 5

    def add_block(self, proof):
        if self.validate_proof(proof):
            new_block = {
                'last_index'    :   self.latest_block['index'] + 1,
                'transactions'  :   self.current_block_transactions,
                'proof'         :   proof,
                'previous_proof':   self.latest_block['proof'],
            }

            self.current_block_transactions = []

    def add_transaction(self, sender, recipient, amount):
        self.current_block_transactions.append(
            {
                'sender'    :   sender,
                'recipient' :   recipient,
                'amount'    :   amount,
            }
        )

    @property
    def latest_block(self):
        return self.chain[-1]
    
    def proof_is_valid(self, proof, prev_proof = None):
        """
        Validates proof when appended to prev_proof. If prev_proof arg is not given, assumes the latest block.
        """
        byte_repr = f"{prev_proof}{proof}".encode()
        hash = sha256(byte_repr).hexdigest()

        if hash[0, self.leading_zeroes] == "0"*self.leading_zeroes:
            return True
        
        return False
        

    def verify_chain(self, start_index = 0):
        pass