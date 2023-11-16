import rsa
import time
import itertools
import hashlib

class Node:

    id_iter = itertools.count()
    network = []

    def __init__(self, authority=False):
        self.id = next(self.id_iter)
        self.authority = authority
        self.public_key, self.private_key = rsa.generate_keys(100)
        self.network.append(self)

    def create_transaction(self, recipient_public_key: [int, int], data: str):
        assert recipient_public_key != self.public_key
        transaction = Transaction(self.public_key, recipient_public_key, int(data))
        self.transaction_signing(transaction)

    def transaction_signing(self, transaction):
        assert transaction.sender_public_key == self.public_key
        d, n = self.private_key
        assert len(str(n)) > len(str(transaction.hash))
        transaction.digital_signature = rsa.fast_modular_exponentiation(transaction.hash, d, n)
        self.transaction_verification(transaction)

    def transaction_verification(self, transaction):
        e, n = transaction.sender_public_key
        verified = rsa.fast_modular_exponentiation(transaction.digital_signature, e, n)
        if transaction.hash == verified:
            transaction.verified_by[self.id] = True
        else:
            transaction.verified_by[self.id] = False
        
        if self.authority:
            self.transaction_validation(transaction)

    def transaction_validation(self, transaction):
        assert self.authority
        verified_number = 0
        total = 0
        for verification in transaction.verified_by.values():
            total += 1
            if verification:
                verified_number += 1
        
        if total == len(self.network):
            if verified_number == len(self.network):
                transaction.validated = True
            else:
                transaction.validated = False
    
    def add_transaction_to_blockchain(self, transaction):
        assert self.authority and transaction.validated
        block = Block(self.public_key, transaction.data)
        self.block_signing(block)

    def block_signing(self, block):
        assert block.creator_public_key == self.public_key
        d, n = self.private_key
        assert len(str(n)) > len(str(block.hash))
        block.digital_signature = rsa.fast_modular_exponentiation(block.hash, d, n)
        self.block_verification(block)

    def block_verification(self, block):
        e, n = block.creator_public_key
        verified = rsa.fast_modular_exponentiation(block.digital_signature, e, n)
        if block.hash == verified:
            block.verified_by[self.id] = True
        else:
            block.verified_by[self.id] = False

        if self.authority:
            self.block_validation(block)        

    def block_validation(self, block):
        assert self.authority
        verified_number = 0
        total = 0
        for verification in block.verified_by.values():
            total += 1
            if verification:
                verified_number += 1
        if total == len(self.network):
            if block.id == 0:
                verified_hash = True if block.previous_hash == "000000" else False
            else:
                previous_block = block.chain[block.id - 1]
                verified_hash = True if block.previous_hash == previous_block else False

            verified_hash = block.chain[block.id-1]
            if verified_number == len(self.network) and verified_hash:
                block.validated = True
            else:
                block.validated = False

    def get_transactions_created(self, transaction):
        return [t.id for t in transaction.transactions if t.sender_public_key == self.public_key]
    
    def get_transactions_pending(self, transaction):
        verified = []
        for t in transaction.transactions:
            if len(t.verified_by) > 0:
                if self.id in t.verified_by.keys():
                    if t.verified_by[self.id] == True:
                        verified.append(t.id)

        return [t.id for t in transaction.transactions if t.id not in verified]

class Block:

    id_iter = itertools.count()
    chain = []
    
    def __init__(self, creator_public_key: [int, int], data: str):
        self.id = next(self.id_iter)
        self.creator_public_key = creator_public_key
        self.time_stamp = str(time.time())
        self.data = data
        self.digital_signature = None
        self.verified_by = {}
        self.validated = None

        if self.id == 0:
            self.previous_hash = "000000" 
        else:
            self.previous_hash = self.chain[-1].hash

        content = str(self.id) + str(self.creator_public_key[0]) + str(self.creator_public_key[1]) + str(self.previous_hash) + self.time_stamp + str(self.data)
        sha256 = hashlib.sha256()
        sha256.update(content.encode('utf-8'))
        self.hash =  int(sha256.hexdigest(), 16)
        self.chain.append(self)

    def digital_signature_decrypted(self):
        e, n = self.creator_public_key
        return rsa.fast_modular_exponentiation(self.digital_signature, e, n)

    def get_verified_blocks(self):
        return [block.id for block in self.chain if block.validated == True]
    
    def get_pending_blocks(self):
        return [block.id for block in self.chain if block.validated == None]
    
    def who_verified_blocks(self):
        nodes = []
        for key, value in self.verified_by.items():
            if value:
                nodes.append("Node " + str(key))
        return " ".join(nodes)
    
    def who_not_verified_blocks(self, node):
        nodes_who_verified = self.who_verified_blocks()
        nodes = []
        if not nodes_who_verified:
            return ", ".join([n.id for n in node.network])
        else:
            for n in node.network:
                if str(n.id) not in nodes_who_verified:
                    nodes.append("Node " + str(n.id)) 
        return ", ".join(nodes)

class Transaction:

    id_iter = itertools.count()
    transactions = []
    
    def __init__(self, sender_public_key: [int,int], recipient_public_key: [int,int], data: str):
        self.id = next(self.id_iter)
        self.sender_public_key = sender_public_key
        self.recipient_public_key = recipient_public_key
        self.data = data
        self.time_stamp = str(time.time())
        self.digital_signature = None
        self.verified_by = {}
        self.validated = None
        self.transactions.append(self)

        content = str(self.id) + str(self.sender_public_key[0]) + str(self.sender_public_key[1]) + str(self.data) + self.time_stamp
        sha256 = hashlib.sha256()
        sha256.update(content.encode('utf-8'))
        self.hash =  int(sha256.hexdigest(), 16)

    def digital_signature_decrypted(self):
        e, n = self.sender_public_key
        return rsa.fast_modular_exponentiation(self.digital_signature, e, n)
    
    def get_verified_transactions(self):
        return [transaction.id for transaction in self.transactions if transaction.validated == True]
    
    def get_pending_transactions(self):
        return [transaction.id for transaction in self.transactions if transaction.validated == None]
    
    def who_verified(self):
        nodes = []
        for key, value in self.verified_by.items():
            if value:
                nodes.append("Node " + str(key)) 
        return ", ".join(nodes)
    
    def who_not_verified(self, node):
        nodes_who_verified = self.who_verified()
        nodes = []
        if not nodes_who_verified:
            return " ".join([n.id for n in node.network])
        else:
            for n in node.network:
                if str(n.id) not in nodes_who_verified:
                    nodes.append("Node " + str(n.id)) 
        return ", ".join(nodes)
    

if __name__ == "__main__":
    ...
