from decimal import Decimal

import brownie
import pytest
from brownie import Token, TokenManager, accounts
from brownie.network.state import Chain

from tests.constants import MAX_SUPPLY


@pytest.fixture
def token_manager():
    return accounts[0].deploy(TokenManager, accounts[0])


def test_burn_fails_no_owner(token_manager):
    with brownie.reverts():
        token_manager.burn(1, {"from": accounts[1]})


@pytest.mark.usefixtures("max_supply")
def test_burn(token_manager, max_supply):
    token = Token.at(token_manager.token())

    token_manager.burn(1, {"from": accounts[0]})
    assert token.totalSupply() == max_supply - 1

    chain = Chain()
    chain.sleep(86400)  # A day

    token_manager.burn(1, {"from": accounts[0]})
    assert token.totalSupply() == max_supply - 2


def test_burn_two_times_one_day_fails(token_manager):
    token_manager.burn(1, {"from": accounts[0]})
    with brownie.reverts():
        token_manager.burn(1, {"from": accounts[1]})


@pytest.mark.usefixtures("max_supply")
def test_burn_more_than_1_percent_fails(token_manager, max_supply):
    with brownie.reverts():
        token_manager.burn(max_supply * 0.011, {"from": accounts[0]})


@pytest.mark.usefixtures("max_supply")
def test_burn_1_percent(token_manager, max_supply):
    token_manager.burn(max_supply * 0.01, {"from": accounts[0]})

    token = Token.at(token_manager.token())

    # Convert to decimal to avoid precision errors
    assert token.totalSupply() == max_supply * Decimal("0.99")


def test_owner_creation(token_manager):
    assert token_manager.owner() == accounts[0]


def test_change_owner(token_manager):
    token_manager.transferOwnership(accounts[1])
    assert token_manager.owner() == accounts[1]


def test_change_token_owner(token_manager):
    token_manager.transferOwnershipToken(accounts[1])
    token = Token.at(token_manager.token())
    assert token.owner() == accounts[1]
