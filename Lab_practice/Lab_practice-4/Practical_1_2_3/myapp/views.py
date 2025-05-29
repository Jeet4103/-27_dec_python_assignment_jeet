from django.shortcuts import render, redirect
from .forms import studinfoForm

def home(request):
    if request.method == "POST":
        form = studinfoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record inserted!")
            return redirect("/")
        else:
            print(form.errors)
    else:
        form = studinfoForm()
    return render(request, "index.html", {"form": form})
