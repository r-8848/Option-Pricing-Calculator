from django.shortcuts import render
import numpy as np
import math
from scipy.stats import norm

# Create your views here.
def home(request):
    return render(request,'black_scholes_pages/home_page.html')

def pricing(request):
    S0=float(request.GET["s0"])
    K=float(request.GET["K"])
    T=float(request.GET["T"])
    r=float(request.GET["rate"])/100
    sigma=float(request.GET["sigma"])

    d1=((np.log(S0/K))+(r+(pow(sigma,2)/2))*T)/(sigma*pow(T,0.5))
    d2=d1-(sigma*pow(T,0.5))
    result = (norm.cdf(d1)*S0)-(norm.cdf(d2)*K*np.exp(-r*T))
    result = round(result,3)
    result_put = result + (K*np.exp(-r*T)) - S0
    result_put = round(result_put,3)
    return render(request,'black_scholes_pages/result.html',{"result":result,"result_put":result_put})