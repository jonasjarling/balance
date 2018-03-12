from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):

    template = loader.get_template('training/index.html')
    context = {

    }
    return HttpResponse(template.render(context,request))

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
    return HttpResponse(template.render(request, context))