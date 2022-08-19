from django.contrib import admin
from .models import Customer,Wallet,Currency,Reward,Receipts,Transaction,ThirdParty,Card,Loan,Notifications,Account
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","address",)
    search_fields = ("first_name","last_name",)

class ReceiptAdmin(admin.ModelAdmin):
    new_display=("receipt_type","receipt_date","recipt_number","account","total_account","recipt_file",)
    my_fields=("receipt_type","receipt_date","recipt_number",)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_ref","wallet","transaction_amount","transaction_type",
    "transaction_charge","transaction_date","receipt","original_account","destination_account",)
    search_fields=("transaction-ref","transaction_type","transaction_date",)

class CardAdmin(admin.ModelAdmin):
    list_display=("date_Issued","card_name","card_number","card_type",
    "expiry_date","card_status","cvv_security","wallet","account",)    
    search_fields=("card_name","card_number","cvv_security","card_type",)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=("account","name","thirdparty_id","phone_Number","currency",)    
    search_fields=("name","thirdparty_id",)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=("amount","country_of_origin",)    
    search_fields=("amount","country_of_origin",) 

class WalletAdmin(admin.ModelAdmin):
    list_display=("currency","customer","balance","amount","date","status","pin",)    
    search_fields=("customer","date","status",) 

class RewardAdmin(admin.ModelAdmin):
    list_display=("transaction","date","customer","gender","bonus",)    
    search_fields=("date","customer",)  

class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_number","loan_type","amount","date","wallet",
    "interest_rate","guaranter","due_date","loan_balance","loan_term",)    
    search_fields=("loan_number","loan_type","date",)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("notification_Id","status","date","recipient",)    
    search_fields=("notification_Id","recipient","status",)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_number","balance","wallet",)    
    search_fields=("account_number","wallet",)                                


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Receipts,ReceiptAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(ThirdParty,ThirdPartyAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Reward,RewardAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Notifications,NotificationAdmin)
admin.site.register(Account,AccountAdmin)


