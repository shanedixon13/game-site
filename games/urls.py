from django.urls import path
from .views import (
    GameListView,
    ActionListView,
    AdventureListView,
    PlatformListView,
    SimListView,
    GameDetailView
)

urlpatterns=[
    path('', GameListView.as_view(), name='game_list'),
    path('action/', ActionListView.as_view(), name='action'),
    path('adventure/', AdventureListView.as_view(), name='adventure'),
    path('platformers/', PlatformListView.as_view(), name='platform'),
    path('sims/', SimListView.as_view(), name='sim'),
    path('<int:pk>/', GameDetailView.as_view(),name='game_detail'),
    ]