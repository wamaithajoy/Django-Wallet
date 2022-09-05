from django.urls import path

from .views import account, card, currency, loan, notification, receipt, register_customer, reward, thirdparty, transaction, wallet

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
 path("reward",reward,name="reward")
 
]
 








 