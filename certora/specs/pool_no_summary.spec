
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

