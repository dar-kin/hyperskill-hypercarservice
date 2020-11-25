from django.urls import path
from django.views import View


class CatView(View):
    pass


class DogView(View):
    pass


urlpatterns = [
    path("cat/", CatView.as_view()),
    path("dog/", DogView.as_view())
]
