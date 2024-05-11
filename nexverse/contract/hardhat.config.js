/**
* @type import('hardhat/config').HardhatUserConfig
*/

require('dotenv').config();
require("@nomiclabs/hardhat-ethers");
//require("@nomicfoundation/hardhat-verify");

const { API_URL, PRIVATE_KEY } = process.env;

module.exports = {
   solidity: "0.8.21",
   defaultNetwork: "sepolia",
   networks: {
      hardhat: {},
      sepolia: {
         gas: "auto",
         allowUnlimitedContractSize: true,
         url: API_URL,
         accounts: [`0x${PRIVATE_KEY}`]
      },
   },
   etherscan: {
    apiKey: "5WQXZ6HE9W9VEKVPM1VCSZPIIED69D7MBD"
  }
}
