<h1> PINE Learning Notes </h1>

细节决定成败！

TreadingView is best tool for automatic stock buy/sell.

- [使用用户手册](#使用用户手册)
- [Basics](#basics)
  - [ta.ema](#taema)


## 使用用户手册
![](images/manual.png) ![](images/manual2.png)

  
## Basics
* [Day-1 画图](https://www.youtube.com/watch?v=6Nz2iPXo3xg)
![Day-1 画图](images/pickupData.png)

* create new indicator
  - ![](images/new.png)
  - ![](images/new_indicator.png)
  
```py
# This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
# © jwang_531122

# @version=5
indicator("My script")
plot(close)

```
![](images/addChart.png)

* [Day-2 金叉⋅死叉⋅报警](https://www.youtube.com/watch?v=1FxV9K9W9Vo)

### ta.ema 

function|meaning
|---|---|
ta|Technical Analysis
ema|Exponential Moving Average

```py
indicator("basic-2")
fast = ta.ema(close, 12)
slow = ta.ema(close, 26)
line1 = plot(fast,color=color.red, title='ema12')
line2 = plot(slow,color=color.yellow)

buy = ta.crossover(fast, slow)
sell = ta.crossover(slow,fast)
plotchar(buy,text='buy',color=color.green)
plotchar(sell,text='sell',color=color.red)

c1 = (fast>slow) ? color.green : color.red

fill(line1,line2,color=color.new(c1, 80))
```

![](images/title.png)
![](images/fill.png)
