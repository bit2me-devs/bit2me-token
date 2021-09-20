import brownie
import pytest
from brownie import accounts


@pytest.mark.usefixtures("token", "max_supply")
def test_wei_sent_creation(token, max_supply):
    assert token.balanceOf(accounts[0]) == max_supply


@pytest.mark.usefixtures("token")
def test_burn_fails_no_owner(token):
    with brownie.reverts():
        token.burn(1, {"from": accounts[1]})


@pytest.mark.usefixtures("token", "max_supply")
def test_burn(token, max_supply):
    token.burn(1, {"from": accounts[0]})
    assert token.totalSupply() == max_supply - 1


@pytest.mark.usefixtures("token")
def test_owner_creation(token):
    assert token.owner() == accounts[0]


@pytest.mark.usefixtures("token")
def test_change_owner(token):
    token.transferOwnership(accounts[1])
    assert token.owner() == accounts[1]
