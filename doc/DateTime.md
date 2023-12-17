# Date time

1. DATE RANGE

```c
//@version=5
indicator("Date Range", overlay = true)

startDate = input.int(defval = 1, minval = 1, maxval = 31, title = "Start Date")
startMonth = input.int(defval = 1, minval = 1, maxval = 12, title = "Start Month")
startYear = input.int(defval = 2022, minval = 2000, maxval = 2100, title = "Start Year")

endDate = input.int(defval = 31, minval = 1, maxval = 31, title = "End Date")
endMonth = input.int(defval = 12, minval = 1, maxval = 12, title = "End Month")
endYear = input.int(defval = 2022, minval = 2000, maxval = 2100, title = "End Year")

inDateRange = (time >= timestamp(syminfo.timezone, startYear, startMonth, startDate, 0, 0, 0)) and
(time < timestamp(syminfo.timezone, endYear, endMonth, endDate, 0, 0, 0))

plot(inDateRange ? close : na, linewidth = 3)
```

2. DATE & TIME RANGE

```c
//@version=5
indicator("Date and Time Range", overlay = true)

startDateTime = timestamp(2023, 10, 06, 09, 30, 0)
endDateTime = timestamp(2023, 11, 06, 09, 30, 0)

inDateAndTimeRange = (time >= startDateTime and time < endDateTime)

bgcolor(inDateAndTimeRange ? color.new(color.gray, 90) : na)

plot(inDateAndTimeRange ? close : na, linewidth = 3)
```

3. CALCULATE DAILY RANGE

```c
//@version=5
indicator("Dailly Range")

daily_high = request.security(syminfo.tickerid, "D", high1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)
daily_low = request.security(syminfo.tickerid, "D", low1, gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on)

daily_range = daily_high - daily_low
plot(daily_range, "Daily Range", color.green, 5)
```

4. HOW TO FIND MARKET HOURS || REGULAR, PRE-MARKET, POST-MARKET

```c
// not work
indicator("Market Sessions", overlay = true)

// mktColor = if session.ismarket
//     color.new(color.gray, 80)
// else
//     if session.ispremarket
//         color.new(color.aqua, 30)
//     else
//         if session.ispostmarket
//             color.new(color.red, 30)
//         else
//             na

is_market_hours = session.ismarket ? true : false

mktColor = is_market_hours ? color.green : color.red

bgcolor(mktColor)

```

5. AROON

What Is the Aroon Oscillator?

```
What Is the Aroon Oscillator?
The Aroon Oscillator is a trend-following indicator that uses aspects of the Aroon Indicator (Aroon Up and Aroon Down) to gauge the strength of a current trend and the likelihood that it will continue.
```

```c
//@version=5
indicator("Aroon", format = format.percent, precision = 2)

length = input.int(14, minval = 1)

upper = 100 * (ta.highestbars(high, length) + length) / length
lower = 100 * (ta.lowestbars(low, length) + length) / length

plot(upper, "Aroon Up", color.green)
plot(lower, "Aroon Down", color.red)
```

6. MULTI TIMEFRAME AROON

```c
//@version=5
indicator("Multi Timeframe Aroon", format = format.percent, precision = 2)

length = input.int(14, minval = 1)
htf = input.timeframe("D", "timeframe")

upper = 100 * (ta.highestbars(high, length) + length) / length
lower = 100 * (ta.lowestbars(low, length) + length) / length

htf_upper = request.security(syminfo.tickerid, htf, upper1, barmerge.gaps_off, barmerge.lookahead_on)
htf_lower = request.security(syminfo.tickerid, htf, lower1, barmerge.gaps_off, barmerge.lookahead_on)

plot(htf_upper, "Aroon Up", color.green)
plot(htf_lower, "Aroon Down", color.red)
```

```
The Difference Between the Aroon Indicator and the Directional Movement Index (DMI)
The Aroon indicator is similar to the Directional Movement Index (DMI) developed by Welles Wilder. It too uses up and down lines to show the direction of a trend. The main difference is that the Aroon indicator formulas are primarily focused on the amount of time between highs and lows. The DMI measures the price difference between current highs/lows and prior highs/lows. Therefore, the main factor in the DMI is price, and not time.
```
