from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request):
    if request.method=='POST':
        name=request.POST['un']
        password=request.POST['pw']
        # print(name)
        # print(password)
        return HttpResponse('data inserted sucessfully')
    return render(request,'hai.html')