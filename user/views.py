from django.shortcuts import render
import pandas
import numpy
import array
# Create your views here.
def index(request):
    path = "E:/BRYNPRYL/user.dat"
    # For attendance
    # for i in open(path).readlines():
    #     print(i.strip().split()[0])
    
    # For user data
    test = int(9999999999999)
    print(test)
    with open(path) as datFile:
        for data in datFile:
            print(data.split()[0])
            print([int(s) for s in data.split()[0] if s.isdigit()])

    return render(request, 'user/index.html',{})