certoraRun \
    contracts/Pool.sol           \
    contracts/Asset.sol          \
    certora/helpers/tokens/*.sol \
    certora/harness/*.sol        \
    --verify Pool:certora/specs/pool.spec \
    --solc solc8.0 \
    --msg "Pool complete spec" \
    --send_only

