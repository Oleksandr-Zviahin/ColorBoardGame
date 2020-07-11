from django.shortcuts import render
from django.views import View
from .forms import GameForm
from .game_session import GameSession


class ColorBoardView(View):
    def get(self, request):
        return render(request, 'game_page.html', {'form': GameForm, 'result': None})

    def post(self, request):
        form = GameForm(request.POST)
        game_result = None
        if form.is_valid():
            game = GameSession(form.cleaned_data)
            game.calculate_result()
            game_result = game.result

        return render(request, 'game_page.html', {'form': form, 'result': game_result})
