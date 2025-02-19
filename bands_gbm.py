import matplotlib.pyplot as mp
import numpy as np
import pandas as p
import pandas_datareader as pd
import random
import copy
import datetime as dt

def gbm():  
    info=pd.DataReader('aapl','yahoo','2021-01-01')
    initial_price=info['Close'][-1]
    returns=np.log(info['Adj Close']).diff().dropna()
    horizon=(info.index[-1]-info.index[1]).days
    n=horizon/365
    change=info['Close'][-1]-info['Close'][1]
    cagr=change ** (1/n) - 1
    mu=np.mean(returns)
    std=np.std(returns)
    T=252
    b=np.random.normal(0,1,T)
    long=mu-0.5*(np.var(returns))
    shock=copy.deepcopy(b)
    W=copy.deepcopy(b)
    sum=0
    for i in range(len(shock)):
        shock[i]=shock[i]*std
    final=[]
    final.append(initial_price)
    for i in range(1,T):
        final.append(final[i-1]*np.exp(long+shock[i]))
    return(final)
def getstrategy(ticker):
    df=pd.DataReader(ticker,'yahoo','2021-01-01')
    date=[]
    for i in df.index:
        date += [i]
    start = date[-1]
    time_series=[]
    index=0
    while(index<=252):
        start+=dt.timedelta(days=1)
        if(start.isoweekday()<=5):
            time_series+=[start]
            index+=1
    date = []
    sum=[]
    price=[]
    for i in range(5):
        a=gbm()
        n=len(a)
        price+=a
    index=0
    fin=[]
    for j in range(n):
        sum=0
        for i in range(5):
            sum+=price[index+n]
        fin+=[sum/5]
        index+=1
    fin=p.DataFrame(fin)
    print(fin)
    print(fin[0][1])
    sm=fin.rolling(20).mean()
    std=fin.rolling(20).std()
    b1=sm  + (2*std)
    b2=sm - (2*(std))
    buy=[]
    buy_index=[]
    sell=[]
    sell_index=[]
    for i in fin.index:
        if(fin[0][i]>=b1[0][i]):
            sell+=[fin[0][i]]
            sell_index+=[i]
        if(fin[0][i]<=b2[0][i]):
            buy+=[fin[0][i]]
            buy_index+=[i]
    d=pd.DataReader('aapl','yahoo','2021-01-01')
    date=[]
    for i in d.index:
        date+=[i]
    mp.xlabel('Time')
    mp.ylabel('Price')
    mp.plot(fin,c='c')
    mp.plot(b1,c='cyan')
    mp.plot(b2,c='lightsalmon')
    mp.scatter(sell_index,sell,s=35,c='r',marker='v',label="Sell Time")
    mp.scatter(buy_index,buy,s=35,c='g',marker='^',label="Buy Time")
    trading_strategy=dict()
    for i in buy_index:
        print(trading_strategy,"here")
        trading_strategy[i]="Buy"
    for j in sell_index:
        trading_strategy[j]="Sell"
    final_trading_strategy=dict()
    order=sorted(trading_strategy.keys())
    for i in order:
        final_trading_strategy[i]=trading_strategy[i]
    strat=""
    for i in final_trading_strategy:
        day=time_series[i]
        decision=final_trading_strategy[i]
        strat=f"{decision} on {day} \n"+strat
    return strat
