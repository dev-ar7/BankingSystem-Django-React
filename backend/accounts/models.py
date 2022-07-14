from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError


class Customer(models.Model):

    MANAGER = 'manager'
    EMPLOYEE = 'employee'
    CUSTOMER = 'customer'

    USER_TYPE = (
        (MANAGER, 'manager'),
        (CUSTOMER, 'customer'),
        (EMPLOYEE, 'employee')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=175, blank=False, null=False)
    last_name = models.CharField(max_length=175, blank=False, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=12, blank=False, null=False)
    user_type = models.CharField(max_length=25, choices=USER_TYPE, default=CUSTOMER)
    mobile_no = models.CharField(max_length=10, null=False)
    branch_name = models.CharField(max_length=255, null=True)


    def __str__(self):
        return f'{self.user} - {self.user_type}'


class Account(models.Model):

    SAVING = 'saving'
    CURRENT = 'current'

    ACCOUNT_TYPE = (
        (SAVING, 'saving'),
        (CURRENT, 'current')
    )

    user = models.OneToOneField(Customer, on_delete=models.PROTECT, related_name='customer')
    account_id = models.CharField(max_length=20, unique=True)
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE, default=SAVING)
    current_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.user} - {self.current_balance}'


class Transaction(models.Model):

    CREDIT = 'credit'
    DEBIT = 'debit'

    TRANSACTION_TYPE = (
        (CREDIT, 'credit'),
        (DEBIT, 'debit')
    )

    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.account} - {self.transaction_type} - {self.amount}'

    def save(self, *args, **kwargs):
        if self.id is None:
            super(Transaction, self).save(*args, **kwargs)
        else:
            raise IntegrityError('Sorry! This model instance cannot be updated.')

