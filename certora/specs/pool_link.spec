//// This spec extends `pool_havoc.spec` using the Prover's support for linking
//// and accessing methods from other contracts.
////
//// You can verify this spec by running the following from the command line:
////
////      sh certora/scripts/verifyWithLinking.sh
////
//// See [the multicontract section of the user guide][guide] for a complete
//// discussion of this example.
////
//// [guide]: https://docs.certora.com/en/latest/docs/user-guide/multicontract/index.html
////

using Asset for underlying

methods
{
    balanceOf(address)                      returns(uint256) envfree
    totalSupply()                           returns(uint256) envfree
    transfer(address, uint256)              returns(bool)
    transferFrom(address, address, uint256) returns(bool)

    deposit(uint256)                        returns(uint256)
    withdraw(uint256)                       returns(uint256)

    flashLoan(address, uint256)
}

/// `deposit` must increase the pool's underlying asset balance
rule integrityOfDeposit {

    uint balance_before = underlying.balanceOf(currentContract);

    env e; uint256 amount;
    deposit(e, amount);

    uint balance_after = underlying.balanceOf(currentContract);

    assert balance_after == balance_before + amount;
}

