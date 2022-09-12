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

def user_exists(address):
    data={'data':[]}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT address,name,email,photo from users where address='{}'".format(address))
    exist=False
    for r in cursor:
        exist=True
    return exist
def get_user(address):
    data={}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT address,name,email,photo from users where address='{}'".format(address))
    exist=False
    for r in cursor:
        data['address']=r[0]
        data['name'] =r[1]
        data['email'] = r[2]
        data['photo'] =r[3]
    return data
def insert_address(address,name,email,photo):
    conn = sqlite3.connect('typearn.db')

    conn.execute("INSERT INTO USERS (address,name,email,photo) VALUES ('{}','{}','{}','{}')".format(address,name,email,photo))
    conn.commit()
    conn.close()
print(user_exists('dummy'))
#insert_address('dummy','dummy','dummy','dummy')