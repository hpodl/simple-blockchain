import flask
from . import api

@api.route('/chain', methods=['GET', 'POST'])
def get_chain():
    return "Chain"