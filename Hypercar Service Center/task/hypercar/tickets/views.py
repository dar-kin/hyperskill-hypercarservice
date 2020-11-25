from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tickets/menu.html", context={"services": services})


services = [{"type": "change_oil", "name": "Change oil"},
            {"type": "inflate_tires", "name": "Inflate tires"},
            {"type": "diagnostic", "name": "Get diagnostic test"}]

tickets = 0

class OilView(View):
    def get(self, request, *args, **kwargs):
        global tickets
        tickets += 1
        queue["oil"]["tickets"].append(tickets)
        time = queue["oil"]["time"]
        queue["oil"]["index"] += 1
        index = queue["oil"]["index"]
        queue["oil"]["time"] += 2
        return HttpResponse(f"<div>Your number is {index}"
                            f"</div><div>Please wait around {time} minutes</div>")


class InflateView(View):
    def get(self, request, *args, **kwargs):
        global tickets
        tickets += 1
        queue["inflate"]["tickets"].append(tickets)
        time = queue["oil"]["time"] + queue["inflate"]["time"]
        queue["inflate"]["index"] += 1
        index = queue["oil"]["index"] + queue["inflate"]["index"]
        queue["inflate"]["time"] += 5
        return HttpResponse(f"<div>Your number is {index}"
                            f"</div><div>Please wait around {time} minutes</div>")


class DiagnosticView(View):
    def get(self, request, *args, **kwargs):
        global tickets
        tickets += 1
        queue["diagnostic"]["tickets"].append(tickets)
        time = queue["oil"]["time"] + queue["inflate"]["time"] + queue["diagnostic"]["time"]
        queue["diagnostic"]["index"] += 1
        index = queue["oil"]["index"] + queue["inflate"]["index"] + queue["diagnostic"]["index"]
        queue["diagnostic"]["time"] += 30
        return HttpResponse(f"<div>Your number is {index}"
                            f"</div><div>Please wait around {time} minutes</div>")


queue = {"oil": {"index": 0, "time": 0, "tickets": []},
         "inflate": {"index": 0, "time": 0, "tickets": []},
         "diagnostic": {"index": 0, "time": 0, "tickets": []}}


ticket_processed = -1


class ProcessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tickets/process.html", context={"queue":queue})

    def post(self, request, *args, **kwargs):
        global tickets, ticket_processed
        if not tickets:
            ticket_processed = -1
            return redirect("/processing")
        else:
            tickets -= 1
            if queue["oil"]["index"] != 0:
                queue["oil"]["index"] -= 1
                queue["oil"]["time"] -= 2
                ticket_processed = queue["oil"]["tickets"].pop(0)
            elif queue["inflate"]["index"] != 0:
                queue["inflate"]["index"] -= 1
                queue["inflate"]["time"] -= 5
                ticket_processed = queue["inflate"]["tickets"].pop(0)
            elif queue["diagnostic"]["index"] != 0:
                queue["diagnostic"]["index"] -= 1
                queue["diagnostic"]["time"] -= 30
                ticket_processed = queue["diagnostic"]["tickets"].pop(0)
            return redirect("/processing")


class NextView(View):
    def get(self, request, *args, **kwargs):
        if ticket_processed == -1:
            return HttpResponse("<div>Waiting for the next client</div>")
        else:
            return HttpResponse(f"<div>Next ticket #{ticket_processed}</div>")

