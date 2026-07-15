def is_valid_tx_hash(tx_hash):
    # Checks for 64-character hex strings starting with '0x'
    return tx_hash.startswith("0x") and len(tx_hash) == 66 and all(c in '0123456789abcdefABCDEF' for c in tx_hash[2:])

sample_tx = "0x" + "a" * 64
print(f"Is valid transaction hash: {is_valid_tx_hash(sample_tx)}")
