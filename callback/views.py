from django.shortcuts import render,redirect

# Create your views here.
def callback(request):
    if request.METHOD == "POST":
        return render(request,'callback/callback.html')
    else:
        return redirect('homepage')
