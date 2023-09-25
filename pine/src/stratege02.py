// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
//  weip2008

//@version=5
strategy("str_macd_cross", overlay=true, margin_long=100, margin_short=100, initial_capital = 19000)

// Input for MACD parameters
fastLength = input(12, title="Fast Length")
slowLength = input(26, title="Slow Length")
signalLength = input(9, title="Signal Length")

// // Calculate MACD
[macdLine, signalLine, _] = ta.macd(close, fastLength, slowLength, signalLength)

// Calculate MACD
// [macd, signal, hist] = ta.macd(close, fastLength, slowLength, signalLength)

// Buy when MACD crosses above signal line
if (ta.crossover(macdLine, signalLine))
    strategy.entry("Long", strategy.long)

// Sell when MACD crosses below signal line
if (ta.crossunder(macdLine, signalLine))
    strategy.close("Long")
