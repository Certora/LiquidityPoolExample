import "../helpers/erc20.spec"

using Pool  as pool
using Asset as underlying

methods
{
    // envfree declarations
    balanceOf(address) returns(uint256) envfree
    totalSupply()      returns(uint256) envfree

    // for checing call backs to the pool's function
    deposit(uint256)  returns(uint256) => DISPATCHER(true)
    withdraw(uint256) returns(uint256) => DISPATCHER(true)
    flashLoan(address, uint256)        => DISPATCHER(true)
   
    // flash loan receiver function
    executeOperation(uint256,uint256,address) => DISPATCHER(true)

    //erc20 function for calling from spec
    underlying.balanceOf(address) returns(uint256) envfree
 
}

/// flash loans must increase the pool's underlying asset balance, assuming the
/// receiver has no pool balance.
rule flashLoanIncreasesBalance {
    address receiver; uint256 amount; env e;

    require e.msg.sender != currentContract;

    mathint balance_before = underlying.balanceOf(currentContract);

    flashLoan(e, receiver, amount);

    mathint balance_after = underlying.balanceOf(currentContract);

    assert balance_after >= balance_before,
        "flash loans must not decrease the contract's underlying balance";
}


/// `deposit` must increase the pool's underlying asset balance
rule integrityOfDeposit {

    mathint balance_before = underlying.balanceOf(currentContract);

    env e; uint256 amount;
    deposit(e, amount);

    mathint balance_after = underlying.balanceOf(currentContract);

    assert balance_after == balance_before + amount,
        "deposit must increase the underlying balance of the pool";
}

