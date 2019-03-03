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
