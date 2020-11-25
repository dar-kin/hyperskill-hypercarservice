from django.shortcuts import redirect, Http404
from django.views import View


class TodoView(View):
    all_todos = []

    def delete(self, request, todo, *args, **kwargs):
        if todo in self.all_todos:
            self.all_todos.remove(todo)
            return redirect("/")
        else:
            raise Http404
