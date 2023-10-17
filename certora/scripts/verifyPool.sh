certoraRun \
    certora/harness/PoolHarness.sol \
    contracts/Asset.sol          \
    certora/helpers/tokens/*.sol \
    certora/harness/*.sol        \
    --verify PoolHarness:certora/specs/pool.spec \
    --solc solc-0.8.0 \
    --msg "Pool complete spec"

