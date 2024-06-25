from django.shortcuts import render
import numpy as np
import math
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

# Create your views here.
def home(request):
    return render(request,'Two_step_pages/home_page.html')

def pricing(request):
    S0=float(request.GET["s0"])
    u=float(request.GET["u"])
    d=float(request.GET["d"])
    K=float(request.GET["K"])
    T=float(request.GET["T"])
    r=float(request.GET["rate"])/100
    # Calculating the price of option according to two-step binomial tree model
    p=(np.exp(r*T/2)-d)/(u-d)
    result=0
    for i in range(2):
        result += ncr(2,i)*(pow(p,2-i))*(pow(1-p,i))*max(0,(pow(u,2-i)*pow(d,i)*S0)-K)
    result= result* np.exp(-r*T)
    result = round(result,3)
    result_put = result + (K*np.exp(-r*T)) - S0
    result_put = round(result_put,3)
    return render(request,'Two_step_pages/result.html',{"result":result, "result_put":result_put})