# color

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

3. change bar color
```c
//@version=5
indicator("PSMC - Bar Wick & Border Color", overlay=true)
bullCandle = close > open
plotcandle(bullCandle ? open : na, bullCandle ? high : na, bullCandle ? low : na, bullCandle ? close : na,
 color=color.green, wickcolor=color.blue, bordercolor=color.lime)
plotcandle(bullCandle ? na : open, bullCandle ? na : high, bullCandle ? na : low, bullCandle ? na : close,
color=color.maroon, wickcolor=color.orange, bordercolor=color.red)
```
