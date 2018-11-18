from django.shortcuts import render

# Create your views here.
from django .http import HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
from django .urls import reverse
from .models import Address, Customer, Order


def result1(request):
    if request.method=='POST':
        v = request.POST['Delivered']
        order = Order.objects.get(pk=v)
        order.Status=True
        order.save()
        objs = Order.objects.all()
        context = {'objs': objs}
    return render(request,'D_delivery/display.html',context=context)


def result(request):
    a = {"Order1": {'Customer_ID': "4365431", 'Order_ID': '1343554', 'Address_ID': '3531', 'Total_Price': 25,
                    'Discount': 3, 'Status': False},
         "Order2": {'Customer_ID': "533451", 'Order_ID': 'r134556', 'Address_ID': '45532', 'Total_Price': 25,
                    'Discount': 3, 'Status': False}}
    for k in ['Order1','Order2']:
        customerid = a[k]['Customer_ID']
        orderid = a[k]['Order_ID']
        addressid = a[k]['Address_ID']
        totalprice = a[k]['Total_Price']
        discount = a[k]['Discount']
        status = a[k]['Status']
        address = Address.objects.create(Address_ID=addressid)
        customer = Customer.objects.create(Customer_ID=customerid)
        Order.objects.create(customer=customer, address=address, Order_ID=orderid, Total_Price=totalprice, Discount=discount, Status=status)
    objs = Order.objects.all()
    context = {'objs': objs}
    return render(request, 'D_delivery/display.html', context=context)

