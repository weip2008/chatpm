# macd

1. MULTI TIMEFRAME MACD HISTOGRAM

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
