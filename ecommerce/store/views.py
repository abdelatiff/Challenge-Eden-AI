from django.shortcuts import render
from .models import *
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