pragma solidity ^0.8.13;

contract Migrations {
  address public owner; //Address of the contract owner 
  uint public last_completed_migration; // Stores the last completed migration step


  modifier restricted() {
    if (msg.sender == owner) _; // Only the contract owner can execute the function
  }

  constructor() {
    owner = msg.sender; // Set the contract creator as the owner
  }

  function setCompleted(uint completed) public restricted {
    last_completed_migration = completed; // Set the completed migration step
  }

  function upgrade(address new_address) public restricted {
    Migrations upgraded = Migrations(new_address); // Create a new instance of the Migrations contract at the specified address
    upgraded.setCompleted(last_completed_migration); // Call the setCompleted function of the upgraded contract
  }
}
