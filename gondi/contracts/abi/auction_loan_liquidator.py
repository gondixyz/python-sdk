ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "currencyManager", "type": "address"},
            {"internalType": "address", "name": "collectionManager", "type": "address"},
            {"internalType": "uint256", "name": "triggerFee", "type": "uint256"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {"inputs": [], "name": "AuctionAlreadyInProgressError", "type": "error"},
    {
        "inputs": [
            {"internalType": "address", "name": "_contract", "type": "address"},
            {"internalType": "uint256", "name": "_tokenId", "type": "uint256"},
        ],
        "name": "AuctionNotExistsError",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "uint96", "name": "_expiration", "type": "uint96"}],
        "name": "AuctionNotOverError",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "uint96", "name": "_expiration", "type": "uint96"}],
        "name": "AuctionOverError",
        "type": "error",
    },
    {"inputs": [], "name": "CollectionNotWhitelistedError", "type": "error"},
    {"inputs": [], "name": "CurrencyNotWhitelistedError", "type": "error"},
    {
        "inputs": [
            {"internalType": "uint256", "name": "triggerFee", "type": "uint256"}
        ],
        "name": "InvalidTriggerFee",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "address", "name": "_loan", "type": "address"}],
        "name": "LoanNotAcceptedError",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_minBid", "type": "uint256"}],
        "name": "MinBidError",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "address", "name": "_owner", "type": "address"}],
        "name": "NFTNotOwnedError",
        "type": "error",
    },
    {"inputs": [], "name": "NoBidsError", "type": "error"},
    {"inputs": [], "name": "ZeroAddressError", "type": "error"},
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "loanContract",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "auctionContract",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "asset",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "highestBid",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "settler",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "triggerFee",
                "type": "uint256",
            },
        ],
        "name": "AuctionSettled",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "auctionContract",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "newBidder",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "bid",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "loanAddress",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            },
        ],
        "name": "BidPlaced",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "loan",
                "type": "address",
            }
        ],
        "name": "LoanContractAdded",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "loan",
                "type": "address",
            }
        ],
        "name": "LoanContractRemoved",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "loanAddress",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint96",
                "name": "duration",
                "type": "uint96",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "asset",
                "type": "address",
            },
        ],
        "name": "LoanLiquidationStarted",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "user",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "triggerFee",
                "type": "uint256",
            }
        ],
        "name": "TriggerFeeUpdated",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "MAX_TRIGGER_FEE",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MIN_INCREMENT_BPS",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_loanContract", "type": "address"}
        ],
        "name": "addLoanContract",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_contract", "type": "address"},
            {"internalType": "uint256", "name": "_tokenId", "type": "uint256"},
        ],
        "name": "getAuction",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "loanAddress",
                        "type": "address",
                    },
                    {"internalType": "uint256", "name": "loanId", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "highestBid",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "highestBidder",
                        "type": "address",
                    },
                    {"internalType": "uint96", "name": "duration", "type": "uint96"},
                    {"internalType": "address", "name": "asset", "type": "address"},
                    {"internalType": "uint96", "name": "startTime", "type": "uint96"},
                    {
                        "internalType": "address",
                        "name": "originator",
                        "type": "address",
                    },
                    {"internalType": "uint96", "name": "lastBidTime", "type": "uint96"},
                ],
                "internalType": "struct AuctionLoanLiquidator.Auction",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTriggerFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getValidLoanContracts",
        "outputs": [{"internalType": "address[]", "name": "", "type": "address[]"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_loanId", "type": "uint256"},
            {"internalType": "address", "name": "_contract", "type": "address"},
            {"internalType": "uint256", "name": "_tokenId", "type": "uint256"},
            {"internalType": "address", "name": "_asset", "type": "address"},
            {"internalType": "uint96", "name": "_duration", "type": "uint96"},
            {"internalType": "address", "name": "_originator", "type": "address"},
        ],
        "name": "liquidateLoan",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "bytes", "name": "", "type": "bytes"},
        ],
        "name": "onERC721Received",
        "outputs": [{"internalType": "bytes4", "name": "", "type": "bytes4"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_contract", "type": "address"},
            {"internalType": "uint256", "name": "_tokenId", "type": "uint256"},
            {"internalType": "uint256", "name": "_bid", "type": "uint256"},
        ],
        "name": "placeBid",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_loanContract", "type": "address"}
        ],
        "name": "removeLoanContract",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_contract", "type": "address"},
            {"internalType": "uint256", "name": "_tokenId", "type": "uint256"},
            {"internalType": "bytes", "name": "_loan", "type": "bytes"},
        ],
        "name": "settleAuction",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "triggerFee", "type": "uint256"}
        ],
        "name": "updateTriggerFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
