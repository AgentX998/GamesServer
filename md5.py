# import code for encoding urls and generating md5 hashes
import urllib, urllib.parse, hashlib

# Set your variables here
def img(email):
    default = "https://www.example.com/default.jpg"
    size = 100

    # construct the url
    gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(
        email.lower().encode(encoding='UTF-8', errors='strict')).hexdigest() + "?"
    gravatar_url += urllib.parse.urlencode({'d': default, 's': str(size)})
    return gravatar_url

#print(img('f138145@nu.edu.pk'))
#print(img('mehfoozijaz786@gmail.com'))
