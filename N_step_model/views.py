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
    return render(request,'N_step_pages/home_page.html')

def pricing(request):
    S0=float(request.GET["s0"])
    K=float(request.GET["K"])
    T=float(request.GET["T"])
    r=float(request.GET["rate"])/100
    n=int(request.GET["n"])
    sigma=float(request.GET["sigma"])
    # Calculating the price of option according to n-step binomial tree model
    u=np.exp(sigma*(pow(T/n,0.5)))
    d=np.exp(-sigma*(pow(T/n,0.5)))
    p=(np.exp(r*T/n)-d)/(u-d)
    result=0
    for i in range(n):
        result += ncr(n,i)*(pow(p,i))*(pow(1-p,n-i))*max(0,(pow(u,i)*pow(d,n-i)*S0)-K)
    result= result* np.exp(-r*T)
    result = round(result,3)
    result_put = result + (K*np.exp(-r*T)) - S0 # put-call parity
    result_put = round(result_put,3)
    return render(request,'N_step_pages/result.html',{
        "result":result,
        "result_put":result_put  
    })