from django.shortcuts import render

# Create your views here.
def create(request):


    context = {}

    return render(
        request,
        "contact/create.html",
        context
    )