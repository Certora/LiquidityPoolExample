import "../helpers/erc20.spec"

methods
{
    // envfree declarations
    balanceOf(address) returns(uint256) envfree
    totalSupply()      returns(uint256) envfree
    asset()            returns(address) envfree

    // for checing call backs to the pool's function
    deposit(uint256)  returns(uint256) => DISPATCHER(true)
    withdraw(uint256) returns(uint256) => DISPATCHER(true)
    flashLoan(address, uint256)        => DISPATCHER(true)
   
    // flash loan receiver function
    executeOperation(uint256,uint256,address) => DISPATCHER(true)

    // harness functions
    underlyingBalance()            returns(uint256) envfree
    underlyingAllowance(address a) returns(uint256) envfree
 
}

function safeAssumptions(address a, env e) {
    require asset()      != currentContract;
    require e.msg.sender != currentContract;
    requireInvariant noAllowance(a);
}

invariant noAllowance(address a)
    underlyingAllowance(a) == 0
{ preserved with (env e) { safeAssumptions(a, e); } }


/// flash loans must increase the pool's underlying asset balance, assuming the
/// receiver has no pool balance.
rule flashLoanIncreasesBalance {
    address receiver; uint256 amount; env e;

    safeAssumptions(receiver, e);

    mathint balance_before = underlyingBalance();

    flashLoan(e, receiver, amount);

    mathint balance_after = underlyingBalance();

    assert balance_after >= balance_before,
        "flash loans must not decrease the contract's underlying balance";
}


/// `deposit` must increase the pool's underlying asset balance
rule integrityOfDeposit {

    mathint balance_before = underlyingBalance();


    env e; uint256 amount;
    safeAssumptions(_, e);

    deposit(e, amount);

    mathint balance_after = underlyingBalance();

    assert balance_after == balance_before + amount,
        "deposit must increase the underlying balance of the pool";
}

