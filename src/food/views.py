# Create your views here.
from django.shortcuts import render_to_response
from food.models import Food, Portion
from django.core import serializers
from django.http import HttpResponse
import django.utils.simplejson as json

def main(request):
    return render_to_response('food.html')

def ajax_portions(request):
    data = []
    for i in Portion.objects.all():
        data.append({
            'title'         : str(i),
            'energy'        : i.energy,
            'proteins'      : i.proteins,
            'fats'          : i.fats,
            'carbohydrates' : i.carbohydrates,
        })
    json_data = json.dumps(data)
    
    return HttpResponse(json_data, mimetype="application/json;  charset=utf-8")