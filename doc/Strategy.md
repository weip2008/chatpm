# Strategy

1. MOVING AVERAGE STRATEGY

```c
//@version=5
strategy("Moving Average strategy", overlay=true, margin_long=100, margin_short=100)

i_ema50 = input.int(50, "EMALength1")
i_ema200 = input.int(200, "EMALength2")

ema50 = ta.ema(close, i_ema50)
ema200 = ta.ema(close, i_ema200)

isLong = ema50 > ema200 and close > ema50 and close > ema200
isShort = ema50 < ema200 and close < ema50 and close < ema200

stopLong = close < ema200 ? close : na
stopShort = close < ema200 ? close : na

longCondition = isLong and strategy.position_size == 0
if (longCondition)
strategy.entry(id = "Long", direction = strategy.long)
strategy.exit(id = "Exit Long", from_entry = "Long", stop = stopLong)

shortCondition = isShort and strategy.position_size == 0
if (shortCondition)
strategy.entry("Short", strategy.short)
strategy.exit(id = "Exit Short", from_entry = "Short", stop = stopShort)
```

2. MACD STRATEGY

```c
//@version=5
strategy("MACD strategy", overlay=true)

macd, signal, _ = ta.macd(close, 12, 24, 9)

isLong = macd > signal and macd > 0
isShort = macd < signal and macd < 0

stopLong = macd < signal ? close : na
stopShort = macd > signal ? close : na

longCondition = isLong and strategy.position_size == 0
if (longCondition)
strategy.entry(id = "Long", direction = strategy.long)
strategy.exit(id = "Exit Long", from_entry = "Long", stop = stopLong)

shortCondition = isShort and strategy.position_size == 0
if (shortCondition)
strategy.entry("Short", strategy.short)
strategy.exit(id = "Exit Short", from_entry = "Short", stop = stopShort)
```

3. RSI STRATEGY

```c
//@version=5
strategy("RSI strategy", overlay=true)

rsi_length = input.int(14, "RSI Length")
ema_length = input.int(14, "EMA Length")

rsi = ta.rsi(close, rsi_length)
ema = ta.ema(rsi, ema_length)

isLong = ema < rsi and rsi > 50 and rsi < 80
isShort = ema > rsi and rsi < 50 and rsi > 20

stopLong = ema > rsi and rsi < 50 ? close : na
stopShort = ema < rsi and rsi > 50 ? close : na

longCondition = isLong and strategy.position_size == 0
if (longCondition)
strategy.entry(id = "Long", direction = strategy.long)
strategy.exit(id = "Exit Long", from_entry = "Long", stop = stopLong)

shortCondition = isShort and strategy.position_size == 0
if (shortCondition)
strategy.entry("Short", strategy.short)
strategy.exit(id = "Exit Short", from_entry = "Short", stop = stopShort)
```

4. SUPERTREND STRATEGY

```c
//@version=5
strategy("Supertrend Strategy", overlay=true)

atrLength = input.int(10, "ATR Length")
factor = input.float(3.0, "Factor", step = 0.01)

supertrend, direction = ta.supertrend(factor, atrLength)

upTrend = direction < 0 ? supertrend : na
downTrend = direction < 0 ? na : supertrend

plot(upTrend, "Up trend", color.green, 1, plot.style_linebr)
plot(downTrend, "Down trend", color.red, 1, plot.style_linebr)

isLong = close > supertrend and direction < 0
isShort = close < supertrend and direction > 0

stopLong = close < supertrend ? close : na
stopShort = close > supertrend ? close : na

longCondition = isLong and strategy.position_size == 0
if (longCondition)
strategy.entry(id = "Long", direction = strategy.long)
strategy.exit(id = "Exit Long", from_entry = "Long", stop = stopLong)

shortCondition = isShort and strategy.position_size == 0
if (shortCondition)
strategy.entry("Short", strategy.short)
strategy.exit(id = "Exit Short", from_entry = "Short", stop = stopShort)
```

5. SINGLE ENTRY -- MULTIPLE EXITS STRATEGY

```c
//@version=5
strategy("Single Entry and Multiple exits Strategy")

rsi = ta.rsi(close, 14)

plot(rsi, "RSI", color.green)

middleLine = hline(50, 'Middle Line', color.white)
overBought = hline(80, 'Over Bought', color.white)
overSold = hline(20, 'Over Sold', color.white)

isLong = rsi > 50

stopLong1 = rsi < 50 ? close : na
stopLong2 = rsi < 40 ? close : na
stopLong3 = rsi < 30 ? close : na
stopLong4 = rsi < 20 ? close : na

longCondition = isLong and strategy.position_size == 0
if (longCondition)
strategy.entry(id = "Long", direction = strategy.long, qty = 4)
strategy.exit(id = "Exit Long-1", from_entry = "Long", qty = 1, stop = stopLong1)
strategy.exit(id = "Exit Long-2", from_entry = "Long", qty = 1, stop = stopLong2)
strategy.exit(id = "Exit Long-3", from_entry = "Long", qty = 1, stop = stopLong3)
strategy.exit(id = "Exit Long-4", from_entry = "Long", qty = 1, stop = stopLong4)
```

6. PYRAMIDING || MULTIPLE ENTRIES -- SINGLE EXIT STRATEGY

```c
//@version=5
strategy("Multiple Entry and Single exits Strategy")

rsi = ta.rsi(close, 14)

plot(rsi, "RSI", color.green)

middleLine = hline(50, 'Middle Line', color.white)
overBought = hline(80, 'Over Bought', color.white)
overSold = hline(20, 'Over Sold', color.white)

isLong1 = rsi > 50
isLong2 = rsi > 60
isLong3 = rsi > 70
isLong4 = rsi > 80

stopLong = rsi < 50 ? close : na

longCondition1 = isLong1 and strategy.position_size == 0
if (longCondition1)
strategy.entry(id = "Long-1", direction = strategy.long, qty = 1)

longCondition2 = isLong2 and strategy.position_size == 0
if (longCondition2)
strategy.entry(id = "Long-2", direction = strategy.long, qty = 1)

longCondition3 = isLong2 and strategy.position_size == 0
if (longCondition3)
strategy.entry(id = "Long-3", direction = strategy.long, qty = 1)

longCondition4 = isLong2 and strategy.position_size == 0
if (longCondition4)
strategy.entry(id = "Long-4", direction = strategy.long, qty = 1)

strategy.exit(id = "Exit Long", qty_percent = 100, stop = stopLong)
```

7. STRATEGY WITH POINTS BASED TARGET EXIT

```c
//@version=5
strategy("Strategy With Points Based Target Exit")

pointToExit = input.int(10, "Points to Exit", minval = 1, maxval = 100)

rsi = ta.rsi(close, 14)

plot(rsi, "RSI", color.green)

middleLine = hline(50, 'Middle Line', color.white)
overBought = hline(80, 'Over Bought', color.white)
overSold = hline(20, 'Over Sold', color.white)

isLong = rsi > 50
stopLong = rsi < 50 ? close : na

targetLong = if(high >= strategy.position_avg_price + pointToExit)
strategy.position_avg_price + pointToExit

longCondition = isLong and strategy.position_size == 0
if (longCondition)
strategy.entry(id = "Long", direction = strategy.long, qty = 4)

strategy.exit(id = "Stop Loss Exit", from_entry = "Long", qty = 1, stop = stopLong)
strategy.exit(id = "Target Exit", from_entry = "Long", qty = 1, stop = targetLong)

```

8. STRATEGY WITH PERCENTAGE BASED TARGET EXIT

```c
//@version=5
strategy("Strategy With Percentage Based Target Exit")

percentTargetTtoExit = input.int(5, "Points to Exit", minval = 1, maxval = 100)

rsi = ta.rsi(close, 14)

plot(rsi, "RSI", color.green)

middleLine = hline(50, 'Middle Line', color.white)
overBought = hline(80, 'Over Bought', color.white)
overSold = hline(20, 'Over Sold', color.white)

isLong = rsi > 50
stopLong = rsi < 50 ? close : na

targetLong = if(high >= strategy.position_avg_price * ((100 + percentTargetTtoExit) / 100))
strategy.position_avg_price * ((100 + percentTargetTtoExit) / 100)

longCondition = isLong and strategy.position_size == 0
if (longCondition)
strategy.entry(id = "Long", direction = strategy.long, qty =100)

strategy.exit(id = "SL Exit", from_entry = "Long", qty = 75, stop = stopLong)
strategy.exit(id = "Target Exit", from_entry = "Long", qty = 25, stop = targetLong)
```

9. DIFFERENT ORDER TYPES

```c
//@version=5
strategy("Order Types", overlay=true)

rsi = ta.rsi(close, 14)

stopLoss = rsi < 50 ? close : na

longCondition = rsi > 80

// Market order
// if (longCondition)
// strategy.entry("Long", strategy.long)
// strategy.exit("Long Exit", from_entry = "Long", stop = stopLoss)

// Limit order (lower)
if (longCondition)
strategy.entry("Long", strategy.long, limit = low)
strategy.exit("Long Exit", from_entry = "Long", stop = stopLoss)

// // Stop order (higher)
// if (longCondition)
// strategy.entry("Long", strategy.long, stop = high)
// strategy.exit("Long Exit", from_entry = "Long", stop = stopLoss)
```

10. MULTI TIMEFRAME DONCHIAN CHANNEL Strategy(asd)

```
looks good for 5 min. HTF on 15min. need modify.
```

```c
//@version=5
strategy("Multi Timeframe Donchian Channel", overlay = true)

htf = input.timeframe("D", "Select Timeframe")
length = input.int(50, "Length", minval = 1)

lower = ta.lowest(length)
upper = ta.highest(length)

lowerHtf = request.security(syminfo.tickerid, htf, lower1, barmerge.gaps_on, barmerge.lookahead_on)
upperHtf = request.security(syminfo.tickerid, htf, upper1, barmerge.gaps_on, barmerge.lookahead_on)

middleHtf = math.avg(lowerHtf, upperHtf)

plot(middleHtf, "Middle", color.orange)
pLower = plot(lowerHtf, "Lower", color.aqua)
pUpper = plot(upperHtf, "Upper", color.aqua)

fill(pLower, pUpper, color = color.new(color.aqua, 90))

isLong = ta.crossunder(close, lowerHtf)
isShort = ta.crossover(close, upperHtf)

longCondition = isLong
shortCondition = isShort

if (longCondition)
strategy.entry("Long", strategy.long)

if (shortCondition)
strategy.entry("Short", strategy.short)
```

11. GET THE STRATEGY SIGNALS EARLY AND ON THE EXACT BAR

```c
//@version=5
strategy("Early strategy", overlay=true, margin_long=100, margin_short=100, process_orders_on_close = true)

ema50 = ta.ema(close, 50)
ema200 = ta.ema(close, 200)

plot(ema50, color = color.maroon)
plot(ema200, color = color.navy)

bullish_stoploss = close < ema50 ? close : na

longCondition = ta.crossover(ema50, ema200)

plotshape(longCondition, style = shape.arrowup, color = color.green, location = location.belowbar, size = size.normal)
if (longCondition)
    strategy.entry("Long", strategy.long, qty = 1)
strategy.exit(id = "Exit", from_entry = "Long", qty = 1, stop = bullish_stoploss)
```

12. TWO SUPER-TRENDS STRATEGY

```c
//@version=5
strategy("Two Supertrend strategy", overlay=true, margin_long=100, margin_short=100, process_orders_on_close = true)
import TradingView/ta/5

// First Supertrend
atr_period_1 = input.int(10, "1st Supertrend ATR length")
factor_1 = input.int(3, '1st Supertrend factor')
supertrend_1, direction_1 = ta.supertrend(factor_1, atr_period_1)
supertrend_color_1 = (direction_1 == -1) ? color.green : color.red
plot(supertrend_1, "1st Supertrend", color = supertrend_color_1)

// Second Supertrend
atr_period_2 = input.int(10, "2nd Supertrend ATR length")
factor_2 = input.int(5, '2nd Supertrend factor')
supertrend_2, direction_2 = ta.supertrend(factor_2, atr_period_2)
supertrend_color_2 = (direction_2 == -1) ? color.lime : color.maroon
plot(supertrend_2, "2nd Supertrend", color = supertrend_color_2)


longCondition = close > supertrend_1 and close > supertrend_2
long_stop_loss = close < supertrend_1 ? close : na

shortCondition = close < supertrend_1 and close < supertrend_2
short_stop_loss = close > supertrend_1 ? close : na

if (longCondition)
    strategy.entry("buy", strategy.long)
strategy.exit(id = 'long', from_entry = "buy", qty = 100, stop = long_stop_loss)

if (shortCondition)
    strategy.entry("sell", strategy.short)
strategy.exit(id = 'short EX', from_entry = "sell", qty = 100, stop = short_stop_loss)
```

13. HOW TO CREATE A STRATEGY WITH STOPLOSS AND TARGET

```c
//@version=5
strategy("Strategy With Stoploss & Target", overlay=true, margin_long=100, margin_short=100, process_orders_on_close = true)

ema = ta.ema(close, input(50, "length"))

longCondition = close > ema
if (longCondition and strategy.position_size1 == 0)
    strategy.entry("Buy", strategy.long)

strategy.exit("Buy-exit", from_entry = "Buy", stop = strategy.position_avg_price - 50, limit = strategy.position_avg_price + 100, comment = "exit")
```
