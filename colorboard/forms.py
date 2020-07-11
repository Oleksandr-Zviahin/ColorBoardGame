from django import forms


class GameForm(forms.Form):
    players = forms.IntegerField(
        label='Number of players',
        min_value=1,
        max_value=4,
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    squares = forms.IntegerField(
        label='Number of squares',
        min_value=1,
        max_value=79,
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    deck_size = forms.IntegerField(
        label='Deck size',
        min_value=1,
        max_value=200,
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sequence = forms.CharField(
        label='The sequence pattern for the board',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    deck_list = forms.CharField(
        label='Deck',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
