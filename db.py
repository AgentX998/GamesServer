import sqlite3
import time

def get_photo_by_address(address):
    data={}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT photo from users where address='{}'".format(address))
    exist=False
    for r in cursor:
        return r[0]
    return 'lala'
def get_photo(email):
    data={}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT photo from users where email='{}'".format(email))
    exist=False
    for r in cursor:
        return r[0]
    return 'lala'
def get_email(address):
    data={}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT email from users where address='{}'".format(address))
    exist=False
    for r in cursor:
        return r[0]
    return 'lala'
def insert_score(email,time,score,photo):
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')

    conn.execute("INSERT INTO SCORES2 (EMAIL, TIME, SCORE,PHOTO) VALUES ('{}',{},{},'{}')".format(email,time,score,photo))
    conn.commit()
    conn.close()

def read_scores():
    data={'data':[]}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT email,time,score, photo from scores2 order by score desc")
    for r in cursor:
        data['data'].append({'email':r[0],
                             'time':r[1],
                             'score':r[2],
                             'photo':r[3]})
    return data

    print(cursor)


def read_scores_latest():
    t = int(time.time()) - 604800
    data = {'data':[]}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT email,time,score, photo from scores2 where time>{} order by score desc".format(t))
    for r in cursor:
        data['data'].append({'email':r[0],
                             'time':r[1],
                             'score':r[2],
                             'photo':r[3]})
    return data


def read_scores_email(email):
    data={'data':[]}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT email,time,score,photo from scores2 where email='{}' order by score desc".format(email))
    for r in cursor:
        data['data'].append({'email':r[0],
                             'time':r[1],
                             'score':r[2],
                             'photo':r[3]})
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



def read_average(email):
    data={'data':[]}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT avg(score)from scores2 where email='{}' order by time desc limit 10".format(email))
    for r in cursor:
        if r[0]==None:
            return 0
        return r[0]

    print(cursor)
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
        #data['photo'] =r[3]
        data['average'] = read_average(r[2])
    return data
def get_user_by_email(email):
    data={}
    #print("INSERT INTO SCORES (EMAIL, TIME, SCORE) \
    #      VALUES ('{}',{},{})".format(email,time,score))
    conn = sqlite3.connect('typearn.db')
    cursor = conn.execute("SELECT address,name,email,photo from users where email='{}'".format(email))
    exist=False
    for r in cursor:
        data['address']=r[0]
        data['name'] =r[1]
        data['email'] = r[2]
        data['photo'] =r[3]
        data['average'] = read_average(r[2])
    return data
def insert_address(address,name,email,photo):
    conn = sqlite3.connect('typearn.db')

    conn.execute("INSERT INTO USERS (address,name,email,photo) VALUES ('{}','{}','{}','{}')".format(address,name,email,photo))
    conn.commit()
    conn.close()
def update_photo(address,photo):
    conn = sqlite3.connect('typearn.db')
    sql = "UPDATE USERS SET photo='{}' WHERE address='{}'".format(photo,address)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print('UPDATE_PHOTO')

#print(user_exists('dummy'))
#print(get_photo('dummy'))
#insert_address('dummy','dummy','dummy','dummy')
#print(read_scores())
#update_photo('dummy','done')
print(get_user('dummy'))
#print(read_average('dummy2'))
#update_photo('dummy','new2')
#print(get_user('dummy'))