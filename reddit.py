import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import seaborn as sns
from IPython import display
from pprint import pprint
import praw
import matplotlib.pyplot as plt
import praw
import json

nltk.download('vader_lexicon')
nltk.download('stopwords')


client_id = "aWnjQ1PKD8O8gA"
client_secret = "rupveYbjtRqAi_oIbuCuT450k0QBWw"
user_agent = "Testing_api"
username = "iwasifirshad"
password = ""

reddit = praw.Reddit(client_id="aWnjQ1PKD8O8gA",
                     client_secret="rupveYbjtRqAi_oIbuCuT450k0QBWw",
                     user_agent="Testing_api",
                     username="iwasifirshad",
                     password="",
                    )


def create_reddit_object():
    reddit = praw.Reddit(client_id="aWnjQ1PKD8O8gA",
                         client_secret="rupveYbjtRqAi_oIbuCuT450k0QBWw",
                         user_agent="Testing_api",
                         username="iwasifirshad",
                         password="",
                         )
    return reddit

reddit= create_reddit_object()

subred=reddit.subreddit("depression")

type(hot)

x=next(hot)

# for i in hot:
#     print(i.title,i.url,i.visited)

import pandas as pd
posts = []
ml_subreddit = reddit.subreddit('depression')
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'subreddit', 'num_comments', 'body'])
# print(posts)


reddit = praw.Reddit(client_id='Wpzp7QFd29yHyg',
                    client_secret='rDzHcv5ntnhxaDI38eYt2nSMPJbIjA',
                    user_agent='iwasifirshad')

headlines = set()
for sub in reddit.subreddit('depression').new(limit=None):
    headlines.add(sub.title)
# print(len(headlines))

df['label']=0
df.loc[df['compound']>0.1,'label'] = 1
df.loc[df['compound']< -0.1,'label'] = -1
# df.head()

fig, ax = plt.subplots(figsize=(8,8))
counts=df.label.value_counts(normalize=True)*100
sns.barplot(x=counts.index, y=counts, ax=ax)
ax.set_xticklabels(['negative','neutral','positive'])
ax.set_ylabel("percentage")
# plt.show()








