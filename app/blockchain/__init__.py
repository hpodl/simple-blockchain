from uuid import uuid4
from app.blockchain.blockchain import Blockchain

blockchain = Blockchain()
node_id = str(uuid4()).replace('-', '')
