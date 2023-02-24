from web3 import Web3

# Accesses ethereum through infura node through HTTP and sets it to variable called w3
w3 = Web3(Web3.HTTPProvider(''))

# Defines the block the algorithm will start processing
block_number = 12965000

current_block = w3.eth.get_block(block_number)

print(current_block)