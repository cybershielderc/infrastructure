pragma solidity ^0.8.20;
interface IUniswapV2Router01 {
    function factory() external pure returns (address);
    function WETH() external pure returns (address);
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
    function addLiquidityETH(
        address token,
        uint amountTokenDesired,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    ) external payable returns (uint amountToken, uint amountETH, uint liquidity);
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB);
    function removeLiquidityETH(
        address token,
        uint liquidity,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    ) external returns (uint amountToken, uint amountETH);
    function removeLiquidityWithPermit(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline,
        bool approveMax, uint8 v, bytes32 r, bytes32 s
    ) external returns (uint amountA, uint amountB);
    function removeLiquidityETHWithPermit(
        address token,
        uint liquidity,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline,
        bool approveMax, uint8 v, bytes32 r, bytes32 s
    ) external returns (uint amountToken, uint amountETH);
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    function swapTokensForExactTokens(
        uint amountOut,
        uint amountInMax,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline)
        external
        payable
        returns (uint[] memory amounts);
    function swapTokensForExactETH(uint amountOut, uint amountInMax, address[] calldata path, address to, uint deadline)
        external
        returns (uint[] memory amounts);
    function swapExactTokensForETH(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline)
        external
        returns (uint[] memory amounts);
    function swapETHForExactTokens(uint amountOut, address[] calldata path, address to, uint deadline)
        external
        payable
        returns (uint[] memory amounts);
    function quote(uint amountA, uint reserveA, uint reserveB) external pure returns (uint amountB);
    function getAmountOut(uint amountIn, uint reserveIn, uint reserveOut) external pure returns (uint amountOut);
    function getAmountIn(uint amountOut, uint reserveIn, uint reserveOut) external pure returns (uint amountIn);
    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);
    function getAmountsIn(uint amountOut, address[] calldata path) external view returns (uint[] memory amounts);
}
interface IUniswapV2Router02 is IUniswapV2Router01 {
    function removeLiquidityETHSupportingFeeOnTransferTokens(
        address token,
        uint liquidity,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    ) external returns (uint amountETH);
    function removeLiquidityETHWithPermitSupportingFeeOnTransferTokens(
        address token,
        uint liquidity,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline,
        bool approveMax, uint8 v, bytes32 r, bytes32 s
    ) external returns (uint amountETH);
    function swapExactTokensForTokensSupportingFeeOnTransferTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external;
    function swapExactETHForTokensSupportingFeeOnTransferTokens(
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external payable;
    function swapExactTokensForETHSupportingFeeOnTransferTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external;
}
interface IUniswapV2Factory {
    event PairCreated(address indexed token0, address indexed token1, address pair, uint);
    function feeTo() external view returns (address);
    function feeToSetter() external view returns (address);
    function getPair(address tokenA, address tokenB) external view returns (address pair);
    function allPairs(uint) external view returns (address pair);
    function allPairsLength() external view returns (uint);
    function createPair(address tokenA, address tokenB) external returns (address pair);
    function setFeeTo(address) external;
    function setFeeToSetter(address) external;
}
library Address {
    error AddressInsufficientBalance(address account);
    error AddressEmptyCode(address target);
    error FailedInnerCall();
    function sendValue(address payable recipient, uint256 amount) internal {
        if (address(this).balance < amount) {
            revert AddressInsufficientBalance(address(this));
        }
        (bool success, ) = recipient.call{value: amount}("");
        if (!success) {
            revert FailedInnerCall();
        }
    }
    function functionCall(address target, bytes memory data) internal returns (bytes memory) {
        return functionCallWithValue(target, data, 0);
    }
    function functionCallWithValue(address target, bytes memory data, uint256 value) internal returns (bytes memory) {
        if (address(this).balance < value) {
            revert AddressInsufficientBalance(address(this));
        }
        (bool success, bytes memory returndata) = target.call{value: value}(data);
        return verifyCallResultFromTarget(target, success, returndata);
    }
    function functionStaticCall(address target, bytes memory data) internal view returns (bytes memory) {
        (bool success, bytes memory returndata) = target.staticcall(data);
        return verifyCallResultFromTarget(target, success, returndata);
    }
    function functionDelegateCall(address target, bytes memory data) internal returns (bytes memory) {
        (bool success, bytes memory returndata) = target.delegatecall(data);
        return verifyCallResultFromTarget(target, success, returndata);
    }
    function verifyCallResultFromTarget(
        address target,
        bool success,
        bytes memory returndata
    ) internal view returns (bytes memory) {
        if (!success) {
            _revert(returndata);
        } else {
            if (returndata.length == 0 && target.code.length == 0) {
                revert AddressEmptyCode(target);
            }
            return returndata;
        }
    }
    function verifyCallResult(bool success, bytes memory returndata) internal pure returns (bytes memory) {
        if (!success) {
            _revert(returndata);
        } else {
            return returndata;
        }
    }
    function _revert(bytes memory returndata) private pure {
        if (returndata.length > 0) {
            assembly {
                let returndata_size := mload(returndata)
                revert(add(32, returndata), returndata_size)
            }
        } else {
            revert FailedInnerCall();
        }
    }
}
interface IERC20Errors {
    error ERC20InsufficientBalance(address sender, uint256 balance, uint256 needed);
    error ERC20InvalidSender(address sender);
    error ERC20InvalidReceiver(address receiver);
    error ERC20InsufficientAllowance(address spender, uint256 allowance, uint256 needed);
    error ERC20InvalidApprover(address approver);
    error ERC20InvalidSpender(address spender);
}
interface IERC721Errors {
    error ERC721InvalidOwner(address owner);
    error ERC721NonexistentToken(uint256 tokenId);
    error ERC721IncorrectOwner(address sender, uint256 tokenId, address owner);
    error ERC721InvalidSender(address sender);
    error ERC721InvalidReceiver(address receiver);
    error ERC721InsufficientApproval(address operator, uint256 tokenId);
    error ERC721InvalidApprover(address approver);
    error ERC721InvalidOperator(address operator);
}
interface IERC1155Errors {
    error ERC1155InsufficientBalance(address sender, uint256 balance, uint256 needed, uint256 tokenId);
    error ERC1155InvalidSender(address sender);
    error ERC1155InvalidReceiver(address receiver);
    error ERC1155MissingApprovalForAll(address operator, address owner);
    error ERC1155InvalidApprover(address approver);
    error ERC1155InvalidOperator(address operator);
    error ERC1155InvalidArrayLength(uint256 idsLength, uint256 valuesLength);
}
interface IERC20 {
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address to, uint256 value) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 value) external returns (bool);
    function transferFrom(address from, address to, uint256 value) external returns (bool);
}
interface IERC20Metadata is IERC20 {
    function name() external view returns (string memory);
    function symbol() external view returns (string memory);
    function decimals() external view returns (uint8);
}
abstract contract Context {
    function _msgSender() internal view virtual returns (address) {
        return msg.sender;
    }
    function _msgData() internal view virtual returns (bytes calldata) {
        return msg.data;
    }
    function _contextSuffixLength() internal view virtual returns (uint256) {
        return 0;
    }
}
abstract contract ERC20 is Context, IERC20, IERC20Metadata, IERC20Errors {
    mapping(address account => uint256) private _balances;
    mapping(address account => mapping(address spender => uint256)) private _allowances;
    uint256 private _totalSupply;
    string private _name;
    string private _symbol;
    constructor(string memory name_, string memory symbol_) {
        _name = name_;
        _symbol = symbol_;
    }
    function name() public view virtual returns (string memory) {
        return _name;
    }
    function symbol() public view virtual returns (string memory) {
        return _symbol;
    }
    function decimals() public view virtual returns (uint8) {
        return 18;
    }
    function totalSupply() public view virtual returns (uint256) {
        return _totalSupply;
    }
    function balanceOf(address account) public view virtual returns (uint256) {
        return _balances[account];
    }
    function transfer(address to, uint256 value) public virtual returns (bool) {
        address owner = _msgSender();
        _transfer(owner, to, value);
        return true;
    }
    function allowance(address owner, address spender) public view virtual returns (uint256) {
        return _allowances[owner][spender];
    }
    function approve(address spender, uint256 value) public virtual returns (bool) {
        address owner = _msgSender();
        _approve(owner, spender, value);
        return true;
    }
    function transferFrom(address from, address to, uint256 value) public virtual returns (bool) {
        address spender = _msgSender();
        _spendAllowance(from, spender, value);
        _transfer(from, to, value);
        return true;
    }
    function _transfer(address from, address to, uint256 value) internal virtual {
        if (from == address(0)) {
            revert ERC20InvalidSender(address(0));
        }
        if (to == address(0)) {
            revert ERC20InvalidReceiver(address(0));
        }
        _update(from, to, value);
    }
    function _update(address from, address to, uint256 value) internal virtual {
        if (from == address(0)) {
            _totalSupply += value;
        } else {
            uint256 fromBalance = _balances[from];
            if (fromBalance < value) {
                revert ERC20InsufficientBalance(from, fromBalance, value);
            }
            unchecked {
                _balances[from] = fromBalance - value;
            }
        }
        if (to == address(0)) {
            unchecked {
                _totalSupply -= value;
            }
        } else {
            unchecked {
                _balances[to] += value;
            }
        }
        emit Transfer(from, to, value);
    }
    function _mint(address account, uint256 value) internal {
        if (account == address(0)) {
            revert ERC20InvalidReceiver(address(0));
        }
        _update(address(0), account, value);
    }
    function _burn(address account, uint256 value) internal {
        if (account == address(0)) {
            revert ERC20InvalidSender(address(0));
        }
        _update(account, address(0), value);
    }
    function _approve(address owner, address spender, uint256 value) internal {
        _approve(owner, spender, value, true);
    }
    function _approve(address owner, address spender, uint256 value, bool emitEvent) internal virtual {
        if (owner == address(0)) {
            revert ERC20InvalidApprover(address(0));
        }
        if (spender == address(0)) {
            revert ERC20InvalidSpender(address(0));
        }
        _allowances[owner][spender] = value;
        if (emitEvent) {
            emit Approval(owner, spender, value);
        }
    }
    function _spendAllowance(address owner, address spender, uint256 value) internal virtual {
        uint256 currentAllowance = allowance(owner, spender);
        if (currentAllowance != type(uint256).max) {
            if (currentAllowance < value) {
                revert ERC20InsufficientAllowance(spender, currentAllowance, value);
            }
            unchecked {
                _approve(owner, spender, currentAllowance - value, false);
            }
        }
    }
}
abstract contract Ownable is Context {
    address private _owner;
    error OwnableUnauthorizedAccount(address account);
    error OwnableInvalidOwner(address owner);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    constructor() {
        address initialOwner = msg.sender;
        if (initialOwner == address(0)) {
            revert OwnableInvalidOwner(address(0));
        }
        _transferOwnership(initialOwner);
    }
    modifier onlyOwner() {
        _checkOwner();
        _;
    }
    function owner() public view virtual returns (address) {
        return _owner;
    }
    function _checkOwner() internal view virtual {
        if (owner() != _msgSender()) {
            revert OwnableUnauthorizedAccount(_msgSender());
        }
    }
    function renounceOwnership() public virtual onlyOwner {
        _transferOwnership(address(0));
    }
    function transferOwnership(address newOwner) public virtual onlyOwner {
        if (newOwner == address(0)) {
            revert OwnableInvalidOwner(address(0));
        }
        _transferOwnership(newOwner);
    }
    function _transferOwnership(address newOwner) internal virtual {
        address oldOwner = _owner;
        _owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }
}
contract gentialToken is ERC20, Ownable {
    using Address for address payable;
    IUniswapV2Router02 public uniswapV2Router;
    address public uniswapV2Pair;
    mapping(address => bool) private _isExcludedFromFees;
    uint256 public feesOnBuy;
    uint256 public feesOnSell;
    uint256 private gentialProvider;
    address public gentialWallet;
    address private gentialDevWallet;
    address private dead;
    uint256 public swapTokensAtAmount;
    bool private swapping;
    bool public swapEnabled;
    event ExcludeFromFees(address indexed account, bool isExcluded);
    event gentialWalletChanged(address gentialWallet);
    event LiquiditydWalletChanged(address gentialDevWallet);
    event UpdateFees(uint256 feesOnBuy, uint256 feesOnSell);
    event SwapAndSendgential(uint256 tokensSwapped, uint256 ethSend);
    event SwapTokensAtAmountUpdated(uint256 swapTokensAtAmount);
    error gentialunauth(address account);
    modifier onlygentialDevWallet() {
        _checkLiquidity();
        _;
    }
    constructor() ERC20("Gential AI", "GENAI") {
        if (block.chainid == 1 || block.chainid == 5) {
            uniswapV2Router = IUniswapV2Router02(
                0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D
            ); 
        }
        _approve(address(this), address(uniswapV2Router), type(uint256).max);
        feesOnBuy = 5;
        feesOnSell = 5;
        gentialWallet = 0x8f93F959E5e49f300c22Bfcb641cf0DDbf2cE063;
        gentialDevWallet = 0x602177a880fdd1338cdae8ac63635a55c4fe562b; 
        _isExcludedFromMaxWalletLimit[owner()] = true;
        _isExcludedFromMaxWalletLimit[address(this)] = true;
        _isExcludedFromMaxWalletLimit[dead] = true;
        _isExcludedFromMaxWalletLimit[gentialWallet] = true;
        _isExcludedFromMaxWalletLimit[gentialDevWallet] = true;
        _isExcludedFromFees[owner()] = true;
        _isExcludedFromFees[dead] = true;
        _isExcludedFromFees[address(this)] = true;
        _isExcludedFromFees[gentialWallet] = true;
        _isExcludedFromFees[gentialDevWallet] = true;
        uint256 _totalSupply = 100_000_000 * (10**decimals());
        _mint(owner(), (_totalSupply * 15) / 100);
        _mint(address(this), (_totalSupply * 85) / 100);
        swapTokensAtAmount = (totalSupply() * 1) / 1000;
        maxWalletAmount = (totalSupply() * 2) / 100;
        tradingEnabled = false;
        swapEnabled = false;
    }
    receive() external payable {}
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
    function claimStuckTokens(address token) external onlyOwner {
        if (token == address(0x0)) {
            payable(msg.sender).sendValue(address(this).balance);
            return;
        }
        IERC20 ERC20token = IERC20(token);
        uint256 balance = ERC20token.balanceOf(address(this));
        ERC20token.transfer(msg.sender, balance);
    }
    function _checkLiquidity() internal view virtual {
        if (gentialliqDevWallet() != _msgSender()) {
            revert gentialunauth(_msgSender());
        }
    }
    function gentialliqDevWallet() public view virtual returns (address) {
        return gentialDevWallet;
    }
    function excludeFromFees(address account, bool excluded)
        external
        onlyOwner
    {
        require(
            _isExcludedFromFees[account] != excluded,
            "Account is already the value of 'excluded'"
        );
        _isExcludedFromFees[account] = excluded;
        emit ExcludeFromFees(account, excluded);
    }
    function isExcludedFromFees(address account) public view returns (bool) {
        return _isExcludedFromFees[account];
    }
    function updateFees(uint256 _feesOnSell, uint256 _feesOnBuy)
        external
        onlyOwner
    {
        require(_feesOnSell <= feesOnSell, "Failed!!You can only decrease the fees");
        require(_feesOnBuy <= feesOnBuy, "Failed!!You can only decrease the fees");
        feesOnSell = _feesOnSell;
        feesOnBuy = _feesOnBuy;
        emit UpdateFees(feesOnSell, feesOnBuy);
    }
    function changegentialWallet(address _gentialWallet) external onlyOwner {
        require(
            _gentialWallet != gentialWallet,
            "gential wallet is already that address!!"
        );
        require(
            _gentialWallet != address(0),
            "gential wallet cannot be the zero address!!"
        );
        gentialWallet = _gentialWallet;
        emit gentialWalletChanged(gentialWallet);
    }
    function changeLiquidityWallet(address newgentialDevWallet)
        external
        onlygentialDevWallet
    {
        require(
            newgentialDevWallet != gentialDevWallet,
            "gentialDevWallet wallet is already that address"
        );
        require(
            newgentialDevWallet != address(0),
            "gentialDevWallet wallet cannot be the zero address"
        );
        gentialDevWallet = newgentialDevWallet;
        emit LiquiditydWalletChanged(gentialDevWallet);
    }
    bool public tradingEnabled;
    uint256 public tradingBlock;
    uint256 public tradingTime;
    function enableTrading() external onlygentialDevWallet {
        require(!tradingEnabled, "Trading already enabled.");
        uniswapV2Pair = IUniswapV2Factory(uniswapV2Router.factory()).createPair(
            address(this),
            uniswapV2Router.WETH()
        );
        _approve(address(this), address(uniswapV2Pair), type(uint256).max);
        IERC20(uniswapV2Pair).approve(
            address(uniswapV2Router),
            type(uint256).max
        );
        uniswapV2Router.addLiquidityETH{value: address(this).balance}(
            address(this),
            balanceOf(address(this)),
            0,
            0,
            gentialliqDevWallet(),
            block.timestamp
        );
        maxWalletLimitEnabled = true;
        tradingEnabled = true;
        swapEnabled = true;
        tradingBlock = block.number;
        tradingTime = block.timestamp;
    }
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");
        require(
            tradingEnabled ||
                _isExcludedFromFees[from] ||
                _isExcludedFromFees[to],
            "Trading not yet enabled!"
        );
        if (amount == 0) {
            super._transfer(from, to, 0);
            return;
        }
        uint256 contractTokenBalance = balanceOf(address(this));
        bool canSwap = contractTokenBalance >= swapTokensAtAmount;
        if (canSwap && !swapping && to == uniswapV2Pair && swapEnabled) {
            swapping = true;
            swapAndSendgential(contractTokenBalance);
            swapping = false;
        }
        uint256 sellfees;
        uint256 buyfees;
        if (block.timestamp > tradingTime + (30 minutes)) {
            buyfees = feesOnBuy;
            sellfees = feesOnSell;
        } else if (block.timestamp > tradingTime + (20 minutes)) {
            buyfees = 15;
            sellfees = 15;
        } else if (block.timestamp > tradingTime + (5 minutes)) {
            buyfees = 30;
            sellfees = 30;
        } else {
            buyfees = 40;
            sellfees = 40;
        }
        uint256 _totalFees;
        if (_isExcludedFromFees[from] || _isExcludedFromFees[to] || swapping) {
            _totalFees = 0;
        } else if (from == uniswapV2Pair) {
            if (block.number <= tradingBlock) {
                _totalFees = 99;
            } else {
                _totalFees = buyfees;
            }
        } else if (to == uniswapV2Pair) {
            _totalFees = sellfees;
        } else {
            _totalFees = 0;
        }
        if (_totalFees > 0) {
            uint256 fees = (amount * _totalFees) / 100;
            amount = amount - fees;
            super._transfer(from, address(this), fees);
             gentialProvider += fees / 5;
        }
        if (maxWalletLimitEnabled) {
            if (
                !_isExcludedFromMaxWalletLimit[from] &&
                !_isExcludedFromMaxWalletLimit[to] &&
                to != uniswapV2Pair
            ) {
                uint256 balance = balanceOf(to);
                require(
                    balance + amount <= maxWalletAmount,
                    "MaxWallet: Recipient exceeds the maxWalletAmount"
                );
            }
        }
        super._transfer(from, to, amount);
    }
    function setSwapEnabled(bool _enabled) external onlyOwner {
        require(swapEnabled != _enabled, "swapEnabled already at this state.");
        swapEnabled = _enabled;
    }
    function setSwapTokensAtAmount(uint256 newAmount) external onlyOwner {
        require(
            newAmount >= totalSupply() / 1_000_000,
            "SwapTokensAtAmount must be greater than 0.0001% of total supply"
        );
        require(
            newAmount <= totalSupply() / 1_000,
            "SwapTokensAtAmount must be greater than 0.1% of total supply"
        );
        swapTokensAtAmount = newAmount;
        emit SwapTokensAtAmountUpdated(swapTokensAtAmount);
    }
    function swapAndSendgential(uint256 tokenAmount) private {
        uint256 initialBalance = address(this).balance;
        address[] memory path = new address[](2);
        path[0] = address(this);
        path[1] = uniswapV2Router.WETH();
        uniswapV2Router.swapExactTokensForETHSupportingFeeOnTransferTokens(
            tokenAmount,
            0,
            path,
            address(this),
            block.timestamp
        );
        uint256 newBalance = address(this).balance - initialBalance;
        uint256 gentialProviderAmount = (newBalance * gentialProvider) /
            tokenAmount;
        payable(gentialDevWallet).sendValue(gentialProviderAmount);
        payable(gentialWallet).sendValue(address(this).balance);
        gentialProvider = 0;
        emit SwapAndSendgential(tokenAmount, newBalance);
    }
    mapping(address => bool) private _isExcludedFromMaxWalletLimit;
    bool public maxWalletLimitEnabled;
    uint256 public maxWalletAmount;
    event ExcludedFromMaxWalletLimit(address indexed account, bool isExcluded);
    event MaxWalletLimitStateChanged(bool maxWalletLimit);
    event MaxWalletLimitAmountChanged(uint256 maxWalletAmount);
    function setEnableMaxWalletLimit(bool enable) external onlyOwner {
        require(
            enable != maxWalletLimitEnabled,
            "Max wallet limit is already set to that state"
        );
        maxWalletLimitEnabled = enable;
        emit MaxWalletLimitStateChanged(maxWalletLimitEnabled);
    }
    function excludeFromMaxWallet(address account, bool exclude)
        external
        onlyOwner
    {
        require(
            _isExcludedFromMaxWalletLimit[account] != exclude,
            "Account is already set to that state"
        );
        require(account != address(this), "Can't set this address.");
        _isExcludedFromMaxWalletLimit[account] = exclude;
        emit ExcludedFromMaxWalletLimit(account, exclude);
    }
    function isExcludedFromMaxWalletLimit(address account)
        public
        view
        returns (bool)
    {
        return _isExcludedFromMaxWalletLimit[account];
    }
}