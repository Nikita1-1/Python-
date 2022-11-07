from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import productForm
from .models import Product

def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/product_page.html', {'products': products})



def details(request, pk):# when user request info, it comes here to pull it
    pk = int(pk) #primary key number
    item = get_object_or_404(Product, pk=pk)# chek for an item if its not here then send 404
    form = productForm(data=request.POST or None, instance=item)# when post the item
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')# goes back to admin console
        else:
            print(form.errors)
    else:
        return render(request, 'products/present_product.html', {'form': form})
