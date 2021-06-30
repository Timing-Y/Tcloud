# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import backtrader as bt
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import backtrader.analyzers as btanalyzers
import math
import numpy as np
import quantstats
import talib
import time
import mail

yingli = 1.3
kuisun = 0.9

outprint = []
outprint = pd.DataFrame(columns=['time','text'])



class Strategy(bt.Strategy):
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    params = (('p1', 12), ('p2', 26), ('p3', 9),)

    def __init__(self):
        self.sma5 = dict()
        self.sma10 = dict()
        self.sma20 = dict()
        self.sma30 = dict()
        self.sma90 = dict()
        self.sma250 = dict()
        self.sma144 = dict()
        self.sma169 = dict()
        self.vma5 = dict()
        self.vma20 = dict()
        self.macd = dict()
        self.rsi = dict()
        self.bolltop = dict()
        self.bollmid = dict()
        self.bollbot = dict()
        self.crossover_520 = dict()
        self.crossovermacd = dict()
        self.DonchianHi = dict()
        self.DonchianLo = dict()
        self.buysignal = dict()
        self.buysignal1 = dict()
        self.buysignal2 = dict()
        self.buysignal3 = dict()
        self.buysignal4 = dict()
        self.buysignal5 = dict()
        self.buysignal6 = dict()
        self.buysignal7 = dict()
        self.buysignal8 = dict()
        self.buysignal9 = dict()
        self.buysignal10 = dict()
        self.buysignal11 = dict()
        self.buysignal12 = dict()
        self.buysignal13 = dict()
        self.buysignal14 = dict()
        self.buysignal15 = dict()
        self.buysignal16 = dict()
        self.buysignal17 = dict()
        self.buysignal18 = dict()
        self.buysignal19 = dict()
        self.buysignal20 = dict()
        self.buysignal21 = dict()
        self.buysignal22 = dict()
        self.buysignal23 = dict()
        self.buysignal24 = dict()
        self.buysignal25 = dict()
        self.buysignal26 = dict()
        self.buysignal27 = dict()
        self.buysignal28 = dict()
        self.buysignal29 = dict()
        self.buysignal30 = dict()
        self.buysignal31 = dict()
        self.buysignal32 = dict()
        self.buysignal33 = dict()
        self.buysignal34 = dict()
        self.buysignal35 = dict()
        self.buysignal36 = dict()
        self.buysignal37 = dict()
        self.sellsignal = dict()
        self.sellsignal1 = dict()
        self.sellsignal2 = dict()
        self.sellsignal3 = dict()
        self.sellsignal4 = dict()
        self.sellsignal5 = dict()
        self.sellsignal6 = dict()
        self.sellsignal7 = dict()
        self.sellsignal8 = dict()
        self.sellsignal9 = dict()
        for i, d in enumerate(self.datas):

            self.sma5[d] = bt.ind.SMA(d.close, period=5)
            self.sma10[d] = bt.ind.SMA(d.close, period=10)
            self.sma20[d] = bt.ind.SMA(d.close, period=20)
            self.sma30[d] = bt.ind.SMA(d.close, period=30)
            self.sma90[d] = bt.ind.SMA(d.close, period=90)
            self.sma250[d] = bt.ind.SMA(d.close, period=250)
            self.sma144[d] = bt.ind.SMA(d.close, period=144)
            self.sma169[d] = bt.ind.SMA(d.close, period=169)

            self.vma5[d] = bt.ind.SMA(d.volume, period=5)
            self.vma20[d] = bt.ind.SMA(d.volume, period=20)
            self.macd[d] = bt.indicators.MACD(d)
            self.rsi[d] = bt.indicators.RSI(d)


            self.bolltop[d] = bt.indicators.BollingerBands(d, period=20).top
            self.bollmid[d] = bt.indicators.BollingerBands(d, period=20).mid
            self.bollbot[d] = bt.indicators.BollingerBands(d, period=20).bot

            #self.crossover_520[d] = bt.ind.CrossOver(self.sma5[d], self.sma10[d])
            self.crossovermacd[d] = bt.indicators.CrossOver(self.macd[d].macd, self.macd[d].signal, plot = False)


            mystrategy = 4

            if mystrategy == 1:
                self.buysignal5[d] = bt.talib.CDLMORNINGSTAR(d.open, d.high, d.low, d.close)#bt.indicators.Highest(self.buysignal6[d](-1), period=2, plot=False)
                self.buysignal3[d] = bt.And(self.rsi[d].rsi < 35, (self.vma5[d] < 1.2 * self.vma20[d]), (self.vma5[d] > 0.8 * self.vma20[d]))
                self.buysignal1[d] = bt.indicators.Highest(self.buysignal3[d](-1), period=3, plot = False)
                self.buysignal2[d] = bt.And(self.crossovermacd[d] == 1, self.rsi[d].rsi < 55)
                self.buysignal4[d] = bt.indicators.Highest(self.buysignal2[d](-1), period=3, plot = False)
                self.buysignal7[d] = bt.And(self.macd[d].macd > 0, self.crossovermacd[d] == 1, (self.vma5[d] <= 1.1 * self.vma20[d]), self.rsi[d].rsi < 55)
                self.buysignal6[d] = bt.And(self.macd[d].macd < 0, self.macd[d].macd < 2 * self.macd[d].signal, self.rsi[d].rsi < 30, bt.indicators.Highest(d.close > self.bollbot[d], period=3, plot = False))
                self.buysignal[d] = bt.indicators.Or(self.buysignal6[d], bt.And(self.buysignal1[d], self.buysignal2[d]), self.buysignal7[d], bt.And(self.buysignal5[d], self.rsi[d].rsi <= 50), plot = True)
            elif mystrategy == 2:
                self.buysignal1[d] = bt.And(bt.indicators.Highest(bt.talib.CDLMORNINGSTAR(d.open, d.high, d.low, d.close), period=3, plot=False), d.close<self.bollmid[d], bt.Or(bt.And(self.rsi[d].rsi < 50, self.macd[d].macd > 0), bt.And(self.rsi[d].rsi < 40, self.macd[d].macd < 0)), (self.vma5[d] < 1.2 * self.vma20[d]), (self.vma5[d] > 0.8 * self.vma20[d]))
                self.buysignal2[d] = bt.And(self.rsi[d].rsi < 33, (self.vma5[d] < 1.2 * self.vma20[d]), (self.vma5[d] > 0.8 * self.vma20[d]))
                self.buysignal3[d] = bt.And(self.crossovermacd[d] == 1, (self.vma5[d] < 1.2 * self.vma20[d]))
                self.buysignal4[d] = bt.And(bt.indicators.Lowest(d.low > self.bollbot[d], period=2, plot = False), d.close > self.bollbot[d])
                self.buysignal9[d] = bt.And(d.close > self.bollbot[d], self.rsi[d].rsi < 20, self.macd[d].macd > self.macd[d].macd(-1))
                self.buysignal5[d] = bt.And(self.crossovermacd[d] == 1, self.macd[d].macd > 0, self.rsi[d].rsi < 45, (self.vma5[d] <= 1.1 * self.vma20[d]))
                self.buysignal6[d] = bt.indicators.Highest(self.buysignal2[d], period = 6, plot = False)
                self.buysignal7[d] = bt.indicators.Highest(self.buysignal3[d], period = 6, plot = False)
                self.buysignal8[d] = bt.And(bt.indicators.Lowest(bt.Or(self.rsi[d].rsi >= 35, (self.vma5[d] >= 1.2 * self.vma20[d]))(-20), period=3, plot = False), self.buysignal6[d])
                self.buysignal[d] = bt.And(bt.Or(self.buysignal1[d], self.buysignal9[d], bt.And(self.buysignal3[d], self.buysignal6[d], self.buysignal8[d]), self.buysignal5[d]), self.buysignal4[d]) #or self.buysignal5[d] or self.buysignal6[d] or self.buysignal7[d]
            elif mystrategy == 3:
                self.buysignal1[d] = bt.And(self.rsi[d].rsi < 30, (self.vma5[d] < 1.2 * self.vma20[d]),(self.vma5[d] > 0.8 * self.vma20[d]))
                self.buysignal2[d] = bt.And(self.rsi[d].rsi > 30, self.rsi[d].rsi < 40, (self.vma5[d] < 1.2 * self.vma20[d]),(self.vma5[d] > 0.8 * self.vma20[d]))
                #self.buysignal3[d] = bt.indicators.Lowest(self.macd[d].macd, period=20, plot = False)
                self.buysignal3[d] = bt.indicators.Highest(self.rsi[d].rsi>=65 ,period=50)
                self.buysignal4[d] = bt.indicators.Highest(self.macd[d].macd, period=20, plot = False)
                self.buysignal5[d] = bt.indicators.Lowest(self.rsi[d].rsi, period=20)
                self.buysignal6[d] = bt.indicators.Highest(self.rsi[d].rsi, period=20)
                self.buysignal7[d] = bt.indicators.Highest(bt.And(self.buysignal5[d] <= 35, self.buysignal6[d] <=50, self.buysignal3[d]), period=1)
                self.buysignal8[d] = bt.And(bt.indicators.Lowest(d.low > self.bollbot[d], period=2, plot = False), d.close > self.bollbot[d])
                self.buysignal9[d] = bt.indicators.Highest(bt.And(self.rsi[d].rsi<=45, self.buysignal4[d] < 0.02*d.close, self.crossovermacd[d] == 1), period=5)

                self.buysignal[d] = bt.And(bt.indicators.Highest(bt.And(self.buysignal7[d]), period=1),self.buysignal9[d], self.buysignal8[d])
            elif mystrategy == 4:
                self.buysignal1[d] = bt.And(self.rsi[d].rsi < 30, (self.vma5[d] < 1.2 * self.vma20[d]),
                                            (self.vma5[d] > 0.8 * self.vma20[d]))
                self.buysignal2[d] = bt.And(self.rsi[d].rsi > 30, self.rsi[d].rsi < 40,
                                            (self.vma5[d] < 1.2 * self.vma20[d]), (self.vma5[d] > 0.8 * self.vma20[d]))
                self.buysignal3[d] = bt.indicators.Lowest(self.macd[d].macd, period=20, plot = False)
                self.buysignal4[d] = bt.indicators.Highest(self.macd[d].macd, period=20, plot=False)
                self.buysignal5[d] = bt.indicators.Lowest(self.rsi[d].rsi, period=20, plot=False)
                self.buysignal6[d] = bt.indicators.Highest(self.rsi[d].rsi, period=20, plot=False)

                self.buysignal7[d] = bt.indicators.Highest(bt.And(self.buysignal5[d] <= 55,
                                                                  self.buysignal5[d] >= 35,
                                                                  self.buysignal6[d] <= 70,

                                                                  self.buysignal5[d] >= self.buysignal5[d](-4),
                                                                  self.buysignal5[d](-4) >= self.buysignal5[d](-8),
                                                                  self.buysignal5[d](-8) >= self.buysignal5[d](-12),
                                                                  self.buysignal5[d](-2) >= self.buysignal5[d](-6),
                                                                  self.buysignal5[d](-6) >= self.buysignal5[d](-10),
                                                                  self.buysignal5[d](-10) >= self.buysignal5[d](-14),
                                                                  ),
                                                           period=3)

                self.buysignal8[d] = bt.indicators.Highest(bt.And(
                                                                    self.buysignal6[d] >= 60,
                                                                  #self.buysignal6[d] > self.buysignal6[d](-21),
                                                                  self.buysignal6[d] >= self.buysignal6[d](-4),
                                                                  self.buysignal6[d](-4) >= self.buysignal6[d](-8),
                                                                  self.buysignal6[d](-8) >= self.buysignal6[d](-12),
                                                                  self.buysignal6[d](-2) >= self.buysignal6[d](-6),
                                                                  self.buysignal6[d](-6) >= self.buysignal6[d](-10),
                                                                  self.buysignal6[d](-10) >= self.buysignal6[d](-14),
                                                                ),
                                                           period=3)
                self.buysignal10[d] = bt.And(bt.indicators.Lowest(d.low > self.bollbot[d], period=2),
                                            d.close > self.bollbot[d])
                self.buysignal11[d] = bt.And(bt.indicators.Lowest(d.close < self.bolltop[d], period=2),
                                            d.close < self.bolltop[d])
                self.buysignal12[d] = bt.And(self.buysignal7[d]==0,bt.Or(self.buysignal10[d]==0,self.buysignal11[d]==0))

                # self.buysignal19[d] = bt.ind.Lowest(d.close, period=160)
                # self.buysignal18[d] = bt.ind.Lowest(d.close, period=120)
                self.buysignal17[d] = bt.ind.Lowest(d.close, period=80)
                self.buysignal16[d] = bt.ind.Lowest(d.close, period=40)
                self.buysignal15[d] = bt.ind.Lowest(d.close, period=20)
                self.buysignal23[d] = bt.ind.Highest(bt.Or(self.buysignal15[d]==self.buysignal16[d],self.buysignal16[d]==self.buysignal17[d],self.buysignal15[d]==self.buysignal17[d]),period=3)

                self.buysignal19[d] = bt.ind.Highest(d.close, period=80)
                self.buysignal20[d] = bt.ind.Highest(d.close, period=40)
                self.buysignal21[d] = bt.ind.Highest(d.close, period=20)
                #self.buysignal23[d] = bt.ind.Highest(d.close, period=120)
                self.buysignal22[d] = bt.ind.Lowest(bt.Or(self.buysignal19[d]==self.buysignal20[d],self.buysignal20[d]==self.buysignal21[d],self.buysignal19[d]==self.buysignal21[d]),period=3)

                self.buysignal13[d] = bt.indicators.Highest(bt.And(bt.talib.CDLMORNINGSTAR(d.open, d.high, d.low, d.close)),period=3)#self.buysignal5[d] <= 50, self.buysignal6[d] <= 70,,self.macd[d].macd < d.close*0.02
                self.buysignal14[d] = bt.And(self.buysignal13[d],(self.vma5[d] <= 1.4 * self.vma20[d]), (self.vma5[d] >= 0.6 * self.vma20[d]), self.buysignal6[d] <= 70)#, (self.vma5[d] <= 1.2 * self.vma20[d]), (self.vma5[d] >= 0.6 * self.vma20[d]),self.rsi[d].rsi<=40)#
                self.buysignal9[d] = bt.indicators.Highest(
                    bt.And(self.buysignal5[d]<=50, (self.vma5[d] < 1.2 * self.vma20[d]), (self.vma5[d] > 0.8 * self.vma20[d]), self.rsi[d].rsi>self.rsi[d].rsi(-1), self.rsi[d].rsi>self.rsi[d].rsi(-2), self.buysignal3[d] > -0.02 * d.close, self.buysignal4[d] < 0.02 * d.close, self.buysignal4[d] >= self.buysignal4[d](-11), self.crossovermacd[d] == 1),
                    period=1)

                self.buysignal26[d] = bt.indicators.Highest(
                    bt.And(bt.talib.CDLMORNINGSTAR(d.open, d.high, d.low, d.close)),
                    period=1)
                self.buysignal27[d] = bt.indicators.Highest(
                    bt.And(bt.talib.CDLSHOOTINGSTAR(d.open, d.high, d.low, d.close)),
                    period=1)
                self.buysignal28[d] = bt.indicators.Highest(
                    bt.And(bt.talib.CDLINVERTEDHAMMER(d.open, d.high, d.low, d.close)),
                    period=1)
                self.buysignal29[d] = bt.indicators.Highest(
                    bt.And(bt.talib.CDLHAMMER(d.open, d.high, d.low, d.close)),
                    period=5)
                self.buysignal30[d] = bt.And(self.buysignal29[d], (self.vma5[d] <= 1.2 * self.vma20[d]),
                                             (self.vma5[d] >= 0.6 * self.vma20[d]),
                                             self.rsi[d].rsi(-1) < self.rsi[d].rsi, self.rsi[d].rsi <= 35,
                                             self.buysignal6[
                                                 d] <= 70)

                #bt.And(self.buysignal14[d],self.buysignal9[d]), ,bt.And(self.buysignal9[d],self.buysignal22[d]==1)bt.And(self.buysignal14[d],self.buysignal23[d]==0
                #self.buysignal[d] = bt.And(self.buysignal9[d], bt.Or(bt.indicators.Highest(bt.And(self.buysignal7[d],self.buysignal8[d], self.buysignal10[d], self.buysignal11[d]),period=3),bt.And(self.buysignal12[d],self.buysignal8[d]))) #bt.And(self.buysignal14[d],self.buysignal23[d]!=self.buysignal22[d])#bt.Or(bt.And(bt.Or(self.buysignal14[d],bt.And(self.buysignal9[d], bt.Or(bt.indicators.Highest(bt.And(self.buysignal7[d],self.buysignal8[d], self.buysignal10[d], self.buysignal11[d]),period=3),bt.And(self.buysignal12[d],self.buysignal8[d])))), bt.Or(self.buysignal23[d]==0,self.buysignal22[d]==self.buysignal23[d])))#self.buysignal22[d]
                self.buysignal[d] = bt.And(self.buysignal14[d], self.buysignal22[d] != self.buysignal23[d])
                #self.buysignal[d] = bt.And(self.buysignal30[d], self.buysignal22[d] == 0)
                #self.buysignal[d] = bt.indicators.Highest(bt.And(bt.Or(self.buysignal14[d],self.buysignal9[d], self.buysignal22[d]),self.buysignal20[d]==0,self.buysignal21[d]==0), period=1)
#bt.And(self.buysignal14[d],self.buysignal9[d]),
            elif mystrategy == 5:
                self.buysignal1[d] = bt.ind.Lowest(d.close, period=20)
                self.buysignal2[d] = bt.ind.Lowest(d.close, period=40)
                self.buysignal3[d] = bt.ind.Lowest(d.close, period=80)
                self.buysignal4[d] = bt.ind.Lowest(d.close, period=120)
                self.buysignal5[d] = bt.ind.Lowest(d.close, period=160)
                self.buysignal6[d] = bt.ind.Highest(d.close, period=20)
                self.buysignal7[d] = bt.ind.Highest(d.close, period=40)
                self.buysignal8[d] = bt.ind.Highest(d.close, period=80)
                self.buysignal9[d] = bt.ind.Highest(d.close, period=120)
                self.buysignal10[d] = bt.ind.Highest(d.close, period=160)
                self.buysignal11[d] = bt.ind.Highest(
                    bt.And(self.buysignal1[d] == self.buysignal2[d],
                           self.buysignal2[d] == self.buysignal3[d],
                           self.buysignal3[d] == self.buysignal4[d],
                           self.buysignal4[d] == self.buysignal5[d]), period=20)

                self.buysignal12[d] = bt.ind.Highest(
                    bt.And(self.buysignal6[d] == self.buysignal7[d],
                           bt.Or(self.buysignal7[d] == self.buysignal9[d],
                                 self.buysignal8[d] == self.buysignal10[d])
                           ), period=5)
                self.buysignal13[d] = bt.ind.Highest(
                    bt.And(self.buysignal6[d] == self.buysignal7[d],
                          self.buysignal7[d] == self.buysignal8[d]), period=5)
                self.buysignal14[d] = bt.indicators.Highest(
                    bt.And(bt.talib.CDLMORNINGSTAR(d.open, d.high, d.low, d.close), (self.vma5[d] < 1.2 * self.vma20[d]), (self.vma5[d] > 0.8 * self.vma20[d])), period=5)
                self.buysignal17[d] = bt.indicators.Lowest(self.rsi[d].rsi, period=20, plot=False)
                self.buysignal15[d] = bt.ind.Highest(bt.And(self.buysignal13[d](-1) == 0, self.buysignal13[d]), period=5)


                #self.buysignal[d] = bt.ind.Highest(bt.And(self.buysignal11[d]==0, self.buysignal12[d], self.rsi[d].rsi<=40, self.buysignal14[d]))
                self.buysignal[d] = bt.ind.Highest(bt.And(bt.ind.Highest(bt.And(self.buysignal12[d]==1)), bt.Or(self.buysignal15[d],self.buysignal14[d])))#self.rsi[d].rsi >= 40,self.rsi[d].rsi <= 60, self.rsi[d].rsi>self.rsi[d].rsi(-1),self.macd[d].macd>self.macd[d].macd(-1))))#bt.Or(bt.And(self.buysignal11[d]!=self.buysignal12[d],self.buysignal14[d]),


            elif mystrategy == 6:
                self.buysignal1[d] = bt.ind.DownDay(d.close, period=20, plot=False)
                self.buysignal2[d] = bt.ind.DownDay(d.close, period=40, plot=False)
                self.buysignal3[d] = bt.ind.DownDay(d.close, period=80, plot=False)
                self.buysignal4[d] = bt.ind.DownDay(d.close, period=160, plot=False)
                #self.buysignal5[d] = bt.ind.DownDay(d.close, period=320, plot=False)
                self.buysignal6[d] = bt.ind.UpDay(d.close, period=20, plot=False)
                self.buysignal7[d] = bt.ind.UpDay(d.close, period=40, plot=False)
                self.buysignal8[d] = bt.ind.UpDay(d.close, period=80, plot=False)
                self.buysignal9[d] = bt.ind.UpDay(d.close, period=160, plot=False)
                #self.buysignal10[d] = bt.ind.UpDay(d.close, period=320, plot=False)

                # self.buysignal11[d] = bt.And(bt.indicators.Lowest(d.low > self.bollbot[d], period=5),
                #                              d.close > self.bollbot[d])
                self.buysignal11[d] = bt.ind.Highest((bt.ind.Highest(self.buysignal1[d]) + d.close), period=11, plot=False)
                self.buysignal16[d] = bt.ind.Lowest(d.close - (bt.ind.Highest(self.buysignal6[d])), period=11, plot=False)
                self.buysignal12[d] = bt.ind.Highest((bt.ind.Highest(self.buysignal2[d]) + d.close), period=22, plot=False)
                self.buysignal17[d] = bt.ind.Lowest(d.close - (bt.ind.Highest(self.buysignal7[d])), period=22, plot=False)
                self.buysignal13[d] = bt.ind.Highest((bt.ind.Highest(self.buysignal3[d]) + d.close), period=44, plot=False)
                self.buysignal18[d] = bt.ind.Lowest(d.close - (bt.ind.Highest(self.buysignal8[d])), period=44, plot=False)
                self.buysignal14[d] = bt.ind.Highest((bt.ind.Highest(self.buysignal4[d]) + d.close), period=88, plot=False)
                self.buysignal19[d] = bt.ind.Lowest(d.close - (bt.ind.Highest(self.buysignal9[d])), period=88, plot=False)
                #self.buysignal15[d] = bt.ind.Highest((bt.ind.Highest(self.buysignal5[d]) + d.close), period=160, plot=False)
                #self.buysignal20[d] = bt.ind.Lowest(d.close - (bt.ind.Highest(self.buysignal10[d])), period=160, plot=False)

                self.buysignal21[d] = bt.ind.Highest(d.close > self.buysignal11[d] * 0.98, period=11, plot=True)
                self.buysignal22[d] = bt.ind.Highest(d.close < self.buysignal16[d] * 1.02,d.close > self.buysignal16[d]* 1.002, period=11)
                self.buysignal23[d] = bt.ind.Highest(d.close > self.buysignal12[d] * 0.98, period=22, plot=True)
                self.buysignal24[d] = bt.ind.Highest(d.close < self.buysignal17[d] * 1.02,d.close > self.buysignal17[d]* 1.002, period=22)
                self.buysignal25[d] = bt.ind.Highest(d.close > self.buysignal13[d] * 0.98, plot=False)
                self.buysignal26[d] = bt.ind.Highest(d.close < self.buysignal18[d] * 1.05,d.close > self.buysignal18[d]* 1.01, period=44)
                self.buysignal27[d] = bt.ind.Highest(d.close > self.buysignal14[d] * 0.98, plot=False)
                self.buysignal28[d] = bt.ind.Highest(d.close < self.buysignal19[d] * 1.05,d.close > self.buysignal19[d]* 1.01, period=88)
                #self.buysignal29[d] = bt.ind.Highest(d.close > self.buysignal15[d] * 0.98, plot=False)
                #self.buysignal30[d] = bt.ind.Highest(d.close < self.buysignal20[d] * 1.05,d.close > self.buysignal20[d]* 1.01, period=10)

                self.buysignal15[d] = bt.ind.Lowest(d.close, period=80)
                self.buysignal20[d] = bt.ind.Lowest(d.close, period=40)
                self.buysignal29[d] = bt.ind.Lowest(d.close, period=20)
                self.buysignal32[d] = bt.ind.Highest(
                    bt.Or(self.buysignal15[d] == self.buysignal20[d], self.buysignal20[d] == self.buysignal29[d],
                          self.buysignal15[d] == self.buysignal29[d]), period=3)

                self.buysignal31[d] = bt.ind.DownDayBool(d.close, period=144, plot=True)
                #self.buysignal32[d] = bt.ind.DownDayBool(d.close, period=72, plot=True)

                self.buysignal30[d] = bt.ind.Highest(bt.And(self.buysignal23[d](-1)==0,self.buysignal23[d],self.buysignal21[d]==0,self.buysignal22[d]), period=1)
                self.buysignal33[d] = bt.ind.Highest(bt.Or(self.buysignal32[d]),period=3)
                self.buysignal34[d] = bt.ind.CrossOver(self.sma5[d], self.sma10[d])
                self.buysignal35[d] = bt.ind.Highest(bt.And(self.buysignal21[d](-1)==0,self.buysignal21[d],self.buysignal23[d],self.buysignal22[d]), period=1)#,self.buysignal26[d]
                self.buysignal36[d] = bt.ind.Highest(bt.Or(bt.And(self.buysignal32[d]==0)), period=5)#,bt.And(self.buysignal33[d]==1,self.rsi[d].rsi>=70) ,self.rsi[d].rsi<=40
                self.buysignal37[d] = bt.ind.Highest(bt.And(self.buysignal36[d], self.buysignal35[d]),
                                                     period=1)#self.buysignal36[d], bt.Or(bt.And(self.buysignal30[d],
                # self.buysignal[d] = bt.ind.Highest(bt.And(self.buysignal11[d]==0, self.buysignal12[d], self.rsi[d].rsi<=40, self.buysignal14[d]))
                self.buysignal[d] = self.buysignal37[d]#bt.And(self.buysignal32[d]==0,bt.Or(self.buysignal34[d],self.buysignal36[d]))#bt.And(self.buysignal32[d]==0,bt.Or(self.buysignal36[d],self.buysignal33[d],self.buysignal34[d]))#,self.buysignal26[d],self.buysignal28[d],self.buysignal30[d])#bt.Or(bt.And((self.buysignal1[d]+self.buysignal2[d]+self.buysignal3[d])>d.close*0.3))#,(self.buysignal1[d]+self.buysignal2[d]+self.buysignal3[d]+self.buysignal4[d]+self.buysignal5[d])>d.close*2.1)
            elif mystrategy == 7:
                self.buysignal1[d] = bt.ind.CrossUp(d.close, self.sma90[d], plot=False)
                self.buysignal2[d] = bt.ind.CrossUp(d.close, self.sma144[d], plot=False)
                self.buysignal3[d] = bt.ind.CrossUp(self.sma144[d], self.sma169[d], plot=False)

                self.buysignal4[d] = bt.ind.Highest(d.close<=self.sma250[d], period=20, plot=False)
                self.buysignal5[d] = bt.And(bt.ind.Highest(self.buysignal2[d], period=40, plot=False),self.buysignal3[d])

                self.buysignal6[d] = bt.And(self.buysignal1[d],self.sma144[d]<self.sma169[d],self.sma169[d]<self.sma250[d])
                self.buysignal7[d] = bt.And(bt.ind.Highest(self.buysignal6[d], period=40),self.buysignal2[d],self.sma144[d]<self.sma169[d],self.sma169[d]<self.sma250[d])

                self.buysignal8[d] = bt.ind.CrossUp(self.sma10[d], self.sma20[d], plot=False)
                self.buysignal9[d] = bt.And(bt.ind.Highest(self.buysignal7[d], period=20), self.buysignal8[d])

                self.buysignal30[d] = bt.ind.Lowest(d.close, period=80, plot=False)
                self.buysignal31[d] = bt.ind.Lowest(d.close, period=40, plot=False)
                self.buysignal32[d] = bt.ind.Lowest(d.close, period=20, plot=False)
                self.buysignal33[d] = bt.ind.Highest(
                    bt.Or(self.buysignal30[d] == self.buysignal31[d], self.buysignal31[d] == self.buysignal32[d],
                          self.buysignal30[d] == self.buysignal32[d]), period=3, plot=False)
                self.buysignal[d] = self.buysignal9[d]
                #bt.And(self.buysignal33[d]==0,self.buysignal3[d])
            elif mystrategy == 8:
                self.buysignal1[d] = bt.ind.CrossDown(d.close, self.sma144[d])
                self.buysignal2[d] = bt.ind.CrossDown(d.close, self.sma169[d])
                self.buysignal3[d] = bt.ind.CrossDown(d.close, self.sma250[d])
                self.buysignal4[d] = self.rsi[d].rsi <= 40
                self.buysignal5[d] = bt.ind.Highest(self.buysignal1[d], period=5)
                self.buysignal6[d] = bt.ind.Highest(self.buysignal2[d], period=10)
                self.buysignal7[d] = bt.ind.Highest(self.buysignal3[d], period=10)
                self.buysignal8[d] = bt.ind.Highest(self.buysignal4[d], period=5)

                self.buysignal11[d] = bt.ind.CrossUp(self.sma90[d], self.sma144[d])
                self.buysignal12[d] = bt.ind.CrossUp(self.sma144[d], self.sma169[d])
                self.buysignal13[d] = bt.ind.CrossUp(self.sma169[d], self.sma250[d])
                self.buysignal15[d] = bt.ind.Highest(self.buysignal11[d], period=30)
                self.buysignal16[d] = bt.ind.Highest(self.buysignal12[d], period=30)
                self.buysignal17[d] = bt.ind.Highest(self.buysignal13[d], period=30)

                self.buysignal21[d] = bt.ind.Lowest(d.close, period=250)
                self.buysignal22[d] = bt.ind.Highest(d.close, period=250)
                self.buysignal23[d] = bt.ind.Lowest(
                    bt.And(d.close <= ((self.buysignal22[d] - self.buysignal21[d]) * 0.618 + self.buysignal21[d])),
                    period=5)
                self.buysignal24[d] = bt.ind.Lowest(
                    bt.And(d.close <= ((self.buysignal22[d] - self.buysignal21[d]) * 0.382 + self.buysignal21[d])),
                    period=5)

                # self.buysignal25[d] = bt.ind.Lowest(
                #     bt.And(self.sma169[d]>=self.sma250[d],self.sma144[d]>=self.sma169[d],self.sma90[d]>=self.sma144[d]),
                #     period=10)
                self.buysignal26[d] = bt.indicators.Highest(
                    bt.And(bt.talib.CDLMORNINGSTAR(d.open, d.high, d.low, d.close)),
                    period=5)  # self.buysignal5[d] <= 50, self.buysignal6[d] <= 70,,self.macd[d].macd < d.close*0.02
                self.buysignal27[d] = bt.indicators.Highest(
                    bt.And(bt.talib.CDLSHOOTINGSTAR(d.open, d.high, d.low, d.close)),
                    period=1)
                self.buysignal28[d] = bt.indicators.Highest(
                    bt.And(bt.talib.CDLINVERTEDHAMMER(d.open, d.high, d.low, d.close)),
                    period=5)
                self.buysignal29[d] = bt.indicators.Highest(
                    bt.And(bt.talib.CDLHAMMER(d.open, d.high, d.low, d.close)),
                    period=5)
                self.buysignal30[d] = bt.indicators.Highest(bt.And(self.buysignal28[d] != self.buysignal29[d]))
                self.buysignal31[d] = bt.indicators.Highest(bt.And(self.buysignal28[d] == self.buysignal29[d]))
                # self.buysignal27[d] = bt.indicators.Lowest(
                #     bt.And(d.close<self.sma90[d]*1.03,d.close>self.sma90[d]*0.97),
                #     period=5)

                self.buysignal32[d] = bt.ind.Highest(
                    bt.Or(bt.And(self.buysignal23[d](-1) == 1, self.buysignal23[d] == 0)),
                    period=10)
                self.buysignal33[d] = bt.ind.Highest(
                    bt.Or(bt.And(self.buysignal24[d](-1) == 1, self.buysignal24[d] == 0)),
                    period=10)
                #self.buysignal[d] = bt.And(self.buysignal15[d],self.buysignal5[d]==0,self.buysignal23[d]==0)
                # self.buysignal[d] = bt.And(bt.Or(bt.And(self.buysignal23[d]),bt.And(self.buysignal24[d](-1)==1,self.buysignal24[d]==0)),self.buysignal25[d])
                #self.buysignal[d] = bt.And(self.buysignal23[d]==0,self.buysignal24[d]==0,self.buysignal26[d])
                self.buysignal[d] = bt.And((self.vma5[d] <= 1.2 * self.vma20[d]), (self.vma5[d] >= 0.6 * self.vma20[d]),self.buysignal32[d]==1,self.buysignal33[d]==1)

            self.sellsignal1[d] = bt.ind.Highest(d.close, period=20, plot=False)
            self.sellsignal2[d] = bt.ind.Highest(d.close, period=40, plot=False)
            self.sellsignal3[d] = bt.ind.Highest(d.close, period=80, plot=False)
            self.sellsignal4[d] = bt.ind.Highest(d.close, period=120, plot=False)
            self.sellsignal5[d] = bt.ind.Highest(d.close, period=160, plot=False)
            self.sellsignal6[d] = bt.indicators.Highest(self.rsi[d].rsi, period=10, plot=False)

            self.sellsignal7[d] = bt.indicators.Highest(bt.And(self.sellsignal1[d] == self.sellsignal2[d], self.sellsignal6[d] >= 65), period=1)
            self.sellsignal8[d] = bt.And(self.sellsignal7[d](-1) == 1, self.sellsignal7[d]==0)
            self.sellsignal9[d] = bt.indicators.Highest(
                bt.And(bt.talib.CDLSHOOTINGSTAR(d.open, d.high, d.low, d.close)),
                period=1)

            # self.sellsignal[d] = bt.And(bt.indicators.Highest(
            #     self.sellsignal5[d], period=20, plot=False),
            #     self.sellsignal7[d])

        # elif mystrategy == 5:


        # for data in self.datas:
        #     self.rvi = RVI()
        #     self.mas5[data.name] = bt.indicators.MovingAverageSimple(data[0].close, period=5)
        #     self.sma10 = bt.indicators.MovingAverageSimple(self.datas[0].close, period=10)
        #     # self.sma20 = bt.indicators.MovingAverageSimple(self.datas[0], period=20)
        #     # self.sma60 = bt.indicators.MovingAverageSimple(self.datas[0], period=60)
        #     # self.sma120 = bt.indicators.MovingAverageSimple(self.datas[0], period=120)
        #     self.vma5 = bt.indicators.MovingAverageSimple(self.datas[0].volume, period=5)
        #     self.vma20 = bt.indicators.MovingAverageSimple(self.datas[0].volume, period=20)
        #
        #     # bt.ind.MACD(self.data)
        #     self.macd = bt.indicators.MACD(self.data)
        #     self.rsi = bt.indicators.RSI(self.data, period=14)
        #     # bt.indicators.BBands(self.data)
        #
        #     self.dataclose=self.datas[0].close
        #
        #     self.crossover_510 = bt.indicators.CrossOver(self.sma5, self.sma10, plot = False)
        #     self.crossovermacd = bt.indicators.CrossOver(self.macd.macd, self.macd.signal, plot = False)
        #
        #
        #     self.buysignal = bt.And(self.rsi.rsi <= 35, (self.vma5 >= 0.8 * self.vma20))
        #
        #     #self.buysignal2 = bt.And(self.rsi.rsi <= 20, self.macd.macd >= self.macd.signal*1.5)
        #
        #     self.buysignal2 = bt.And(self.crossovermacd==1, self.rsi.rsi <= 55, self.rvi.rvi1<=self.rvi.rvi+10)
        #
        #     self.buysignal1 = bt.Or(self.buysignal,self.buysignal(-1),self.buysignal(-2),self.buysignal(-3),self.buysignal(-4),self.buysignal(-5),self.buysignal(-6))
        #
        #     self.buysignal3 = bt.And(self.buysignal1, self.buysignal2)
        #
        #     bt.LinePlotterIndicator(self.buysignal, name='buysignal')
        #     bt.LinePlotterIndicator(self.buysignal2, name='buysignal2')
        #     bt.LinePlotterIndicator(self.buysignal3, name='buysignal3')
        #     self.sellsignal = bt.And(self.macd.macd >= 0, self.crossovermacd == -1, self.rsi.rsi >= 50)
        #     #self.sellsignal3 = bt.And(self.rsi.rsi <= 40, self.crossovermacd == -1, (self.vma5 >= 1.2 * self.vma20))
        #     self.sellsignal2 = bt.And((self.vma5 >= 1.9 * self.vma20), self.rsi.rsi >= 55)
        #     self.sellsignal3 = bt.And((self.vma5 >= 1.6 * self.vma20), self.rsi.rsi >= 60)
        #     self.sellsignal4 = bt.And((self.vma5 >= 1.3 * self.vma20), self.rsi.rsi >= 65)
        #     # self.buysignal10 = bt.ind.CrossOver(self.sma10, self.sma20)
        #     # self.buysignal20 = bt.ind.CrossOver(self.sma20, self.sma60)
        #     # self.buysignal60 = bt.ind.CrossOver(self.sma60, self.sma120)
        #
        #     # self.macdhist = bt.ind.MACDHisto(self.datas[0],
        #     #                                  period_me1=self.p.p1,
        #     #                                  period_me2=self.p.p2,
        #     #                                  period_signal=self.p.p3)



    # def notify_order(self, order):
    #     if order.status in [order.Submitted, order.Accepted]:
    #         # Buy/Sell order submitted/accepted to/by broker - Nothing to do
    #         return
    #
    #     # Check if an order has been completed
    #     # Attention: broker could reject order if not enough cash
    #     if order.status in [order.Completed]:
    #         if order.isbuy():
    #             self.log(
    #                 'BUY EXECUTED, Price: {:.2f}, Cost: {:.2f}, Comm {:.2f}'.format(
    #                     order.executed.price,
    #                     order.executed.value,
    #                     order.executed.comm))
    #
    #             self.buyprice = order.executed.price
    #             self.buycomm = order.executed.comm
    #         else:  # Sell
    #             self.log('SELL EXECUTED, Price: {:.2f}, Cost: {:.2f}, Comm {:.2f}'.format(
    #                 order.executed.price,
    #                 order.executed.value,
    #                 order.executed.comm))
    #
    #         self.bar_executed = len(self)
    #
    #     elif order.status in [order.Canceled, order.Margin, order.Rejected]:
    #         self.log('Order Canceled/Margin/Rejected')
    #
    #     self.order = None
    # def notify_trade(self, trade):
    #     if not trade.isclosed:
    #         return
    #
    #     self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
    #              (trade.pnl, trade.pnlcomm))


    # 记录交易执行情况（可省略，默认不输出结果）
    def notify_order(self, order):
        # 如果order为submitted/accepted,返回空
        if order.status in [order.Submitted, order.Accepted]:
            return
        # 如果order为buy/sell executed,报告价格结果
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'买入: 价格:{order.executed.price:.2f}, 成本:{order.executed.value:.2f}, 手续费:{order.executed.comm:.2f}')
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:
                self.log(f'卖出: 价格：{order.executed.price:.2f}, 成本: {order.executed.value:.2f}, 手续费{order.executed.comm:.2f}')
            self.bar_executed = len(self)
            # 如果指令取消/交易失败, 报告结果
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('交易失败')
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log(f'策略收益：毛收益 {trade.pnl:.2f}, 净收益 {trade.pnlcomm:.2f}')



    def next(self):
        # rate_list = []
        # for data in self.datas:
        #     if len(data) > self.p.look_back_days:
        #         p0 = data.close[0]
        #         pn = data.close[-self.p.look_back_days]
        #         rate = (p0 - pn) / pn
        #         rate_list.append([data._name, rate])
        # long_list=[]
        # sorted_rate=sorted(rate_list,key=lambda x:x[1],reverse=True)
        # long_list=[i[0] for i in sorted_rate[:10]]
        # total_value = self.broker.getvalue()
        # p_value = total_value * 0.9 / 10


        for i, d in enumerate(self.datas):
            size_1 = math.floor((cerebro.broker.getvalue() * 0.075 / d.close[0])/100)*100#cerebro.broker.get_cash() * 0.25
            size_2 = math.floor((cerebro.broker.getvalue() * 0.1 / d.close[0])/100)*100#cerebro.broker.get_cash() * 0.1
            pos = self.getposition(d)
            if len(pos):  # 不在场内，则可以买入
                self.log('{}， {}, 持仓:{}, 成本价:{:.2f}, 当前价:{:.2f}, 价值:{:.2f}, 盈亏:{:.2f}'.format(
                    self.datas[0].datetime.date(0), d._name, pos.size, pos.price, pos.adjbase, pos.adjbase * pos.size, pos.size * (pos.adjbase - pos.price)))
                datalist = [self.datas[0].datetime.date(0) ,'持仓:{}, 成本价:{:.2f}, 当前价:{:.2f}, 价值:{:.2f}, 盈亏:{:.2f}'.format(
                    pos.size, pos.price, pos.adjbase, pos.adjbase * pos.size, pos.size * (pos.adjbase - pos.price))]
                #datalist = pd.DataFrame(columns = ['time', 'test'])

                outprint.loc['{}， {}'.format(self.datas[0].datetime.date(0), d._name)] = datalist


                # if self.sellsignal[d][0]:# or self.sellsignal2[d][0] or self.sellsignal3[d][0] or self.sellsignal4[d][0]:# or self.sellsignal6[d][0] or self.sellsignal7[d][0]:# or self.sellsignal5[d][0]:
                #     self.close(data = d)
                #     self.log('SELL：{:.6s}'.format(d._name))
                #     #break
                # elif (d.close[-1] >= 1.05 * pos.price or d.close[0] >= 1.08 * pos.price) and (self.macd[d].macd[0] < d.close[0]*0.02 and (self.macd[d].macd[0] < self.macd[d].macd[-1] and self.rsi[d].rsi[0] < self.rsi[d].rsi[-1])):
                #     self.close(data = d)
                #     self.log('SELL：{:.6s}'.format(d._name))
                # el
                # if d.high[0] >= 1.5 * pos.price:
                #     self.close(data=d)
                #     self.log('SELL：{:.6s}'.format(d._name))
                if d.close[0] >= yingli * pos.price and self.sellsignal8[d][0]:
                    self.close(data = d)
                    self.log('SELL：{:.6s}'.format(d._name))
                    datalist = [self.datas[0].datetime.date(0) ,'SELL：{:.6s}'.format(d._name)]
                    outprint.loc['{}， {}'.format(self.datas[0].datetime.date(0), d._name)] = datalist
                elif d.close[0] <= kuisun * pos.price:
                    self.close(data=d)
                    self.log('SELL：{:.6s}'.format(d._name))
                    datalist = [self.datas[0].datetime.date(0) ,'SELL：{:.6s}'.format(d._name)]
                    outprint.loc['{}， {}'.format(self.datas[0].datetime.date(0), d._name)] = datalist
                elif d.close[0] >= 1.15 * pos.price and self.sellsignal7[d][0] and self.sellsignal1[d]>d.high[0]:
                    self.close(data=d)
                    self.log('SELL：{:.6s}'.format(d._name))
                    datalist = [self.datas[0].datetime.date(0) ,'SELL：{:.6s}'.format(d._name)]
                    outprint.loc['{}， {}'.format(self.datas[0].datetime.date(0), d._name)] = datalist
                elif self.sellsignal9[d][0]:
                    self.close(data=d)
                    self.log('SELL：{:.6s}'.format(d._name))
                    datalist = [self.datas[0].datetime.date(0) ,'SELL：{:.6s}'.format(d._name)]
                    outprint.loc['{}， {}'.format(self.datas[0].datetime.date(0), d._name)] = datalist
                # if self.buysignal23[d]==0:
                #     self.close(data=d)
                #     self.log('SELL：{:.6s}'.format(d._name))
                elif self.buysignal[d][0] and pos.size<size_2*1.5 and (not self.buysignal[d][-1]) and (not self.buysignal[d][-2]) and (not self.buysignal[d][-3]):
                    self.buy(data=d,size=size_2)
                    self.log('BUY：{}, {}, 收盘价：{}'.format(d._name, size_2, pos.adjbase))
                    datalist = [self.datas[0].datetime.date(0) ,'BUY：{}, {}, 收盘价：{}'.format(d._name, size_2, pos.adjbase)]
                    outprint.loc['{}， {}'.format(self.datas[0].datetime.date(0), d._name)] = datalist
                #     #break

                #self.order = self.sell(data=d, size=1, exectype=bt.Order.StopTrail, trailpercent=0.2)

                # elif d.close[0] >= 1.5 * self.buyprice:
                #     self.close(data = d)
                #     break
            elif self.buysignal[d][0] and (not self.buysignal[d][-1]) and (not self.buysignal[d][-2]) and (not self.buysignal[d][-3]):
                self.buy(data=d,size=size_1)
                self.log('BUY：{}, {}, 收盘价：{}'.format(d._name, size_1, pos.adjbase))
                datalist = [self.datas[0].datetime.date(0) ,'BUY：{}, {}, 收盘价：{}'.format(d._name, size_2, pos.adjbase)]
                outprint.loc['{}， {}'.format(self.datas[0].datetime.date(0), d._name)] = datalist
        #print(outprint)
        # for i, d in enumerate(self.datas):
        #     dt, dn = self.datetime.date(), d._name
        # if not self.position:
        #     if self.rvi.rvi[0] >= up and self.rvi.rvi1[0] >= up:
        #         #if self.rvi.rvi[-1] <= up and self.rvi.rvi[-2] <= up:
        #             self.order = self.buy(size=size_1, exectype=bt.Order.StopTrail, trailpercent=0.11)

        # if self.rvi.rvi[-1] <= down:
        #     self.order = self.buy(size=size_1, exectype=bt.Order.StopTrail, trailpercent=0.11)
        # if self.position:
        #     if self.sellsignal[0] or self.sellsignal2[0] or self.sellsignal3[0] or self.sellsignal4[0]:
        #         self.order = self.sell()
        #     elif self.datas[0].close[0] >= 1.09*self.buyprice:
        #         self.order = self.sell()
        # if self.buysignal3[0]:
        #     self.order = self.buy(size=size_1)




def aquire_data(stock, start_date, end_date):
    df = ts.pro_bar(ts_code=stock,adj='qfq', start_date=start_date, end_date=end_date)
    dates = pd.to_datetime(df["trade_date"])
    print(df)
    df  = df[['open', 'high', 'low', 'close', 'vol']]#, 'pcfeedst_chg'
    df.columns = ['open', 'high', 'low', 'close', 'volume']#, 'pct_chg'
    df.index = dates
    df.sort_index(ascending=True, inplace=True)
    return df

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #from data.tushare import config
    import tushare as ts
    token = '3b732609d7546245122611a67e2f26bd783a009fc55112bd692af80a'
    ts.set_token(token)
    curdate = datetime.datetime.now().strftime('%Y%m%d')
    startdate = time.strftime('%Y%m%d', time.localtime(time.mktime(time.strptime(curdate, "%Y%m%d"))-172800*365))

    #stock = '000558.SZ'
    start_date = startdate
    end_date = curdate
    stock_list = ['600571.SH', '000932.SZ', '000987.SZ', '600475.SH', '002594.SZ', '002024.SZ', '601633.SH', '600436.SH', '600735.SH',
                  '600887.SH', '600585.SH', '601088.SH', '601336.SH', '600050.SH', '600010.SH', '601919.SH', '601788.SH', '600150.SH',
                  '601318.SH', '600703.SH', '601668.SH', '600466.SH', '600567.SH', '603000.SH', '603799.SH', '600655.SH', '600795.SH', '002475.SZ',
                  '600546.SH', '600970.SH', '601966.SH', '603816.SH', '601233.SH', '600110.SH', '603658.SH', '600068.SH', '601021.SH', '601211.SH',
                  '600486.SH', '603868.SH', '600104.SH', '600547.SH', '600000.SH', '603288.SH', '600115.SH', '600900.SH', '600383.SH', '600030.SH',
                  '601766.SH', '601225.SH', '600111.SH', '600362.SH', '600009.SH', '603993.SH', '000825.SZ', '601117.SH', '601727.SH', '603260.SH',
                  '600352.SH', '601899.SH', '600854.SH', '600346.SH', '600011.SH', '002605.SZ', '000926.SZ', '002437.SZ', '601127.SH', '600726.SH', '000721.SZ', '002123.SZ', '600515.SH', '600570.SH', '600406.SH', '601601.SH']
    flagqx = 1
    #
    # stock_list = ['600546.SH', '600406.SH', '600703.SH', '601601.SH', '601088.SH', '600735.SH', #'603501.SH', '601066.SH', '603986.SH', '601012.SH',
    #               '600585.SH', '600570.SH',]
    # flagqx = 1
    # # # # #
    # start_date = '20170101'
    # end_date = '20220101'
    # stock_list = ['002123.SZ']
    # flagqx = 0


    #df = aquire_data(stock, start_date, end_date)
    cerebro = bt.Cerebro()
    for s in stock_list:
        df = aquire_data(s, start_date, end_date)
        feed = bt.feeds.PandasData(dataname=df)
        cerebro.adddata(feed, name=s)
    # cerebro = bt.Cerebro()
    # data = bt.feeds.PandasData(dataname=df)
    # cerebro.adddata(data)

    cerebro.addstrategy(Strategy)
    cerebro.broker.setcash(1000000)
    cerebro.broker.setcommission(commission=0.003)
    cerebro.addsizer(bt.sizers.PercentSizer, percents=100)

    cerebro.addanalyzer(btanalyzers.SharpeRatio, _name = 'sharpe')
    cerebro.addanalyzer(btanalyzers.DrawDown, _name = 'drawdown')
    cerebro.addanalyzer(btanalyzers.Returns, _name='returns')
    cerebro.addanalyzer(btanalyzers.SQN, _name='sqn')
    cerebro.addanalyzer(bt.analyzers.PyFolio, _name='PyFolio')




    print(f'Starte Portfolio Value {cerebro.broker.getvalue()}')
    result = cerebro.run()

    #print(outprint)

    curtime = datetime.datetime.now().strftime('%Y%m%d%H%M')
    outprint['difftime'] = outprint.apply(lambda x: (int)((time.mktime(
        time.strptime(str(x['time']), "%Y-%m-%d")) - time.mktime(
        time.strptime(str(curtime), '%Y%m%d%H%M'))) / 172800), axis=1)
    outprint = outprint.loc[outprint["difftime"] >= -1]
    outprint = outprint[['text']]
    outprint_html = outprint.to_html
    ret = mail.mail(outprint_html,curtime,1)
    #print(outprint)

    print('----------------------------')
    print(f'End portfolio value {cerebro.broker.getvalue()}')
    print('----------------------------')
    print(f"Total Return:  {round(result[0].analyzers.returns.get_analysis()['rtot']*100, 2)}%")
    print(f"APR:           {round(result[0].analyzers.returns.get_analysis()['rnorm100'],2)}%")
    print(f"Max DrawDown:  {round(result[0].analyzers.drawdown.get_analysis()['max']['drawdown'],2)}%")
    print(f"Sharpe Ratio:  {round(result[0].analyzers.sharpe.get_analysis()['sharperatio'],2)}")

    #print(f"SQN:           {round(result[0].analyzers.sqn.get_analysis()['sqn'],2)}")
    #portfolio_stats = result[0].analyzers.getbyname('PyFolio')
    #returns, positions, transactions, gross_lev = portfolio_stats.get_pf_items()
    #returns.index = returns.index.tz_convert(None)

    #quantstats.reports.html(returns, output=f'results/123Result_3.html', title=f'123Analysis')
    #if flagqx==1:
    #    for d in cerebro.datas:
    #        d.plotinfo.plot = False
    #cerebro.plot()
