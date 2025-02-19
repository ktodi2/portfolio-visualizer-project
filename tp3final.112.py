from cmu_112_graphics import *
# from tp3 import checkPressed,drawLoader
from simulate import simulation,displaySimulate
from understand import portfolioHistoric,understandHome,bollinger
from sentimentanalysis import doSentimentAnalysis,graphicSentiment
from bands_gbm import getstrategy,strategyVisual
from elon import elonMode,elonVisual
from optimise import optimisePortfolio
"""
Image citation:-
app.image1=https://www.google.com/
url?sa=i&url=https%3A%2F%2Fwww.shacknews.com%2
Farticle%2F128278%2F2022- united-states-stock-market-holiday-calendar&psig=
AOvVaw0Mmfq9qt6- 
a\QHS5u4Ah6z&ust=1668501823631000&source=images&cd=vfe&ved=0CA8Q 
jhxqFwoTCOiFtOWjrfsCFQAAAAAd AAAAABAE]

app.image2=https://www.etsy.com/
uk/listing/264825202/landmark-ny-wall-street-bull


For brownian motion:-
Only understood the equations from this website:-
https://medium.com/the-quant-journey/
a-gentle-introduction-to-geometric-brownian-motion-in-finance-68c37ba6f828

Downloaded the elon musk tweets dataset from kaggle

Learnt about sharpe ratio from here:-
https://www.investopedia.com/terms/s/sharperatio.asp

"""
import random
import math
import copy
import numpy as np
import pandas as p
import pandas_datareader as pd
import matplotlib.pyplot as mp
from datetime import date
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
def appStarted(app):
    app.cx,app.cy=0,0
    app.image1 = app.loadImage('resize.final.jpg')
    app.image2 = app.loadImage('page2.jpg')
    app.image3= app.loadImage('fgh.jpg')
    app.cx1=1200
    app.click=0
    app.message=''
    app.message1=''
    app.message2=''
    app.message3=''
    app.strategy=''
    app.message4=''
    app.displayImage=""
    app.page=0
    app.optimiseStocks=[]
    app.key=''
    app.stock=''
    app.stocks1=[]
    app.elonview=''
    app.final=[]
    app.stocks=[]
    app.n=0
    app.weights=[]
    app.sentimentmessage=""
    app.info=[]
    app.count=0
    app.ratio=''
    app.l=''
    app.symbols= get_nasdaq_symbols()
    app.date=dict()
    app.date1=''
    app.quantity=dict()
    app.display=""
    app.qty=dict()
    app.value=dict()
    app.pl=0
    app.stockSimulate=''

    app.l=['MSFT','AAPL','GOOGL','TSLA','NKLA','AMZN','NVDA','META','NFLX','COST']
    for i in app.l:
        n=pd.DataReader(i,'yahoo','2022-12-02')['Close'][0]
        n=n.round(2)
        n= f" {i} : {n} | "
        app.display=app.display+f"{n}   "
    app.timerDelay=80

def timerFired(app):
    app.cx1-=10
    if(app.cx1 <=0):
        app.cx1 = app.width

def mousePressed(app,event):
    app.cx=event.x
    app.cy=event.y
    x1,y1,x2,y2=app.width/12,12/20*app.height,18/20*app.width,17/22*app.height
    if((app.cx>=x1 and app.cx<=x2) and (app.cy>=y1 and app.cy<=y2) and 
    app.page==0):
        app.page=1
    ba1,ba2,ba3,ba4=0,0,app.width/12,app.height/12
    if((app.cx>=ba1 and app.cx<=ba3) and (app.cy>=ba2 and app.cy<=ba4)):
         if(app.page<=3):
             app.page-=1
         else:
             app.page=2
             app.message3=''
             app.message=''
             app.message1=''
             app.message2=''
             app.message4=''
             app.sentimentmessage=""
             app.info=[]
             app.elonview=''

    b1,b2,b3,b4=5/80*app.width,72/80*app.height,35/80*app.width,79/80*app.height
    if((event.x>=b1 and event.x<=b3) and (event.y>=b2 and event.y<=b4) and 
    app.page==1):
            addStock(app)
    s1,s2=45/80*app.width,72/80*app.height
    s3,s4=75/80*app.width,79/80*app.height
    if((app.cx>=s1 and app.cx<=s3) and (app.cy>=s2 and app.cy<=s4) and 
    app.page==1):
            removeStock(app)  
    p1,p2,p3,p4=0,30,60,80
    if((app.cx>=p1 and app.cx<=p3) and (app.cy>=p2 and app.cy<=p4) and 
    app.page==1):
        app.page=0
    n1,n2,n3,n4=740,30,800,80
    if((app.cx>=n1 and app.cx<=n3) and (app.cy>=n2 and app.cy<=n4) and 
    app.page==1):
            app.page=2
    
    if(app.page>=2):
        x0,y0,x1,y1=app.width/8,app.height/10,17/40*app.width,9/40*app.height
        x2,y2,x3,y3=23/40*app.width,app.height/10,7/8*app.width,9/40*app.height
        x4,y4,x5,y5=app.width/8,13/40*app.height,17/40*app.width,9/20*app.height
        x6,y6,x7,y7=23/40*app.width,13/40*app.height,7/8*app.width,9/20*app.height
        x8,y8=app.width/8,11/20*app.height
        x9,y9=17/40*app.width,27/40*app.height
        x10,y10=23/40*app.width,11/20*app.height
        x11,y11=7/8*app.width,27/40*app.height
        # x12,y12=23/40*app.width,11/20*app.height
        # x13,y13=7/8*app.width,27/40*app.height

        t1,t2,t3,t4=23/40*app.width,31/40*app.height,7/8*app.width,9/10*app.height
        e1,e2,e3,e4=app.width/8,11/20*app.height,17/40*app.width,27/40*app.height
        if((app.cx>=x0 and app.cx<=x1) and (app.cy>=y0 and app.cy<=y1)):
            app.page=3
        if((app.cx>=x2 and app.cx<=x3) and (app.cy>=y2 and app.cy<=y3)):
            app.page=4
        if((app.cx>=x4 and app.cx<=x5) and (app.cy>=y4 and app.cy<=y5)):
            app.page=5
        if((app.cx>=x6 and app.cx<=x7) and (app.cy>=y6 and app.cy<=y7)):
            app.page=6
        if((app.cx>=x8 and app.cx<=x9) and (app.cy>=y8 and app.cy<=y9)):
            app.page=7
        if((app.cx>=x10 and app.cx<=x11) and (app.cy>=y10 and app.cy<=y11)):
            app.page=8
        # if((app.cx>=x12 and app.cx<=x13) and (app.cy>=y12 and app.cy<=y13)):
        #     app.page=9
        if((app.cx>=t1 and app.cx<=t3) and (app.cy>=t2 and app.cy<=t4)):
            app.page=14

        x14,y14=200,200
        x15,y15=600,400
        if((app.cx>=x14 and app.cx<=x15) and (app.cy>=y14 and app.cy<=y15) and 
            app.page==3):
            app.page=10
            app.stockSimulate=app.getUserInput('Enter the stock !')
            simulation(app.stockSimulate,app)
        x16,y16=3/16*app.width,3/20*app.height
        x17,y17=7/8*app.width,27/80*app.height
        if((app.cx>=x16 and app.cx<=x17) and (app.cy>=y16 and app.cy<=y17) and 
            app.page==5):
            app.date1=app.getUserInput(
            'Enter the date of portfolio investment in the format (y-mm-d)')
            if(app.date!=None):
                app.n=int(app.getUserInput(
                'Enter the number of stocks you invested in the entered date'))
                if(app.n!=None):
                    for i in range(app.n):
                        n1=app.getUserInput('Enter ticker name: ')
                        app.stocks1.append(n1)
                    for i in range(app.n):
                        i=float(app.getUserInput(
                        f'Enter percentage of {app.stocks1[i]}'))
                        app.weights.append(i)
                    app.value=float(app.getUserInput('Enter amount'))
                else:
                    app.message4='Invalid Input'
            else:
                app.message4='Invalid Input'
            portfolioHistoric(app)
        x20,y20=3/16*app.width,7/16*app.height
        x21,y21=7/8*app.width,6/10*app.height
        if((app.cx>=x20 and app.cx<=x21) and (app.cy>=y20 and app.cy<=y21) and 
            app.page==5):
            app.l=app.getUserInput('Enter the stock')
            bollinger(app)
        s1,s2,s3,s4=200,300,600,500
        if((app.cx>=s1 and app.cx<=s3) and (app.cy>=s2 and app.cy<=s4) and 
            app.page==4):
            for i in app.stocks:
                f=doSentimentAnalysis(i)
                app.sentimentmessage=f"{i}: {f}\n"+app.sentimentmessage
        tb1,tb2,tb3,tb4=200,150,600,350
        if((app.cx>=tb1 and app.cx<=tb3) and (app.cy>=tb2 and app.cy<=tb4) and 
            app.page==8):
            n=app.getUserInput("Enter the ticker: ")
            app.strategy,app.count=getstrategy(n)
        te1,te2,te3,te4=200,200,600,400
        if((app.cx>=te1 and app.cx<=te3) and (app.cy>=te2 and app.cy<=te4) and 
            app.page==7):
            n=app.getUserInput("Do you want to search for a stock or keyword?")
            if(n=='keyword'):
                s=app.getUserInput("Enter the keyword: ")
            else:
                s=app.getUserInput("Enter the ticker: ")
            app.elonview=elonMode(s,n)
        o1,o2,o3,o4=150,100,650,300
        if((app.cx>=o1 and app.cx<=o3) and (app.cy>=o2 and app.cy<=o4) and 
            app.page==6):
            app.n=int(app.getUserInput(
                'Enter the number of stocks you want to invest in: '))
            if(app.n!=None):
                for i in range(app.n):
                    s=app.getUserInput('Enter ticker name: ')
                    app.info.append(s)
            optimisePortfolio(app)

def addStock(app):
    n=app.getUserInput("Enter the ticker: ")
    date=app.getUserInput("Enter the date of investment(y-mm-dd)")
    quantity=int(app.getUserInput("How much did you buy?"))
    val=pd.DataReader(n,'yahoo',date)['Close'][0]*quantity
    if(n in app.stocks):
        app.value[n.upper()]+=val
        app.quantity[n.upper()]+=quantity
    if(n not in app.stocks):
        app.value[n.upper()]=val
        app.quantity[n.upper()]=quantity
        app.date[n.lower()]=date
        app.stocks.append(n)
    app.pl-=app.value[n.upper()]
    app.l.append(n)

def removeStock(app):
    n=app.getUserInput("Enter the ticker")
    quantity=int(app.getUserInput("How much do you wanna sell?"))
    k=pd.DataReader(n.upper(),'yahoo','2022-12-01')['Close'][-1]
    k=k*app.quantity[n.upper()]
    app.pl+=quantity*k
    if(quantity==app.quantity[n.upper()]):
        app.stocks.pop(app.stocks.index(n.upper()))
    elif(quantity<app.quantity[n.upper()]):
        p=app.value[n.upper()]/app.quantity[n.upper()]
        s=app.quantity[n.upper()]-quantity
        app.value[n.upper()]=p*s
        app.quantity[n.upper()]=s
    else:
        app.stocks.pop(app.stocks.index(n.upper()))

def redrawAll(app,canvas):
    homePage(app,canvas)
    if(app.page==1):
        portfolioMode(app,canvas)
    if(app.page>=2):
        indexPage(app,canvas)

def homePage(app,canvas):
    size=(app.width+app.height)//50
    canvas.create_image(400, 400, image=ImageTk.PhotoImage(app.image1))
    canvas.create_rectangle(app.width/12,12/20*app.height,18/20*app.width,
        17/20*app.height,fill="black")
    gapx=(18/20*app.width-app.width/9)/2
    gapy=(app.height-12/30*app.height)/2
    canvas.create_text((app.width/8+gapx),(12/30*app.height+gapy),
    text="Click to make the best trade \n       you will ever make!",
    fill="white", font=f"Calligrapher {size}")
    x1,y1=app.width/9,12/16*app.height
    x2,y2=18/20*app.width,17/18*app.height
def portfolioMode(app,canvas):
    size=(app.width+app.height)//40
    canvas.create_rectangle(0,0,800,800,fill="black")
    canvas.create_text(app.cx1,20,text=(app.display)*2,anchor="c",
    font=f"Calligrapher {size//3} bold",fill="crimson")

    canvas.create_rectangle(0,30,60,80,fill="white")
    canvas.create_text(30,55,text="Back",anchor='c',font= 
    f"Calligrapher {size//3} bold", fill="black")

    canvas.create_rectangle(740,30,800,80,fill="white")
    canvas.create_text(770,55,text="Next",anchor='c',font= 
    f"Calligrapher {size//3} bold", fill="black")

    canvas.create_rectangle(50,720,350,790,fill="green")
    canvas.create_text(200,750,text="ADD",anchor="c",
        font=f"Helvetica {int(size)} ")
    canvas.create_rectangle(450,720,750,790, fill="red")
    canvas.create_text(600,750,text="REMOVE",anchor="c",
        font=f"Helvetica {int(size)} ")
    canvas.create_text(400,85,text="YOUR PORTFOLIO",anchor="c",
        font=f"Copperplate {int((app.width+app.height)//42)}",fill="white")
    canvas.create_line(30,100,770,100,fill="white",width=3)
    a,b,c,d=30,135,770,135
    canvas.create_line(30,100,30,135,fill="white",width=3)
    canvas.create_text(115,119,text="Quantity",anchor="c",
    font=f"Copperplate {int((app.width+app.height)//72)} bold",fill="white")
    canvas.create_line(180,100,180,135,fill="white",width=2)
    canvas.create_line(a,b,c,d,fill="white",width=2)
    canvas.create_line(600,100,600,135,fill="white",width=2)
    canvas.create_text(390,119,text="Security Name",anchor="c",
    font=f"Copperplate {int((app.width+app.height)//72)} bold",fill="white")
    canvas.create_line(770,100,770,135,fill="white",width=2)
    canvas.create_text(685,119,text="Total Value",anchor="c",
    font=f"Copperplate {int((app.width+app.height)//72)} bold",fill="white")
    a,b,c,d=30,135,770,135
    for i in app.stocks:
            # canvas.create_line()
            canvas.create_text(380,b+17,text=f"""\
            {app.symbols['Security Name'][i.upper()]} ({i.upper()})""",
            anchor="c",font=f"Times {int((app.width+app.height)//95)} bold",
            fill="white")
            canvas.create_line(30,b,30,b+35,fill="white",width=3)
            canvas.create_text(115,
            b+17,text=f"{app.quantity[i.upper()]}",anchor="c",
            font=f"Times {int((app.width+app.height)//95)} bold",
            fill="white")
            canvas.create_line(180,b,180,b+35,fill="white",width=2)
            canvas.create_line(600,b,600,b+35,fill="white",width=2)
            canvas.create_text(685,
            b+17,text=f"{app.value[i.upper()].round(2)} $",
            anchor="c",font=f"Times {int((app.width+app.height)//95)} bold",
            fill="white")
            canvas.create_line(770,b,770,b+35,fill="white",width=3)
            b+=35
            d+=35
            canvas.create_line(a,b,c,d,fill="white",width=2)
    if(app.pl!=0):
        canvas.create_line(30,b,30,b+35,fill="white",width=3)
        canvas.create_line(770,b,770,b+35,fill="white",width=3)
        canvas.create_text(200,b+35-9,text=f"Total Cash Balance {app.pl}$",
            anchor="c",font=f"Times {int((app.width+app.height)//95)} bold",
            fill="white")
        canvas.create_line(30,b+35,770,b+35,fill="white")
def indexPage(app,canvas):
    size=(app.width+app.height)//40
    # canvas.create_rectangle(0,0,app.width,app.height,fill="blue")
    canvas.create_rectangle(0,0,app.width,app.height,fill="blue")
    canvas.create_image(400, 400, image=ImageTk.PhotoImage(app.image2))
    canvas.create_rectangle(0,0,app.width/12,app.height/12,fill="gray1")
    canvas.create_text(app.width/20,app.height/21,text="Back",anchor='c',
        fill="white")
    
    canvas.create_rectangle(app.width/8,app.height/10,17/40*app.width,
    9/40*app.height,fill="black")
    canvas.create_text(app.width/3.6,app.height/6.5,text="Simulate",anchor="c",
    font=f"Calligrapher {size//2} bold", fill="white")
    x0,y0,x1,y1=app.width/8,app.height/10,17/40*app.width,9/40*app.height

    canvas.create_rectangle(23/40*app.width,app.height/10,7/8*app.width,
    9/40*app.height,fill="black")
    canvas.create_text(23/32*app.width,app.height/6.5,
    text="Sentiment\n Analysis",anchor="c",font=f"Calligrapher {size//2} bold",
    fill="white")
    x2,y2,x3,y3=23/40*app.width,app.height/10,7/8*app.width,9/40*app.height

    canvas.create_rectangle(app.width/8,13/40*app.height,17/40*app.width,
    9/20*app.height,fill="black")
    canvas.create_text(app.width/3.6,app.height/2.65,text="Understand",
    anchor="c",
    font=f"Calligrapher {size//2} bold",fill="white")
    x4,y4,x5,y5=app.width/8,13/40*app.height,17/40*app.width,9/20*app.height

    canvas.create_rectangle(23/40*app.width,13/40*app.height,7/8*app.width,
    9/20*app.height,fill="black")
    canvas.create_text(23/32*app.width,app.height/2.65,text="Optimise",
    anchor="c",font=f"Calligrapher {size//2} bold",fill="white")
    x6,y6,x7,y7=23/40*app.width,13/40*app.height,7/8*app.width,9/20*app.height

    canvas.create_rectangle(app.width/8,11/20*app.height,17/40*app.width,
    27/40*app.height,fill="black")
    canvas.create_text(app.width/3.6,app.height/1.65,text="Elon Mode",
    anchor="c",font=f"Calligrapher {size//2} bold",fill="white")
    x8,y8,x9,y9=app.width/8,11/20*app.height,17/40*app.width,27/40*app.height

    canvas.create_rectangle(23/40*app.width,11/20*app.height,
    7/8*app.width,27/40*app.height,fill="black")
    canvas.create_text(23/32*app.width,app.height/1.65,text="Trading Strategy",
        anchor="c",font=f"Calligrapher {size//2} bold",fill="white")
    x10,y10=23/40*app.width,11/20*app.height
    x11,y11=7/8*app.width,27/40*app.height

    # canvas.create_rectangle(app.width/8,31/40*app.height,17/40*app.width,
    #     9/10*app.height,fill="black")
    # canvas.create_text(app.width/3.6,app.height/1.2,text="Market Maker",
    # anchor="c",font=f"Calligrapher {size//2} bold",fill="white")
    # x12,y12=7/20*app.width,31/40*app.height
    # x13,y13=13/20*app.width,9/10*app.height
    # canvas.create_rectangle(23/40*app.width,31/40*app.height,7/8*app.width,
    # 9/10*app.height,fill="black")
    # canvas.create_text(23/32*app.width,app.height/1.2,text="Trading Strategy",
    # anchor="c",font=f"Calligrapher {size//2} bold",fill="white")

    if(app.page==3 or app.page==10):
        displaySimulate(app,canvas)
    if(app.page==4):
        graphicSentiment(app,canvas)
    if(app.page==5 or app.page==11):
        understandHome(app,canvas)
    if(app.page==6):
        optimise(app,canvas)
    if(app.page==7):
        elonVisual(app,canvas)
    if(app.page==8):
        strategyVisual(app,canvas)
    # if(app.page==9):
    #     marketmaker(app,canvas)
    # if(app.page==14):
    #     strategyVisual(app,canvas)

def sentimentAnalysis(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="yellow")
    canvas.create_rectangle(0,0,app.width/12,app.height/12,fill="gray1")
    canvas.create_text(app.width/20,app.height/21,text="Back",anchor='c',
        fill="white")
def marketmaker(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="blue")
    canvas.create_rectangle(0,0,app.width/12,app.height/12,fill="gray1")
    canvas.create_text(app.width/20,app.height/21,text="Back",anchor='c',
        fill="white")
def optimise(app,canvas):
    size=(app.width+app.height)//30
    canvas.create_rectangle(0,0,app.width,app.height,fill="white")
    canvas.create_rectangle(0,0,app.width/12,app.height/12,fill="gray1")
    canvas.create_text(app.width/20,app.height/21,text="Back",anchor='c',
        fill="white")
    canvas.create_rectangle(150,100,650,300,fill="black")
    canvas.create_text(400,200,
        text=" Click to Optimise Portfolio!",
        fill="white",anchor="c",font=f"Calligrapher {size//2} bold")
    canvas.create_rectangle(150,500,650,700,fill="black")
    canvas.create_text(400,600,text=app.ratio,fill="blue",
        anchor="c",
        font=f"Calligrapher {size//2} bold")

def MuskMode(app,canvas):
    size=(app.width+app.height)//30
    # canvas.create_rectangle(0,0,app.width,app.height,fill="purple")
    canvas.create_image(400, 400, image=ImageTk.PhotoImage(app.image3))
    canvas.create_rectangle(0,0,app.width/12,app.height/12,fill="gray1")
    canvas.create_text(app.width/20,app.height/21,text="Back",anchor='c',
        fill="white")
    canvas.create_rectangle(200,200,600,400,fill="black")
    canvas.create_text(400,300,
    text="Click to learn what Elon thinks!",fill="white",
    anchor="c",font=f"Calligrapher {size//2} bold")
    canvas.create_rectangle(200,500,600,700,fill="black")
    canvas.create_text(400,600,text=app.elonview,fill="white",
    anchor="c",font=f"Calligrapher {size//2} bold")

def companyInfo(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="red")
    canvas.create_rectangle(0,0,app.width/12,app.height/12,fill="gray1")
    canvas.create_text(app.width/20,app.height/21,text="Back",anchor='c',
        fill="white")
    
def understand(app,canvas):
    size=(app.width+app.height)//30
    canvas.create_rectangle(0,0,app.width,app.height,fill="orange")
    canvas.create_rectangle(0,0,app.width/12,app.height/12,fill="gray1")
    canvas.create_text(app.width/20,app.height/21,text="Back",anchor='c',
        fill="white")
    canvas.create_rectangle(3/16*app.width,3/20*app.height,
    7/8*app.width,27/80*app.height,fill="black")
    canvas.create_text(430,200,
    text="     Click to understand \nPortfolio Value over time",
        fill="white",anchor="c",font=f"Calligrapher {size//2} bold")
    canvas.create_rectangle(3/16*app.width,7/16*app.height,7/8*app.width,
    6/10*app.height,fill="black")
    canvas.create_text(430,700,text=app.message3,fill="red",anchor="c",
        font=f"Calligrapher {size//2} bold")
    canvas.create_text(430,430,
    text="""Previous Bollinger Bands\n    buying opportunities""",
            fill="white",anchor="c",font=f"Calligrapher {size//2} bold")
    
runApp(width=800,height=800)
