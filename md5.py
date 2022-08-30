# import code for encoding urls and generating md5 hashes
import urllib, hashlib

# Set your variables here
email = 'mehfoozijaz786@gmail.com'
default = "https://www.example.com/default.jpg"
size = 100

# construct the url
gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
gravatar_url += urllib.urlencode({'d':default, 's':str(size)})

print(gravatar_url)