"""
Simple program to generate the price of the tea in China
Author: Edward
"""

import yfinance as yf

#define the ticker symbol
tickerSymbol = input("What ticker are you interested in?\n")

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

#see your data
print(tickerDf)

