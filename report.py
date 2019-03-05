#!/usr/bin/env python

import newsdb


def show_top_three_articles():
    try:
        print("1. What are the most popular three articles of all time?\n")
        articles = newsdb.get_top_three_articles()
        for article in articles:
            print("\"" + article[0] + "\" - " + str(article[1]) + " Views.")
    except BaseException:
        print("Error occurred showing top three articles")


def show_popular_authors():
    try:
        print("2. Who are the most popular article authors of all time?\n")
        authors = newsdb.get_popular_authors()
        for author in authors:
            print(author[0] + " - " + str(author[1]) + " Views.")
    except BaseException:
        print("Error occurred showing popular authors")


def show_highest_error_day():
    try:
        print("3. On which days did more than 1% of request lead to errors?\n")
        error_day = newsdb.get_highest_error_day()
        for info in error_day:
            print(str(info[0]) + " - " + str(round(info[1], 1)) + " % errors.")
    except BaseException:
        print("Error occurred showing highest error day")


def run_reports():
    try:
        """Running Report ..."""
        print("\n")
        print("Running reports ...")
        print("\n")

        print("************************** Report 1 **************************")
        print("\n")
        show_top_three_articles()
        print("\n")

        print("************************** Report 2 **************************")
        print("\n")
        show_popular_authors()
        print("\n")

        print("************************** Report 3 **************************")
        print("\n")
        show_highest_error_day()
        print("\n")

        print("Reports completed!")
        print("\n")
    except BaseException:
        print("Error occurred running reports")


if __name__ == '__main__':
    run_reports()
