certoraRun contracts/Pool.sol \
    --verify Pool:certora/specs/pool_havoc.spec \
    --solc solc-0.8.0 \
    --msg "Pool with no summarization"

