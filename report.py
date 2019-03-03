#!/usr/bin/env python

from newsdb import get_top_three_articles, get_popular_authors, get_highest_error_day


def show_top_three_articles():
    try:
    print("1. What are the most popular three articles of all time?\n")
    articles = get_top_three_articles()
    for article in articles:
        print("\"" + article[0] + "\" - " + str(article[1]) + " Views.")
    except:
        print("Error occurred showing top three articles")
