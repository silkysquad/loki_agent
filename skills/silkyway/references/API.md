# Silkyway API Reference

## Endpoints

### POST /api/tx/create-transfer
Build escrow transfer transaction.

```json
{
  "sender": "BrKz4GQN1sxZWoGLbNTojp4G3JCFLRkSYk3mSRWhKsXp",
  "recipient": "7xKXz9BpR3mFVDg2Thh3AG6sFRPqNrDJ4bHUkR8Y7vNx",
  "amount": 10.00,
  "token": "usdc",
  "memo": "Payment for code review"
}
```

### POST /api/tx/claim-transfer
Claim escrow transfer.

```json
{
  "transferPda": "9aE5kBqRvF3mNcXz8BpR3mFVDg2Thh3AG6sFRPqNrDJ4",
  "claimer": "7xKXz9BpR3mFVDg2Thh3AG6sFRPqNrDJ4bHUkR8Y7vNx"
}
```

### POST /api/tx/cancel-transfer
Cancel escrow transfer (refunds sender).

```json
{
  "transferPda": "9aE5kBqRvF3mNcXz8BpR3mFVDg2Thh3AG6sFRPqNrDJ4",
  "canceller": "BrKz4GQN1sxZWoGLbNTojp4G3JCFLRkSYk3mSRWhKsXp"
}
```

### POST /api/tx/submit
Submit signed transaction.

```json
{
  "signedTx": "AQAAAAAAAAAAAAAA...base64-signed...AAAAAAA="
}
```

### GET /api/transfers/:pda
Get transfer details.

### GET /api/transfers?wallet=<pubkey>
List all transfers for wallet.

### POST /api/tx/faucet
Devnet airdrop (devnet only).

```json
{
  "wallet": "BrKz4GQN1sxZWoGLbNTojp4G3JCFLRkSYk3mSRWhKsXp",
  "token": "usdc"
}
```

### GET /api/account/by-operator/:pubkey
Find accounts where wallet is operator.

### POST /api/account/transfer
Transfer from account (policy-enforced).

```json
{
  "signer": "7xKXz9BpR3mFVDg2Thh3AG6sFRPqNrDJ4bHUkR8Y7vNx",
  "accountPda": "9aE5kBqRvF3mNcXz8BpR3mFVDg2Thh3AG6sFRPqNrDJ4",
  "recipient": "Dg2Thh3AG6sFRPqNrDJ4bHUkR8Y7vNx7xKXz9BpR3mFV",
  "amount": 3000000
}
```

## Transfer Statuses

| Status | Description |
|--------|-------------|
| ACTIVE | Tokens locked in escrow |
| CLAIMED | Recipient claimed tokens |
| CANCELLED | Sender cancelled, tokens refunded |
| EXPIRED | Transfer expired |

## Error Codes

| Code | Description |
|------|-------------|
| 6000 | TransferAlreadyClaimed |
| 6001 | TransferAlreadyCancelled |
| 6002 | TransferExpired |
| 6003 | ClaimTooEarly |
| 6004 | Unauthorized |
| 6005 | PoolPaused |
| 6006 | InsufficientFunds |
| 6001 | ExceedsPerTxLimit (accounts) |
| 6003 | AccountPaused |
