import pandas as pd

# Data collection
df = pd.read_csv("./data.tsv", nrows=10000)
df = df.loc[df['language'] == "English"]
df = df[df['content'].str.contains('?', regex=False) == False]

# Data annotation
trump_mention = df['content'].str.contains("(?<!\w)Trump(?!\w)", regex=True)
trump_mention = trump_mention.astype('string').replace('True', 'T')
trump_mention = trump_mention.astype('string').replace('False', 'F')
df = df.assign(trump_mention=trump_mention)

#Analysis
number_trump_mention = len(df.loc[df['trump_mention'].str.contains('T', regex=False) == True])
stats = number_trump_mention/len(df)

# Adding tweets to tsv
ds = df[['tweet_id', 'publish_date', 'content', 'trump_mention']]
ds.to_csv("dataset.tsv", sep="\t", index=False)

# Add results to tsv
dr = {'result': ['frac-trump-result'], 'value': ["{:0.3f}%".format(stats*100)]}
result_df = pd.DataFrame(data=dr)
result_df.to_csv("results.tsv", sep="\t", index=False)
