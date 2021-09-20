from brownie import Token, TokenManager, accounts


def main():
    acct = accounts.load("mainnet")
    token_manager = TokenManager.deploy(
        "0xF7E2D2bA320020fE1B6975b049a8afff4a5aC6C7",
        {"from": acct},
        publish_source=True,
    )

    # Verify token contract
    Token.at(token_manager.token())
    print(Token.get_verification_info())
