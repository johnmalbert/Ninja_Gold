from django.shortcuts import render, HttpResponse, redirect
import random, time

# Create your views here.
def main(request):
    request.session['gold_amount'] = 0
    request.session['counter'] = 0
    request.session['activity_log'] = []
    print("Current gold is ", request.session['gold_amount'])
    context = {
        'gold' : request.session['gold_amount'],
        'counter' : request.session['counter']
    }
    return render(request, "index.html", context)

#if passing request only via URL
def farmhouse(request):
    change = random.randint(10,20)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    request.session['gold_amount'] += change
    request.session['activity_log'].append(f"{current_time}: Entered farmhouse, found {change} pieces of Gold!")
    return render(request, "index.html")

def cave(request):
    change = random.randint(5,10)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    request.session['gold_amount'] += change
    request.session['activity_log'].append(f"{current_time}: Entered Cave, found {change} pieces of Gold!")
    return render(request, "index.html")

def house(request):
    change =  random.randint(2,5)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    request.session['gold_amount'] += change        
    request.session['activity_log'].append(f"{current_time}: Entered House, found {change} pieces of Gold!")
    return render(request, "index.html")

def casino(request):
    change =  random.randint(2,5)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    change = random.randint(-50,50)
    request.session['gold_amount'] += change
    if change > 0:
        request.session['activity_log'].append(f"{current_time}: Entered Casino, won {change} pieces of Gold!")
    elif change < 0:
        change = 0 - change
        request.session['activity_log'].append(f"{current_time}: Entered Casino, lost {change} pieces of Gold...")
    return render(request, "index.html")


#If using the form method (before refactoring code)
def process_money(request):
    #do some code adding or taking money
    print("entered a room")
    print(request.POST['casino'])
    request.session['counter'] += 1
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    if int(request.POST['casino']) == 0:
        change = random.randint(10,20)
        request.session['gold_amount'] += change
        request.session['activity_log'].append(f"{current_time}: Entered farmhouse, found {change} pieces of Gold!")
    if int(request.POST['casino']) == 1:
        change = random.randint(5,10)
        request.session['gold_amount'] += change
        request.session['activity_log'].append(f"{current_time}: Entered Cave, found {change} pieces of Gold!")
    if int(request.POST['casino']) == 2:
        change =  random.randint(2,5)
        request.session['gold_amount'] += change        
        request.session['activity_log'].append(f"{current_time}: Entered House, found {change} pieces of Gold!")
    if int(request.POST['casino']) == 3:
        change = random.randint(-50,50)
        request.session['gold_amount'] += change
        if change > 0:
            request.session['activity_log'].append(f"{current_time}: Entered Casino, won {change} pieces of Gold!")
        elif change < 0:
            change = 0 - change
            request.session['activity_log'].append(f"{current_time}: Entered Casino, lost {change} pieces of Gold...")
    context = {
        'gold' : request.session['gold_amount'],
        'activity_log' : request.session['activity_log'],
        'counter' : request.session['counter']
    }
    return render(request, "index.html", context)

def reset(request):
    request.session.clear()
    print('cleared the session')
    return redirect('/')