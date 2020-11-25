from django.views.generic.base import TemplateView

book = {
    'Page 1': 'This is the cat',
    'Page 2': 'That killed the rat',
    'Page 3': 'That ate the malt',
    'Page 4': 'That lay in the house that Jack built.',
}


class PageView(TemplateView):
    template_name = "book/page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        n_page = kwargs["n_page"]
        context["n_page"] = n_page
        context["content"] = book["Page " + n_page]
        return context
