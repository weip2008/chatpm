# Bollinger Band

1. BOLLINGER BAND WIDTH

```c
//@version=5
indicator("BOLLINGER BAND WIDTH")

bb_length = input.int(50, "Bollinger Band Length")
bb_multiplier = input.int(2, "Bollinger Band Multiplier")

bb_width = ta.bbw(close, bb_length, bb_multiplier)
plot(bb_width)
```
