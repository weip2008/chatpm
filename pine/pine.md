<h1> PINE Learning Notes </h1>

细节决定成败！

TreadingView is best tool for automatic stock buy/sell.

- [Getting Started](#getting-started)
- [Basics](#basics)
- [使用用户手册](#使用用户手册)
  - [ta.ema()](#taema)
  - [overlay](#overlay)
- [对接交易所下单](#对接交易所下单)
- [Strategy](#strategy)
- [回测](#回测)
  - [strategy.entry](#strategyentry)
  - [Strategy Properties](#strategy-properties)
- [Boolinger Band](#boolinger-band)
- [ATR](#atr)
  
## Getting Started
* install TreadingView software
> Download Website: [Download Website](https://www.tradingview.com/desktop/)
File: TradingView.msix

## Basics
* [Day-1 画图](https://www.youtube.com/watch?v=6Nz2iPXo3xg)
![Day-1 画图](images/pickupData.png)

* create new indicator
  - ![](images/new_indicator.png)<br>
  - ![](images/new.png)
  - ![](images/dataWindow.png)
  
> Source Code: [first indicator](src/indicator01.pine)

![](images/addChart.png)

## 使用用户手册
![](images/manual.png) ![](images/manual2.png)

* [Day-2 金叉⋅死叉⋅报警](https://www.youtube.com/watch?v=1FxV9K9W9Vo)

### ta.ema() 

name|type|meaning
|---|---|---|
ta|class|Technical Analysis
ema|function|Exponential Moving Average

> Source Code: [金叉⋅死叉 buy & sell](src/indicator02.pine)

![](images/title.png)
![](images/fill.png)
![](images/alert.png)

### overlay
```py
indecator("basic02", overlay = true)
```

* [Day-3](https://www.youtube.com/watch?v=1yOFqMzrjWM&list=PL8nVz3ceLBeDRy9EFzd8Adux40Rxz94yi&index=9)

## 对接交易所下单
```mermaid
graph LR
T[TreadingView]
A(Alert)
O[Order-Python]
S[Stock Exchange]
TVC[TVCBOT]
T-->A-->O--API-->S
A-->TVC-->S
```

## Strategy

Open -> new Stratege

> Source Code: [first stratege](src/strategy01.pine)
Save ⟹ Strategy Tester(tab) ⟹ Load your strategy ⟹ 

![](images/strategy.png)

> Source Code:[MACD strateg from 邢](src/strategy02.pine)

## 回测

### strategy.entry
![](images/strategy.entry.png)
![](images/开多单.png)
> Source Code: [自动开单平仓，回测结果](src/strategy03.pine)
![total 97 trades](images/basic03.png)

### Strategy Properties
![](images/strategyProperties.png)
![](images/properties.png)

## Boolinger Band
![](images/boolingerBand.png)

## ATR

ATR: Average True Range
![](images/atr.png)
> Source Code: [add atr to buy](src/strategy05.pine)

```py
// ATR 满足上涨条件: 今天的atr大于前两天的atr
atr = ta.atr(14)[0]>ta.atr(14)[2]

//开多单
if buy and atr
    strategy.entry('long1', strategy.long, 1)  //做多， 交易数量1
```
![Reduce trades from 97 to 46](images/atrReduceTrade.png)