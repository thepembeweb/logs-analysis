#!/usr/bin/env python

import psycopg2


def connect(dbname="news"):
    try:
        conn = psycopg2.connect("dbname={}".format(dbname))
        cursor = conn.cursor()
        return conn, cursor
    except:
        print("Error in connecting to database")
