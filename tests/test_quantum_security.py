import pytest
from src.quantum_security import encrypt_data

def test_encrypt_data():
    data = "Test data".encode('utf-8')
    encrypted = encrypt_data(data)
    assert isinstance(encrypted, np.ndarray)
    assert len(encrypted) == len(data)
