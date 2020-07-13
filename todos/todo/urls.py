from django.urls import path

from .views import sign_in_view, sign_up_view, home_view, logoutUser, update_todo


urlpatterns = [
    path('', sign_in_view, name='sign_in'),
    path('update_todo/<int:todo_id>/<str:space>', update_todo, name='update_todo'),
    path('sign_up', sign_up_view, name='sign_up'),
    path('logout', logoutUser, name='logout'),
    path('<str:username>/<str:req_type>', home_view, name='home'),
]
