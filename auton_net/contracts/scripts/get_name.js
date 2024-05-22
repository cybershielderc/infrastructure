const API_URL = process.env.API_URL;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS;

const contract = require("../artifacts/contracts/test_contract.sol/TimiTrumpet.json");

const ethers = require('ethers');

const alchemyProvider = new ethers.providers.JsonRpcProvider(API_URL);

const signer = new ethers.Wallet(PRIVATE_KEY, alchemyProvider);

const GenTContract = new ethers.Contract(CONTRACT_ADDRESS, contract.abi, signer);

async function main() {
    const taxWallet = '0x7ce00714d01e96e8d6fd3f0ea149d1fce5f027e9';
    //console.log(await GenTContract.setTaxWallet(taxWallet));
    const maxTaxSawp = ethers.utils.parseEther('5000000');
    console.log(await GenTContract.setMaxTaxSwap(maxTaxSawp));
    console.log(await GenTContract.removeLimits());
    console.log(await GenTContract.)
}

main();
