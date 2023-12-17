# IT WALA

1. HOW TO COLOR THE BACKGROUND ?

```py
//@version=5
indicator("Background Color", overlay = true)

bgcolor(color.new ( color.orange, 85)) // 15
plot(close)

```

2. HOW TO COLOR A BAR ?

```py
//@version=5
indicator("Bar Color")
barcolor(close > open ? color.white : color.orange)
```

3. HOW TO PLOT PREVIOUS CLOSE VALUE ?

```c
//@version=5
indicator("Plot Previous close")

plot(close, color = color.red) // This is the current close value
plot(close1, color = color.white) // This is the previous close value
```

4. HOW TO PLOT OHLC VALUES ?

```c
//@version=5
indicator("Plot OHLC")

plot(open)
plot(high, 'high', color.green)
plot(low, color = color.red)
plot(close, color = color.white)
```

5. HOW TO PLOT A BAR ?

```c
//@version=5
indicator("Plot Bar")

barColor = (close > open) ? color.green : color.red
plotbar(open, high, low, close, title="BAR", color=barColor)
```

6. PLOT CANDLE

```c
//@version=5
indicator("Plot candle")

barColor = (close > open) ? color.green : color.red
plotcandle(open, high, low, close, title="BAR", color = barColor)
```

7. PLOT ARROW

```c
//@version=5
indicator("Plot arrow", overlay = true)

arrowType = close - open
plotarrow(arrowType, title ="Arrow", colorup = color.green, colordown = color.red, minheight = 12, maxheight = 50)
```

8. PLOT CHARACTER AND TEXT

```c
//@version=5
indicator("Plot char", overlay = true)

bullish = close > open
bearish = close < open

plotchar(bullish, char="^", location = location.belowbar, color= color.green, text = "bullish", textcolor = color.white, size = size.tiny)
plotchar(bearish, char="$", location = location.abovebar, color= color.red, text = "bearish", textcolor = color.white, size = size.tiny)
```

9. PLOT SHAPE AND TEXT

```c
//@version=5
indicator("Plot shape", overlay = true)

diff = close > open

plotshape(diff, title = "SHAPE", style = shape.diamond, location = location.abovebar, color= color.orange, text = "bullish", textcolor = color.green, size = size.tiny)
```

10. INTEGER INPUT

```c
//@version=5
indicator("Input integer")

plot(input.int(title = "integer value", defval = 1, maxval = 10, minval = 1, step = 2))
```

11. DECIMAL INPUT

```c
//@version=5
indicator("Input Decimal Values")

plot(input.int(title = "Enter value:", defval = 1.5, maxval = 10.0, minval = 1.0, step = 0.5))
```

12. BOOLEAN INPUT

```c
//@version=5
indicator("Input boolean")

changeColor = input.bool(defval = true, title = "change Color yes/no") ? color.green : color.red
plot(close, color = changeColor)
```

13. COLOR INPUT

```c
//@version=5
indicator("Input color")

i_color = input.color(defval = color.orange, title = "Select Color")
plot(close, color = i_color)
```

14. PRICE INPUT

```c
//@version=5
indicator("Input Price")

i_price = input.price(defval = 10, title = "Enter Price:")
plot(i_price)
```

15. RESOLUTION INPUT

```c
//@version=5
indicator("Input Resolution")

i_resolution = input.timeframe(defval = "D", title = "Select Resolution", options = 'D','W','M')
plot(close)
```

16. SYMBOL INPUT

```c
//@version=5
indicator("Input Symbol")

i_symbol = input.symbol(defval = "TSLA", title = "Select Symbol")
plot(close)
```

17. STRING INPUT

```c
//@version=5
indicator("Input String")

i_txt = input.string(defval = "TSLA will up", title = "Enter Text")
plot(close)
```

18. SOURCE INPUT

```c
//@version=5
indicator("Input Source")

i_source = input.source(defval = high, title = "Select Source")
plot(i_source)
```

19. SESSION INPUT

```c
//@version=5
indicator("Input Session")

i_session = input.session(defval = "0930-1600", title = "Select Session", options = "0930-1600", "1300-1700", "1700-2100")

t = time(timeframe.period, i_session)

plot(close, color = (time == t) ? color.green : color.red)
```

20. BAR STATE, IS FIRST BAR, IS LAST BAR

```c
//@version=5
indicator("First and Last Bar")

isFirstBar = (barstate.isfirst) ? 1 : 0
isLastBar = (barstate.islast) ? 1 : 0

plot(isFirstBar, color = color.green)
plot(isLastBar, color = color.red)
```

21. NA values

```c
//@version=5
indicator("NA Value")

value = (close > open) ? close : na

plot(value, style = plot.style_linebr)
```

22. BARS SINCE FUNCTION

```c
//@version=5
indicator("Bars Since", '')

value = ta.barssince(close > open)

// count bars since bull
// value = ta.barssince(open > close)
// calculate how many bullish (green) bars continuous

plot(value)
```

23. VALUE WHEN FUNCTION

```c

//@version=5
indicator("Value When", '')

value = ta.valuewhen(close > open, close, 0)
// (open > close) // more info.
plot(value)

```

24. INDICATOR REPAINTING ISSUE

```c
//@version=5
indicator("Indicator Repaint", 'Ind RP')

higherTFClose = request.security(syminfo.tickerid, "W", close) // Repaint
//higherTFClose = request.security(syminfo.tickerid, "W", close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on) //Does not Repaint

plot(higherTFClose)
```

25. MOVING AVERAGES - SIMPLE, EXPONENTIAL

```c
//@version=5
indicator("Moving Average", 'MA')

i_length = input.int(20, 'Length', minval = 1, maxval = 1000)

sma = ta.sma(close, i_length)
ema = ta.ema(close, i_length)

plot(sma, color = color.red)
plot(ema, color = color.green)
```

26. EMA CROSS DEMO (private published)

```C
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © weip2008

//@version=5
indicator("MT EMA CROSS BUY/SELL V1", overlay = true)

xUnder = ta.crossunder(ta.ema(close, 5), ta.ema(close, 20))
xOver = ta.crossover(ta.ema(close, 5), ta.ema(close, 20))

plotshape(xUnder, title = "SELL", style = shape.xcross, location = location.abovebar, color= color.orange, text = "sell", textcolor = color.red, size = size.tiny)
plotshape(xOver, title = "BUY", style = shape.circle, location = location.belowbar, color= color.green, text = "buy", textcolor = color.green, size = size.tiny)

```

27. MACD

```c
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © weip2008

//@version=5
indicator("MACD")

fast_length = input.int(12, "Fast length")
slow_length = input.int(26, "Slow length")
signal_length = input.int(9, "Signal length")

fast_ma = ta.ema(close, fast_length)
slow_ma = ta.ema(close, slow_length)

macd = fast_ma - slow_ma
signal = ta.ema(macd, signal_length)

plot(macd, title = "MACD", color = color.yellow)
plot(signal, "Signal", color.white)
hline(0, 'zero line', color.green)
```

28. RSI WITH AVERAGE

```c
//@version=5
indicator("RSI WITH AVERAGE", "RSI")

rsi_length = input.int(14, "RSI Length")
ema_length = input.int(14, "EMA Length")

rsi = ta.rsi(close, rsi_length)
ma = ta.ema(rsi, ema_length)

plot(rsi, title = "RSI", color = color.purple)
plot(ma, title = "EMA", color = color.yellow)

hline(50, 'Middle Line', color.white)
hline(70, 'Over Bought', color.white)
hline(30, 'Over Sold', color.white)
```

29. ATR

```c
//@version=5
indicator("Average True Range", "ATR")

length = input.int(14, "Length")

atr = ta.atr(length)

plot(atr, color = color.yellow)
```

30. VWAP

```c
//@version=5
indicator("VWAP", "VWAP", true)
plot(ta.vwap(close))
```

31. COMMODITY CHANNEL INDEX

```c
//@version=5
indicator("COMMODITY CHANNEL INDEX", "CCI")
plot(ta.cci(close, input.int(14, "Length")))
```

32. STOCHASTIC INDICATOR

```c
//@version=5
indicator("Stochastic")
i_kLength = input.int(14, "%K Length", minval = 1)
i_dSmoothing = input.int(3, "%D Smoothing", minval = 1)

k = ta.stoch(close, high, low, i_kLength)
d = ta.sma(k, i_dSmoothing)

plot(k, "%K", color.green)
plot(d, "%D", color.red)

h0 = hline(80, "Upper Band", color.white)
h1 = hline(20, "Lower Band", color.white)
fill(h0, h1, color.rgb(33, 150, 243, 90), "Background")
```

33. PARABOLIC SAR INDICATOR

```c
//@version=5
indicator("Parabolic SAR", overlay = true)

start = input.float(defval = 0.02, title = "Start", step = 0.01)
increment = input.float(defval = 0.02, title = "Increment", step = 0.01)
maximum = input.float(defval = 0.2, title = "Maximum Value", step = 0.1)

sar = ta.sar(start, increment, maximum)
plot(sar, style = plot.style_circles, color = close > sar ? color.green : color.red)
```

34. SUPERTREND

```c
//@version=5
indicator("Supertrend", overlay = true)
import TradingView/ta/5

atrLength = input.int(10, "ATR Length")
factor = input.float(3.0, "Factor", step = 0.01)

supertrend, direction = ta.supertrend(factor, atrLength)

upTrend = direction < 0 ? supertrend : na
downTrend = direction < 0 ? na : supertrend

plot(upTrend, "Up trend", color.green, 1, plot.style_linebr)
plot(downTrend, "Down trend", color.red, 1, plot.style_linebr)
```

35. MULTI TIME-FRAME MOVING AVERAGE

```c
//@version=5
indicator("Multi Timeframe Moving Average", overlay = true)

tf = input.timeframe("D", "Select Timeframe")
length = input.int(defval = 50, title = "length")

currentMA = ta.sma(close, length)

higherTFMA = request.security(syminfo.tickerid, tf, currentMA1, barmerge.gaps_on, barmerge.lookahead_on)

plot(higherTFMA)
```

36. MULTI TIME-FRAME MACD

```c
//@version=5
indicator("Multi Timeframe MACD")

tf = input.timeframe("D", "Select Timeframe")

macd, signal, _ = ta.macd(close, 12, 26, 9)

length = input.int(defval = 50, title = "length")

currentMA = ta.sma(close, length)

higherTFMACD = request.security(syminfo.tickerid, tf, macd1, barmerge.gaps_on, barmerge.lookahead_on)
higherTFSignal = request.security(syminfo.tickerid, tf, signal1, barmerge.gaps_on, barmerge.lookahead_on)

plot(higherTFMACD, "MACD", color.red)
plot(higherTFSignal, "signal", color.green)
hline(0, "Zero Line", color.white)
```

37. MULTI TIME-FRAME RSI with AVERAGE

```c
indicator("Multi Timeframe RSI")

tf = input.timeframe("D", "Select Timeframe")

rsi_length = input.int(14, "RSI Length")
ema_length = input.int(14, "EMA Length")

rsi = ta.rsi(close, rsi_length)
ma = ta.ema(rsi, ema_length)

higherTFRSI = request.security(syminfo.tickerid, tf, rsi1, barmerge.gaps_on, barmerge.lookahead_on)
higherTFMA = request.security(syminfo.tickerid, tf, ma1, barmerge.gaps_on, barmerge.lookahead_on)

plot(higherTFRSI, "RSI", color.red)
plot(higherTFMA, "EMA", color.green)

hline(50, 'Middle Line', color.white)
hline(70, 'Over Bought', color.white)
hline(30, 'Over Sold', color.white)
```

38. MULTI TIME-FRAME SUPER TREND

```c
//@version=5
indicator("Multi Timeframe Supertrend", overlay = true)

tf = input.timeframe("D", "Select Timeframe")

atrLength = input.int(10, "ATR Length")
factor = input.float(3.0, "Factor", step = 0.01)

supertrend, direction = ta.supertrend(factor, atrLength)

higherTFSuperTrend = request.security(syminfo.tickerid, tf, supertrend1, barmerge.gaps_off, barmerge.lookahead_on)
higherTFDirection = request.security(syminfo.tickerid, tf, direction1, barmerge.gaps_off, barmerge.lookahead_on)

supertrendColor = higherTFDirection == -1 and higherTFDirection1 == -1 ? color.green :
higherTFDirection == 1 and higherTFDirection1 == 1 ? color.red :
color.new(color.white, 100)

plot(higherTFSuperTrend, "Super Trend", supertrendColor)
```

39. HIGHEST / LOWEST FUNCTION

```c
//@version=5
indicator("H/L function")

highest = ta.highest(close, 10)
plot(highest)
plot(ta.lowest(close, 10), "lowest", color.red)
```

40. DRAW A LINE

```c
//@version=5
indicator("Line", overlay = true)

if barstate.islast
highLine = line.new(x1=bar_index10, y1=high10, x2=bar_index, y2=high)
line.set_color(highLine, color.green)

if barstate.islast
lowLine = line.new(x1=bar_index10, y1=low10, x2=bar_index, y2=low)
line.set_color(lowLine, color.red)
line.set_extend(lowLine, extend.none)
line.set_style(lowLine, line.style_dashed)
line.set_width(lowLine, 2)
// line.delete(lowLine1)
```

41. DRAW A HORIZONTAL LINE

```c
//@version=5
indicator("Horizontal Line", overlay = true)

hline(4400, title = "hline High", color = color.gray, linestyle = hline.style_dashed, linewidth = 2, editable = true)
```

42. Draw a label

```c
//@version=5
indicator("Label", overlay = true)

//@version=5
indicator("Label", overlay = true)

label1 = label.new(bar_index, high, text = str.tostring(high), color = color.green, style = label.style_label_down, textcolor = color.white)
label.delete(label11)
```

43. DRAW A TABLE

```c
//@version=5
indicator("Tabel", overlay = true)

var myTable = table.new(position = position.bottom_center, columns = 4, rows = 2,
bgcolor =color.white, border_width = 1, frame_color = color.green, frame_width = 3, border_color = color.green)

table.cell(myTable, column = 0, row = 0, text = "Open", text_color = color.white, bgcolor = color.orange)
table.cell(myTable, column = 1, row = 0, text = "High", text_color = color.white, bgcolor = color.green)
table.cell(myTable, column = 2, row = 0, text = "Low", text_color = color.white, bgcolor = color.red)
table.cell(myTable, column = 3, row = 0, text = "Close", text_color = color.white, bgcolor = color.blue)

table.cell(myTable, column = 0, row = 1, text = str.tostring(open))
table.cell(myTable, column = 1, row = 1, text = str.tostring(high))
table.cell(myTable, column = 2, row = 1, text = str.tostring(low))
table.cell(myTable, column = 3, row = 1, text = str.tostring(close))
```

44. DRAW A BOX

```c
//@version=5
indicator("Box", overlay = true)

myBox = box.new(left = bar_index10, top = high, right = bar_index, bottom = low10)
box.set_border_color(myBox, color.green)
box.set_border_width(myBox, 3)
box.set_border_style(myBox,line.style_solid)
box.set_bgcolor(myBox, color.white)
box.set_text(myBox, "BOX")
box.set_text_size(myBox, size.huge)
box.set_text_color(myBox,color.orange)
box.set_text_wrap(myBox, text.wrap_auto)
box.delete(myBox1)
```

45. CROSS-OVER & CROSS-UNDER FUNCTIONS

```c
//@version=5
indicator("Cross over and cross under", "cross", overlay = true)

ema50 = ta.ema(close, 50)
ema200 = ta.ema(close, 200)

isCross = ta.cross(ema50, ema200)

plotshape(isCross, style = shape.diamond, color = color.green, size = size.tiny)

plot(ema50, color = color.green)
plot(ema200, color = color.blue)
```

46. MOVING AVERAGE STRATEGY

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

47. MACD STRATEGY

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

48. RSI STRATEGY

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

49. SUPERTREND STRATEGY

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

50. SINGLE ENTRY -- MULTIPLE EXITS STRATEGY

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

51. PYRAMIDING || MULTIPLE ENTRIES -- SINGLE EXIT STRATEGY

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

52. STRATEGY WITH POINTS BASED TARGET EXIT

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

53. STRATEGY WITH PERCENTAGE BASED TARGET EXIT

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

54. DATE RANGE

```c
//@version=5
indicator("Date Range", overlay = true)

startDate = input.int(defval = 1, minval = 1, maxval = 31, title = "Start Date")
startMonth = input.int(defval = 1, minval = 1, maxval = 12, title = "Start Month")
startYear = input.int(defval = 2022, minval = 2000, maxval = 2100, title = "Start Year")

endDate = input.int(defval = 31, minval = 1, maxval = 31, title = "End Date")
endMonth = input.int(defval = 12, minval = 1, maxval = 12, title = "End Month")
endYear = input.int(defval = 2022, minval = 2000, maxval = 2100, title = "End Year")

inDateRange = (time >= timestamp(syminfo.timezone, startYear, startMonth, startDate, 0, 0, 0)) and
(time < timestamp(syminfo.timezone, endYear, endMonth, endDate, 0, 0, 0))

plot(inDateRange ? close : na, linewidth = 3)
```

55. DATE & TIME RANGE

```c
//@version=5
indicator("Date and Time Range", overlay = true)

startDateTime = timestamp(2023, 10, 06, 09, 30, 0)
endDateTime = timestamp(2023, 11, 06, 09, 30, 0)

inDateAndTimeRange = (time >= startDateTime and time < endDateTime)

bgcolor(inDateAndTimeRange ? color.new(color.gray, 90) : na)

plot(inDateAndTimeRange ? close : na, linewidth = 3)
```

56. ARRAY

```c
//@version=5
indicator("Array")

myArray = array.new_int()
array.insert(myArray, 0, 0)
array.insert(myArray, 1, 10)
array.insert(myArray, 2, 20)
array.insert(myArray, 3, 30)
array.insert(myArray, 4, 40)

plot(array.get(myArray, 0), color=color.red)
plot(array.get(myArray, 1), color=color.blue)
plot(array.get(myArray, 2), color=color.green)
plot(array.get(myArray, 3), color=color.white)
plot(array.get(myArray, 4), color=color.orange)

```

57. FOR LOOP

```c
//@version=5
indicator("Array")

arr = array.new_int()
array.insert(arr, 0, 0)
array.insert(arr, 1, 1)
array.insert(arr, 2, 2)
array.insert(arr, 3, 3)
array.insert(arr, 4, 4)

int result = 0
int size = array.size(arr) - 1

for i=0 to size
result := result + array.get(arr, i)

plot(result, color=color.orange)

// plot(array.sum(arr))

1. MTF BB

```c
//@version=5
indicator("Multi Ttimeframe Bollinger Band", "MTF BB", true)

length = input.int(50, "Length")
multiplier = input.int(2, "multiplier")
htf = input.timeframe("D", "timeframe")

middle, upper, lower = ta.bb(close, length, multiplier)

middleHtf = request.security(syminfo.tickerid, htf, middle1,
gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
upperHtf = request.security(syminfo.tickerid, htf, upper1,
gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
lowerHtf = request.security(syminfo.tickerid, htf, lower1,
gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

plot(middleHtf, color = color.white)
plot(upperHtf, color = color.orange)
plot(lowerHtf, color = color.lime)
```

58. DIFFERENT ORDER TYPES

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

1. INTRA-DAY FIRST AND LAST BARS

```c
//@version=5
indicator("Daily First And Last Bar")

t = time("1440", session.regular)
bgcolor(session.isfirstbar ? color.new(color.aqua, 70) : na)
bgcolor(session.islastbar ? color.new(color.red, 70) : na)
```

59. PIVOT POINT LEVELS

```c
//@version=5
indicator("Pivot Points", overlay = true)

prevClose = request.security(syminfo.tickerid, "D", close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevHigh = request.security(syminfo.tickerid, "D", high1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevLow = request.security(syminfo.tickerid, "D", low1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

pivot = (prevClose + prevHigh + prevLow) / 3

R1 = (pivot * 2) - prevLow
R2 = pivot + (prevHigh - prevLow)
R3 = prevHigh + (2 * (pivot - prevLow))

S1 = (pivot * 2) - prevHigh
S2 = pivot - (prevHigh - prevLow)
S3 = prevLow - (2 * (prevHigh - pivot))

plot(pivot, "pivot", color.white)

plot(R1, "R1", color = color.red)
plot(R2, "R2", color = color.red)
plot(R3, "R3", color = color.red)

plot(S1, color = color.green)
plot(S2, color = color.green)
plot(S3, color = color.green)

PVlbl = label.new(bar_index, pivot, "PV", color = color.white)
R1lbl = label.new(bar_index, R1, "R1", color = color.red)
R2lbl = label.new(bar_index, R2, "R2", color = color.red)
R3lbl = label.new(bar_index, R3, "R3", color = color.red)

S1lbl = label.new(bar_index, S1, "S1", color = color.green)
S2lbl = label.new(bar_index, S2, "S2", color = color.green)
S3lbl = label.new(bar_index, S3, "S3", color = color.green)

label.delete(PVlbl1)
label.delete(R1lbl1)
label.delete(R2lbl1)
label.delete(R3lbl1)
label.delete(S1lbl1)
label.delete(S2lbl1)
label.delete(S3lbl1)
```

60. FIBONACCI PIVOT POINT LEVELS

```c
//@version=5
indicator("Fibonacci Pivot Points", overlay = true)

prevClose = request.security(syminfo.tickerid, "D", close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevHigh = request.security(syminfo.tickerid, "D", high1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevLow = request.security(syminfo.tickerid, "D", low1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

pivot = (prevClose + prevHigh + prevLow) / 3

R1 = pivot + (0.382 * (prevHigh - prevLow))
R2 = pivot + (0.618 * (prevHigh - prevLow))
R3 = pivot + (1 * (prevHigh - prevLow))

S1 = pivot - (0.382 * (prevHigh - prevLow))
S2 = pivot - (0.618 * (prevHigh - prevLow))
S3 = pivot - (1 * (prevHigh - prevLow))

plot(pivot, "pivot", color.white)

plot(R1, "R1", color = color.red)
plot(R2, "R2", color = color.red)
plot(R3, "R3", color = color.red)

plot(S1, color = color.green)
plot(S2, color = color.green)
plot(S3, color = color.green)

PVlbl = label.new(bar_index, pivot, "PV", color = color.white)
R1lbl = label.new(bar_index, R1, "R1-0.382", color = color.red)
R2lbl = label.new(bar_index, R2, "R2-0.618", color = color.red)
R3lbl = label.new(bar_index, R3, "R3-1", color = color.red)

S1lbl = label.new(bar_index, S1, "S1-0.382", color = color.green)
S2lbl = label.new(bar_index, S2, "S2-0.618", color = color.green)
S3lbl = label.new(bar_index, S3, "S3-1", color = color.green)

label.delete(PVlbl1)
label.delete(R1lbl1)
label.delete(R2lbl1)
label.delete(R3lbl1)
label.delete(S1lbl1)
label.delete(S2lbl1)
label.delete(S3lbl1)
```

61. DONCHIAN CHANNEL

```sh
The Donchian Channels strategy is a market volatility indicator; if price movements are small indicating low volatility, the channel will be relatively narrow. However, in periods of high volatility where price fluctuates excessively, the channel will be relatively wide

Donchian Channels Formula, Calculations, and Uses

```

```c
//@version=5
indicator("Donchian Channel", overlay = true)

length = input.int(50, "Length", minval = 1)

lower = ta.lowest(length)
upper = ta.highest(length)

middle = math.avg(lower, upper)

plot(middle, "Middle", color.orange)
pLower = plot(lower, "Lower", color.aqua)
pUpper = plot(upper, "Upper", color.aqua)

fill(pLower, pUpper, color = color.new(color.aqua, 90))
```

62. MULTI TIMEFRAME DONCHIAN CHANNEL

```c
//@version=5
indicator("Multi Timeframe Donchian Channel", overlay = true)

Htf = input.timeframe("D", "Select Timeframe")
length = input.int(50, "Length", minval = 1)

lower = ta.lowest(length)
upper = ta.highest(length)

lowerHtf = request.security(syminfo.tickerid, Htf, lower1, barmerge.gaps_on, barmerge.lookahead_on)
upperHtf = request.security(syminfo.tickerid, Htf, upper1, barmerge.gaps_on, barmerge.lookahead_on)

middleHtf = math.avg(lowerHtf, upperHtf)

plot(middleHtf, "Middle", color.orange)
pLower = plot(lowerHtf, "Lower", color.aqua)
pUpper = plot(upperHtf, "Upper", color.aqua)

fill(pLower, pUpper, color = color.new(color.aqua, 90))
```

63. MULTI TIMEFRAME DONCHIAN CHANNEL Strategy(asd)

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

64. CPR LEVEL

```c
//@version=5
indicator("Central Pivote Range", "CPR", overlay = true)

htf = input.timeframe(defval = "D", title = "Timeframe")

prevClose = request.security(syminfo.tickerid, htf, close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevHigh = request.security(syminfo.tickerid, htf, high1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevLow = request.security(syminfo.tickerid, htf, low1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

pivot = (prevClose + prevHigh + prevLow) / 3

btmCPR = (prevHigh + prevLow) / 2
topCPR = (pivot - btmCPR) + pivot

plot(pivot, "pivot", color.white)
plot(topCPR, "topCPR", color.lime)
plot(btmCPR, "btmCPR", color.lime)

pivlbl = label.new(bar_index, pivot, "Pivot", color = color.white)
toplbl = label.new(bar_index, topCPR, "Top CPR", color = color.red)
btmlbl = label.new(bar_index, btmCPR, "Bottoml CPR", color = color.red)

label.delete(pivlbl1)
label.delete(toplbl1)
label.delete(btmlbl1)
```

65. NEXT DAY'S CPR LEVELS

```c
//@version=5
indicator("Next Day CPR", "CPR", overlay = true)

htf = input.timeframe(defval = "D", title = "Timeframe")

prevClose = request.security(syminfo.tickerid, htf, close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevHigh = request.security(syminfo.tickerid, htf, high1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevLow = request.security(syminfo.tickerid, htf, low1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

pivot = (prevClose + prevHigh + prevLow) / 3

btmCPR = (prevHigh + prevLow) / 2
topCPR = (pivot - btmCPR) + pivot

if barstate.islast
line.new(bar_index, pivot, bar_index + 1, pivot, extend = extend.right, color = color.white)
line.new(bar_index, topCPR, bar_index + 1, topCPR, extend = extend.right, color = color.lime)
line.new(bar_index, btmCPR, bar_index + 1, btmCPR, extend = extend.right, color = color.lime)

pivlbl = label.new(bar_index, pivot, "Pivot", color = color.white)
toplbl = label.new(bar_index, topCPR, "Top CPR", color = color.red)
btmlbl = label.new(bar_index, btmCPR, "Bottoml CPR", color = color.red)

label.delete(pivlbl1)
label.delete(toplbl1)
label.delete(btmlbl1)
```

66. Live Alerts

```c
//@version=5
indicator("Live Alerts", overlay = true)

ma = ta.sma(close, 1)

if close > ma1
alert("Bullish alert", alert.freq_once_per_bar_close)

if close < ma1
alert("Bearish alert", alert.freq_once_per_bar_close)

plot(ma)
```

67. ALERT CONDITIONS

```c
//@version=5
indicator("Alert Condition", overlay = true)

ma = ta.sma(close, 1)
plot(ma)

bullishCondition = close > ma1
bearishCondition = close < ma1

alertcondition(bullishCondition, "Alert on Green Bar", message = "Green Bar!")
alertcondition(bearishCondition, "Alert on Red Bar", message = "Red Bar!")
```

68. KELTNER CHANNEL

```c
//@version=5
indicator("Keltner Channel", "KC", true)

length = input.int(20, "Length")
multi = input.int(2, "multiplier")
atrLength = input.int(10, "Atr Length")

middleBand = ta.ema(close, length = length)

rangeEma = ta.atr(atrLength)

upperBand = middleBand + rangeEma * multi
lowerBand = middleBand - rangeEma * multi

plot(middleBand, color = color.white)
plot(upperBand, color = color.orange)
plot(lowerBand, color = color.lime)
```

69. MULTI TIMEFRAME KELTNER CHANNEL

```c
//@version=5
indicator("Multi TimeFrame Keltner Channel", "MultiKC", true)

length = input.int(20, "Length")
multi = input.int(2, "multiplier")
atrLength = input.int(10, "Atr Length")
htf = input.timeframe(defval = "D", title = "Time Frame")

middleBand = ta.ema(close, length = length)

middleHtf = request.security(syminfo.tickerid, htf, middleBand1,
gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

rangeEma = ta.atr(atrLength)

rangeEmaHtf = request.security(syminfo.tickerid, htf, rangeEma1,
gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

upperBand = middleHtf + rangeEmaHtf * multi
lowerBand = middleHtf - rangeEmaHtf * multi

plot(middleHtf, color = color.white)
plot(upperBand, color = color.orange)
plot(lowerBand, color = color.lime)
```

70. RUN AN INDICATOR ON A PARTICULAR STOCK SCRIP ONLY

```c
//@version=5
indicator("Script Validation", overlay = true)

isScriptValid = syminfo.ticker == "TSLA" or syminfo.ticker == "AAPL"
plot(isScriptValid ? close : na)
```

71. RUN AN INDICATOR ON A PARTICULAR TIMEFRAME ONLY

```c
//@version=5
indicator("Timeframe Validation", overlay = true)

isTimeframeValid = timeframe.period == "15"
plot(isTimeframeValid ? close : na)
```

72. DRAW A VERTICAL LINE

```c
//@version=5
indicator("Verttical Line", overlay = true)

//if barstate.islast
myLine = line.new(bar_index, open, bar_index, close, extend = extend.both, color = color.green)
line.delete(myLine1)

myLbl = label.new(bar_index, close, text = str.tostring(high), style = label.style_label_lower_left, color = color.yellow, textcolor = color.blue)
label.delete(myLbl1)
```

73. DRAW A HORIZONTAL LINE WITH CO-ORDINATE IN THE TEXT

```c
//@version=5
indicator("Horizontal Line With Co-ordinate", overlay = true)

val = 4400

hline(val, "Top line", color.green, hline.style_dashed, linewidth = 2)

var label myLbl = na
if barstate.islast
myLbl := label.new(bar_index + 5, val, text = str.tostring(val), style = label.style_none, color = color.orange, textcolor = color.white)
label.delete(myLbl1)
```

74. MOVING AVERAGE RIBBON

```c
//@version=5
indicator("Moving Average Ribbon", overlay = true)

myMA(length) =>
ema = ta.ema(close, length)
isUp = ema > ema1
isDn = ema < ema1

var color emaColor = color.white
emaColor := (isUp or (isUp and isUp1)) ? color.green : (isDn or (isDn and isDn1)) ? color.red : emaColor1

ema, emaColor

var lineWidth = 1

ema10, emaColor10 = myMA(10)
ema20, emaColor20 = myMA(20)
ema30, emaColor30 = myMA(30)
ema40, emaColor40 = myMA(40)
ema50, emaColor50 = myMA(50)
ema60, emaColor60 = myMA(60)
ema70, emaColor70 = myMA(70)
ema80, emaColor80 = myMA(80)
ema90, emaColor90 = myMA(90)
ema100, emaColor100 = myMA(100)

plot(ema10, color = emaColor10, linewidth = lineWidth)
plot(ema20, color = emaColor20, linewidth = lineWidth)
plot(ema30, color = emaColor30, linewidth = lineWidth)
plot(ema40, color = emaColor40, linewidth = lineWidth)
plot(ema50, color = emaColor50, linewidth = lineWidth)
plot(ema60, color = emaColor60, linewidth = lineWidth)
plot(ema70, color = emaColor70, linewidth = lineWidth)
plot(ema80, color = emaColor80, linewidth = lineWidth)
plot(ema90, color = emaColor90, linewidth = lineWidth)
plot(ema100, color = emaColor100, linewidth = lineWidth)
```

75. MULTI TIMEFRAME MOVING AVERAGE RIBBON

```c
//@version=5
indicator("Multi Timeframe Moving Average Ribbon", overlay = true)

htf = input.timeframe(defval = "D", title = "Higher timeframe")

myMA(length) =>
ema = ta.ema(close, length)
emaHtf = request.security(syminfo.tickerid, htf, ema1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
isUp = emaHtf > emaHtf1
isDn = emaHtf < emaHtf1

var color emaColor = color.white
emaColor := (isUp or (isUp and isUp1)) ? color.green : (isDn or (isDn and isDn1)) ? color.red : emaColor1

emaHtf, emaColor

var lineWidth = 1

ema10, emaColor10 = myMA(10)
ema20, emaColor20 = myMA(20)
ema30, emaColor30 = myMA(30)
ema40, emaColor40 = myMA(40)
ema50, emaColor50 = myMA(50)
ema60, emaColor60 = myMA(60)
ema70, emaColor70 = myMA(70)
ema80, emaColor80 = myMA(80)
ema90, emaColor90 = myMA(90)
ema100, emaColor100 = myMA(100)

plot(ema10, color = emaColor10, linewidth = lineWidth)
plot(ema20, color = emaColor20, linewidth = lineWidth)
plot(ema30, color = emaColor30, linewidth = lineWidth)
plot(ema40, color = emaColor40, linewidth = lineWidth)
plot(ema50, color = emaColor50, linewidth = lineWidth)
plot(ema60, color = emaColor60, linewidth = lineWidth)
plot(ema70, color = emaColor70, linewidth = lineWidth)
plot(ema80, color = emaColor80, linewidth = lineWidth)
plot(ema90, color = emaColor90, linewidth = lineWidth)
plot(ema100, color = emaColor100, linewidth = lineWidth)
```

76. INDICATOR SCREENER

```c
//@version=5
indicator("indicator Screener", overlay = true)

length = input.int(defval = 200, title = "Length")
htf = input.timeframe(defval = "15", title = "Higher timeframe")

myScreener(stock) =>
_close = request.security(stock, htf, close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
ema = ta.ema(close, length)
emaHtf = request.security(syminfo.tickerid, htf, ema1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
isUp = _close > emaHtf ? "YES" : "NO"


var tbl = table.new(position = position.bottom_right, columns = 2, rows = 10, bgcolor = color.white, border_width = 1)

table.cell(tbl, 0, 0, "STOCK", text_color = color.white, bgcolor = color.orange)
table.cell(tbl, 0, 1, "TSLA", text_color = color.white, bgcolor = color.green)
table.cell(tbl, 0, 2, "AAPL", text_color = color.white, bgcolor = color.green)
table.cell(tbl, 0, 3, "MSFT", text_color = color.white, bgcolor = color.green)
table.cell(tbl, 0, 4, "GOOG", text_color = color.white, bgcolor = color.green)

table.cell(tbl, 1, 0, "STOCK above 200 EMA")
table.cell(tbl, 1, 1, str.tostring(myScreener("TSLA")))
table.cell(tbl, 1, 2, str.tostring(myScreener("AAPL")))
table.cell(tbl, 1, 3, str.tostring(myScreener("MSFT")))
table.cell(tbl, 1, 4, str.tostring(myScreener("GOOG")))
```

77. PLOT HORIZONTAL LINE FROM A CUSTOM POINT

```c
//@version=5
indicator("Draw a Horizontal Line From Certtain Bar", overlay = true)

ema = ta.ema(close, 200)

plot(ema, color = color.gray)

xEma = ta.cross(close, ema)

barIndexWhenCross = ta.valuewhen(xEma, bar_index, 0)
highValueWhenCross = ta.valuewhen(xEma, high, 0)
// timeWhenCross = ta.valuewhen(xEma, time, 0)

my_line = line.new(barIndexWhenCross, highValueWhenCross, barIndexWhenCross + 1, highValueWhenCross, color = color.green, extend = extend.right)
line.delete(my_line1)
```

78. PLOT VIX

```c
//@version=5
indicator("VIX")

vix = request.security("VIX", "D", close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

plot(vix, color = color.gray, style = plot.style_stepline)
```

79. Center of Gravity

```c
//@version=5
indicator("Center of Gravity")

cog = ta.cog(close, 14)

plot(cog, color = color.gray)
```

80. MULTI TIMEFRAME CENTER OF GRAVITY

```c
//@version=5
indicator("Center of Gravity")

htf = input.timeframe("D", "timeframe")
cog = ta.cog(close, 14)
coghtf = request.security(syminfo.tickerid, htf, cog1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
plot(coghtf, color = color.gray)
```

81. SHOW DIFFERENT STOCK'S CANDLES ON THE CURRENT CHART

```c
//@version=5
indicator("Show Different Stock's Candles")

stock_name = input.symbol("TSLA", "Choose Stock")
htf = input.timeframe("D", "timeframe")

stock_open = request.security(stock_name, htf, open, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
stock_high = request.security(stock_name, htf, high, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
stock_low = request.security(stock_name, htf, low, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
stock_close = request.security(stock_name, htf, close, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

candel_color = stock_close > stock_open ? color.green : stock_close < stock_open ? color.red : color.white

plotcandle(open = stock_open, high = stock_high, close = stock_close, low = stock_low, color = candel_color)
```

82. GET LOWER TIMEFRAME DATA

```c

//@version=5
indicator("Get Lower Timeframe Data", overlay = true)

htf = input.timeframe("D", "timeframe")

lowertf_open, lowertf_high, lowertf_low, lowertf_close = request.security_lower_tf(syminfo.tickerid, htf, open, high, low, close, true, ignore_invalid_timeframe = true)

// Plot lower timeframe data if available
lowertfCloseValue = na(lowertf_close0) ? na : array.get(lowertf_close, 0)
plot(lowertfCloseValue, color=color.red, title="Lower Timeframe Close")
```

```c
// Input for higher timeframe
htf = input.timeframe("D", "Higher Timeframe")

// Request lower timeframe data
lowertf_open, lowertf_high, lowertf_low, lowertf_close = request.security_lower_tf(syminfo.tickerid, htf, open, high, low, close, true, ignore_invalid_timeframe=true)

// Plot higher timeframe data
plot(close, color=color.blue, title="Higher Timeframe Close")

// Plot lower timeframe data if available
lowertfCloseValue = na(lowertf_close0) ? na : array.get(lowertf_close, 0)
plot(lowertfCloseValue, color=color.red, title="Lower Timeframe Close")
```

83. HIDE THE INDICATOR SETTINGS

```c
//@version=5
indicator("Hide indicator Settings", overlay = true)

plot(close, style = plot.style_stepline_diamond, editable = false)
```

84. FILL THE GAPS BETWEEN THE LINES USING FILL FUNCTION

```c
//@version=5
indicator("Fill Plots", overlay = true)
open_plot = plot(open, color = color.red, editable = false)
close_plot = plot(close, color = color.green, editable = false)
fill(open_plot, close_plot, color = color.new(color.blue, 80))
```

85. CALCULATE DAILY RANGE

```c
//@version=5
indicator("Dailly Range")

daily_high = request.security(syminfo.tickerid, "D", high1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
daily_low = request.security(syminfo.tickerid, "D", low1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

daily_range = daily_high - daily_low
plot(daily_range, "Daily Range", color.green, 5)
```

86. ALIGN INPUTS INLINE HORIZONTALLY

```c
// 网格思路
//@version=5
indicator("Horizontal Inline Inputs")

// value1 = input.int(10, "Value 1")
// value2 = input.int(20, "Value 2")
// value3 = input.int(30, "Value 3")

value1 = input.int(10, "Value 1", inline = "Value")
value2 = input.int(20, "Value 2", inline = "Value")
value3 = input.int(30, "Value 3", inline = "Value")

plot(value1)
plot(value2)
plot(value3)
```

87. GET THE STRATEGY SIGNALS EARLY AND ON THE EXACT BAR

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

88. ARNAUD LEGOUX MOVING AVERAGE

```c
//@version=5
indicator("Arnaud Legoux Moving Average", overlay = true)

length = input.int(9, "Length")
offset = input.float(0.85, "Offset")
smoothness = input.int(6, "smoothness")

alma = ta.alma(close, length, offset, smoothness)
plot(alma)
```

89. MULTI TIMEFRAME ARNAUD LEGOUX MOVING AVERAGE

```c
//@version=5
indicator("Multi Timeframe Arnaud Legoux Moving Average", overlay = true)

length = input.int(9, "Length")
offset = input.float(0.85, "Offset")
smoothness = input.int(6, "smoothness")
htf = input.timeframe("D", "timeframe")

alma = ta.alma(close, length, offset, smoothness)
almahtf = request.security(syminfo.tickerid, htf, alma1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

plot(almahtf)
```

90. GROUP USER INPUTS & APPLY HEADER LABEL

```c
//@version=5
indicator("Group Input Headers")

ema_length = input.int(50, "EMA Length", group = "EMA Inputs")
ema_source = input.source(close, "EMA source", group = "EMA Inputs")

rsi_length = input.int(14, "RSI Length", group = "RSI Inputs", inline = 'a')
rsi_source = input.source(close, "RSI Length", group = "RSI Inputs", inline = 'a')

ema50 = ta.ema(ema_source, ema_length)
rsi = ta.rsi(rsi_source, rsi_length)

plot(ema50, "ema", color = color.purple)
plot(rsi, 'rsi', color.maroon)
```

91. HOW TO CREATE AND USE A LIBRARY

```c

import weip2008/MALibrary/1

//@version=5
library("MALibrary", true)

export showMovingAverage(int length) =>
	ema = ta.ema(close, length)
	ema // try return clearly

```c

//@version=5
indicator("Import Lib", overlay = true)

import weip2008/MALibrary/1 as malib

plot(malib.showMovingAverage(20), "MA20", color = color.green)
plot(malib.showMovingAverage(50), "MA50", color = color.yellow)
plot(malib.showMovingAverage(200), "MA200",color = color.red)
```

92. TWO SUPER-TRENDS STRATEGY

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

93. SWING HIGH-LOW

```c
// there is no perfict logic to find swing high and low

//@version=5
indicator("Swing hign low", overlay = true)

swing_high = high < high1 and high1 > high2
swing_low = low > low1 and low1 < low2

plotshape(swing_high, "swing_high", style = shape.triangledown, color = color.red, location = location.abovebar, offset = -1)
plotshape(swing_low, "swing_low", style = shape.triangleup, color = color.green, location = location.belowbar, offset = -1)
```

94. DMI - DIRECTIONAL MOMENTUM INDEX

```c
//@version=5
indicator("Directional Moving Index", "DMI")

length = input.int(14, "DI length", minval = 1)
smoothing = input.int(14, "ADX Smoothing", minval = 1, maxval = 50)

di_plus, di_minus, adx = ta.dmi(length, smoothing)

plot(adx, "ADX", color.white)
plot(di_plus, "+DI", color.green)
plot(di_minus, "-DI", color.red)
```

95. MULTI-TIMEFRAME DMI - DIRECTIONAL MOMENTUM INDEX

```c
//@version=5
indicator("Directional Moving Index", "DMI")

length = input.int(14, "DI length", minval = 1)
smoothing = input.int(14, "ADX Smoothing", minval = 1, maxval = 50)
htf = input.timeframe("D", "Timeframe")

di_plus, di_minus, adx = ta.dmi(length, smoothing)

htf_di_plus = request.security(syminfo.tickerid, htf, di_plus1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
htf_di_minus = request.security(syminfo.tickerid, htf, di_minus1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
htf_adx = request.security(syminfo.tickerid, htf, adx1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)


plot(htf_adx, "ADX", color.white)
plot(htf_di_plus, "+DI", color.green)
plot(htf_di_minus, "-DI", color.red)
```

96. HOW TO GET THE VOLUME PROGRAMMATICALLY

```c
//@version=5
indicator("Voluume", format = format.volume)
var volume_color = color.green
volume_color := close > open ? color.green : close < open ? color.red : volume_color1
// volume_color = htf_close > htf_open ? color.green : color.red
plot(volume, style = plot.style_columns, color = volume_color)
```

97.MULTI-TIMEFRAME VOLUME

```c
//@version=5
indicator("Multi Timeframe Voluume", format = format.volume)

htf = input.timeframe("W", "timeframe")

htf_close = request.security(syminfo.tickerid, htf, close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
htf_open = request.security(syminfo.tickerid, htf, open1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
htf_volume = request.security(syminfo.tickerid, htf, volume1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

var volume_color = color.green
volume_color := htf_close > htf_open ? color.green : htf_close < htf_open ? color.red : volume_color1
plot(htf_volume, style = plot.style_columns, color = volume_color)
```

98. CAMARILLA PIVOT POINTS

```c
//@version=5
indicator("Camerilla Pivot Points", overlay = true)

htf = input.timeframe("D", "timeframe")

prevClose = request.security(syminfo.tickerid, htf, close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevHigh = request.security(syminfo.tickerid, htf, high1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevLow = request.security(syminfo.tickerid, htf, low1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

pivot = (prevClose + prevHigh + prevLow) / 3
pivot_range = prevHigh - prevLow

R1 = prevClose + pivot_range * 1.1 / 12.0
R2 = prevClose + pivot_range * 1.1 / 6.0
R3 = prevClose + pivot_range * 1.1 / 4.0
R4 = prevClose + pivot_range * 1.1 / 2.0


S1 = prevClose - pivot_range * 1.1 / 12.0
S2 = prevClose - pivot_range * 1.1 / 6.0
S3 = prevClose - pivot_range * 1.1 / 4.0
S4 = prevClose - pivot_range * 1.1 / 2.0

plot(pivot, "pivot", color.white)

plot(R1, "R1", color = color.red)
plot(R2, "R2", color = color.red)
plot(R3, "R3", color = color.red)
plot(R4, "R4", color = color.red)

plot(S1, "S1", color = color.green)
plot(S2, "S2", color = color.green)
plot(S3, "S3", color = color.green)
plot(S4, "S4", color = color.green)

PVlbl = label.new(bar_index, pivot, "PV", color = color.white)
R1lbl = label.new(bar_index, R1, "R1", color = color.red)
R2lbl = label.new(bar_index, R2, "R2", color = color.red)
R3lbl = label.new(bar_index, R3, "R3", color = color.red)
R4lbl = label.new(bar_index, R4, "R4", color = color.red)

S1lbl = label.new(bar_index, S1, "S1", color = color.green)
S2lbl = label.new(bar_index, S2, "S2", color = color.green)
S3lbl = label.new(bar_index, S3, "S3", color = color.green)
S4lbl = label.new(bar_index, S4, "S4", color = color.green)

label.delete(PVlbl1)
label.delete(R1lbl1)
label.delete(R2lbl1)
label.delete(R3lbl1)
label.delete(R4lbl1)
label.delete(S1lbl1)
label.delete(S2lbl1)
label.delete(S3lbl1)
label.delete(S4lbl1)
```

99. NEXT DAY'S CAMARILLA PIVOT POINTS

```c

//@version=5
indicator("Next Day Camerilla Pivot Points", overlay = true)

htf = input.timeframe("D", "timeframe")

prevClose = request.security(syminfo.tickerid, htf, close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevHigh = request.security(syminfo.tickerid, htf, high1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
prevLow = request.security(syminfo.tickerid, htf, low1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

PV = (prevClose + prevHigh + prevLow) / 3
pivot_range = prevHigh - prevLow

R1 = prevClose + pivot_range * 1.1 / 12.0
R2 = prevClose + pivot_range * 1.1 / 6.0
R3 = prevClose + pivot_range * 1.1 / 4.0

S1 = prevClose - pivot_range * 1.1 / 12.0
S2 = prevClose - pivot_range * 1.1 / 6.0
S3 = prevClose - pivot_range * 1.1 / 4.0

if barstate.islast
    line.new(bar_index, PV, bar_index + 1, PV, extend = extend.right, color = color.white)
    line.new(bar_index, R1, bar_index + 1, R1, extend = extend.right, color = color.red)
    line.new(bar_index, R2, bar_index + 1, R2, extend = extend.right, color = color.red)
    line.new(bar_index, R3, bar_index + 1, R3, extend = extend.right, color = color.red)
    line.new(bar_index, S1, bar_index + 1, S1, extend = extend.right, color = color.lime)
    line.new(bar_index, S2, bar_index + 1, S2, extend = extend.right, color = color.lime)
    line.new(bar_index, S3, bar_index + 1, S3, extend = extend.right, color = color.lime)

PVlbl = label.new(bar_index, PV, "PV", color = color.white)
R1lbl = label.new(bar_index, R1, "R1", color = color.red)
R2lbl = label.new(bar_index, R2, "R2", color = color.red)
R3lbl = label.new(bar_index, R3, "R3", color = color.red)

S1lbl = label.new(bar_index, S1, "S1", color = color.green)
S2lbl = label.new(bar_index, S2, "S2", color = color.green)
S3lbl = label.new(bar_index, S3, "S3", color = color.green)

label.delete(PVlbl1)
label.delete(R1lbl1)
label.delete(R2lbl1)
label.delete(R3lbl1)
label.delete(S1lbl1)
label.delete(S2lbl1)
label.delete(S3lbl1)
```

100. FIND TODAY'S PRICE BAR ONLY

```c
//@version=5
indicator("Find Today", overlay = true)

// isToday = false
// if year(timenow) == year(time) and month(timenow) == month(time) and dayofmonth (timenow) == dayofmonth(time)
//     isToday := true

isToday = year(timenow) == year(time) and month(timenow) == month(time) and weekofyear(timenow) == weekofyear(time)

plot_value = isToday ? close : na
plotshape(plot_value, "isToday", shape.arrowup, location.belowbar, color.green)

bgcolor(isToday ? color.new(color.gray, 95) : na)
```

101. SWING HIGH-LOW

```c
//@version=5
indicator("Swing hign low", overlay = true, max_lines_count = 100)

length = input.int(defval = 20, title = "length")

swing_high = ta.highest(length)
high_when_swing_high = ta.valuewhen(swing_high > swing_high1, high, 0)
low_when_swing_high = ta.valuewhen(swing_high > swing_high1, low, 0)
bar_index_swing_high = ta.valuewhen(swing_high > swing_high1, bar_index, 0)
is_swing_high_found = close < low_when_swing_high

swing_high_bar_diff = is_swing_high_found ? -1 * (bar_index - bar_index_swing_high) : na
line.new(bar_index + swing_high_bar_diff -1, high_when_swing_high, bar_index + swing_high_bar_diff + 1, high_when_swing_high, color = color.green)

swing_low = ta.lowest(length)
high_when_swing_low = ta.valuewhen(swing_low < swing_low1, high, 0)
low_when_swing_low = ta.valuewhen(swing_low < swing_low1, low, 0)
bar_index_swing_low = ta.valuewhen(swing_low < swing_low1, bar_index, 0)
is_swing_low_found = close > high_when_swing_low
swing_low_bar_diff = is_swing_low_found ? -1 * (bar_index - bar_index_swing_low) : na

line.new(bar_index + swing_low_bar_diff - 1, low_when_swing_low, bar_index + swing_low_bar_diff + 1, low_when_swing_low, color = color.red)

// plotshape(swing_high, "swing_high", style = shape.triangledown, color = color.red, location = location.abovebar, offset = -1)
// plotshape(swing_low, "swing_low", style = shape.triangleup, color = color.green, location = location.belowbar, offset = -1)
```

102. SUPPORT AND RESISTANCE LEVELS

```c
//@version=5
indicator("Supports and Resistances", overlay = true, max_boxes_count = 500)

length = input.int(defval = 20, title = "length")

swing_high = ta.highest(length)

high_when_swing_high = ta.valuewhen(swing_high > swing_high1, high, 0)
low_when_swing_high = ta.valuewhen(swing_high > swing_high1, low, 0)
close_when_swing_high = ta.valuewhen(swing_high > swing_high1, close, 0)
bar_index_swing_high = ta.valuewhen(swing_high > swing_high1, bar_index, 0)
is_swing_high_found = close < low_when_swing_high

swing_high_bar_diff = is_swing_high_found ? -1 * (bar_index - bar_index_swing_high) : na
box.new(bar_index + swing_high_bar_diff -1, high_when_swing_high, bar_index + swing_high_bar_diff + 10,
     close_when_swing_high, color.green, bgcolor = color.new(color.green, 80))

// line.new(bar_index + swing_high_bar_diff -1, high_when_swing_high, bar_index + swing_high_bar_diff + 1, high_when_swing_high, color = color.green)

swing_low = ta.lowest(length)
high_when_swing_low = ta.valuewhen(swing_low < swing_low1, high, 0)
low_when_swing_low = ta.valuewhen(swing_low < swing_low1, low, 0)
close_when_swing_low = ta.valuewhen(swing_low < swing_low1, close, 0)
bar_index_swing_low = ta.valuewhen(swing_low < swing_low1, bar_index, 0)
is_swing_low_found = close > high_when_swing_low
swing_low_bar_diff = is_swing_low_found ? -1 * (bar_index - bar_index_swing_low) : na

box.new(bar_index + swing_low_bar_diff -1, low_when_swing_low , bar_index + swing_low_bar_diff + 10,
     close_when_swing_low, color.red, bgcolor = color.new(color.red, 80))

// line.new(bar_index + swing_low_bar_diff - 1, low_when_swing_low, bar_index + swing_low_bar_diff + 1, low_when_swing_low, color = color.red)
```

103. HOW TO FIND AN INSIDE BAR

```c

//@version=5
indicator("Inside Bar", overlay = true)

isInsideBar = high < high1 and low > low1
insideBarColor = isInsideBar ? color.white : na
barcolor(insideBarColor)

plotshape(series = isInsideBar, title = "insde bar", style = shape.arrowup, color = color.white, location = location.belowbar)
```

104. FIND A MULTI-TIMEFRAME INSIDE BAR

```c
//@version=5
indicator("Inside Bar", overlay = true)

htf = input.timeframe("W", "timeframe")

htf_high = request.security(syminfo.tickerid, htf, high1, barmerge.gaps_off, barmerge.lookahead_on)
htf_low = request.security(syminfo.tickerid, htf, low1, barmerge.gaps_off, barmerge.lookahead_on)

isInsideBar = htf_high < htf_high1 and htf_low > htf_low1
insideBarColor = isInsideBar ? color.white : na
barcolor(insideBarColor)

plotshape(series = isInsideBar, title = "insde bar", style = shape.arrowup, color = color.white, location = location.belowbar)
```

105. ALL-IN-ONE INDICATOR

```c
If anyone wants to try the ALL-IN-ONE indicator, please send me your trading view username.

Contact details:

Email: who.it.wala@proton.me

Instagram ID: woh.it.wala

Twitter ID : WOH_IT_WALA

Google Chat: woh.it.wala@gmail.com

Discord ID: IT Wala#3998

```

106. ICHIMOKU CLOUD

```c

//@version=5
indicator("Multi Timeframe Ichimoku Cloud", overlay = true)

htf = input.timeframe("D", "timeframe")
conversion_line_length = input.int(9, minval = 1, title = "Conversion Line Length")
base_line_length = input.int(26, minval = 1, title = "Base Line Length")
leading_span_length = input.int(52, minval = 1, title = "Leading Span A Length")
laggding_span_length = input.int(26, minval = 1, title = "Lagging Span B Length")

calculateAverage(value) => math.avg(ta.lowest(value), ta.highest(value))

conversion_line = calculateAverage(conversion_line_length)
base_line = calculateAverage(base_line_length)
leading_line = math.avg(conversion_line, base_line)
lagging_line = calculateAverage(leading_span_length)

plot(conversion_line, color = color.blue, title = "Coonversion Line")
plot(base_line, color = color.orange, title = "Base Line")
plot(close, offset = -laggding_span_length + 1, color = color.lime, title = "Lagging Span")

p1 = plot(leading_line, offset = laggding_span_length - 1, color = color.green, title = "Leading Span A")
p2 = plot(lagging_line, offset = laggding_span_length - 1, color = color.red, title = "Lagging Span B")

fill(p1, p2, color = leading_line > lagging_line ? color.rgb(67,160,71,90) : color.rgb(244,67,54,90))
```

107. MULTI-TIMEFRAME ICHIMOKU CLOUD

```c
//@version=5
indicator("Multi Timeframe Ichimoku Cloud", overlay = true)

htf = input.timeframe("D", "timeframe")
conversion_line_length = input.int(9, minval = 1, title = "Conversion Line Length")
base_line_length = input.int(26, minval = 1, title = "Base Line Length")
leading_span_length = input.int(52, minval = 1, title = "Leading Span A Length")
laggding_span_length = input.int(26, minval = 1, title = "Lagging Span B Length")

calculateAverage(value) => math.avg(ta.lowest(value), ta.highest(value))

conversion_line = calculateAverage(conversion_line_length)
base_line = calculateAverage(base_line_length)
leading_line = math.avg(conversion_line, base_line)
lagging_line = calculateAverage(leading_span_length)

htf_conversion_line = request.security(syminfo.tickerid, htf, conversion_line1, barmerge.gaps_off, barmerge.lookahead_on)
htf_base_line = request.security(syminfo.tickerid, htf, base_line1, barmerge.gaps_off, barmerge.lookahead_on)
htf_leading_line = request.security(syminfo.tickerid, htf, leading_line1, barmerge.gaps_off, barmerge.lookahead_on)
htf_lagging_line = request.security(syminfo.tickerid, htf, lagging_line1, barmerge.gaps_off, barmerge.lookahead_on)
htf_close = request.security(syminfo.tickerid, htf, close1, barmerge.gaps_off, barmerge.lookahead_on)

plot(htf_conversion_line, color = color.blue, title = "Coonversion Line")
plot(htf_base_line, color = color.orange, title = "Base Line")
plot(htf_close, offset = -laggding_span_length + 1, color = color.lime, title = "Lagging Span")

p1 = plot(htf_leading_line, offset = laggding_span_length - 1, color = color.green, title = "Leading Span A")
p2 = plot(htf_lagging_line, offset = laggding_span_length - 1, color = color.red, title = "Lagging Span B")

fill(p1, p2, color = htf_leading_line > htf_lagging_line ? color.rgb(67,160,71,90) : color.rgb(244,67,54,90))
```

108. INTRADAY INTENSITY INDEX

```c
//@version=5
indicator("Intraday Intensity Index")
plot(ta.iii, color = ta.iii > 0 ? color.green : color.red)
hline(0, "Zero Line", color.white, hline.style_dotted, 1)
```

109. MULTI TIMEFRAME INTRADAY INTENSITY INDEX

```c
//@version=5
indicator("Multi Timeframe Intraday Intensity Index")

htf = input.timeframe("30", "timeframe")

iii = ta.iii
htf_iii = request.security(syminfo.tickerid, htf, iii1, barmerge.gaps_off, barmerge.lookahead_on)

plot(htf_iii, color = ta.iii > 0 ? color.green : color.red)
hline(0, "Zero Line", color.yellow, hline.style_dotted, 1)
```

110. ACCUMULATION DISTRIBUTION INDEX

```c
//@version=5
indicator("Accumulation Distribution Index", format = format.volume)
adi = ta.accdist

plot(adi, "adi", (adi > adi1) ? color.green : color.red)
```

111. MULTI TIMEFRAME ACCUMULATION DISTRIBUTION INDEX

```c
//@version=5
indicator("Multi Timeframe Accumulation Distribution Index", format = format.volume)

htf = input.timeframe("W", "timeframe")
adi = ta.accdist

htf_adi = request.security(syminfo.tickerid, htf, adi1, barmerge.gaps_off, barmerge.lookahead_on)

plot(htf_adi, "adi", (adi > adi1) ? color.green : color.red)
```

112. WOODIE PIVOT POINT LEVELS

```c
//@version=5
indicator("WOODIE PIVOT POINT LEVELS", overlay = true)

htf = input.timeframe("D", "timeframe")

todaysOpen = request.security(syminfo.tickerid, htf, open, barmerge.gaps_off, barmerge.lookahead_on)
preHigh = request.security(syminfo.tickerid, htf, high1, barmerge.gaps_off, barmerge.lookahead_on)
preLow = request.security(syminfo.tickerid, htf, low1, barmerge.gaps_off, barmerge.lookahead_on)

pivot = (preHigh + preLow + todaysOpen * 2)/4
pivot_range = preHigh - preLow

R1 = pivot * 2 - preLow
R2 = pivot + 1 * pivot_range
S1 = pivot * 2 - preHigh
S2 = pivot - 1 * pivot_range

plot(pivot, "pivot", color = color.white)
plot(R1, "R1", color = color.red)
plot(R2, "R2", color = color.red)
plot(S1, "S1", color = color.green)
plot(S2, "S2", color = color.green)
```

113. BOLLINGER BAND WIDTH

```c
//@version=5
indicator("BOLLINGER BAND WIDTH")

bb_length = input.int(50, "Bollinger Band Length")
bb_multiplier = input.int(2, "Bollinger Band Multiplier")

bb_width = ta.bbw(close, bb_length, bb_multiplier)
plot(bb_width)
```

114. HOW TO FIND IF A SOURCE IS FALLING OR NOT

```c
//@version=5
indicator("Falling Source")

is_falling = ta.falling(close, input.int(3, "length"))
plot(close, "falling", is_falling ? color.red : color.green)

// when length 3 then 守K
```

115. HOW TO FIND IF A SOURCE IS RISING OR NOT

```c
//@version=5
indicator("Rising Source")

isRising = ta.rising(close, input.int(10, "length"))
plot(close, "rising", isRising ? color.green : color.red)
```

116. DO NOT USE ANY HEIKIN ASHI STRATEGY || STOP IMMEDIATELY

117. MULTI TIMEFRAME MACD HISTOGRAM

```c
//@version=5
indicator("MULTI TIMEFRAME MACD HISTOGRAM", "MTF MACD")

htf = input.timeframe("D", "timeframe")

// Getting inputs
fast_length = input(title="Fast Length", defval=12)
slow_length = input(title="Slow Length", defval=26)
signal_length = input.int(title="Signal Smoothing",  minval = 1, maxval = 50, defval = 9)

// Calculating
fast_ma = ta.ema(close, fast_length)
slow_ma = ta.ema(close, slow_length)

macd = fast_ma - slow_ma
signal = ta.ema(macd, signal_length)

htfMACD = request.security(syminfo.tickerid, htf, macd1, barmerge.gaps_off, barmerge.lookahead_on)
htfSignal = request.security(syminfo.tickerid, htf, signal1, barmerge.gaps_off, barmerge.lookahead_on)

hist = htfMACD - htfSignal
// Plot colors
col_macd = input(#2962FF, "MACD Line", group="Color Settings", inline="MACD")
col_signal = input(#FF6D00, "Signal Line", group="Color Settings", inline="Signal")
col_grow_above = input(#26A69A, "Above Grow", group="Histogram", inline="Above")
col_fall_above = input(#B2DFDB, "Fall", group="Histogram", inline="Above")
col_grow_below = input(#FFCDD2, "Below Grow", group="Histogram", inline="Below")
col_fall_below = input(#FF5252, "Fall", group="Histogram", inline="Below")

hline(0, "Zero Line", color=color.new(#787B86, 50))
plot(hist, title="Histogram", style=plot.style_columns, color=(hist>=0 ? (hist1 < hist ? col_grow_above : col_fall_above) : (hist1 < hist ? col_grow_below : col_fall_below)))
plot(htfMACD, title="MACD", color=col_macd)
plot(htfSignal, title="Signal", color=col_signal)
```

118. HOW TO FIND MARKET HOURS || REGULAR, PRE-MARKET, POST-MARKET

```c
// not work
indicator("Market Sessions", overlay = true)

// mktColor = if session.ismarket
//     color.new(color.gray, 80)
// else
//     if session.ispremarket
//         color.new(color.aqua, 30)
//     else
//         if session.ispostmarket
//             color.new(color.red, 30)
//         else
//             na

is_market_hours = session.ismarket ? true : false

mktColor = is_market_hours ? color.green : color.red

bgcolor(mktColor)

```

119. AROON

What Is the Aroon Oscillator?

```
What Is the Aroon Oscillator?
The Aroon Oscillator is a trend-following indicator that uses aspects of the Aroon Indicator (Aroon Up and Aroon Down) to gauge the strength of a current trend and the likelihood that it will continue.
```

```c
//@version=5
indicator("Aroon", format = format.percent, precision = 2)

length = input.int(14, minval = 1)

upper = 100 * (ta.highestbars(high, length) + length) / length
lower = 100 * (ta.lowestbars(low, length) + length) / length

plot(upper, "Aroon Up", color.green)
plot(lower, "Aroon Down", color.red)
```

120. MULTI TIMEFRAME AROON

```c
//@version=5
indicator("Multi Timeframe Aroon", format = format.percent, precision = 2)

length = input.int(14, minval = 1)
htf = input.timeframe("D", "timeframe")

upper = 100 * (ta.highestbars(high, length) + length) / length
lower = 100 * (ta.lowestbars(low, length) + length) / length

htf_upper = request.security(syminfo.tickerid, htf, upper1, barmerge.gaps_off, barmerge.lookahead_on)
htf_lower = request.security(syminfo.tickerid, htf, lower1, barmerge.gaps_off, barmerge.lookahead_on)

plot(htf_upper, "Aroon Up", color.green)
plot(htf_lower, "Aroon Down", color.red)
```

```
The Difference Between the Aroon Indicator and the Directional Movement Index (DMI)
The Aroon indicator is similar to the Directional Movement Index (DMI) developed by Welles Wilder. It too uses up and down lines to show the direction of a trend. The main difference is that the Aroon indicator formulas are primarily focused on the amount of time between highs and lows. The DMI measures the price difference between current highs/lows and prior highs/lows. Therefore, the main factor in the DMI is price, and not time.
```

121. FEWER NUMBER OF LABELS PROBLEM

```c
//@version=5
indicator("Fewer Labels Issue", overlay = true, max_labels_count = 5) //500 defval 50
label.new(x = bar_index, y = high, text = str.tostring(high), style = label.style_label_down, textcolor = color.white)
```

122. TEXT AREA

```c
//@version=5
indicator("TEXT AREA", overlay = true)
i_txt = input.text_area("This indicator takes the user input for the length of the exponential moving average, and then draws the moving average on the chart", title = "Message")
i_length = input.int(100, "EMA Length")
ema = ta.ema(close, i_length)
plot(ema, color = color.lime)
```

123. HOW TO CREATE A MATRIX

```c
//@version=5
indicator("MATRIX", overlay = true)

// Create a 2X3 (2 rows X 3 columns) "int" matrix with values zero.
var m = matrix.new<int>(2,3,0)

matrix.set(m, 0, 0, 1)
matrix.set(m, 0, 1, 2)
matrix.set(m, 0, 2, 3)

matrix.set(m, 1, 0, 4)
matrix.set(m, 1, 1, 5)
matrix.set(m, 1, 2, 6)

if barstate.islast
    label.new(bar_index, high, str.tostring(m), textcolor = color.white)

// lbl = label.new(bar_index, high)
// if barstate.islast
//     lbl := label.new(bar_index, high, str.tostring(m), textcolor = color.white)
// label.delete(lbl1)

```

124. AWESOME OSCILLATOR

```c
//@version=5
indicator("AWESOME OSCILLATOR")

osc = ta.sma(hl2, 5) - ta.sma(hl2, 34)
diff = osc - osc1
osc_color = diff<=0 ? color.red : color.green
plot(osc, "oscillator", osc_color, style = plot.style_columns) // style_histgram
```

125. MULTI TIMEFRAME AWESOME OSCILLATOR

```c
//@version=5
indicator("Multi Titmeframe AWESOME OSCILLATOR")

htf = input.timeframe("D", "timeframe")

osc = ta.sma(hl2, 5) - ta.sma(hl2, 34)

htf_osc = request.security(syminfo.tickerid, htf, osc1, barmerge.gaps_off, barmerge.lookahead_on)
diff = htf_osc - htf_osc1
osc_color = diff<=0 ? color.red : color.green
plot(htf_osc, "oscillator", osc_color, style = plot.style_columns)
```

126. BALANCE OF POWER

```c
//@version=5
indicator("BALANCE OF POWER") //, format = format.price, precision = 2

close_open = close - open
high_low = high - low

balanceOfPower = close_open / high_low

plot(balanceOfPower, "Balance of Power", color.green)
hline(0, "zero", color.gray, linestyle = hline.style_dashed)

// > 0 bullish trend and < 0 means bearish trend
```

127. MULTI TIME FRAME BALANCE OF POWER

```c
//@version=5
indicator("MULTI TIME FRAME BALANCE OF POWER")

htf = input.timeframe("D", "timeframe")

close_open = close - open
high_low = high - low

balanceOfPower = close_open / high_low

htf_balanceOfPower = request.security(syminfo.tickerid, htf, balanceOfPower1, barmerge.gaps_off, barmerge.lookahead_on)

plot(htf_balanceOfPower, "Balance of Power", color.green)
hline(0, "zero", color.gray, linestyle = hline.style_dashed)

// > 0 bullish trend and < 0 means bearish trend
```

128. THROW RUNTIME ERROR VIA CODE

```c
//@version=5
indicator("THROW RUNTIME ERROR", overlay = true)

ema = ta.ema(close, 50)
plot(ema, color= color.green)

isError = close < ema and barstate.islast

if isError
    runtime.error("Error!")
```

129. UP-DOWN VOLUME

```c
//@version=5
indicator("UP-DOWN VOLUME", format = format.volume)

upVolume = close > close1 ? volume : na
downVolume = close < close1 ? -1*volume : na

plot(upVolume, "Up Volume", style = plot.style_columns, color= color.new(color.green, 60))
plot(downVolume, "Down Volume", style = plot.style_columns, color= color.new(color.red, 60))
plot(0, "Zero line", color = color.white, linewidth = 1)
```

130. MULTI TIMEFRAME UP-DOWN VOLUME

```c
//@version=5
indicator("Multi timeframe UP-DOWN VOLUME", format = format.volume)

htf = input.timeframe("D", "timeframe")
htf_Volume = request.security(syminfo.tickerid, htf, volume1, barmerge.gaps_off, barmerge.lookahead_on)

upVolume = close > close1 ? htf_Volume : na
downVolume = close < close1 ? -1*htf_Volume : na


plot(upVolume, "Up Volume", style = plot.style_columns, color= color.new(color.green, 60))
plot(downVolume, "Down Volume", style = plot.style_columns, color= color.new(color.red, 60))
plot(0, "Zero line", color = color.white, linewidth = 1)
```

131. HOW TO FIND THE STOCK SPLIT PROGRAMATICALLY?

```c
//@version=5
indicator("STOCK SPLIT", overlay = true)

has_stock_split = request.splits(syminfo.tickerid, splits.numerator, barmerge.gaps_off, barmerge.lookahead_on)
is_splite_day = (has_stock_split != has_stock_split1) or (na(has_stock_split1) and na(has_stock_split))
bgcolor(is_splite_day ? color.red : na)

// TradeView include build in split symbol on daily chart. therefore this code useless
```

132. BULL-BEAR POWER

```c
//@version=5
indicator("BULL-BEAR POWER")

length = input.int(13, "length")

bullPower = high - ta.ema(close, length)
bearPower = low - ta.ema(close, length)

bbp = bullPower * bearPower
bbp_color = bbp > bbp1 ? color.green : color.red

plot(bbp, color = bbp_color)
hline(0, "Zero Line", color.white, linestyle = hline.style_dashed)
```

133. MULTI TIMEFRAME BULL-BEAR POWER

```c
//@version=5
indicator("MULTI TIMEFRAME BULL-BEAR POWER")

length = input.int(13, "length")
htf = input.timeframe("D", "timeframe")

bullPower = high - ta.ema(close, length)
bearPower = low - ta.ema(close, length)

bbp = bullPower + bearPower
htf_bbp = request.security(syminfo.tickerid, htf, bbp1, barmerge.gaps_off, barmerge.lookahead_on)
bbp_color = htf_bbp > htf_bbp1 ? color.green : color.red

plot(htf_bbp, color = bbp_color)
hline(0, "Zero Line", color.white, linestyle = hline.style_dashed)
```

134. YOU WON'T NEED ANY OTHER TRADING STRATEGY AFTER THIS! G.O.A.T Strategy

135. PROGRAMMATICALLY FIND OUT IF A STOCK HAS GIVEN A DIVIDEND OR NOT

```c
//@version=5
indicator("STOCK Dividend", overlay = true)

has_stock_dividend = request.dividends(syminfo.tickerid, dividends.gross, barmerge.gaps_off, barmerge.lookahead_on)
is_dividend_day = (has_stock_dividend != has_stock_dividend1) or (na(has_stock_dividend1) and na(has_stock_dividend))
bgcolor(is_dividend_day ? color.green : na)

// TradeView include build in dividend symbol on daily chart. therefore this code useless
```

136. FIND OUT A 'DOJI CANDLE'

```c
//@version=5
indicator("find DOJI Candle", overlay = true)

dojiCandle = (close == open) ? color.white : na

bgcolor(dojiCandle)
```

137. PINE SCRIPT OBJECT

```c
//@version=5
indicator("PineScript Object", overlay = true)

type candleObj
    float open
    float high
    float low
    float close

// obj1 = candleObj.new(100, 200, low = 90, close = 150)
obj1 = candleObj.new(100)

lbl = label.new(na, na)

if barstate.islast
    lbl := label.new(bar_index, high,
         "Open: " + str.tostring(obj1.open) +
         "\nHigh: " + str.tostring(obj1.high) +
         "\nLow: " + str.tostring(obj1.low) +
         "\nClose: " + str.tostring(obj1.close), textcolor = color.white)
label.delete(lbl1)  // NaN: Not a Number
```

138. OPENING RANGE BREAKOUT SCREENER

139. IMPORT SOURCE FROM OTHER INDICATOR ~ NEW FEATURE

140. TRIX INDICATOR

```c
//@version=5
indicator("TRIX")

length = input.int(18, "length", minval = 1)

// trix = 10000 * ta.change(ta.ema(ta.ema(math.log(close), length), length),length)

ema1 = ta.ema(math.log(close), length)
ema2 = ta.ema(ema1, length)
ema3 = ta.ema(ema2, length)

trix = ta.change(ema3) * 10000

plot(trix, color = color.green)
hline(0, color=color.white, title = "Zero")
```

141. MULTI TIMEFRAME TRIX INDICATOR

```c
//@version=5
indicator("MULTI TIMEFRAME TRIX")

length = input.int(18, "length", minval = 1)
htf = input.timeframe("D", "timeframe")

// trix = 10000 * ta.change(ta.ema(ta.ema(math.log(close), length), length),length)

ema1 = ta.ema(math.log(close), length)
ema2 = ta.ema(ema1, length)
ema3 = ta.ema(ema2, length)

trix = ta.change(ema3) * 10000

htfTrix = request.security(syminfo.tickerid, htf, trix, barmerge.gaps_off, barmerge.lookahead_on)

plot(htfTrix, color = color.green)
hline(0, color=color.white, title = "Zero")
```

142. FIND THE NUMBER OF EMPLOYEES IN A COMPANY

```c
//@version=5
indicator("FIND THE NUMBER OF EMPLOYEES IN A COMPANY")

numOfEmployees = request.financial(syminfo.tickerid, "NUMBER_OF_EMPLOYEES", "FY")

var lineColor = color.green
lineColor := numOfEmployees > numOfEmployees1 ? color.green : numOfEmployees < numOfEmployees1 ? color.red : lineColor
plot(numOfEmployees, style = plot.style_stepline_diamond, color = lineColor)
```

143. NR-4 CANDLES ~ NARROW RANGE CANDLES

```c
//@version=5
indicator("MR 4 Bar", overlay = true)

barRange = high - low

isInsideBar = high < high1 and low > low1

var isBarRangOk = false

for i = 0 to 3
    if barRange < barRangei+1
        isBarRangOk := true
    else
        isBarRangOk := false
        break

isNR4Candle = isBarRangOk and isInsideBar

if isNR4Candle and close > open
    label.new(bar_index, low, text = "NR4", color = color.green, textcolor = color.white, style = label.style_label_up)

if isNR4Candle and close < open
    label.new(bar_index, high, text = "NR4", color = color.red, textcolor = color.white, style = label.style_label_down)

```

144. HOW TO RETURN MULTIPLE VALUES FROM A FUNCTION

145. FRACTALS

```c
//@version=5
indicator("Fracttals", overlay = true)
// 顶，底，分型
is_green_fractal_fond = high1 > high and high1 > high2
is_red_fractal_fond = low1 < low and low1 < low2

plotshape(is_green_fractal_fond, "Green Fracttal", shape.triangledown, color = color.green, offset = -1, size = size.small)
plotshape(is_red_fractal_fond, "Red Fracttal", shape.triangleup, location.belowbar, color = color.red, offset = -1, size = size.small)
```

146. MOVING AVERAGE SCREENER(no code)
147. TRADING VIEW WIDGETS

```c
for html website use only
```

148. OPEN INTEREST

```c
//@version=5
indicator("Open Interest")

htf = input.timeframe("D", "timeframe")

oiOpen, oiClose, oiColorCond = request.security(syminfo.ticker+"_OI", htf, open, close, close > close1, ignore_invalid_symbol = true)

hasOHLC = ta.cum(oiOpen)

line_color = oiColorCond ? color.green : color.red

plot(hasOHLC ? na : oiClose, "Open Interest", color = line_color, style = plot.style_stepline, linewidth = 4)
// not work properly
```

149. BEST SWING HIGH-LOW INDICATOR

use supertrend color find high and low and label it.

150. NR-7 CANDLES ~ NARROW RANGE CANDLES

```c
//@version=5
indicator("MR 7 Bar", overlay = true)

barRange = high - low

isInsideBar = high < high1 and low > low1

var isBarRangOk = false

for i = 0 to 6
    if barRange < barRangei+1
        isBarRangOk := true
    else
        isBarRangOk := false
        break

isNR7Candle = isBarRangOk and isInsideBar

if isNR7Candle and close > open
    label.new(bar_index, low, text = "NR7", color = color.green, textcolor = color.white, style = label.style_label_up)

if isNR7Candle and close < open
    label.new(bar_index, high, text = "NR7", color = color.red, textcolor = color.white, style = label.style_label_down)
```

151. HOW TO CREATE A STRATEGY WITH STOPLOSS AND TARGET

```c
//@version=5
strategy("Strategy With Stoploss & Target", overlay=true, margin_long=100, margin_short=100, process_orders_on_close = true)

ema = ta.ema(close, input(50, "length"))

longCondition = close > ema
if (longCondition and strategy.position_size1 == 0)
    strategy.entry("Buy", strategy.long)

strategy.exit("Buy-exit", from_entry = "Buy", stop = strategy.position_avg_price - 50, limit = strategy.position_avg_price + 100, comment = "exit")
```

152. HOW TO PUBLISH AN INDICATOR IN TRADING VIEW WITHOUT EXPOSING SOURCE CODE



153. DRAW A LINE FROM LEFTMOST TO RIGHTMOST CANDLE ON THE VISIBLE CHART

```c
//@version=5
indicator("DRAW A LINE FROM LEFTMOST TO RIGHTMOST CANDLE ON THE VISIBLE CHART", overlay = true)

time_left = chart.left_visible_bar_time
time_right = chart.right_visible_bar_time

var line l = na
if barstate.islast
    line.delete(l1)
    l := line.new(time_left, close, time_right, close, xloc = xloc.bar_time, color = color.lime, width = 3)
```

154. SEND TRADING VIEW ALERTS TO A DISCORD CHANNEL

155. PINE SCRIPT MAP ~ STORE DATA IN KEY-VALUE PAIR

```c
//@version=5
indicator("MAP", overlay = true)

var data = map.new<string, int>()

map.put(data, 'a', 1)
map.put(data, 'bar_time', 2)
map.put(data, 'c', 3)

var line l = na
if barstate.islast
    txt = str.tostring(map.get(data, 'a')) + "\n" + str.tostring(map.get(data, 'bar_time')) + "\n" + str.tostring(map.get(data, 'c'))
    lbl = label.new(bar_index, high, text = txt)
```

156. LOGS : INFO, WARNING & ERROR

```c
//@version=5
indicator("logs", overlay = true)

if close > open and barstate.isconfirmed
    log.warning("This candle is Bullish {0}, {1}", open, close)
if close < open and barstate.isconfirmed
    log.error("This candle is Bullish {0}, {1}", open, close)
if barstate.islast and barstate.isconfirmed
    log.info("This candle is Bullish {0}, {1}", open, close)
plot(high)
```

157. BULLISH ABANDONED BABY - CANDLE STICK PATTERN

```c
//@version=5
indicator("Bullish Abandoned Baby", overlay = true)

is_red_candle = close2 < open2
is_gapup_green_candle = close > open and low > high1
is_gap_down_doji_candle = high1 < low2 and open1 == close1
is_bullish_abandoned_baby_fouund = is_gapup_green_candle and is_gap_down_doji_candle and is_red_candle

if is_bullish_abandoned_baby_fouund
    box.new(bar_index2, high2, bar_index, low1, bgcolor = color.new(color.green, 50))
```

158. DRAW POLY-LINES

```c
//@version=5
indicator("Polyline", overlay = true)

var px1 = 0
var px2 = 0
var px3 = 0

var py1 = 0.0
var py2 = 0.0
var py3 = 0.0

if session.isfirstbar
    px1 := bar_index
    py1 := high

if barstate.islastconfirmedhistory
    px2 := bar_index
    py2 := close

if session.isfirstbar
    px3 := bar_index
    py3 := low

point1 = chart.point.from_index(index = px1, price = py1)
point2 = chart.point.from_index(index = px2, price = py2)
point3 = chart.point.from_index(index = px3, price = py3)

var _points = array.new<chart.point>()
if barstate.islastconfirmedhistory
    _points.push(point1)
    _points.push(point2)
    _points.push(point3)

polyline.new(points = _points,
     line_color = color.green,
     fill_color = color.new(color.green, 60),
     line_style = line.style_dotted,
     line_width = 3,
     curved = true,
     closed = true)

polyline.new(points = _points,
     line_color = color.red,
     fill_color = color.new(color.green, 60),
     line_style = line.style_dotted,
     line_width = 3,
     curved = false,
     closed = false)
```

159. BULLISH DOJI STAR PATTERN

```c
//@version=5
indicator("Bullish doji star pattern", overlay = true)

is_first_candle_red = close1 < open1
is_curr_canddle_doji = close == open
is_curr_candle_gapdown = high < low1

is_bullish_doji_star_found = is_first_candle_red and is_curr_canddle_doji and is_curr_candle_gapdown

if is_bullish_doji_star_found
    box.new(bar_index1, high1, bar_index + 1, low, bgcolor = color.new(color.green, 80))

```

160. PAY VIA TRADING VIEW COINS

161. DISPLAY OPTIONS : ALL, NONE, PANE, STATUS LINE, SCALE, DATA WINDOW

162. ANCHORED VWAP

```c
//@version=5
indicator("Anchored VWAP", overlay = true)

// Year = input.time(defval = 2023, title = "Year")
Year = input.int(defval = 2023, title = "Year", minval = 1, maxval = 2099)
Month = input.int(defval = 11, title = "Month", minval = 1, maxval = 12)
Day = input.int(defval = 10, title = "Day", minval = 1, maxval = 31)
Hour = input.int(defval = 9, title = "Hour", minval = 0, maxval = 23)
Minute = input.int(defval = 10, title = "Minute", minval = 0, maxval = 59)

source = input.source(hlc3, "Source")

isAnchorFound = timestamp(Year, Month, Day, Hour, Minute) < time

calculateAnchoredVwap() =>
    float priceVolume = na
    float onlyVolume = na
    priceVolume := isAnchorFound and not isAnchorFound1 ? source * volume : priceVolume1 + (source * volume)
    onlyVolume := isAnchorFound and not isAnchorFound1 ? volume : onlyVolume1 + volume
    avwap = priceVolume/onlyVolume

plot(calculateAnchoredVwap(), "Anchored VWAP", color.white, 3)
```

163. Percent Rank

```c
//@version=5
indicator("Percent Rank", overlay = true)

length = input.int(5, "length", minval = 1)

prank = ta.percentrank(close, length)

var label l = na
if barstate.islast
    label.delete(l1)
    l := label.new(bar_index, high, str.tostring(prank) + "%", textcolor = color.white)
```

164.
