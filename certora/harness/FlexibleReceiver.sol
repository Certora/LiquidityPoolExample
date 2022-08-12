pragma solidity >= 0.8.0;

import "../../contracts/IFlashLoanReceiver.sol";
import "../../contracts/IPool.sol";

contract FlexibleReceiver is IFlashLoanReceiver {
    IPool   token;
    uint8   callbackChoice;

    uint    arbitraryUint;
    address arbitraryAddress1;
    address arbitraryAddress2;

    function executeOperation(
        uint256 amount,
        uint256 premium,
        address initiator
    ) external override(IFlashLoanReceiver) returns (bool) {
        if (callbackChoice == 0)
            token.deposit(arbitraryUint);
        else if (callbackChoice == 1)
            token.transferFrom(arbitraryAddress1,arbitraryAddress2,arbitraryUint);
        else if (callbackChoice == 2)
            token.withdraw(arbitraryUint);
        else if (callbackChoice == 3)
            token.transfer(arbitraryAddress1,arbitraryUint);
        else if (callbackChoice == 4)
            token.approve(arbitraryAddress1,arbitraryUint);
        else assert(false);

        return true;
    }
}

