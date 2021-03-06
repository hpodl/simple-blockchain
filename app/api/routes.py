import flask
from . import api
from app.blockchain import blockchain, node_id

@api.route('/chain', methods=['GET'])
def get_chain():
    response = {
        'chain' : blockchain.chain,
        'length' : blockchain.latest_block['index'] + 1
    }

    return flask.jsonify(response), 200


@api.route('/mine', methods=['GET'])
def mine():
    proof = blockchain.proof_of_work()
    if blockchain.proof_is_valid(proof, blockchain.latest_block['proof']):
        #reward the miner for mining a new block
        blockchain.add_transaction(
            sender = "0",
            recipient = node_id,
            amount = 1
        )

        new_block = blockchain.add_block(proof)
        
        response = {
            'message'       :   "Mined a new block.",
            'id'            :   new_block['index'],
            'transactions'  :   new_block['transactions'],
            'previous_hash' :   new_block['previous_hash'],
            'proof'         :   new_block['proof'],
        }

    return flask.jsonify(response), 200

@api.route('/verify', methods=['GET'])
def verify():
    return "Valid chain" if blockchain.verify_chain() else "Invalid chain"