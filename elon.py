import pandas as p
import pandas_datareader as pd
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
from textblob import TextBlob
from cmu_112_graphics import *

def elonMode(ticker,decision):
    symbols=get_nasdaq_symbols()['Security Name']
    for i in symbols.index:
        s=symbols[i]
        symbols[i]=symbols[i][:symbols[i].find(' ') ]
    if(decision=='stock'):
        search=symbols[ticker.upper()]
    if(decision=='keyword'):
        search=ticker
    elon= p.read_csv('TweetsElonMusk.csv')['tweet']
    s=dict()
    l=set()
    n=0
    sum=0
    tweets=list()
    for i in elon:
        if(search in i):
            n+=1
            sum+=TextBlob(i).sentiment.polarity
            tweets.append(i)
    if(n!=0):
        sentiment=sum/n
    if(n==0):
        return ("Elon luckily does not have an opinion!")
    if(n>0.6):
        return ("Elon thinks well about it!")
    elif(n>0.3 and n<0.6):
        return ("Elon does not have a problem with it: Neutral Feeling")
    elif(n!=0):
        return ("Elon does not think well about it! Consider selling!")
def elonVisual(app,canvas):
    size=(app.width+app.height)//30
    canvas.create_rectangle(0,0,app.width,app.height,fill="purple")
    # canvas.create_image(400, 400, image=ImageTk.PhotoImage(app.image3))
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
