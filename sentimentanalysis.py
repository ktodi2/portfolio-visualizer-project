from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,Request
import requests as r
import ssl
import certifi
import pandas as pd
from textblob import TextBlob
def doSentimentAnalysis(ticker):
    ticker=ticker.upper()
    url=f"https://finviz.com/quote.ashx?t={ticker}&ty=c&ta=1&p=d"
    req=Request(url=url,headers={'user-agent':'my-app'})
    response=urlopen(req, context=ssl.create_default_context(cafile=certifi.where()))
    html=bs(response,'html')
    s=html.find(id='news-table')
    rows=s.findAll('tr')
    title=[]
    for row in (s):
        title+=[row.text]
    sentiments=[]
    index=0

    for i in range(len(title)):
        w=""
        s=title[i]
        for j in range(len(s)):
            w=w+s[j]
            if("AM" in w or "PM" in w):
                title[i]=s[j:]
                break

    for i in range(len(title)):
        if(title[index]=='\n' or title[index].startswith('\n')):
            title.pop(index)
            continue
        index+=1

    print(title)
    s=[]
    for i in title:
        n=TextBlob(i).sentiment.polarity
        if(n!=0):
            s.append(n)
    sentiment1=sum(s)/len(s)
    final=""
    for i in title:
        final=i+"."+final
    sentiment2=TextBlob(final).sentiment.polarity
    sentiment=(sentiment1+sentiment2)/2
    # print(sentiment)
    if(sentiment>0.3):
        return "Buy"
    elif(sentiment>0.2 and sentiment<0.3):
        return "Hold"
    else:
        return "Sell"

def graphicSentiment(app,canvas):
    size=(app.width+app.height)//30
    canvas.create_rectangle(0,0,app.width,app.height,fill="yellow")
    canvas.create_rectangle(0,0,app.width/12,app.height/12,fill="gray1")
    canvas.create_text(app.width/20,app.height/21,text="Back",anchor='c',
        fill="white")
    canvas.create_rectangle(200,200,600,400,fill="black")
    canvas.create_text(400,300,text="Sentiment Analysis",
        fill="white",anchor="c",font=f"Calligrapher {size//(2)} bold")
    canvas.create_rectangle(200,500,600,700,fill="black")
    canvas.create_text(400,600,text=app.sentimentmessage,
        fill="white",anchor="c",font=f"Calligrapher {size//(2)} bold")
# doSentimentAnalysis("CS")
