from django.shortcuts import render
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, ReceiptRegistationForm, RewardRegistrtionForm, ThirdpartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.

def register_customer(request):
    form=CustomerRegistrationForm()
    return render(request,"register_customer.html",{"form":form})

def wallet(request):
    form=WalletRegistrationForm()
    return render(request,"wallet.html",{"form":form})

def currency(request):
    form=CurrencyRegistrationForm()
    return render(request,"currency.html",{"form":form})  

def account(request):
    form=AccountRegistrationForm()
    return render(request,"account.html",{"form":form}) 

def transaction(request):
    form=TransactionRegistrationForm()
    return render(request,"transaction.html",{"form":form}) 

def card(request):
    form=CardRegistrationForm()
    return render(request,"card.html",{"form":form})

def thirdparty(request):
    form=ThirdpartyRegistrationForm()
    return render(request,"thirdparty.html",{"form":form})

def notification(request):
    form=NotificationsRegistrationForm()
    return render(request,"notifications.html",{"form":form}) 

def receipt(request):
    form=ReceiptRegistationForm()
    return render(request,"receipt.html",{"form":form})

def loan(request):
    form=LoanRegistrationForm()
    return render(request,"loan.html",{"form":form}) 

def reward(request):
    form=RewardRegistrtionForm()
    return render(request,"reward.html",{"form":form})






