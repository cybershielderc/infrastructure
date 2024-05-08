async function main() {
    const GenT = await ethers.getContractFactory("contract.sol");
 
    // Start deployment, returning a promise that resolves to a contract object
    const _gent = await GenT.deploy("Hello World!");   
    console.log("Contract deployed to address:", _gent.address);
 }
 
 main()
   .then(() => process.exit(0))
   .catch(error => {
     console.error(error);
     process.exit(1);
   });