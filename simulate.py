import matplotlib.pyplot as mp
import pandas as p
import pandas_datareader as pd
from brownianmotion import geometricBrownianMotion as gb
def simulation(ticker,app):
    if(ticker==None):
            app.message = 'Nothing entered!'
    else:
        sum1=[]
        sum_x=[]
        sum_y=[]
        xy=[]
        x_2=[]
        y_2=[]
        sum2=[]
        for i in range(20):
            a=gb(ticker)
            print(a)
            sum_x.append(sum(a))
            sum_y.append(31878)
            xy.extend(a[i]*i for i in range(len(a)))
            x_2.extend([a[i]*a[i] for i in range(len(a))])
            y_2.extend([i*i for i in range(len(a))])
            mp.plot(a)
            sum2.append(a[-1])
            n=len(y_2)
        sum_x=sum(sum_x)
        sum_y=sum(sum_y)
        xy=sum(xy)
        x_2=sum(x_2)
        y_2=sum(y_2)
        m=n*(xy)-(sum_x)*(sum_y)
        m=(m/((n)*(x_2)-(sum_x**2)))
        b=(sum_y-m*(sum_x))/n
        regression=[]
        for i in range(252):
            regression.append(m*i+a[0])
        mp.plot(regression,label=f"Regression line predicting the price of {ticker}")
        app.message="Forecasted Average: ",regression[-1]
        mp.xlabel('Time')
        mp.ylabel('Price')
        mp.legend()
        mp.title(f'Price of {ticker} stock 1 year from now.')
        app.message=f'Price Prediction: {regression[-1]}'
        app.message1=pd.DataReader(ticker,'yahoo','2012-01-01')['Close'][-1]
        mp.show()

def displaySimulate(app,canvas):
    size=(app.width+app.height)//30
    canvas.create_rectangle(0,0,app.width,app.height,fill="brown")
    canvas.create_rectangle(0,0,app.width/12,app.height/12,fill="gray1")
    canvas.create_text(app.width/20,app.height/21,text="Back",anchor='c',
        fill="white")
    canvas.create_rectangle(200,200,600,400,fill="black")
    canvas.create_text(400,300,
        text="            Path prediction using \n  Geometric Brownian Motion!",
        fill="white",anchor="c",font=f"Calligrapher {size//(2)} bold")
    canvas.create_rectangle(200,500,600,700,fill="black")
    m=f"Current Price: {app.message1}\n"+f"{app.message}"
    canvas.create_text(400,600,text=m,fill="white",anchor="c",
        font=f"Calligrapher {size//3} bold")