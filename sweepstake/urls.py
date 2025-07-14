from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('update-scores/', views.update_scores, name='update_scores'),
    path('import-excel/', views.import_excel, name='import_excel'),
    path('reset-leaderboard/', views.reset_leaderboard, name='reset_leaderboard'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('reset-players/', views.reset_players, name='reset_players'),
] 