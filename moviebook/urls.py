

from django.urls import path
from . import views
from . import url_handlers

urlpatterns = [
    path("film_index/", views.FilmIndex.as_view(), name="filmovy_index"),
    path("<int:pk>/film_detail/", views.CurrentFilm.as_view(), name="filmovy_detail"),
    path("create_film/", views.CreateFilm.as_view(), name="novy_film"),
    path("<int:pk>/edit/", views.EditFilm.as_view(), name="edit_film"),
    path("register/", views.UzivatelViewRegister.as_view(), name="registrace"),
    path("login/", views.UzivatelViewLogin.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("", url_handlers.index_handler),
]