# bars

1. HOW TO FIND AN INSIDE BAR

```c

//@version=5
indicator("Inside Bar", overlay = true)

isInsideBar = high < high1 and low > low1
insideBarColor = isInsideBar ? color.white : na
barcolor(insideBarColor)

plotshape(series = isInsideBar, title = "insde bar", style = shape.arrowup, color = color.white, location = location.belowbar)
```

2. FIND A MULTI-TIMEFRAME INSIDE BAR

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

2. FIND OUT A 'DOJI CANDLE'

```c
//@version=5
indicator("find DOJI Candle", overlay = true)

dojiCandle = (close == open) ? color.white : na

bgcolor(dojiCandle)
```

3. NR-4 CANDLES ~ NARROW RANGE CANDLES

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

4. FRACTALS

```c
//@version=5
indicator("Fracttals", overlay = true)
// 顶，底，分型
is_green_fractal_fond = high1 > high and high1 > high2
is_red_fractal_fond = low1 < low and low1 < low2

plotshape(is_green_fractal_fond, "Green Fracttal", shape.triangledown, color = color.green, offset = -1, size = size.small)
plotshape(is_red_fractal_fond, "Red Fracttal", shape.triangleup, location.belowbar, color = color.red, offset = -1, size = size.small)
```

5. NR-7 CANDLES ~ NARROW RANGE CANDLES

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

6. BULLISH ABANDONED BABY - CANDLE STICK PATTERN

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

7. BULLISH DOJI STAR PATTERN

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

8. Percent Rank

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
