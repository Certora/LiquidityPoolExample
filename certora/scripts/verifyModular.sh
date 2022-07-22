certoraRun contracts/Pool.sol contracts/Asset.sol contracts/SymbolicFlashLoanReceiver.sol \
    --link Pool:asset=Asset \
	--verify Pool:certora/specs/highLevelModular.spec \
    --solc solc8.0 \
    --staging \
    --msg "Abstract Pool, modular - no quantifiers" \

