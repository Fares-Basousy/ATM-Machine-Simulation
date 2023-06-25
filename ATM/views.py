from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from .models import Person,machine
import itertools

@login_required
def operations(request):
    data = Person.objects.get(person_name=request.user)
    context = {'user': data}
    data = machine.objects.get(pk=1)
    context['machine']=data
    context['operation']=request.POST.get('op')
    print(context['operation'])
    return render(request, 'ATM/operations.html', context)

@login_required
def details(request):
    data=Person.objects.get(person_name=request.user)
    context={'user':data}
    return render(request, 'ATM/detail.html',context)


@login_required
def deposit(request):
    # Calculate the number of papers
    twoh   = int(request.POST['twoh'])
    oneh   = int(request.POST['oneh'])
    fifty  = int(request.POST['fifty'])
    twenty = int(request.POST['twenty'])
    ten    =int(request.POST['ten'])
    sum = twoh*200 +oneh*100 +fifty*50 +twenty*20 + ten*10


    # Updates user database
    person=Person.objects.get(person_name=request.user)
    person.cash+=sum
    person.save()

    # Updates machine database
    data = machine.objects.get(pk=1)
    data.money += sum
    data.money_200 += twoh
    data.money_100 += oneh
    data.money_50 += fifty
    data.money_20 += twenty
    data.money_10 += ten
    data.save()

    return redirect('/ATM/details/')

@login_required
def withdrawal(request):
    cash = int(request.POST['withdrawn'])
    cash1=cash
    person=Person.objects.get(person_name=request.user)
    context={'user':person}
    atm=machine.objects.get(pk=1)
    paper=0
    output=0
    bills={"twoh":0,"oneh":0,"fifty":0,"twenty":0,"ten":0}
    values=[200,100,50,20,10]
    atm_bills=[atm.money_200,atm.money_100,atm.money_50,atm.money_20,atm.money_10]
    if cash>8000:
        output=1
        context["output"] = output
        return render(request, 'ATM/withdrawal.html', context)
    if cash <= 0 or cash%10 != 0:
        output=2
        context["output"] = output
        return render(request, 'ATM/withdrawal.html', context)
    for i,j,k in zip(bills.keys(),values,atm_bills):
        if cash//j<=k:
            paper+=cash//j
            bills[i]=cash//j
            cash-=(cash//j)*j
        else:
            paper+=k
            bills[i]=k
            cash-=k*j

    if cash != 0:
        output = 2
        context["output"] = output
        return render(request, 'ATM/withdrawal.html', context)

    person.cash -= cash1
    atm.money -= cash1
    atm.money_200 -= bills["twoh"]
    atm.money_100 -= bills["oneh"]
    atm.money_50 -= bills["fifty"]
    atm.money_20 -= bills["twenty"]
    atm.money_10 -= bills["ten"]
    atm.save()
    person.save()
    context['user']=person
    context['output']=output
    context['cash']=cash1
    context.update(bills)
    print("bills",bills)
    return render(request, 'ATM/withdrawal.html', context)