from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview),
    path("all-users/", views.get_all_clients),
    path("user/<str:client_no>/", views.get_user),
    path("create-user/", views.create_user),

]