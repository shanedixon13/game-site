from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Game


class GameListView(LoginRequiredMixin, ListView):
    model=Game
    template_name="game_list.html"

class ActionListView(LoginRequiredMixin, ListView):
    model=Game
    template_name="action.html"

class AdventureListView(LoginRequiredMixin, ListView):
    model=Game
    template_name="adventure.html"

class PlatformListView(LoginRequiredMixin, ListView):
    model=Game
    template_name="platform.html"

class SimListView(LoginRequiredMixin, ListView):
    model=Game
    template_name="sim.html"


class GameDetailView(LoginRequiredMixin, DetailView):
    model = Game
    template_name ="game_detail.html"




