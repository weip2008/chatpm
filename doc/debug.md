# debug

1. use label

```c
//@version=5
indicator("Drawing Variable Values", overlay=true)

// Calculate difference between 50 EMA and 100 EMA
variableValue = (ta.ema(close, 100) - ta.ema(close, 50)) / syminfo.mintick

// Create a label
labelText = str.tostring(variableValue)
ourLabel = label.new(x=bar_index, y=na, text=labelText, yloc=yloc.belowbar, color=color.green, textcolor=color.white,
 style=label.style_label_up, size=size.normal)

label.delete(ourLabel[1])
```
