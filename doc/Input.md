# Input

1. INTEGER INPUT

```c
//@version=5
indicator("Input integer")

plot(input.int(title = "integer value", defval = 1, maxval = 10, minval = 1, step = 2))
```

2. DECIMAL INPUT

```c
//@version=5
indicator("Input Decimal Values")

plot(input.int(title = "Enter value:", defval = 1.5, maxval = 10.0, minval = 1.0, step = 0.5))
```

3. BOOLEAN INPUT

```c
//@version=5
indicator("Input boolean")

changeColor = input.bool(defval = true, title = "change Color yes/no") ? color.green : color.red
plot(close, color = changeColor)
```

4. COLOR INPUT

```c
//@version=5
indicator("Input color")

i_color = input.color(defval = color.orange, title = "Select Color")
plot(close, color = i_color)
```

5. PRICE INPUT

```c
//@version=5
indicator("Input Price")

i_price = input.price(defval = 10, title = "Enter Price:")
plot(i_price)
```

6. RESOLUTION INPUT

```c
//@version=5
indicator("Input Resolution")

i_resolution = input.timeframe(defval = "D", title = "Select Resolution", options = 'D','W','M')
plot(close)
```

7. SYMBOL INPUT

```c
//@version=5
indicator("Input Symbol")

i_symbol = input.symbol(defval = "TSLA", title = "Select Symbol")
plot(close)
```

8. STRING INPUT

```c
//@version=5
indicator("Input String")

i_txt = input.string(defval = "TSLA will up", title = "Enter Text")
plot(close)
```

9. SOURCE INPUT

```c
//@version=5
indicator("Input Source")

i_source = input.source(defval = high, title = "Select Source")
plot(i_source)
```

10. SESSION INPUT

```c
//@version=5
indicator("Input Session")

i_session = input.session(defval = "0930-1600", title = "Select Session", options = "0930-1600", "1300-1700", "1700-2100")

t = time(timeframe.period, i_session)

plot(close, color = (time == t) ? color.green : color.red)
```

11. ALIGN INPUTS INLINE HORIZONTALLY

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

12. GROUP USER INPUTS & APPLY HEADER LABEL

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
