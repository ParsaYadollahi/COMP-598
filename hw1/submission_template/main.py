from os import stat
import pandas as pd

# Data collection
df = pd.read_csv("./data.tsv", nrows=10000)
df = df.loc[df['language'] == "English"]
df = df.loc[df['content'].str.contains('?', regex=False) == True]


# Data annotation
trump_mention = df['content'].str.contains("(?<!\w)Trump(?!\w)", regex=True)
trump_mention = trump_mention.astype('string').replace('True', 'T')
trump_mention = trump_mention.astype('string').replace('False', 'F')
df = df.assign(trump_mention=trump_mention)

#Analysis
number_trump_mention = len(df.loc[df['trump_mention'].str.contains('T', regex=False) == True])
stats = number_trump_mention/len(df)
print("Number of Trump mentions = ", stats)

# Adding to tsv
ds = df[['tweet_id', 'publish_date', 'content', 'trump_mention']]
