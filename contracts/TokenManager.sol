// SPDX-License-Identifier: MIT

pragma solidity 0.8.4;

import "./Token.sol";

import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenManager is Ownable {
    Token public token;
    uint256 public lastBurnCall = 0;

    constructor(address bit2me) {
        token = new Token(bit2me);
    }

    function burn(uint256 amount) public onlyOwner {
        // Only allow burning once per day and less than 1%
        require(
            amount <= (token.maxSupply() * 10) / 1000,
            "Cannot burn more than 1% of max supply."
        );
        require(
            lastBurnCall + 1 days <= block.timestamp,
            "Cannot burn, time since last burn call is less than 24H."
        );
        lastBurnCall = block.timestamp;
        token.burn(amount);
    }

    function transferOwnershipToken(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Ownable: new owner is the zero address");
        token.transferOwnership(newOwner);
    }
}
