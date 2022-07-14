import uuid
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from django.db import transaction
from .models import Account, Transaction, Customer
from .serializers import AccountSerializer, TransactionSerializer, CustomerSerializer, UserDetailSerializer
from .utils import BankAccountTransactions
from .constants import CREDIT_AMOUNT_EMAIL_BODY, DEBIT_AMOUNT_EMAIL_BODY


class CustomerSignUpAPIView(generics.CreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request):
        if request.method == 'POST':
            email = request.data.get('email')
            user_exists = Customer.objects.filter(email = email).exists()
            if user_exists:
                return Response({'message': 'Request Failed! User already Exist!'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                token = Token.objects.create(user=instance)
                data = dict()
                data['token'] = token.key
                return Response({'message': 'User Account Created Successfully.'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, {'message': 'Request Failed! Invalid Data!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class LogInAPIView(generics.UpdateAPIView):

    queryset = Customer.objects.all()
    serializer_class = UserDetailSerializer

    def post(self, request):
        if request.method == 'POST':
            password = request.data.pop('password')

            try:
                user = self.queryset.get(request.data)
                auth_token = Token.objects.get(user=user).key
                if not check_password(password, user.password) or (user.user_type != request.data.get('user_type')):
                    return Response({'message': 'Request Failed! Wrong Usernaem or Password'},
                                    status=status.HTTP_401_UNAUTHORIZED)
            except:
                return Response({'message': 'Request Failed! Wrong Usernaem or Password'},
                                    status=status.HTTP_401_UNAUTHORIZED)

            user.is_active = True
            user.save()
            data = self.serializer_class(instance=user).data
            data['token'] = auth_token
            return Response({'message': 'User Logged In Successfully.'},
                                    status=status.HTTP_200_OK)


class CustomerDepositAPIView(generics.CreateAPIView):

    serializer_class = TransactionSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    @transaction.atomic
    def post(self, request):

        if request.method == 'POST':
            user = request.user
            account = Account.objects.select_for_update().get(user=user)
            amount = request.data.get('amount')
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                try:
                    deposit_amount = BankAccountTransactions(amount, account).deposit_amount()
                except:
                    return Response({'message': 'Max Value for Account Balance Exceeded!'}, status=status.HTTP_400_BAD_REQUEST)
            
                instance = serializer.save(account = account, 
                                        transaction_id = uuid.uuid4(), 
                                        transaction_type = Transaction.CREDIT)
                transaction_msg = {'message': CREDIT_AMOUNT_EMAIL_BODY}
                return Response(serializer.data, {'message': transaction_msg}, status=status.HTTP_200_OK)
            return Response(serializer.errors, {'message': 'Request Failed!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CustomerWithdrawAPIView(generics.CreateAPIView):

    serializer_class = TransactionSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):

        if request.method == 'POST':
            user = request.user
            account = Account.objects.select_for_update().get(user=user)
            amount = request.data.get('amount')
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                try:
                    withdraw_amount = BankAccountTransactions(amount, account).withdraw_amount()
                except:
                    return Response({'message': 'Negetive Amount Not Allowed!'}, status=status.HTTP_400_BAD_REQUEST)

                if withdraw_amount:
                    instance = serializer.save(account = account,
                                            transaction_id = uuid.uuid4(), 
                                            transaction_type = Transaction.DEBIT)
                    transaction_msg = {'message': DEBIT_AMOUNT_EMAIL_BODY}
                return Response(serializer.data, {'message': transaction_msg}, status=status.HTTP_200_OK)
            return Response(serializer.errors, {'message': 'Request Failed!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

                
class CustomerDetailsAPIView(generics.RetrieveAPIView):

    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )

    def retrive(self, request):
        try:
            user = request.user
            instance = Account.objects.get(user=user)
        except:
            return Response({'message': 'The user_id you\'re trying to access does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(instance)
        return Response(serializer.data, {'message': 'Request Successful'}, status=status.HTTP_200_OK)