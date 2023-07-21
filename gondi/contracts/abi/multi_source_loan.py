ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "loanLiquidator", "type": "address"},
            {
                "components": [
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint256", "name": "fraction", "type": "uint256"},
                ],
                "internalType": "struct IBaseLoan.ProtocolFee",
                "name": "protocolFee",
                "type": "tuple",
            },
            {"internalType": "address", "name": "currencyManager", "type": "address"},
            {"internalType": "address", "name": "collectionManager", "type": "address"},
            {"internalType": "uint8", "name": "maxSources", "type": "uint8"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {"inputs": [], "name": "AddressZeroError", "type": "error"},
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {"internalType": "uint256", "name": "_offerId", "type": "uint256"},
        ],
        "name": "CancelledOrExecutedOfferError",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {"internalType": "uint256", "name": "_offerId", "type": "uint256"},
        ],
        "name": "CancelledRenegotiationOffer",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {"internalType": "uint256", "name": "_renegotiationId", "type": "uint256"},
        ],
        "name": "CancelledRenegotiationOfferError",
        "type": "error",
    },
    {"inputs": [], "name": "CannotLiquidateError", "type": "error"},
    {"inputs": [], "name": "CollectionNotWhitelistedError", "type": "error"},
    {"inputs": [], "name": "CurrencyNotWhitelistedError", "type": "error"},
    {"inputs": [], "name": "ExpiredLoanError", "type": "error"},
    {
        "inputs": [
            {"internalType": "uint256", "name": "_expirationTime", "type": "uint256"}
        ],
        "name": "ExpiredOfferError",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_expirationTime", "type": "uint256"}
        ],
        "name": "ExpiredRenegotiationOfferError",
        "type": "error",
    },
    {"inputs": [], "name": "InvalidBorrowerError", "type": "error"},
    {"inputs": [], "name": "InvalidCallbackError", "type": "error"},
    {"inputs": [], "name": "InvalidCollateralIdError", "type": "error"},
    {"inputs": [], "name": "InvalidLiquidationError", "type": "error"},
    {
        "inputs": [{"internalType": "uint256", "name": "_loanId", "type": "uint256"}],
        "name": "InvalidLoanError",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_fraction", "type": "uint256"}],
        "name": "InvalidProtocolFeeError",
        "type": "error",
    },
    {"inputs": [], "name": "InvalidRenegotiationOfferError", "type": "error"},
    {"inputs": [], "name": "InvalidSignatureError", "type": "error"},
    {"inputs": [], "name": "InvalidSignerError", "type": "error"},
    {"inputs": [], "name": "LengthMismatchError", "type": "error"},
    {
        "inputs": [
            {"internalType": "address", "name": "_liquidator", "type": "address"}
        ],
        "name": "LiquidatorOnlyError",
        "type": "error",
    },
    {"inputs": [], "name": "LoanExpiredError", "type": "error"},
    {
        "inputs": [
            {"internalType": "uint256", "name": "_expirationTime", "type": "uint256"}
        ],
        "name": "LoanNotDueError",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_loanId", "type": "uint256"}],
        "name": "LoanNotFoundError",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {"internalType": "uint256", "name": "_newMinOfferId", "type": "uint256"},
            {"internalType": "uint256", "name": "_minOfferId", "type": "uint256"},
        ],
        "name": "LowOfferIdError",
        "type": "error",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {
                "internalType": "uint256",
                "name": "_newMinRenegotiationOfferId",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "_minOfferId", "type": "uint256"},
        ],
        "name": "LowRenegotiationOfferIdError",
        "type": "error",
    },
    {"inputs": [], "name": "MaxCapacityExceededError", "type": "error"},
    {
        "inputs": [{"internalType": "uint256", "name": "_id", "type": "uint256"}],
        "name": "NotMintedError",
        "type": "error",
    },
    {"inputs": [], "name": "NotStrictlyImprovedError", "type": "error"},
    {"inputs": [], "name": "OnlyBorrowerCallableError", "type": "error"},
    {"inputs": [], "name": "OnlyLenderOrSignerCallableError", "type": "error"},
    {"inputs": [], "name": "PartialOfferCannotChangeDurationError", "type": "error"},
    {"inputs": [], "name": "PartialOfferCannotHaveFeeError", "type": "error"},
    {"inputs": [], "name": "RefinanceFullError", "type": "error"},
    {"inputs": [], "name": "RepaymentError", "type": "error"},
    {
        "inputs": [
            {"internalType": "uint256", "name": "sourcePrincipal", "type": "uint256"},
            {"internalType": "uint256", "name": "loanPrincipal", "type": "uint256"},
        ],
        "name": "TargetPrincipalTooLowError",
        "type": "error",
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_pendingProtocolFeeSetTime",
                "type": "uint256",
            }
        ],
        "name": "TooEarlyError",
        "type": "error",
    },
    {
        "inputs": [{"internalType": "uint8", "name": "sources", "type": "uint8"}],
        "name": "TooManySourcesError",
        "type": "error",
    },
    {"inputs": [], "name": "Unauthorized", "type": "error"},
    {
        "inputs": [
            {"internalType": "address", "name": "_authorized", "type": "address"}
        ],
        "name": "UnauthorizedError",
        "type": "error",
    },
    {"inputs": [], "name": "ZeroAddressError", "type": "error"},
    {"inputs": [], "name": "ZeroDurationError", "type": "error"},
    {"inputs": [], "name": "ZeroInterestError", "type": "error"},
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "lender",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "minOfferId",
                "type": "uint256",
            },
        ],
        "name": "AllOffersCancelled",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "lender",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "minRenegotiationId",
                "type": "uint256",
            },
        ],
        "name": "AllRenegotiationOffersCancelled",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "lender",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "signer",
                "type": "address",
            },
        ],
        "name": "ApprovedSigner",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "interest", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                ],
                "indexed": False,
                "internalType": "struct IBaseLoan.ImprovementMinimum",
                "name": "minimum",
                "type": "tuple",
            }
        ],
        "name": "ImprovementMinimumUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newDuration",
                "type": "uint256",
            }
        ],
        "name": "LiquidationAuctionDurationUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "liquidator",
                "type": "address",
            }
        ],
        "name": "LiquidationContractUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "offerId",
                "type": "uint256",
            },
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "indexed": False,
                "internalType": "struct IMultiSourceLoan.Loan",
                "name": "loan",
                "type": "tuple",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "fee",
                "type": "uint256",
            },
        ],
        "name": "LoanEmitted",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            }
        ],
        "name": "LoanForeclosed",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "repayment",
                "type": "uint256",
            },
        ],
        "name": "LoanLiquidated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "renegotiationId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "oldLoanId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "newLoanId",
                "type": "uint256",
            },
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "indexed": False,
                "internalType": "struct IMultiSourceLoan.Loan",
                "name": "loan",
                "type": "tuple",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "fee",
                "type": "uint256",
            },
        ],
        "name": "LoanRefinanced",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "totalRepayment",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "fee",
                "type": "uint256",
            },
        ],
        "name": "LoanRepaid",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "loanId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "liquidator",
                "type": "address",
            },
        ],
        "name": "LoanSentToLiquidator",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint8",
                "name": "newMax",
                "type": "uint8",
            }
        ],
        "name": "MaxSourcesUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "lender",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "offerId",
                "type": "uint256",
            },
        ],
        "name": "OfferCancelled",
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
                "components": [
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint256", "name": "fraction", "type": "uint256"},
                ],
                "indexed": False,
                "internalType": "struct IBaseLoan.ProtocolFee",
                "name": "fee",
                "type": "tuple",
            }
        ],
        "name": "ProtocolFeePendingUpdate",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "components": [
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint256", "name": "fraction", "type": "uint256"},
                ],
                "indexed": False,
                "internalType": "struct IBaseLoan.ProtocolFee",
                "name": "fee",
                "type": "tuple",
            }
        ],
        "name": "ProtocolFeeUpdated",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "lender",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "renegotiationId",
                "type": "uint256",
            },
        ],
        "name": "RenegotiationOfferCancelled",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "contract_added",
                "type": "address",
            }
        ],
        "name": "WhitelistedCallbackContractAdded",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "contract_removed",
                "type": "address",
            }
        ],
        "name": "WhitelistedCallbackContractRemoved",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "DOMAIN_SEPARATOR",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "FEE_UPDATE_NOTICE",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "INITIAL_DOMAIN_SEPARATOR",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "MAX_PROTOCOL_FEE",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_contract", "type": "address"}],
        "name": "addWhitelistedCallbackContract",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_signer", "type": "address"}],
        "name": "approveSigner",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {"internalType": "uint256", "name": "_minOfferId", "type": "uint256"},
        ],
        "name": "cancelAllOffers",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {
                "internalType": "uint256",
                "name": "_minRenegotiationId",
                "type": "uint256",
            },
        ],
        "name": "cancelAllRenegotiationOffers",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {"internalType": "uint256", "name": "_offerId", "type": "uint256"},
        ],
        "name": "cancelOffer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {"internalType": "uint256[]", "name": "_offerIds", "type": "uint256[]"},
        ],
        "name": "cancelOffers",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {"internalType": "uint256", "name": "_renegotiationId", "type": "uint256"},
        ],
        "name": "cancelRenegotiationOffer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {
                "internalType": "uint256[]",
                "name": "_renegotiationIds",
                "type": "uint256[]",
            },
        ],
        "name": "cancelRenegotiationOffers",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "uint256", "name": "offerId", "type": "uint256"},
                    {"internalType": "address", "name": "lender", "type": "address"},
                    {"internalType": "uint256", "name": "fee", "type": "uint256"},
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {"internalType": "uint256", "name": "capacity", "type": "uint256"},
                    {"internalType": "address", "name": "signer", "type": "address"},
                    {
                        "internalType": "bool",
                        "name": "requiresLiquidation",
                        "type": "bool",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "aprBps", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "expirationTime",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "address",
                                "name": "validator",
                                "type": "address",
                            },
                            {
                                "internalType": "bytes",
                                "name": "arguments",
                                "type": "bytes",
                            },
                        ],
                        "internalType": "struct IBaseLoan.OfferValidator[]",
                        "name": "validators",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct IBaseLoan.LoanOffer",
                "name": "_loanOffer",
                "type": "tuple",
            },
            {"internalType": "uint256", "name": "_tokenId", "type": "uint256"},
            {"internalType": "bytes", "name": "_lenderOfferSignature", "type": "bytes"},
            {"internalType": "bool", "name": "_withCallback", "type": "bool"},
        ],
        "name": "emitLoan",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.Loan",
                "name": "",
                "type": "tuple",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "getApprovedSigner",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCollectionManager",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getCurrencyManager",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getImprovementMinimum",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "interest", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                ],
                "internalType": "struct IBaseLoan.ImprovementMinimum",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLiquidationAuctionDuration",
        "outputs": [{"internalType": "uint48", "name": "", "type": "uint48"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getLiquidator",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_loanId", "type": "uint256"}],
        "name": "getLoanHash",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getMaxSources",
        "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_loanPrincipal", "type": "uint256"}
        ],
        "name": "getMinSourcePrincipal",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getPendingProtocolFee",
        "outputs": [
            {
                "components": [
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint256", "name": "fraction", "type": "uint256"},
                ],
                "internalType": "struct IBaseLoan.ProtocolFee",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getPendingProtocolFeeSetTime",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getProtocolFee",
        "outputs": [
            {
                "components": [
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint256", "name": "fraction", "type": "uint256"},
                ],
                "internalType": "struct IBaseLoan.ProtocolFee",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTotalLoansIssued",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_lender", "type": "address"},
            {"internalType": "uint256", "name": "_offerId", "type": "uint256"},
        ],
        "name": "getUsedCapacity",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
        ],
        "name": "isOfferCancelled",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "uint256", "name": "", "type": "uint256"},
        ],
        "name": "isRenegotiationOfferCancelled",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_contract", "type": "address"}],
        "name": "isWhitelistedCallbackContract",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "lenderMinOfferId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "name": "lenderMinRenegotiationOfferId",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_loanId", "type": "uint256"},
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.Loan",
                "name": "_loan",
                "type": "tuple",
            },
        ],
        "name": "liquidateLoan",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_collateralAddress",
                "type": "address",
            },
            {
                "internalType": "uint256",
                "name": "_collateralTokenId",
                "type": "uint256",
            },
            {"internalType": "uint256", "name": "_loanId", "type": "uint256"},
            {"internalType": "uint256", "name": "_repayment", "type": "uint256"},
            {"internalType": "bytes", "name": "_loan", "type": "bytes"},
        ],
        "name": "loanLiquidated",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
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
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "renegotiationId",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "loanId", "type": "uint256"},
                    {"internalType": "address", "name": "lender", "type": "address"},
                    {"internalType": "uint256", "name": "fee", "type": "uint256"},
                    {"internalType": "address", "name": "signer", "type": "address"},
                    {
                        "internalType": "uint256[]",
                        "name": "targetPrincipal",
                        "type": "uint256[]",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "aprBps", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "expirationTime",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "internalType": "bool",
                        "name": "strictImprovement",
                        "type": "bool",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.RenegotiationOffer",
                "name": "_renegotiationOffer",
                "type": "tuple",
            },
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.Loan",
                "name": "_loan",
                "type": "tuple",
            },
            {
                "internalType": "bytes",
                "name": "_renegotiationOfferSignature",
                "type": "bytes",
            },
        ],
        "name": "refinanceFull",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.Loan",
                "name": "",
                "type": "tuple",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "renegotiationId",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "loanId", "type": "uint256"},
                    {"internalType": "address", "name": "lender", "type": "address"},
                    {"internalType": "uint256", "name": "fee", "type": "uint256"},
                    {"internalType": "address", "name": "signer", "type": "address"},
                    {
                        "internalType": "uint256[]",
                        "name": "targetPrincipal",
                        "type": "uint256[]",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "aprBps", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "expirationTime",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "internalType": "bool",
                        "name": "strictImprovement",
                        "type": "bool",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.RenegotiationOffer",
                "name": "_renegotiationOffer",
                "type": "tuple",
            },
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.Loan",
                "name": "_loan",
                "type": "tuple",
            },
        ],
        "name": "refinancePartial",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.Loan",
                "name": "",
                "type": "tuple",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "renegotiationId",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "loanId", "type": "uint256"},
                    {"internalType": "address", "name": "lender", "type": "address"},
                    {"internalType": "uint256", "name": "fee", "type": "uint256"},
                    {"internalType": "address", "name": "signer", "type": "address"},
                    {
                        "internalType": "uint256[]",
                        "name": "targetPrincipal",
                        "type": "uint256[]",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "aprBps", "type": "uint256"},
                    {
                        "internalType": "uint256",
                        "name": "expirationTime",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "internalType": "bool",
                        "name": "strictImprovement",
                        "type": "bool",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.RenegotiationOffer[]",
                "name": "_renegotiationOffer",
                "type": "tuple[]",
            },
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.Loan[]",
                "name": "_loan",
                "type": "tuple[]",
            },
        ],
        "name": "refinancePartialBatch",
        "outputs": [
            {"internalType": "uint256[]", "name": "loanId", "type": "uint256[]"},
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.Loan[]",
                "name": "loans",
                "type": "tuple[]",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "_contract", "type": "address"}],
        "name": "removeWhitelistedCallbackContract",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_collateralTo", "type": "address"},
            {"internalType": "uint256", "name": "_loanId", "type": "uint256"},
            {
                "components": [
                    {"internalType": "address", "name": "borrower", "type": "address"},
                    {
                        "internalType": "uint256",
                        "name": "nftCollateralTokenId",
                        "type": "uint256",
                    },
                    {
                        "internalType": "address",
                        "name": "nftCollateralAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "address",
                        "name": "principalAddress",
                        "type": "address",
                    },
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "startTime", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "loanId",
                                "type": "uint256",
                            },
                            {
                                "internalType": "address",
                                "name": "lender",
                                "type": "address",
                            },
                            {
                                "internalType": "uint256",
                                "name": "principalAmount",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "accruedInterest",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "startTime",
                                "type": "uint256",
                            },
                            {
                                "internalType": "uint256",
                                "name": "aprBps",
                                "type": "uint256",
                            },
                        ],
                        "internalType": "struct IMultiSourceLoan.Source[]",
                        "name": "source",
                        "type": "tuple[]",
                    },
                ],
                "internalType": "struct IMultiSourceLoan.Loan",
                "name": "_loan",
                "type": "tuple",
            },
            {"internalType": "bool", "name": "_withCallback", "type": "bool"},
        ],
        "name": "repayLoan",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint8", "name": "maxSources", "type": "uint8"}],
        "name": "setMaxSources",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "setProtocolFee",
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
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "principalAmount",
                        "type": "uint256",
                    },
                    {"internalType": "uint256", "name": "interest", "type": "uint256"},
                    {"internalType": "uint256", "name": "duration", "type": "uint256"},
                ],
                "internalType": "struct IBaseLoan.ImprovementMinimum",
                "name": "_newMinimum",
                "type": "tuple",
            }
        ],
        "name": "updateImprovementMinimum",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint48", "name": "_newDuration", "type": "uint48"}
        ],
        "name": "updateLiquidationAuctionDuration",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "contract ILoanLiquidator",
                "name": "loanLiquidator",
                "type": "address",
            }
        ],
        "name": "updateLiquidationContract",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint256", "name": "fraction", "type": "uint256"},
                ],
                "internalType": "struct IBaseLoan.ProtocolFee",
                "name": "_newProtocolFee",
                "type": "tuple",
            }
        ],
        "name": "updateProtocolFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
