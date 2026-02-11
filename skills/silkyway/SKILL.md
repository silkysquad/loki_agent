---
name: silkyway
description: Agent payments on Solana. Send and receive USDC with cancellable escrow transfers. Optional on-chain accounts with policy-enforced spending limits for human-delegated automation.
---

# Silkyway

Agent payments on Solana using non-custodial escrow transfers.

## Setup

```bash
# Install the SDK
npm install -g https://silkyway.ai/sdk/silkyway-sdk-0.1.0.tgz

# Initialize (creates wallet and agent ID)
silk init

# Check your wallet address
silk wallet list

# Set to devnet for testing
silk config set-cluster devnet

# Fund with test tokens
silk wallet fund
silk balance
```

## Key Commands

### Sending Payments (Escrow)

```bash
silk pay <recipient> <amount> [--memo <text>]
```

- Locks USDC into on-chain escrow
- Recipient claims with `silk claim`
- Sender can cancel anytime before claim

### Claiming

```bash
silk payments list
silk claim <transfer-pda>
```

### Cancelling

```bash
silk cancel <transfer-pda>
```

### On-Chain Accounts (with spending limits)

If your human set up an account for you:

```bash
silk account sync
silk account status
silk account send <recipient> <amount>
```

Direct transfer with on-chain spending limits enforced.

## API Base

- Mainnet: `https://api.silkyway.ai`
- Devnet: `https://devnet-api.silkyway.ai`
