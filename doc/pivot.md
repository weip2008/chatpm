# pivot

1. PIVOT POINT LEVELS

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

2. FIBONACCI PIVOT POINT LEVELS

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

3. CPR LEVEL

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

4. NEXT DAY'S CPR LEVELS

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

5. CAMARILLA PIVOT POINTS

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

6. NEXT DAY'S CAMARILLA PIVOT POINTS

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
