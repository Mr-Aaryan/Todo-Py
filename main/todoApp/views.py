from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import TodoApp
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def todoApp(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        mytasks = request.POST.get('tasks')
        if mytasks:
            x = TodoApp(tasks = mytasks)
            x.save()
            return JsonResponse({"task": mytasks})
        else:
            return JsonResponse({"message": "empty message"})
    else:
        mytasks = TodoApp.objects.all()
        return render(request, 'index.html', {"mytasks": mytasks})