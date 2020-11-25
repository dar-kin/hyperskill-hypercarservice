from django.urls import path
from django.views import View


class ContactsView(View):
    pass


urlpatterns = [
    path("contacts/", ContactsView.as_view())
]
