from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')


def Detail(request):
    return render(request, 'portfolio-details.html')


def Page(request):
    return render(request, 'inner-page.html')

    
