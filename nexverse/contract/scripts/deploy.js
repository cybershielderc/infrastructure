async function main() {
    const gentialToken = await ethers.getContractFactory("gentialToken");
 
    // Start deployment, returning a promise that resolves to a contract object
    const _gent = await gentialToken.deploy({gasLimit: 100000});   
    console.log("Contract deployed to address:", _gent.address);
 }
 
 main()
   .then(() => process.exit(0))
   .catch(error => {
     console.error(error);
     process.exit(1);
   });