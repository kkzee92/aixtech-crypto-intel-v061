# Asset-class strategies (v0.61)

Research playbooks only. Scores on synthetic data.

## Major (BTC/ETH style)
Adaptive multi-factor: EMA cross, Supertrend, Ichimoku cloud, Bollinger, Keltner, VWAP, MACD, Heikin-Ashi, Parabolic SAR, Donchian, GARCH/EWMA/realized/term-structure vol forecast, Fibonacci retracement/extension, Elliott wave proxy, options skew/gamma/vanna/charm, funding/basis/on-chain/OI/order-flow/liquidity/MVRV/SOPR/reserve/NVTS/Puell/CDD proxies. Correlation/beta/factor-adjusted outside stress. Risk cap 8%.

## Large-cap alt
Volume-profile/POC/VAH breakout + VWAP + MACD + multi-TF + relative strength z-score + regime cluster + volume delta + netflow + OI + order-flow + Fib + DEX LP depth + residual + factor. Cap 4%.

## Stablecoin
Adaptive peg deviation with volume + netflow + liquidity depth + SOPR + residual + CDD confirmation. Cap 0%.

## DeFi
Calm multi-scale + low anomaly + Supertrend + ADX + on-chain activity/smart-money + isolation + risk-parity + CVaR + LP depth/IL/fee dynamic + residual + HODL. Cap 2%.

## Meme
Qualified burst + StochRSI + hard horizon + volume-flow decay + anomaly/residual/liq heat/order-flow/social synthetic/Fib/narrative filter. Cap 0.5%.

## L2
Relative strength + MACD vs benchmark + adaptive MTF + correlation + cluster + vol forecast + transition probability + Elliott proxy + residual + factor. Cap 3%.

## RWA
Slow multi-scale + gap/anomaly halt + volume + isolation + forecast + CVaR + realized-cap + NVTS + residual + age-weighted. Cap 2%.

## Perpetual
Negative funding carry + contained drift + low anomaly + funding flip + correlation + residual + OI + order-flow + gamma/vanna/charm proxy + basis momentum. Cap 2%.

## AI-token
Hybrid burst + activity proxy + divergence + low isolation + strict horizon + smart-money + OI + transition + options vanna + social + residual + narrative + factor. Cap 1%.

All include multi-horizon consistency, RSI/MACD/Stoch/CCI divergence, regime clustering (k-means + HMM + GMM + transition + LOF + DBSCAN + spectral), adaptive Kelly/risk-parity/CVaR/entropy sizing research, vol-of-vol.
