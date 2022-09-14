from django.shortcuts import render
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationsRegistrationForm, ReceiptRegistationForm, RewardRegistrtionForm, ThirdpartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipts, Reward, ThirdParty, Transaction, Wallet

# Create your views here.

def register_customer(request):
    if request.method=="POST":
       form=CustomerRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=CurrencyRegistrationForm()
    return render(request,"register_customer.html",{"form":form})

def list_Customer(request):
    customers=Customer.objects.all()
    return render(request,"customer_list.html",{"customers":customers}) 

def wallet(request):
    if request.method=="POST":
       form=WalletRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=WalletRegistrationForm()   
    return render(request,"wallet.html",{"form":form})

def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request,"wallet_list.html",{"wallets":wallets})    

def currency(request):
    if request.method=="POST":
       form=CurrencyRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=CurrencyRegistrationForm()
    return render(request,"currency.html",{"form":form})  

def list_currency(request):
    currencys=Currency.objects.all()
    return render(request,"currency_list.html",{"currencys":currencys})    

def account(request):
    if request.method=="POST":
       form=AccountRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=AccountRegistrationForm()
    return render(request,"account.html",{"form":form}) 

def list_account(request):
    accounts=Account.objects.all()
    return render(request,"account_list.html",{"accounts":accounts})    

def transaction(request):
    if request.method=="POST":
       form=TransactionRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=TransactionRegistrationForm()      
    return render(request,"transaction.html",{"form":form}) 

def list_transaction(request):
    transactions=Transaction.objects.all() 
    return render(request,"transaction_list.html",{"transactions":transactions})   

def card(request):
    if request.method=="POST":
       form=CardRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=CardRegistrationForm()      
    return render(request,"card.html",{"form":form})

def list_card(request):
    cards=Card.objects.all()
    return render(request,"card_list.html",{"cards":cards})  

def thirdparty(request):
    if request.method=="POST":
       form=ThirdpartyRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=ThirdpartyRegistrationForm()      
    return render(request,"thirdparty.html",{"form":form})

def list_thirdparty(request):
    partys=ThirdParty.objects.all()
    return render(request,"thirdparty_list.html",{"partys":partys})    

def notification(request):
    if request.method=="POST":
       form=NotificationsRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=NotificationsRegistrationForm()      
    return render(request,"notifications.html",{"form":form}) 

def list_notification(request):
    notifications=Notifications.objects.all()
    return render(request,"notifications_list.html",{"notifications":notifications})  

def receipt(request):
    if request.method=="POST":
       form=ReceiptRegistationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=ReceiptRegistationForm()      
    return render(request,"receipt.html",{"form":form})

def list_receipt(request):
    receipts=Receipts.objects.all()
    return render(request,"receipt_list.html",{"receipts":receipts})


def loan(request):
    if request.method=="POST":
       form=LoanRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=LoanRegistrationForm()      
    return render(request,"loan.html",{"form":form}) 

def list_loan(request):
    loans=Loan.objects.all()
    return render(request,"loan_list.html",{"loans":loans})   

def reward(request):
    if request.method=="POST":
        form=RewardRegistrtionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RewardRegistrtionForm()
    return render(request,"reward.html",{"form":form})

def list_reward(request):
    rewards=Reward.objects.all()
    return render(request,"reward_list.html",{"rewards":rewards})    






