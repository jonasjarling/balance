from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context, Template

def index(request):

    template = loader.get_template('training/training.html')
    context = {
        "context" : {
            "plan1": {
                "id": "1",
                "name": "fett pumpen",
                "exercise1": {
                    "id": "123",
                    "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                    "repeat": "6",
                    "weight": "42",
                },
                "exercise2": {
                    "id": "124",
                    "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                    "repeat": "62",
                    "weight": "45",
                },
                "exercise3": {
                    "id": "125",
                    "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                    "repeat": "37",
                    "weight": "69",
                },
            },
            "plan2": {
                "id": "2",
                "name": "disco pumpen",
                "exercise4": {
                    "id": "1",
                    "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                    "repeat": "6",
                    "weight": "42",
                },
                "exercise5": {
                    "id": "12",
                    "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                    "repeat": "62",
                    "weight": "45",
                },
                "exercise6": {
                    "id": "3",
                    "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                    "repeat": "37",
                    "weight": "69",
                },
            },
        },
    }

    context ={
        "Rudern":{
            "Gewicht":"43",
            "height":"2",
            "repetition": "12",
        },
        "Rückenstrecker":{
            "weight": "43",
            "height": "2",
            "repetition": "12",
        },
        "Situps": {
            "weight": "43",
            "height": "2",
            "repetition": "12",
        },
        "Liege Stütze": {
            "weight": "43",
            "height": "2",
            "repetition": "12",
        }
    }

    return render(request, "training/training.html", {"context":context})
    #return HttpResponse(template.render(context))

def plan(request, plan_id):

    template = loader.get_template('training/index.html')
    context = {
        "plan":{
            "id":"1",
            "name":"fett pumpen",
            "exercise":{
                "id":"123",
                "image":"http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat":"6",
                "weight":"42",
            },
            "exercise": {
                "id": "124",
                "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat": "62",
                "weight": "45",
            },
            "exercise": {
                "id": "125",
                "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat": "37",
                "weight": "69",
            },
        },
        "plan": {
            "id": "2",
            "name":"disco pumpen",
            "exercise": {
                "id": "1",
                "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat": "6",
                "weight": "42",
            },
            "exercise": {
                "id": "12",
                "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat": "62",
                "weight": "45",
            },
            "exercise": {
                "id": "3",
                "image": "http://img.pr0gramm.com/2018/03/05/0ea61924c23f153c.jpg",
                "repeat": "37",
                "weight": "69",
            },
        },
    }
    return render(request, "training/training.html", context)
    #return HttpResponse(template.render(context)) #request