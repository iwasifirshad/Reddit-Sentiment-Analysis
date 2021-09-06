from flask import Flask, request, render_template
import praw
import json
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import seaborn as sns
from IPython import display
from pprint import pprint
import praw
import matplotlib.pyplot as plt



app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('integrate.html')










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








results = []

@app.route('/',methods=['POST'])
def mypost():
    reddit = create_reddit_object()
    text = request.form['text']

    subred = reddit.subreddit(text)

    hot = subred.hot(limit=10)
    type(hot)
    x = next(hot)
    post = []
    # text ='hello'
    for i in hot:
        post.append([i.title, i.url, i.likes])
    # print(i.title, i.url, i.visited)
    # print(post)


    sns.set(style='darkgrid', context='talk', palette='Dark2')

    reddit = praw.Reddit(client_id='Wpzp7QFd29yHyg',
                         client_secret='rDzHcv5ntnhxaDI38eYt2nSMPJbIjA',
                         user_agent='iwasifirshad')

    headlines = set()
    for sub in reddit.subreddit(text).new(limit=10):
        headlines.add(sub.title)
    # print(len(headlines))

    sia = SIA()

    for line in headlines:
        scores = sia.polarity_scores(line)
        scores['headline'] = line
        results.append(scores)
        # df = pd.DataFrame.from_records(results)
    print(results)


    # print(item)
    return render_template('abc.html', posts=post, result=results)

@app.route("/test_link")
def test_link():
 return render_template('test_link.html', result=results)



if __name__ == '__main__':
    app.run(debug=True)
