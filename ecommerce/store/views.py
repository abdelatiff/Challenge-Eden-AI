from django.shortcuts import render,redirect
from .models import *
from cart.cart import Cart
# Create your views here.
lst = [['Fromage','1','fromage.jpg',3.0],['Pain','2','pain.jpg',1.0],['Tomate','3','tomate.jpg',1.0]]
def store(request):

    queryset = product.objects.filter(name='fromage')

    for i in lst:
        prod = product()
        prod.name = i[0]
        prod.Reference = i[1]
        prod.image = i[2]
        prod.price = i[3]
        prod.save()

    qs = product.objects.all()
    key_set = set()
    delete_ids_list = []
    for object in qs:
        object_key = object.name  # photo_id here
        if object_key in key_set:
            delete_ids_list.append(object.id)
        else:
            key_set.add(object_key)
    product.objects.filter(id__in=delete_ids_list).delete()
    query_results = product.objects.all()
    print(query_results)
    context = {'query_results': query_results}
    return render(request, 'store.html',context=context)





def cart_add(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.add(product=Product)
    return redirect("/")



def item_clear(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.remove(Product)
    return redirect("/cart/cart_detail/")



def item_increment(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.add(product=Product)
    return redirect("/cart/cart_detail/")



def item_decrement(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.decrement(product=Product)
    return redirect("/cart/cart_detail/")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/cart/cart_detail/")



def cart_detail(request):
    return render(request, 'cart.html')