# Volume

1. HOW TO GET THE VOLUME PROGRAMMATICALLY

```c
//@version=5
indicator("Voluume", format = format.volume)
var volume_color = color.green
volume_color := close > open ? color.green : close < open ? color.red : volume_color1
// volume_color = htf_close > htf_open ? color.green : color.red
plot(volume, style = plot.style_columns, color = volume_color)
```

2. MULTI-TIMEFRAME VOLUME

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

3. UP-DOWN VOLUME

```c
//@version=5
indicator("UP-DOWN VOLUME", format = format.volume)

upVolume = close > close1 ? volume : na
downVolume = close < close1 ? -1*volume : na

plot(upVolume, "Up Volume", style = plot.style_columns, color= color.new(color.green, 60))
plot(downVolume, "Down Volume", style = plot.style_columns, color= color.new(color.red, 60))
plot(0, "Zero line", color = color.white, linewidth = 1)
```

4. MULTI TIMEFRAME UP-DOWN VOLUME

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
