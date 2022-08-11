pragma solidity >= 0.8.0;

import "../../contracts/IFlashLoanReceiver.sol";
import "../../contracts/Pool.sol";

contract TransferReceiver is IFlashLoanReceiver {
    address donor;
    uint    transfer_amount;
    Pool    pool;

    function executeOperation(
        uint256 amount,
        uint256 premium,
        address initiator
    ) external override(IFlashLoanReceiver) returns (bool) {
        // receive tokens from a donor, and then withdraw them.  This is a valid
        // way to reduce the underlying balance of the pool.
        pool.transferFrom(donor, address(this), amount);
        pool.withdraw(amount);
    }
}

