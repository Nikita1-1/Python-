
from django.shortcuts import render, get_object_or_404,redirect
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction



def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']# if the form is submitted retrive which account the user whants to view
        return balance(request, pk) # call balance function to render that account's Balance Sheet
    content = {'form': form}
    return render(request, 'checkbook/index.html')


# this function will render the Create New Account page when requeste


def create_account(request):
    form = AccountForm(data=request.POST or None) # Retrive the account form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index') # Returns user back to home page
    content = {'form': form}# saves content to the template as a dictionary
        # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # retrive the requested account using its primiry key
    transactions = Transaction.Transactions.filter(account=pk) # retrive all of that account's transactions
    current_total = account.initial_deposit # create account that variable, starting with initial deposit value
    table_contents ={} # creates a dictionary into which transaction information will be placed
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount # if deposit than add amount
            table_contents.update({t: current_total}) # add transaction and total to the dictionary
        else:
            current_total -= t.amount # if withdrawl substract money
            table_contents.update({t: current_total})
        # pass account, account total balance and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'blance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account'] # retrive which account transaction  was for
            form.save()
            return balance(request, pk)# renders balance of the accounts Balace Sheets
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
# Create your views here.



