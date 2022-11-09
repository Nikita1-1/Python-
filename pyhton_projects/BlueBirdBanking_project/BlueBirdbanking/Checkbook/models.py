from django.db import models

# Choices for a transaction
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # defanies the model Manager for Acounts
    # A Manager’s base QuerySet returns all objects in the system.

    Accounts = models.Manager()

    def __str__(self):
        return self.first_name + '' + self.last_name


class Transaction(models.Model):
    data = models.DateTimeField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transaction = models.Manager()
