from django.urls import path

from .views import account, card, currency, list_Customer, list_account, list_card, list_currency, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallet, loan, notification, receipt, register_customer, reward, thirdparty, transaction, wallet

urlpatterns = [
 path("register/",register_customer,name="registration"), 
 path("wallet/",wallet,name="wallet") ,
 path("currency",currency,name="currency"),
 path("account",account,name="account"),
 path("transaction",transaction,name="transaction"),
 path("card",card,name="card"),
 path("thirdparty",thirdparty,name="thirdparty"),
 path("notification",notification,name="notification"),
 path("receipt",receipt,name="receipt"),
 path("loan",loan,name="loan"),
 path("reward",reward,name="reward"),
 path("customers",list_Customer,name="customers_list"),
 path("walletlist",list_wallet,name="walletlist"),
 path("currencylist",list_currency,name="currencylist"),
 path("accountlist",list_account,name="accountlist"),
 path("transactionlist",list_transaction,name="transactionlist"),
 path("cardlist",list_card,name="cardlist"),
 path("thirdpartylist",list_thirdparty,name="thirdpartylist"),
 path("notificationlist",list_notification,name="notificationlist"),
 path("receiptlist",list_receipt,name="receiptlist"),
 path("loanlist",list_loan,name="loanlist"),
 path("rewardlist",list_reward,name="rewardlist"),

 
]
 








 