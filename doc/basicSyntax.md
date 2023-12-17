# basic syntax

1. BAR STATE, IS FIRST BAR, IS LAST BAR

```c
//@version=5
indicator("First and Last Bar")

isFirstBar = (barstate.isfirst) ? 1 : 0
isLastBar = (barstate.islast) ? 1 : 0

plot(isFirstBar, color = color.green)
plot(isLastBar, color = color.red)
```

2. NA values

```c
//@version=5
indicator("NA Value")

value = (close > open) ? close : na

plot(value, style = plot.style_linebr)
```

3. BARS SINCE FUNCTION

```c
//@version=5
indicator("Bars Since", '')

value = ta.barssince(close > open)

// count bars since bull
// value = ta.barssince(open > close)
// calculate how many bullish (green) bars continuous

plot(value)
```

4. VALUE WHEN FUNCTION

```c

//@version=5
indicator("Value When", '')

value = ta.valuewhen(close > open, close, 0)
// (open > close) // more info.
plot(value)

```

5. HIGHEST / LOWEST FUNCTION

```c
//@version=5
indicator("H/L function")

highest = ta.highest(close, 10)
plot(highest)
plot(ta.lowest(close, 10), "lowest", color.red)
```

6. DRAW A LINE

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

7. DRAW A HORIZONTAL LINE

```c
//@version=5
indicator("Horizontal Line", overlay = true)

hline(4400, title = "hline High", color = color.gray, linestyle = hline.style_dashed, linewidth = 2, editable = true)
```

8. Draw a label

```c
//@version=5
indicator("Label", overlay = true)

//@version=5
indicator("Label", overlay = true)

label1 = label.new(bar_index, high, text = str.tostring(high), color = color.green, style = label.style_label_down, textcolor = color.white)
label.delete(label11)
```

9. DRAW A TABLE

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

10. DRAW A BOX

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

11. CROSS-OVER & CROSS-UNDER FUNCTIONS

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

12. ARRAY

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

13. FOR LOOP

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
```

14. INTRA-DAY FIRST AND LAST BARS

```c
//@version=5
indicator("Daily First And Last Bar")

t = time("1440", session.regular)
bgcolor(session.isfirstbar ? color.new(color.aqua, 70) : na)
bgcolor(session.islastbar ? color.new(color.red, 70) : na)
```

15. Live Alerts

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

16. ALERT CONDITIONS

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

17. DRAW A VERTICAL LINE

```c
//@version=5
indicator("Verttical Line", overlay = true)

//if barstate.islast
myLine = line.new(bar_index, open, bar_index, close, extend = extend.both, color = color.green)
line.delete(myLine1)

myLbl = label.new(bar_index, close, text = str.tostring(high), style = label.style_label_lower_left, color = color.yellow, textcolor = color.blue)
label.delete(myLbl1)
```

18. DRAW A HORIZONTAL LINE WITH CO-ORDINATE IN THE TEXT

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

19. FILL THE GAPS BETWEEN THE LINES USING FILL FUNCTION

```c
//@version=5
indicator("Fill Plots", overlay = true)
open_plot = plot(open, color = color.red, editable = false)
close_plot = plot(close, color = color.green, editable = false)
fill(open_plot, close_plot, color = color.new(color.blue, 80))
```

20. HOW TO CREATE AND USE A LIBRARY

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

21. SWING HIGH-LOW

```c
// there is no perfict logic to find swing high and low

//@version=5
indicator("Swing hign low", overlay = true)

swing_high = high < high1 and high1 > high2
swing_low = low > low1 and low1 < low2

plotshape(swing_high, "swing_high", style = shape.triangledown, color = color.red, location = location.abovebar, offset = -1)
plotshape(swing_low, "swing_low", style = shape.triangleup, color = color.green, location = location.belowbar, offset = -1)
```

22. SWING HIGH-LOW

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

23. FIND TODAY'S PRICE BAR ONLY

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

24. SUPPORT AND RESISTANCE LEVELS

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

25. HOW TO FIND IF A SOURCE IS FALLING OR NOT

```c
//@version=5
indicator("Falling Source")

is_falling = ta.falling(close, input.int(3, "length"))
plot(close, "falling", is_falling ? color.red : color.green)

// when length 3 then 守K
```

26. HOW TO FIND IF A SOURCE IS RISING OR NOT

```c
//@version=5
indicator("Rising Source")

isRising = ta.rising(close, input.int(10, "length"))
plot(close, "rising", isRising ? color.green : color.red)
```

27. FEWER NUMBER OF LABELS PROBLEM

```c
//@version=5
indicator("Fewer Labels Issue", overlay = true, max_labels_count = 5) //500 defval 50
label.new(x = bar_index, y = high, text = str.tostring(high), style = label.style_label_down, textcolor = color.white)
```

28. TEXT AREA

```c
//@version=5
indicator("TEXT AREA", overlay = true)
i_txt = input.text_area("This indicator takes the user input for the length of the exponential moving average, and then draws the moving average on the chart", title = "Message")
i_length = input.int(100, "EMA Length")
ema = ta.ema(close, i_length)
plot(ema, color = color.lime)
```

29. HOW TO CREATE A MATRIX

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

30. THROW RUNTIME ERROR VIA CODE

```c
//@version=5
indicator("THROW RUNTIME ERROR", overlay = true)

ema = ta.ema(close, 50)
plot(ema, color= color.green)

isError = close < ema and barstate.islast

if isError
    runtime.error("Error!")
```

31. HOW TO FIND THE STOCK SPLIT PROGRAMATICALLY?

```c
//@version=5
indicator("STOCK SPLIT", overlay = true)

has_stock_split = request.splits(syminfo.tickerid, splits.numerator, barmerge.gaps_off, barmerge.lookahead_on)
is_splite_day = (has_stock_split != has_stock_split1) or (na(has_stock_split1) and na(has_stock_split))
bgcolor(is_splite_day ? color.red : na)

// TradeView include build in split symbol on daily chart. therefore this code useless
```

32. PROGRAMMATICALLY FIND OUT IF A STOCK HAS GIVEN A DIVIDEND OR NOT

```c
//@version=5
indicator("STOCK Dividend", overlay = true)

has_stock_dividend = request.dividends(syminfo.tickerid, dividends.gross, barmerge.gaps_off, barmerge.lookahead_on)
is_dividend_day = (has_stock_dividend != has_stock_dividend1) or (na(has_stock_dividend1) and na(has_stock_dividend))
bgcolor(is_dividend_day ? color.green : na)

// TradeView include build in dividend symbol on daily chart. therefore this code useless
```

33. PINE SCRIPT OBJECT

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

34. FIND THE NUMBER OF EMPLOYEES IN A COMPANY

```c
//@version=5
indicator("FIND THE NUMBER OF EMPLOYEES IN A COMPANY")

numOfEmployees = request.financial(syminfo.tickerid, "NUMBER_OF_EMPLOYEES", "FY")

var lineColor = color.green
lineColor := numOfEmployees > numOfEmployees1 ? color.green : numOfEmployees < numOfEmployees1 ? color.red : lineColor
plot(numOfEmployees, style = plot.style_stepline_diamond, color = lineColor)
```

35. OPEN INTEREST

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

36. DRAW A LINE FROM LEFTMOST TO RIGHTMOST CANDLE ON THE VISIBLE CHART

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

37. PINE SCRIPT MAP ~ STORE DATA IN KEY-VALUE PAIR

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

38. LOGS : INFO, WARNING & ERROR

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

38. DRAW POLY-LINES

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
