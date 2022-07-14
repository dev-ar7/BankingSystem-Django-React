from django.urls import path
from .views import CustomerSignUpAPIView, LogInAPIView, CustomerDetailsAPIView, CustomerDepositAPIView, CustomerWithdrawAPIView


urlpatterns = [
    path('signup', CustomerSignUpAPIView.as_view(), name='signup'),
    path('login', LogInAPIView.as_view(), name='login'),
    path('customer/deposit', CustomerDepositAPIView.as_view(), name='deposit'),
    path('customer/withdraw', CustomerWithdrawAPIView.as_view(), name='withdraw'),
    path('customer/account-details', CustomerDetailsAPIView.as_view(), name='customer-details'),
]