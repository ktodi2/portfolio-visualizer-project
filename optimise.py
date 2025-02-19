import numpy as np
import pandas_datareader as pd
import copy
import math
import pandas as p

def optimisePortfolio(app):
                portfolio=copy.deepcopy(app.info)
                a=dict()
                b=dict()
                info=pd.DataReader(portfolio,"yahoo",'2018-01-01')['Adj Close']
                for i in range(10000):
                    weight=np.random.random(app.n)
                    sum1=weight.sum()
                    for n in range(len(weight)):
                        weight[n]=weight[n]/sum1
                    s=sharpe(weight,portfolio,info)
                    a[i]=s
                    b[i]=weight
                best=0
                index=0
                for j in range(10000):
                    if(a[j]>best):
                        best=a[j]
                        index=j
                final=b[index]
                ind=0
                for k in app.info:
                    if(ind<len(final)):
                        app.ratio+= f" \n{k.upper()} : {final[ind]} "
                        ind+=1
                    else:
                        break

def sharpe(weights,portfolio,info):
    returns=info/info.shift()
    returns=np.sum((np.log(returns)*weights),axis=1)
    sr=((np.mean(returns))/np.std(returns))*math.sqrt(252)
    return sr