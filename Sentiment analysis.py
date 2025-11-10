import requests
from requests.sessions import session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime
import pandas as pd
from textblob import TextBlob


url="https://api.spaceflightnewsapi.net/v4/articles"
params={"limit":"50"}


Retrey_strategy=Retry(
    total=5,
    status_forcelist=[429, 500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=Retrey_strategy)
with requests.Session() as session:
    session.mount('https://', adapter)
    response=session.get(url,params=params,timeout=(5,10))


    artikles=response.json()


data=artikles["results"]
print (data)
data_df=pd.DataFrame(data)
print(data_df)
data_df.to_csv("data.csv,index=False")
df=pd.read_csv("data.csv,index=False")
scores=[]
labels=[]
for text in df["title"]:
    blob=TextBlob(str(text))
    polarity=blob.sentiment.polarity

    if polarity>0.1 :
        label="positive"
    elif polarity<-0.1 :
        label="negative"
    else:
        label="neutral"
    scores.append(polarity)
    labels.append(label)
df["sentiment_score"]=scores
df["sentiment_label"]=labels
df.to_csv("data_sentiment.csv,index=False")










