from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

def index(request):
    print User.objects.all()
    return render(request, 'store/index.html')

def create(request):
    #create a dictionary for post data input.
    postData = {
        'first_name' : request.POST['first_name'],
        'last_name' : request.POST['last_name'],
        'email' : request.POST['email'],
        'password' : request.POST['password'],
        'confirm' : request.POST['confirm'],
    }
    #error handler checks user input and sets session.
    errors = User.objects.register(postData)
    if len(errors) == 0:

        request.session['id'] = User.objects.filter(email=postData['email'])[0].id
        request.session['first_name'] = postData['first_name']
        return redirect('/success')
    else:
        for errors in errors:
            messages.info(request, errors)
        return redirect('/')

def login(request):
    postData = {
        'email' : request.POST['email'],
        'password' : request.POST['password']
    }
    errors = User.objects.login(postData)
    if len(errors) == 0:
        request.session['id'] = User.objects.filter(email=postData['email'])[0].id
        request.session['first_name'] = User.objects.filter(email=postData['email'])[0].first_name
        return redirect('/success')
    for error in errors:
        messages.info(request, errors)
    return redirect('/')

def success(request):
    context = {'users' : User.objects.all().order_by('-created_at')}
    return render(request, 'store/index.html', context)

def confirm(request):
    price = {
        "1" : 69,
        "2" : 89,
        "3" : 89,
        "4" : 129,
        "5" : 129,
        "6" : 179

    }
    
    try:
        request.session['counter']
    except KeyError:
        request.session['counter'] = 0
    try:
        request.session['quantity']
    except KeyError:
        request.session['quantity'] = 0
    request.session['counter'] += int(request.POST['quantity'])
    request.session['quantity'] += int(request.POST['quantity'])

    quantity = request.POST['quantity']
    product = request.POST['product']
    request.session['total_price'] = int(quantity) * price[product]

    if 'total_purchase' not in request.session:
        request.session['total_purchase'] = request.session['total_price']
    else:
        request.session['total_purchase'] += request.session['total_price']
        print request.session['total_purchase']
    

    return redirect('/checkout')
# return redirect('/confirm')
# def confirm(request):
#     return redirect('/checkout')

def checkout(request):
    return render(request,'store/checkout.html')

def result(request):
    return render(request, 'store/complete.html')

def iphone6s(request):
    return render(request, 'store/iphone6s.html')

def iphone6(request):
    return render(request, 'store/iphone6.html')
    
def iphone7(request):
    return render(request, 'store/iphone7.html')

def iphone7plus(request):
    return render(request, 'store/iphone7plus.html')

def iphone6plus(request):
    return render(request, 'store/iphone6plus.html')

def iphone6splus(request):
    return render(request, 'store/iphone6splus.html')
