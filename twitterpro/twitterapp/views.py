import tweepy
from twitterapp.key import * 
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.method == 'POST':
        content = request.POST.get('content','')

        if content:
            print('Content :',content)

            api = tweepy.API(auth)
            api.update_status(content)
            return redirect('index')

    return render(request,'post/posttweet.html')

def user_timeline(request):

        api = tweepy.API(auth)
        public_tweets = api.user_timeline()
        return render(request, 'post/gettweet.html', {'public_tweets': public_tweets})
def home_timeline(request):
        api = tweepy.API(auth)
        public_tweets = api.home_timeline()
        return render(request, 'post/gettweet.html', {'public_tweets': public_tweets})

def search(request):
         
        api = tweepy.API(auth)
        india_woeid = 23424848
        trend_result = api.get_place_trends(india_woeid)
        return render(request, 'post/search.html', {'trend_result': trend_result})        

      



