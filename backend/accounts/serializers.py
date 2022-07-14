from rest_framework import serializers
from .models import Account, Customer, Transaction
import uuid
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string


def createAcNo():

    account_no = get_random_string(length=20, allowed_chars='1234567890'),
    return account_no


class CustomerSerializer(serializers.ModelSerializer):

    account_type = serializers.ChoiceField(choices=Account.ACCOUNT_TYPE)


    class Meta:
        model = Customer
        fields = ('email', 'password', 'first_name', 'last_name', 'account_type')

    def create(self, validated_data):
        username=validated_data.get('email')
        password = make_password(validated_data.pop('password'))
        account_id=uuid.uuid4()
        account_type = validated_data.pop('account_type')
        instance = Customer.objects.create(*validated_data, username = username,
                                        password=password, user_type=Customer.CUSTOMER)

        Account.objects.create(user = instance, account_id = account_id,
                               account_number = createAcNo, account_type = account_type)
        return instance


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'email', 'first_name', 'last_name', 'user_type', 'mobile_no')


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'account_id', 'user', 'account_number', 'account_type', 'current_balance')


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'transaction_id', 'transaction_type', 'amount', 'account')