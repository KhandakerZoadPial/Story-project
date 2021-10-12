from django.shortcuts import render



# git commit -am "Project Initialization & starting porint with all configuration" && git push 

def home(request):
    return render(request, 'story/home.html')