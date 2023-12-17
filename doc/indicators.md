# indicators

1. INDICATOR REPAINTING ISSUE

```c
//@version=5
indicator("Indicator Repaint", 'Ind RP')

higherTFClose = request.security(syminfo.tickerid, "W", close) // Repaint
//higherTFClose = request.security(syminfo.tickerid, "W", close1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on) //Does not Repaint

plot(higherTFClose)
```

2. MOVING AVERAGES - SIMPLE, EXPONENTIAL

```c
//@version=5
indicator("Moving Average", 'MA')

i_length = input.int(20, 'Length', minval = 1, maxval = 1000)

sma = ta.sma(close, i_length)
ema = ta.ema(close, i_length)

plot(sma, color = color.red)
plot(ema, color = color.green)
```

3. EMA CROSS DEMO (private published)

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

4. MACD

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

5. RSI WITH AVERAGE

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

6. ATR

```c
//@version=5
indicator("Average True Range", "ATR")

length = input.int(14, "Length")

atr = ta.atr(length)

plot(atr, color = color.yellow)
```

7. VWAP

```c
//@version=5
indicator("VWAP", "VWAP", true)
plot(ta.vwap(close))
```

8. COMMODITY CHANNEL INDEX

```c
//@version=5
indicator("COMMODITY CHANNEL INDEX", "CCI")
plot(ta.cci(close, input.int(14, "Length")))
```

9. STOCHASTIC INDICATOR

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

10. PARABOLIC SAR INDICATOR

```c
//@version=5
indicator("Parabolic SAR", overlay = true)

start = input.float(defval = 0.02, title = "Start", step = 0.01)
increment = input.float(defval = 0.02, title = "Increment", step = 0.01)
maximum = input.float(defval = 0.2, title = "Maximum Value", step = 0.1)

sar = ta.sar(start, increment, maximum)
plot(sar, style = plot.style_circles, color = close > sar ? color.green : color.red)
```

11. SUPERTREND

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

12. MULTI TIME-FRAME MOVING AVERAGE

```c
//@version=5
indicator("Multi Timeframe Moving Average", overlay = true)

tf = input.timeframe("D", "Select Timeframe")
length = input.int(defval = 50, title = "length")

currentMA = ta.sma(close, length)

higherTFMA = request.security(syminfo.tickerid, tf, currentMA1, barmerge.gaps_on, barmerge.lookahead_on)

plot(higherTFMA)
```

13. MULTI TIME-FRAME MACD

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

14. MULTI TIME-FRAME RSI with AVERAGE

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

15. MULTI TIME-FRAME SUPER TREND

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

16. MTF BB

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

17. DONCHIAN CHANNEL

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

18. MULTI TIMEFRAME DONCHIAN CHANNEL

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

19. KELTNER CHANNEL

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

20. MULTI TIMEFRAME KELTNER CHANNEL

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

21. RUN AN INDICATOR ON A PARTICULAR STOCK SCRIP ONLY

```c
//@version=5
indicator("Script Validation", overlay = true)

isScriptValid = syminfo.ticker == "TSLA" or syminfo.ticker == "AAPL"
plot(isScriptValid ? close : na)
```

22. RUN AN INDICATOR ON A PARTICULAR TIMEFRAME ONLY

```c
//@version=5
indicator("Timeframe Validation", overlay = true)

isTimeframeValid = timeframe.period == "15"
plot(isTimeframeValid ? close : na)
```

23. MOVING AVERAGE RIBBON

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

24. MULTI TIMEFRAME MOVING AVERAGE RIBBON

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

25. Center of Gravity

```c
//@version=5
indicator("Center of Gravity")

cog = ta.cog(close, 14)

plot(cog, color = color.gray)
```

26. MULTI TIMEFRAME CENTER OF GRAVITY

```c
//@version=5
indicator("Center of Gravity")

htf = input.timeframe("D", "timeframe")
cog = ta.cog(close, 14)
coghtf = request.security(syminfo.tickerid, htf, cog1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
plot(coghtf, color = color.gray)
```

27. ARNAUD LEGOUX MOVING AVERAGE

```c
//@version=5
indicator("Arnaud Legoux Moving Average", overlay = true)

length = input.int(9, "Length")
offset = input.float(0.85, "Offset")
smoothness = input.int(6, "smoothness")

alma = ta.alma(close, length, offset, smoothness)
plot(alma)
```

28. MULTI TIMEFRAME ARNAUD LEGOUX MOVING AVERAGE

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

29. DMI - DIRECTIONAL MOMENTUM INDEX

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

30. MULTI-TIMEFRAME DMI - DIRECTIONAL MOMENTUM INDEX

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

31. ICHIMOKU CLOUD

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

32. MULTI-TIMEFRAME ICHIMOKU CLOUD

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

33. INTRADAY INTENSITY INDEX

```c
//@version=5
indicator("Intraday Intensity Index")
plot(ta.iii, color = ta.iii > 0 ? color.green : color.red)
hline(0, "Zero Line", color.white, hline.style_dotted, 1)
```

34. MULTI TIMEFRAME INTRADAY INTENSITY INDEX

```c
//@version=5
indicator("Multi Timeframe Intraday Intensity Index")

htf = input.timeframe("30", "timeframe")

iii = ta.iii
htf_iii = request.security(syminfo.tickerid, htf, iii1, barmerge.gaps_off, barmerge.lookahead_on)

plot(htf_iii, color = ta.iii > 0 ? color.green : color.red)
hline(0, "Zero Line", color.yellow, hline.style_dotted, 1)
```

35. ACCUMULATION DISTRIBUTION INDEX

```c
//@version=5
indicator("Accumulation Distribution Index", format = format.volume)
adi = ta.accdist

plot(adi, "adi", (adi > adi1) ? color.green : color.red)
```

36. MULTI TIMEFRAME ACCUMULATION DISTRIBUTION INDEX

```c
//@version=5
indicator("Multi Timeframe Accumulation Distribution Index", format = format.volume)

htf = input.timeframe("W", "timeframe")
adi = ta.accdist

htf_adi = request.security(syminfo.tickerid, htf, adi1, barmerge.gaps_off, barmerge.lookahead_on)

plot(htf_adi, "adi", (adi > adi1) ? color.green : color.red)
```

37. AWESOME OSCILLATOR

```c
//@version=5
indicator("AWESOME OSCILLATOR")

osc = ta.sma(hl2, 5) - ta.sma(hl2, 34)
diff = osc - osc1
osc_color = diff<=0 ? color.red : color.green
plot(osc, "oscillator", osc_color, style = plot.style_columns) // style_histgram
```

38. MULTI TIMEFRAME AWESOME OSCILLATOR

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

39. BALANCE OF POWER

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

40. MULTI TIME FRAME BALANCE OF POWER

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

41. BULL-BEAR POWER

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

42. MULTI TIMEFRAME BULL-BEAR POWER

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

43. TRIX INDICATOR

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

44. MULTI TIMEFRAME TRIX INDICATOR

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

45. ANCHORED VWAP

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
