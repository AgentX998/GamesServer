import sqlite3
import time

def insert_score(email,time,score):
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')

    conn.execute("INSERT INTO SCORES (EMAIL, TIME, SCORE) VALUES ('{}',{},{})".format(email,time,score))
    conn.commit()
    conn.close()

def read_scores():
    data={'data':[]}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT email,time,score from scores order by score desc")
    for r in cursor:
        data['data'].append({'email':r[0],
                             'time':r[1],
                             'score':r[2]})
    return data

    print(cursor)


def read_scores_latest():
    t = int(time.time()) - 604800
    data = {'data':[]}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT email,time,score from scores where time>{} order by score desc".format(t))
    for r in cursor:
        data['data'].append({'email':r[0],
                             'time':r[1],
                             'score':r[2]})
    return data


def read_scores_email(email):
    data={'data':[]}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT email,time,score from scores where email='{}' order by score desc".format(email))
    for r in cursor:
        data['data'].append({'email':r[0],
                             'time':r[1],
                             'score':r[2]})
    return data

    print(cursor)

#print(read_scores())
#print(read_scores_email('AAA@gmail.com'))
#print(read_scores_latest())

#insert_score('mehfoozijaz786@gmail.com',1659608807,10)