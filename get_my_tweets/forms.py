from django import forms


class get_tweets_form(forms.Form):
    username = forms.CharField(max_length=100, help_text='Máximo 100 caracteres', required=True)
