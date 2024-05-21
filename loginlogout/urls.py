from django.urls import path
from loginlogout.views import Record, Login, Logout

urlpatterns = [
    path('register/<int:pk>/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]