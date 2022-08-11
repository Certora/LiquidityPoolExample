//// TODO
//// With the `HAVOC_ALL` summary, the `flashLoanIncreasesBalance` rule will
//// not pass, because the Prover allows the `executeOperation` method to change
//// everything.
////
//// You can verify this spec by running the following from the command line:
////
////      sh certora/scripts/verifyFlashLoanHavoc.sh
////
//// See [the multicontract section of the user guide][guide] for a complete
//// discussion of this example.
////
//// [guide]: https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html
////

using Asset as underlying

methods {
    balanceOf(address)                      returns(uint256) envfree

    underlying.balanceOf(address)           returns(uint256) envfree
    executeOperation(uint256,uint256,address) returns (bool) => HAVOC_ALL
}

/// flash loans must increase the pool's underlying asset balance, assuming the
/// receiver has no pool balance.
rule flashLoanIncreasesBalance {
    address receiver; uint256 amount; env e;

    require balanceOf(receiver) == 0;

    mathint balance_before = underlying.balanceOf(currentContract);

    flashLoan(e, receiver, amount);

    mathint balance_after = underlying.balanceOf(currentContract);

    assert balance_after >= balance_before,
        "flash loans must not decrease the contract's underlying balance";
}

