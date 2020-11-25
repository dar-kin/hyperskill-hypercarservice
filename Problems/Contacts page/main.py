from django.views.generic.base import TemplateView


class ContactsView(TemplateView):
    template_name = "book/contacts.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
