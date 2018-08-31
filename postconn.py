# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# "Project Name"        :   "PyPostgres"                                #
# "File Name"           :   "postconn"                                  #
# "Author"              :   "rishabhzn200"                              #
# "Date of Creation"    :   "Aug-29-2018"                               #
# "Time of Creation"    :   "5:19 PM"                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import psycopg2 as postgreconn


try:
    # connect to database
    con = postgreconn.connect("dbname='postgres' user='rishabhzn200' host='localhost' password=''")

    con.autocommit = True

    cur = con.cursor()

    cur.execute("""create database test""")

    cur.close()
    con.close()

    # open database test
    contest = postgreconn.connect("dbname='test' user='rishabhzn200' host='localhost' password=''")
    contest.autocommit = True

    cur = contest.cursor()

    # Create 3 tables and add values

    # Create Table
    tbl1 = """CREATE TABLE USERS(USERID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL);"""
    tbl2 = """CREATE TABLE MOVIES (MOVIEID INT PRIMARY KEY NOT NULL, TITLE TEXT NOT NULL, GENRE TEXT);"""
    tbl3 = """CREATE TABLE RATINGS(USERID INT REFERENCES USERS(USERID), NOVIEID INT REFERENCES MOVIES(MOVIEID), RATING NUMERIC NOT NULL CHECK(RATING>=0 AND RATING<=5));"""

    for tbl in [tbl1, tbl2, tbl3]:
        cur.execute(tbl)

    # # insert values
    # User table
    users = [(1, 'David'), (2, 'Eric'), (3, 'Kevin')]
    for userid, user in users:
        cur.execute(f"INSERT INTO users VALUES ({userid}, '{user}');")

    # Movies table
    # Insert from the file
    cur.execute(f"COPY MOVIES FROM '/Users/rishabhzn200/movies.dat' delimiter '_';")

    # Ratings Table
    allratings = [(1, 122, 5.0), (1, 185, 4.5), (2, 231, 4.0), (2, 294, 3.5), (3, 316, 3.0)]
    for uid, movieid, rating in allratings:
        cur.execute(f"insert into ratings VALUES ({uid}, {movieid}, {rating});")


except:
    print("Error Occured")









