import asyncio
import json
import pathlib
import random
import ssl
import time
from db import insert_score, user_exists, get_user, insert_address,get_photo
from md5 import img
from websockets import serve
from websockets import WebSocketServerProtocol
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


users=dict()
games=dict()


f = open('l4.txt','r')
lines = f.readlines()
#print(lines[0])
#paragraph='I cant tell you that this is definitely gonna work out, theres no guarantees. But if this turns out to be a big mistake, then lets make it the most fun, big mistake weve ever made.'
#xx= paragraph.split(" ")
##print(len(xx))



ID=1


def update_vals(id):
    #if int(games[id]['joined']) == int(games[id]['noOfPlayers']) and
    if int(games[id]['timestamp_created']) <int(time.time()*1000):
        games[id]['timer'] = (int(games[id]['timestamp_created']) - int(time.time() * 1000)) / 1000
        #print('calc')
        t = int(time.time() * 1000)
        #print(t)
        #print(int(games[id]["timestamp_created"]))
        t = t - int(games[id]["timestamp_created"])
        t=int(t/1000)
        l=2
        if (t< 4):
            l = 1
        if(t<2):
            l=0
        #print(t-6)
        t = int(t - 6)
        games[id]['light']=l
        if l == 2 and t>0:
            games[id]['time'] = str(int(t / 60)) + ":" + str(int(t % 60))
            total = len(games[id]['sentence'].split(" "))

            for pl in games[id]['players']:
                curr = int(pl["currentWord"])
                percent = int(curr / total * 100)
                #print(curr)
                #print(total)
                #print(t)

                pl["percentageCompleted"]=str(percent)
                if pl["percentageCompleted"]!='100':
                    pl["speed"] = int(int(pl["currentWord"])/(t/60))
    else:
        games[id]['timer']=(int(games[id]['timestamp_created'])-int(time.time() * 1000))/1000


def add_to_game(email,id,type):
    #print('add'+id)
    users[email]['currentWord']=0;
    users[email]['myIndex']=games[id]['joined']
    games[id]['joined'] = games[id]['joined'] + 1
    temp = {
        "carType": "silver",
        "currentWord": 0,
        "speed": "0",
        "percentageCompleted": "0",
        'email':''
      }
    temp['carType'] = type
    temp['email'] = email
    games[id]['players'].append(temp)
    users[email]['gameData'] = games[id]
    users[email]['message']="Added to game"
    #if int(games[id]['joined']) == int(games[id]['noOfPlayers']):
    #    games[id]['timestamp_created']=int(time.time()*1000)


def create_game(game_type,email,id,type,num):
    temp={
    "id":"",
    "time": "00:00",
    "type":"random",#random
    "timestamp_created":int((time.time()+30)*1000),
    "timer":30,
    "light": 0,
    "sentence": lines[random.randint(0,8273)][:-1],
    #"sentence": lines[0][:-1],
    "noOfPlayers": 2,
    "joined":0,
    "players": [

    ],
    "positions": [

    ]
  }
    temp['id']=str(id)
    temp['type']=game_type
    temp['noOfPlayers'] = num
    games[id]=temp
    add_to_game(email,id,type)




async def echo(ws:WebSocketServerProtocol):
    global ID
    async for message in ws:
        print(message)
        if(message[0]=='9'):
            m = message.split('\n')
            code = m[0]
        else:
            m = message.split(' ')
            code = m[0]
        if (code=="1"):
            print("ADD user")
            #print("InShaAllah")#m is email
            temp={
    "currentWord": 0,
    "myIndex": 0,
    "email":"Muhammad.Abdullah.Shahid@gmail.com",
    "message":"Connected",#connected, room full,
    "gameData": {}
}
            temp['email']=m[1]
            temp['message']='connected'
            users[m[1]]=temp
            await ws.send(json.dumps(users[m[1]]))
            #print(json.dumps(users[m[1]]))
        if (code == "2"):#join random game
            print("joining")
            num_of_players=int(m[2])
            added=False
            for key in games:
                if games[key]['type']=='random' \
                        and int(games[key]['noOfPlayers'])==num_of_players\
                        and games[key]['joined'] <int(games[key]["noOfPlayers"])\
                        and int(games[key]['timestamp_created']) >int(time.time()*1000):
                    cont=False
                    for elem in games[key]['players']:
                        if elem['email']==m[1]:
                            cont=True
                    if cont:
                        continue
                    add_to_game(m[1], key, m[2])
                    print("key"+str(key))
                    added=True
                    break;
            if not added:
                print("creating")
                create_game("random", m[1], str(ID), m[3], m[2])
                ID=ID+1
                print(ID)
            await ws.send(json.dumps(users[m[1]]))
            #print("InShaAllah")
            #print(games)
        if (code == "3"):
            create_game("random", m[1], str(ID), m[3], m[2])
            ID = ID + 1
            #print("InShaAllah")#create new game ID
            await ws.send(json.dumps(users[m[1]]))
        if (code == "4"):
            if not m[2] in games:
                users[m[1]]['message']="ID does not exist"
            else:
                if int(games[m[2]]['joined']) <int(games[m[2]]["noOfPlayers"])\
                        and int(games[m[2]]['timestamp_created']) >int(time.time()*1000):
                    add_to_game(m[1], m[2], m[3])
            #print("InShaAllah")#join game id, m is game id
            await ws.send(json.dumps(users[m[1]]))
        if (code == "5"):
            #print("InShaAllah")  #request update
            if users[m[1]]['gameData'] != {}:
                print('lala')
                print(users[m[1]]['gameData'])
                print('lala')
                print("5 " + str(users[m[1]]['gameData']['id']))
                update_vals(str(users[m[1]]['gameData']['id']))
                users[m[1]]['gameData'] = games[str(users[m[1]]['gameData']['id'])]
            await ws.send(json.dumps(users[m[1]]))
        if (code == "6"):
            #print("InShaAllah")  #m is word count, update word count
            print('inc')
            if not users[m[1]]['gameData'] is {} and users[m[1]]['gameData']['light']==2:
                gid=str(users[m[1]]['gameData']['id'])
                count = int(users[m[1]]['currentWord'])
                total = len(games[gid]['sentence'].split(" "))
                print('=============================')
                print('=============================')
                print('=============================')
                print('=============================')
                print('total')
                print(total)
                print('count')
                if(total>count):
                    print('=============================')
                    print('total')
                    print(total)
                    print('count')
                    print(count)
                    users[m[1]]['currentWord'] = count + 1
                    mi = users[m[1]]['myIndex']
                    games[gid]['players'][int(mi)]['currentWord'] = count + 1
                    update_vals(gid)

                    users[m[1]]['gameData'] = games[gid]
                    if total==count+1:
                        print('write condition to list position')
                        games[gid]['positions'].append({
                            'email':m[1],
                            'speed':games[gid]['players'][mi]['speed']
                        })
                    if total-1 == count and int(games[gid]['joined'])>1:
                        ti=int(time.time())
                        sp=int(games[gid]['players'][mi]['speed'])
                        insert_score(m[1], ti, sp, get_photo(m[1]))

            await ws.send(json.dumps(users[m[1]]))
        if (code == "7"):
            print("InShaAllah")  #leave current game
            users[m[1]]['gameData']={}
            await ws.send(json.dumps(users[m[1]]))
        if (code == "8"): #address
            print("InShaAllah")  #leave current game
            if(user_exists(m[1])):
                await ws.send(json.dumps({"auth":{"exists":"yes", "data":get_user(m[1])}}))
            else:
                await ws.send(json.dumps({"auth": {"exists": "no","address":m[1]}}))
        if (code == "9"): #address
            print("InShaAllah")  #leave current game
            if(user_exists(m[1])):
                await ws.send(json.dumps({"auth":{"exists":"yes"}}))
            else:
                insert_address(m[1],m[2],m[3],m[4])
                await ws.send(json.dumps({"auth": "user_created"}))

async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    path_cert = pathlib.Path(__file__).with_name("cert.pem")
    path_key = pathlib.Path(__file__).with_name("key.pem")
    ssl_context.load_cert_chain(path_cert, keyfile=path_key)
    async with serve(echo, "0.0.0.0", 8766):
        print('lala')
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
