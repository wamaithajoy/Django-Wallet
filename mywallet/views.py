from calendar import c
from django.shortcuts import redirect, render
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

def customer_profile(request,id):
    customer=Customer.objects.get(id=id)
    return render(request,"customer_profile.html",{"customer":customer})

def edit_profile(request,id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST,instance=customer) 
        if form.is_valid():
            form.save()
        return redirect("customer_profile",id=customer.id)

    else:
        form=CustomerRegistrationForm(instance=customer) 
        return render(request,"edit_profile.html",{"form":form})  


def wallet_profile(request,id):
    wallet=Wallet.objects.get(id=id)
    return render (request,"wallet_profile.html",{"wallet":wallet})     

def edit_wallet(request,id):
    wallet=Wallet.objects.get(id=id)
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST,instance=wallet) 
        if form.is_valid():
            form.save()
        return redirect("wallet_profile",id=wallet.id)

    else:
        form=WalletRegistrationForm(instance=wallet) 
        return render(request,"edit_wallet.html",{"form":form})  

def account_profile(request,id):
    account=Account.objects.get(id=id)
    return render (request,"account_profile.html",{"account":account})

def edit_account(request,id):
    account=Account.objects.get(id=id)
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST,instance=account) 
        if form.is_valid():
            form.save()
        return redirect("account_profile",id=account.id)

    else:
        form=AccountRegistrationForm(instance=account) 
        return render(request,"edit_account.html",{"form":form})

def card_profile(request,id):
    card=Card.objects.get(id=id)
    return render (request,"card_profile.html",{"card":card})

def edit_card(request,id):
    card=Card.objects.get(id=id)
    if request.method=="POST":
        form=CardRegistrationForm(request.POST,instance=card) 
        if form.is_valid():
            form.save()
        return redirect("account_profile",id=card.id)

    else:
        form=CardRegistrationForm(instance=card) 
        return render(request,"edit_card.html",{"form":form})

def transaction_profile(request,id):
    transaction=Transaction.objects.get(id=id)
    return render (request,"transaction_profile.html",{"transaction":transaction})

def edit_transaction(request,id):
    transaction=Transaction.objects.get(id=id)
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST,instance=transaction) 
        if form.is_valid():
            form.save()
        return redirect("transaction_profile",id=transaction.id)

    else:
        form=TransactionRegistrationForm(instance=transaction) 
        return render(request,"edit_transaction.html",{"form":form})

def receipt_profile(request,id):
    receipts=Receipts.objects.get(id=id)
    return render (request,"receipts_profile.html",{"receipts":receipts})

def edit_receipt(request,id):
    receipts=Receipts.objects.get(id=id)
    if request.method=="POST":
        form=ReceiptRegistationForm(request.POST,instance=receipts) 
        if form.is_valid():
            form.save()
        return redirect("receipts_profile",id=receipts.id)

    else:
        form=ReceiptRegistationForm(instance=receipts) 
        return render(request,"edit_receipts.html",{"form":form})                           
  
