certoraRun contracts/Pool.sol contracts/Asset.sol contracts/SymbolicFlashLoanReceiver.sol \
    --link Pool:asset=Asset \
	--verify Pool:certora/specs/mathProperties.spec \
    --solc solc8.0 \
    --staging \
    --rule $1 \
    --msg "Abstract Pool, mathProperties" \

