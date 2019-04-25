from django import forms

from get_my_tweets.models import username


class get_tweets_form(forms.ModelForm):
    username = forms.CharField(max_length=100, help_text='Máximo 100 caracteres', required=True)

    class Meta:
        model = username
        fields = ('username',)
