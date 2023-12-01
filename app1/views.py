from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Farma

###ФУНКЦИИ ДЛЯ РЕКВЕСТОВ (СТРАНИЦЫ)###
def index(request):
    farma = Farma.objects.all()
    return render(request, "html/index.html", {"farma": farma})


def index_addDel(request):
    farma = Farma.objects.all()
    return render(request, "html/index_addDel.html", {"farma": farma})

# сохранение данных в бд
def create(request):
    if request.method == "POST":
        farma = Farma()
        farma.name = request.POST.get("name")
        farma.agent = request.POST.get("agent")
        farma.form = request.POST.get("form")
        farma.action = request.POST.get("action")
        farma.need = request.POST.get("need")
        farma.non = request.POST.get("non")
        farma.subAction = request.POST.get("subAction")
        farma.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        farma = Farma.objects.get(id=id)

        if request.method == "POST":
            farma = Farma()
            farma.name = request.POST.get("name")
            farma.agent = request.POST.get("agent")
            farma.form = request.POST.get("form")
            farma.action = request.POST.get("action")
            farma.need = request.POST.get("need")
            farma.non = request.POST.get("non")
            farma.subAction = request.POST.get("subAction")
            farma.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "html/edit.html", {"farma": farma})
    except Farma.DoesNotExist:
        return HttpResponseNotFound("<h2>Farma not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        farma = Farma.objects.get(id=id)
        farma.delete()
        return HttpResponseRedirect("/")
    except Farma.DoesNotExist:
        return HttpResponseNotFound("<h2>Farma not found</h2>")

def index_auth(request):
    return render(request, "html/index_auth.html")


def index_info(request):
    return render(request, "html/index_info.html")
