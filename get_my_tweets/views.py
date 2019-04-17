from django.shortcuts import render
from django.conf import settings
from . import forms
from .src import twitter_word_count


def index(request):
    return render(request, 'index.html')


def get_tweets(request):
    if request.is_ajax():
        form = forms.get_tweets_form(request.GET)
        if form.is_valid():
            username = request.username
            words = twitter_word_count.twitter_word_count(settings.API_TWITTER).get_words_of_tweets(username)
            return render(request, 'tweets_list.html', {'words': words})

