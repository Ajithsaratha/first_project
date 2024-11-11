from django.shortcuts import render

# Create your views here.


def calculator(request):
    return render(request,'calculator.html')

def fun(request):
    if request.method=="POST":
        num1=int(request.POST["number1"])
        num2=int(request.POST["number2"])
        operation=request.POST['operations']
        if operation=='Addition':
            result=num1+num2
        elif operation=='Subtraction':
            result=num1-num2
        elif operation=='Multiplication':
            result=num1*num2
        elif operation=='Division':
            result=num1/num2   
    return render(request,'calculator.html',{"answer":result})         