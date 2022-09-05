from django import forms
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipts, Reward, ThirdParty, Transaction, Wallet

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"       

class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
        model=Currency
        fields="__all__"      

class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields="__all__" 
class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Card
        fields="__all__"    

class ThirdpartyRegistrationForm(forms.ModelForm):
    class Meta:
        model=ThirdParty
        fields="__all__" 

class NotificationsRegistrationForm(forms.ModelForm):
    class Meta:
        model=Notifications
        fields="__all__" 

class ReceiptRegistationForm(forms.ModelForm):
    class Meta:
        model=Receipts
        fields="__all__"  

class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        models=Loan
        fields="__all__"   

class RewardRegistrtionForm(forms.ModelForm):
    class Meta:
        models=Reward
        fields="__all__"                          


