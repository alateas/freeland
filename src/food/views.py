# Create your views here.
from django.shortcuts import render_to_response
from food.models import Food
from django.core import serializers
from django.http import HttpResponse
import django.utils.simplejson as json

def main(request):
    return render_to_response('food.html')

def ajax(request):
    data = json.dumps([i.title for i in Groceries.objects.all()])
    print [i.title for i in Food.objects.all()]
    return HttpResponse(data, mimetype="application/json;  charset=utf-8")