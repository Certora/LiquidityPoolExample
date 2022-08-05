
methods
{
    // pool's erc20 function
    balanceOf(address) returns(uint256) envfree
    totalSupply() returns(uint256) envfree
    // for checing call backs to the pool's function
    deposit(uint256) returns(uint256)  => DISPATCHER(true)
    withdraw(uint256) returns (uint256)  => DISPATCHER(true)
    flashLoan(address, uint256)  => DISPATCHER(true)
   
    // flash loan receiver function
    executeOperation(uint256,uint256,address) => DISPATCHER(true)
    //erc20 function
    transfer(address, uint256) returns (bool) => DISPATCHER(true)
    transferFrom(address, address, uint256) returns (bool) => DISPATCHER(true)
    //erc20 function for calling from spec
    underlying.balanceOf(address) returns(uint256) envfree
 
}


/// check that `withdraw` updates sender's balance appropriately
rule integrityOfWithdraw {
    env e; uint256 amount;

    mathint balance_before = balanceOf(e.msg.sender);

    withdraw(e, amount);

    assert balanceOf(e.msg.sender) == balance_before - amount,
        "withdraw must increase the sender's value by `amount`";
} 

