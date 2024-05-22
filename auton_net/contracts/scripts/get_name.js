const API_URL = process.env.API_URL;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS;

const contract = require("../artifacts/contracts/test_contract.sol/TimiTrumpet.json");

const ethers = require('ethers');

const alchemyProvider = new ethers.providers.JsonRpcProvider(API_URL);

const signer = new ethers.Wallet(PRIVATE_KEY, alchemyProvider);

const GenTContract = new ethers.Contract(CONTRACT_ADDRESS, contract.abi, signer);

async function main() {
    const name = await GenTContract.name();
    const symbol = await GenTContract.symbol();
    const decimals = await GenTContract.decimals();
    console.log("The name is: " + name);
    console.log("The symbol is: " + symbol);
    console.log("The decimals is: " + decimals);
    //const gasLimit = await GenTContract.console.log("The gasLimit for reduceTax is: " + gasLimit);
    //console.log(await GenTContract.tradeTimiTrumpet())
}

main();
