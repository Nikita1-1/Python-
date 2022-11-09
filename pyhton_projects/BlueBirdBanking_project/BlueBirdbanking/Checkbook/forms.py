
# We’re going to create an Account form and a Transaction
# form based on the models we created.
# In your forms.py file add the following code


from django.forms import ModelForm
from .models import Account, Transaction


# creates Account from based on Account Model

class AccountForm (ModelForm):
    class Meta:
        model = Account
        fields = '__all__'



class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'


# Now we need to import these forms in the views.py file
# as well as the CreateNewAccount and AddTransaction templates.