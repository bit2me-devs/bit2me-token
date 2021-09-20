import brownie
import pytest
from brownie import Token, accounts


@pytest.fixture
def max_supply():
    return brownie.web3.toWei(5_000_000_000, "ether")


@pytest.fixture
def token():
    return accounts[0].deploy(Token, accounts[0])
