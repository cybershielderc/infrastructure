abstract contract Context {
    function _msgSender() internal view virtual returns (address) {
        return msg.sender;
    }
}

interface IERC20 {
    function totalSupply() external view returns (uint256);

    function balanceOf(address account) external view returns (uint256);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function allowance(address owner, address spender) external view returns (uint256);

    function approve(address spender, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "SafeMath: addition overflow");
        return c;
    }

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        return sub(a, b, "SafeMath: subtraction overflow");
    }

    function sub(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
        require(b <= a, errorMessage);
        uint256 c = a - b;
        return c;
    }

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) {
            return 0;
        }
        uint256 c = a * b;
        require(c / a == b, "SafeMath: multiplication overflow");
        return c;
    }

    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        return div(a, b, "SafeMath: division by zero");
    }

    function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {
        require(b > 0, errorMessage);
        uint256 c = a / b;
        return c;
    }
}

contract Ownable is Context {
    address private _owner;

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    constructor () {
        address msgSender = _msgSender();
        _owner = msgSender;
        emit OwnershipTransferred(address(0), msgSender);
    }
    function owner() public view returns (address) {
        return _owner;
    }
    modifier onlyOwner() {
        require(_owner == _msgSender(), "Ownable: caller is not the owner");
        _;
    }
    function renounceOwnership() public virtual onlyOwner {
        emit OwnershipTransferred(_owner, address(0));
        _owner = address(0);
    }
}

interface IUniswapV2Factory {
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

interface IUniswapV2Router02 {
    function swapExactTokensForETHSupportingFeeOnTransferTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external;

    function factory() external pure returns (address);

    function WETH() external pure returns (address);

    function addLiquidityETH(
        address token,
        uint amountTokenDesired,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    ) external payable returns (uint amountToken, uint amountETH, uint liquidity);
}

contract TimiTrumpet is Context, IERC20, Ownable {
    using SafeMath for uint256;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    mapping(address => bool) private _isExcludedFromFee;
    address payable private  _taxWallet;
    address private constant deadAddress = address(0xdead);
    uint256 private constant _initialBuyTax = 50;
    uint256 private constant _initialSellTax = 50;
    uint256 private constant _reduceBuyTaxAt = 50;
    uint256 private constant _reduceSellTaxAt = 50;
    uint256 private constant _preventSwapBefore = 25;
    uint256 private _finalBuyTax = 50;
    uint256 private _finalSellTax = 50;
    uint256 private _buyCount = 0;
    uint8 private constant _decimals = 9;
    uint256 private constant _tTotal = 100 * 10 ** _decimals;
    string private constant _name = unicode"TimiTrumpet";
    string private constant _symbol = unicode"TITRUMP";
    uint256 public constant _taxSwapThreshold = 100000 * 10 ** _decimals;
    uint256 public _maxTaxSwap = 5000000 * 10 ** _decimals;
    uint256 public _maxTxAmount = 1000000 * 10 ** _decimals;
    uint256 public _maxWalletSize = 2000001 * 10 ** _decimals;
    IUniswapV2Router02 private uniswapV2Router;
    address private uniswapV2Pair;
    bool private tradingOpen;
    bool private limitEffect = true;
    bool private inSwap = false;
    bool private swapEnabled = false;

    event FinalTax (uint256 _valueBuy, uint256 _valueSell);
    event Launch (bool _tradingOpen, bool _swapEnabled);
    event maxAmount(uint256 _value);
    modifier lockTheSwap {
        inSwap = true;
        _;
        inSwap = false;
    }
    constructor () {
        _taxWallet = payable(0x7ce00714D01e96e8d6FD3F0Ea149d1fCE5F027E9);
        _balances[_msgSender()] = _tTotal;
        _isExcludedFromFee[owner()] = true;
        _isExcludedFromFee[_taxWallet] = true;
        _isExcludedFromFee[deadAddress] = true;
        _isExcludedFromFee[address(this)] = true;
        emit Transfer(address(0), _msgSender(), _tTotal);
    }
    function name() public pure returns (string memory) {
        return _name;
    }

    function symbol() public pure returns (string memory) {
        return _symbol;
    }

    function decimals() public pure returns (uint8) {
        return _decimals;
    }

    function totalSupply() public pure override returns (uint256) {
        return _tTotal;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(_msgSender(), spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), _allowances[sender][_msgSender()].sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }

    function _approve(address owner, address spender, uint256 amount) private {
        require(owner != address(0) && spender != address(0), "ERC20: approve the zero address");
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    function _transfer(address from, address to, uint256 amount) private {
        require(from != address(0) && to != address(0), "ERC20: transfer the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        uint256 taxAmount = 0;
        if (from != owner() && to != owner()) {
            if (!tradingOpen) {
                require(
                    _isExcludedFromFee[from] || _isExcludedFromFee[to],
                    "trading is not yet open"
                );
            }
            if (from == uniswapV2Pair && to != address(uniswapV2Router) && !_isExcludedFromFee[to]) {
                if (limitEffect) {
                    require(amount <= _maxTxAmount, "Exceeds the _maxTxAmount.");
                    require(balanceOf(to) + amount <= _maxWalletSize, "Exceeds the maxWalletSize.");
                }
                _buyCount++;
            }
            if (to == uniswapV2Pair && from != address(this)) {
                taxAmount = amount.mul
                    ((_buyCount > _reduceSellTaxAt)
                        ? _finalSellTax : _initialSellTax).div(100
                );
            } else if (from == uniswapV2Pair && to != address(this)) {
                taxAmount = amount.mul
                    ((_buyCount > _reduceBuyTaxAt)
                        ? _finalBuyTax : _initialBuyTax).div(100
                );
            }
            uint256 contractTokenBalance = balanceOf(address(this));
            if (
                !inSwap &&
            to == uniswapV2Pair &&
            swapEnabled &&
            contractTokenBalance > _taxSwapThreshold &&
            _buyCount > _preventSwapBefore
            ) {
                uint256 getMin = (contractTokenBalance > _maxTaxSwap) ? _maxTaxSwap : contractTokenBalance;
                uint256 amountToSwap = (amount > getMin) ? getMin : amount;
                swapTokensForEth(amountToSwap);
                uint256 contractETHBalance = address(this).balance;
                if (contractETHBalance > 0) {
                    sendETHToFee(address(this).balance);
                }
            }
        }
        if (taxAmount > 0) {
            _balances[address(this)] = _balances[address(this)].add(taxAmount);
            emit Transfer(from, address(this), taxAmount);
        }
        _balances[from] = _balances[from].sub(amount);
        _balances[to] = _balances[to].add(amount.sub(taxAmount));
        emit Transfer(from, to, amount.sub(taxAmount));
    }

    function sendETHToFee(uint256 amount) private {
        _taxWallet.transfer(amount);
    }

    function setTaxWallet(address payable _newTaxWallet) external onlyOwner {
        _taxWallet = _newTaxWallet;
    }

    function setMaxTaxSwap(uint256 _value) external onlyOwner {
        _maxTaxSwap = _value;
    }

    function airdrop(address[] calldata recipients, uint256[] calldata values) external onlyOwner {
        require(recipients.length == values.length, "Mismatched recipinients and values.");
        for (uint256 i = 0; i < recipients.length; i++) {
            _transfer(_msgSender(), recipients[i], values[i]);
        }
    }

    function swapTokensForEth(uint256 tokenAmount) private lockTheSwap {
        address[] memory path = new address[](2);
        path[0] = address(this);
        path[1] = uniswapV2Router.WETH();
        _approve(address(this), address(uniswapV2Router), tokenAmount);
        uniswapV2Router.swapExactTokensForETHSupportingFeeOnTransferTokens(
            tokenAmount,
            0,
            path,
            address(this),
            block.timestamp
        );
    }

    function createPair() external onlyOwner {
        require(!tradingOpen, "init already called");
        uint256 tokenAmount = balanceOf(address(this)).sub(_tTotal.mul(_initialBuyTax).div(100));
        uniswapV2Router = IUniswapV2Router02(0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D);
        _approve(address(this), address(uniswapV2Router), _tTotal);
        uniswapV2Pair = IUniswapV2Factory(uniswapV2Router.factory())
            .createPair(address(this), uniswapV2Router.WETH()
        );
        uniswapV2Router.addLiquidityETH{value: address(this).balance} (
            address(this),
            tokenAmount,
            0,
            0,
            _msgSender(),
            block.timestamp
        );
        IERC20(uniswapV2Pair).approve(address(uniswapV2Router), type(uint).max);
    }

    function tradeTimiTrumpet() external onlyOwner {
        require(!tradingOpen, "trading already open");
        swapEnabled = true;
        tradingOpen = true;
        emit Launch(tradingOpen, swapEnabled);
    }

    function removeLimits() external onlyOwner {
        limitEffect = false;
        _maxTxAmount = _tTotal;
        _maxWalletSize = _tTotal;
        emit maxAmount(_tTotal);
    }

    function manualSwap() external onlyOwner {
        require(!inSwap && swapEnabled, "Already in swap");
        swapTokensForEth(_maxTaxSwap);
    }

    function reduceTax(uint256 _valueBuy, uint256 _valueSell) external onlyOwner {
        require(_valueBuy <= 100 && _valueSell <= 100 && tradingOpen, "Tax exceeds maximum amount");
        _finalBuyTax = _valueBuy;
        _finalSellTax = _valueSell;
        emit FinalTax(_valueBuy, _valueSell);
    }

    receive() external payable {}
}