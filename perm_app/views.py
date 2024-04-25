from django.shortcuts import render
from perm_app.permutation import Permutation
from .forms import selection
from django.http import JsonResponse
# Create your views here.

def home(request):
    form = selection()  # Instantiate form by default
    if request.method == "POST":
        form = selection(request.POST)
    return render(request, 'perm_app/index.html', {"form": form})

def findPermutation(request):
    if request.method == "POST":
        form = selection(request.POST)
        if form.is_valid():
            perm=Permutation()
            list1=[]
            data = form.cleaned_data.get('input')
            if len(data)==1:
                list1=[data]
            elif len(data)==2:
                list1=[data,data[::-1]]
            if len(data)==3:
                list1 =perm.perm3(data)
            elif len(data)==4:
               list1 = perm.perm4(data)
            elif len(data)==5:
                list1 =perm.perm5(data)
            elif len(data)==6:
                list1 =perm.perm6(data)
            elif len(data)==7:
                list1 =perm.perm7(data)
            elif len(data)==8:
                list1 =perm.perm8(data)
            elif len(data)==9:
                list1 =perm.perm9(data)
            else:
                list1=[data]
            return JsonResponse({'param1': list1})
        else:
            return JsonResponse({'error': 'Form data is invalid'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)