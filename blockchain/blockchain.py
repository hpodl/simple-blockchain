from hashlib import sha256

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_block_transactions = []
        self.nodes = set()

        self.leading_zeroes = 5

    def add_block(self, proof, last_hash):
        if self.proof_is_valid(proof, self.latest_block['proof']):
            new_block = {
                'last_index'    :   self.latest_block['index'] + 1,
                'transactions'  :   self.current_block_transactions,
                'proof'         :   proof,
                'previous_hash':   self.hash_block(self.latest_block),
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
    
    def proof_is_valid(self, proof, prev_proof):
        """
        Validates proof when appended to prev_proof.
        """
        byte_repr = f"{prev_proof}{proof}".encode()
        hashed = sha256(byte_repr).hexdigest()

        if hashed[0, self.leading_zeroes] == "0"*self.leading_zeroes:
            return True
        
        return False

    def hash_block(self, block = latest_block):
        pass

    def proof_of_work(self):
        proof = 0
        prev_proof = self.latest_block['proof']
        while not self.proof_is_valid(proof, prev_proof):
            proof += 1

        return proof


    def verify_chain(self, start_index = 0):
        pass
