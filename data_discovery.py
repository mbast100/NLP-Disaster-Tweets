import pandas as pd

train_data = pd.read_csv("data/train.csv")

print(train_data.info())
print(train_data.head(5))

def get_top_tweets(n):

    tweets = []
    df = get_pd_dataframe(path="data/train.csv")
    for i in range(n):
        tweets.append(df.iloc[i][3])
    
    return tweets

def get_pd_dataframe(path):

    train_data = pd.read_csv(path)
    return train_data

print(get_top_tweets(10))