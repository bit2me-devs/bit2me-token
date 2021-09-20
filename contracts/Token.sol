// SPDX-License-Identifier: MIT

pragma solidity 0.8.4;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Token is ERC20, Ownable {
    address public bit2me;
    uint256 public maxSupply = 5000000000 ether;

    constructor(address bit2me_) ERC20("Bit2Me", "B2M") {
        bit2me = bit2me_;
        _mint(bit2me, maxSupply);
    }

    function burn(uint256 amount) public onlyOwner {
        _burn(bit2me, amount);
    }
}
