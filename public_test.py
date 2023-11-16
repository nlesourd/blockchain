import pytest

import blockchain as bc
import rsa

@pytest.fixture(scope="module")
def node1():
    return bc.Node(authority=True)

@pytest.fixture(scope="module")
def node2():
    return bc.Node()

@pytest.fixture(scope="module")
def transaction1(node1, node2):
    return bc.Transaction(node1.public_key, node2.public_key, 5134564234)

@pytest.fixture(scope="module")
def block1(node1):
    return bc.Block(node1.public_key, 5134564234)

@pytest.fixture(scope="module")
def block2(node1):
    return bc.Block(node1.public_key, 3134564234)

#Test blockchain

def test_transaction_signing(transaction1):
    assert transaction1.data == 5134564234
    assert transaction1.digital_signature == None

def test_transaction_verification(transaction1, node1, node2):
    node1.transaction_signing(transaction1)
    assert transaction1.data == 5134564234
    assert transaction1.digital_signature != None 

    node2.transaction_verification(transaction1)
    assert transaction1.verified_by[node2.id] == True

    transaction1.hash = 513456423
    node2.transaction_verification(transaction1)
    assert transaction1.verified_by[node2.id] == False

def test_transaction_validation(transaction1, node1, node2):
    transaction1.verified_by = {}
    node1.transaction_signing(transaction1)

    node2.transaction_verification(transaction1)
    node1.transaction_validation(transaction1)
    assert transaction1.validated == True

    assert 0 == transaction1.get_verified_transactions()[0]


def test_transaction_pending(transaction1, node1, node2):
    transaction1.validated = None
    assert transaction1.get_pending_transactions()[0] == 0

def test_block_signing(block1, node1):
    assert block1.data == 5134564234
    assert block1.digital_signature == None 

    node1.block_signing(block1)

    assert block1.data == 5134564234
    assert block1.digital_signature != None
    assert block1.id == 0

def test_block_verification(block1, node1, node2):
    node1.block_signing(block1)
    assert block1.data == 5134564234
    assert block1.digital_signature != None 

    node2.block_verification(block1)
    assert block1.verified_by[node2.id] == True

    block1.hash = 513456423
    node2.block_verification(block1)
    assert block1.verified_by[node2.id] == False

def test_chain(block1, block2):
    assert block2.previous_hash == block1.hash

#TEST RSA

def test_isprime():
    prime_numbers = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for prime_number in prime_numbers:
        assert rsa.isprime_miller_rabin(prime_number)
    non_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99]
    for non_prime_number in non_prime_numbers:
        assert not rsa.isprime_miller_rabin(non_prime_number)

def test_modular_exponentiation():
    assert rsa.fast_modular_exponentiation(2,10,7) == 2
    assert rsa.fast_modular_exponentiation(5,7,11) == 3
    assert rsa.fast_modular_exponentiation(3,20,17) == 13
    assert rsa.fast_modular_exponentiation(2,64,13) == 3
    assert rsa.fast_modular_exponentiation(17,3,5) == 3

def test_modular_inverse():
    assert rsa.modular_inverse(7,10) == 3
    assert rsa.modular_inverse(11,5) == 1
    assert rsa.modular_inverse(20,17) == 6
    assert rsa.modular_inverse(64,13) == 12
    assert rsa.modular_inverse(3,5) == 2