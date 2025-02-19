import pandas_datareader as pd
import pandas as p
import numpy as np
import copy
def geometricBrownianMotion(ticker):  
    info=pd.DataReader(ticker.lower(),'yahoo','2012-01-01')
    initial_price=info['Close'][-1]
    returns=np.log(info['Adj Close']).diff().dropna()
    horizon=(info.index[-1]-info.index[1]).days
    mu=np.mean(returns)
    std=np.std(returns)
    T=252
    b=np.random.normal(0,1,T)
    long=mu-0.5*(np.var(returns))
    shock=copy.deepcopy(b)
    W=copy.deepcopy(b)
    sum1=0
    for i in range(len(shock)):
        shock[i]=shock[i]*std
    final=[]
    final.append(initial_price)
    for i in range(1,T):
        final.append(final[i-1]*np.exp(long+shock[i]))
    return(final)