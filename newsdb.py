#!/usr/bin/env python

import psycopg2


def connect(dbname="news"):
    try:
        conn = psycopg2.connect("dbname={}".format(dbname))
        cursor = conn.cursor()
        return conn, cursor
    except:
        print("Error in connecting to database")


def get_top_three_articles():
    try:
        """Return top three articles"""
        conn, cursor = connect()
        query = "SELECT articles.title, COUNT(log.path) as views \
        FROM articles, log \
        WHERE position(articles.slug in log.path) != 0 \
        AND log.status = '200 OK' \
        GROUP BY articles.title \
        ORDER BY views DESC LIMIT 3;"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except:
        print("Error in returning top three articles")


def get_popular_authors():
    try:
        """Return popular authors"""
        conn, cursor = connect()
        query = "SELECT authors.name, COUNT(log.path) as view \
        FROM authors, articles, log \
        WHERE authors.id = articles.author \
        AND position(articles.slug in log.path) != 0 \
        AND log.status = '200 OK' \
        GROUP BY authors.name \
        ORDER BY view DESC;"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except:
        print("Error in returning popular authors")


def get_highest_error_day():
    try:
        """Return highest error day"""
        conn, cursor = connect()
        query = "SELECT to_char(time, 'Mon DD, YYYY') as error_day, \
        (100*COUNT(CASE WHEN status = '404 NOT FOUND' \
        THEN id END)::decimal/COUNT(id)) as errors_p \
        FROM LOG \
        GROUP BY error_day \
        HAVING (100*COUNT(CASE WHEN status = '404 NOT FOUND' \
        THEN id END)::decimal/COUNT(id)) > 1 \
        ORDER BY errors_p DESC;"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except:
        print("Error in returning highest error day")
