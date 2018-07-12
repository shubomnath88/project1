from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy
from paralleldots import set_api_key,get_api_key
from paralleldots import *
import nltk
from nltk.corpus import *
nltk.download('stopwords')
stop_word=set(stopwords.words('english'))
set_api_key("IOEJcuuQyQwF0R1Ii7BbZO3jadNBpjVPsdaZLYdNJo4")
get_api_key()
oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
def menu():
    print('''1:-Retrieve Tweets
    2:-Count the followers
    3:-Determine the sentiment
    4:-Determine location,language and time zone.
    5:-Compare tweets 
    6:-Analyze top usage 
    7:-Tweet a message
    8:-exit 
    ''')
def tweets():
    q=input("enter what you want : ")
    search_results = api.search(q)
    for search_result in search_results:
        print(search_result.text)
def count():
    user = api.get_user('@ShubomN')
    print(user.screen_name)
    print(user.followers_count)
def sentimentl():
    print("sentiments")
    print(sentiment("I am very happy")["sentiment"])
def location():
    q = input("enter what you want : ")
    search_results = api.search(q)
    for search_result in search_results:
        print('location = ',search_result.user.location)
        print('language = ',search_result.user.lang)
        print('time_zone = ',search_result.user.time_zone)
def compare():
    pass
def top_usage():
    pass
def message():
    pass
menu()
choice=int(input('enter your choices'))
if(choice==1):
    tweets()
    menu()
elif(choice==2):
    count()
    menu()
elif(choice==3):
    sentimentl()
    menu()
elif(choice==4):
    location()
    menu()
elif(choice==5):
    compare()
    menu()
elif(choice==6):
    top_usage()
    menu()
elif(choice==7):
    message()
    menu()
elif(choice==8):
    exit()
else:
    print('invalid choice')

