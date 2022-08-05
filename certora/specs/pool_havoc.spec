//// Without linking, the `integrityOfDeposit` rule will not pass, because the
//// `deposit` and `balanceOf` methods are unresolved and the prover allows them
//// to return arbitrary values.
////
//// You can verify this spec by running the following from the command line:
////
////      sh certora/scripts/verifyJustPool.sh
////
//// See [the multicontract section of the user guide][guide] for a complete
//// discussion of this example.
////
//// [guide]: https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html
////

methods
{
    balanceOf(address)                      returns(uint256) envfree
    totalSupply()                           returns(uint256) envfree
    transfer(address, uint256)              returns(bool)
    transferFrom(address, address, uint256) returns(bool)

    deposit(uint256)                        returns(uint256)
    withdraw(uint256)                       returns(uint256)
    assetBalance()                          returns(uint256) envfree

    flashLoan(address, uint256)
}

/// `deposit` must increase the pool's underlying asset balance
rule integrityOfDeposit {

    uint balance_before = assetBalance();

    env e; uint256 amount;
    deposit(e, amount);

    uint balance_after = assetBalance();

    assert balance_after == balance_before + amount,
        "deposit must increase pool's underlying asset balance";
} 

