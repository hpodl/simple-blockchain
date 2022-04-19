import flask
from numpy import block
from . import api
from start import blockchain


@api.route('/chain', methods=['GET', 'POST'])
def get_chain():
    return "Chain"


@api.route('/mine', methods=['GET'])
def mine():
    proof = blockchain.proof_of_work()
    if blockchain.proof_is_valid(proof):
        reward_transaction = blockchain.add_transaction(
            sender = "0",
            recipient = 123, #node_id,
            amount = 1
        )
        
        
        response = {
            'message'   :   "Mined a new block.",
            'id'        :   blockchain.latest_block['index'] + 1,

        }
    
