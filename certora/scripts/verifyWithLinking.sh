certoraRun contracts/Pool.sol contracts/Asset.sol \
    --verify Pool:certora/specs/pool_link.spec \
    --solc solc8.0 \
    --verify Pool:certora/specs/pool_link.spec \
    --link   Pool:asset=Asset
    --msg "Pool with linking" \
    --send_only

