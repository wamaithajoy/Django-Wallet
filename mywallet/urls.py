from django.urls import path

from .views import account, account_profile, card, card_profile, currency, customer_profile, edit_account, edit_card, edit_profile, edit_receipt, edit_transaction, edit_wallet, list_Customer, list_account, list_card, list_currency, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallet, loan, notification, receipt, receipt_profile, register_customer, reward, thirdparty, transaction, transaction_profile, wallet, wallet_profile

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
 path("customers/<int:id>/",customer_profile,name="customer_profile"),
 path("customers/edit/<int:id>/",edit_profile,name="edit_profile"),
 path("wallet/<int:id>/",wallet_profile,name="wallet_profile"),
 path("wallet/edit/<int:id>/",edit_wallet,name="edit_wallet"),
 path("account/<int:id>/",account_profile,name="account_profile"),
 path("account/edit/<int:id>/",edit_account,name="edit_account"),
 path("card/<int:id>/",card_profile,name="card_profile"),
 path("card/edit/<int:id>/",edit_card,name="edit_card"),
 path("transaction/<int:id>/",transaction_profile,name="transaction_profile"),
 path("transaction/edit/<int:id>/",edit_transaction,name="edit_transaction"),
 path("receipts/<int:id>/",receipt_profile,name="receipts_profile"),
 path("receipts/edit/<int:id>/",edit_receipt,name="edit_receipt"),
]


 






 