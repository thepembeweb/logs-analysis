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


def show_popular_authors():
    try:
    print("2. Who are the most popular article authors of all time?\n")
    authors = get_popular_authors()
    for author in authors:
        print(author[0] + " - " + str(author[1]) + " Views.")
    except:
        print("Error occurred showing popular authors")
