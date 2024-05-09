/**
* @type import('hardhat/config').HardhatUserConfig
*/

require('dotenv').config();
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-etherscan");

const { API_URL, PRIVATE_KEY } = process.env;

module.exports = {
   solidity: "0.8.20",
   defaultNetwork: "sepolia",
   networks: {
      hardhat: {},
      sepolia: {
        allowUnlimitedContractSize: true,
         url: API_URL,
         accounts: [`0x${PRIVATE_KEY}`]
      },
      etherscan: {
        apiKey: "Y4exjmDVLGQ8h9twwUc7DSqDPx6WwhbE"
      }
   },
}