from django.shortcuts import render, redirect
from .forms import ProductForm
from .services import ProductService
from .models import Product

def products_list(request):

    search = request.GET.get('search')

    products = Product.objects

    if search:

        products = products.filter(
            name__icontains=search
        )

    return render(
        request,
        'products/list.html',
        {
            'products': products
        }
    )

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

def delete_product(request, product_id):

    product = Product.objects(
        id=product_id
    ).first()

    if product:

        product.delete()

    return redirect('products')