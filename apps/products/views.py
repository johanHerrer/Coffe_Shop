from django.shortcuts import render, redirect

from .forms import ProductForm
from .services import ProductService
from .models import Product
from apps.users.decorators import admin_required

def products_list(request):
    search_query = request.GET.get('search')
    
    if search_query:
        products = Product.objects(name__icontains=search_query)
    else:
        products = Product.objects()

    return render(request, 'products/list.html', {'products': products})


@admin_required
def create_product(request):

    form = ProductForm()

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            ProductService.create_product(
                form.cleaned_data,
                request.FILES.get('image')
            )

            return redirect('products')

    return render(
        request,
        'products/create.html',
        {
            'form': form
        }
    )

@admin_required
def delete_product(request, product_id):
    product = Product.objects(id=product_id).first()
    if product:
        product.delete()
    return redirect('products')


def dashboard_products(request):
    products = Product.objects()
    return render(request, 'dashboard/products.html', {'products': products})