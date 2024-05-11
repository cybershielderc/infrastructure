async function main() {
    const [deployer] = await ethers.getSigners();
    const gentialToken = await ethers.getContractFactory("gentialToken");
  
    const accountBalance = await deployer.provider.getBalance(deployer.address); 
    console.log(
      "Deploying the contracts with the account:",
      await deployer.getAddress()
    );

    console.log("Account balance:", accountBalance.toString());
    // Start deployment, returning a promise that resolves to a contract object
    const _gent_estimation = await gentialToken.estimateGas.deploy();
    console.log("Contract Deploy Gas Price: ", _gent_estimation);
    //console.log("Contract deployed to address:", _gent.address);
 }
 
 main()
   .then(() => process.exit(0))
   .catch(error => {
     console.error(error);
     process.exit(1);
   });