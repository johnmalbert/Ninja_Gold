from django.shortcuts import render, HttpResponse, redirect
import random, time

# Create your views here.
def main(request):
    #check to see if key exists, if not then initialize
    if "gold_amount" in request.session:
        pass
    else:
        request.session['gold_amount'] = 0
        request.session['counter'] = 0
        request.session['activity_log'] = []
    return render(request, "index.html")

#if passing request only via URL
def farmhouse(request):
    change = random.randint(10,20)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    request.session['counter'] += 1
    request.session['gold_amount'] += change
    request.session['activity_log'].append(f"{current_time}: Entered farmhouse, found {change} pieces of Gold!")
    return redirect('/')

def cave(request):
    change = random.randint(5,10)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    request.session['counter'] += 1
    request.session['gold_amount'] += change
    request.session['activity_log'].append(f"{current_time}: Entered Cave, found {change} pieces of Gold!")
    return redirect('/')

def house(request):
    change =  random.randint(2,5)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    request.session['counter'] += 1
    request.session['gold_amount'] += change        
    request.session['activity_log'].append(f"{current_time}: Entered House, found {change} pieces of Gold!")
    return redirect('/')

def casino(request):
    change =  random.randint(2,5)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    change = random.randint(-50,50)
    request.session['counter'] += 1
    request.session['gold_amount'] += change
    if change > 0:
        request.session['activity_log'].append(f"{current_time}: Entered Casino, won {change} pieces of Gold!")
    elif change < 0:
        change = 0 - change
        request.session['activity_log'].append(f"{current_time}: Entered Casino, lost {change} pieces of Gold...")
    #return render(request, "index.html")
    return redirect('/')

def reset(request):
    request.session.clear()
    print('cleared the session')
    return redirect('/')