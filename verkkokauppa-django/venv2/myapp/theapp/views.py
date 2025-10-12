from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json

global isOrderId
global theid
theid = [] 
isOrderId = False

def main(request):
    orderid = ""
    global isOrderId

    if "Oid" in request.POST:
        orderid = request.POST.get("Oid")
        theid.append(orderid)
        isOrderId = True
    
    return render(request, 'index.html', {"onko": isOrderId})

def products(request):
    ordersdata = {}
    total_price = 0
    oders = 0
    
    if len(theid) > 0: 
        orderid = theid[0]
    
    with open('products.json', 'r') as file:
        data = json.load(file)    
    
    if 'orders' in request.POST:
        orders = request.POST.get("orders") 
        data1 = orders.split()

        write_ordes = {
            "id" : f"{data1[0]}", 
            "malli" : f"{data1[1]}", 
            "hinta" : f"{data1[2]}" 
        }

        # appends orders in json file
        with open("orders.json", "r+") as f:
            file_data = json.load(f)

            if orderid not in file_data:
                file_data[orderid] = []
                
            file_data[orderid].append(write_ordes)

            f.seek(0)
            json.dump(file_data, f, indent=4)
            f.truncate()

    
    with open('orders.json', 'r') as file:
        ordersdata = json.load(file)    
    
    for keyy, valuee in ordersdata.items():
        for xx in valuee:
            total_price += float(xx["hinta"])
            oders += 1

    return render(request, 'products.html',  {"json_data": data, "o_data": ordersdata, "total": total_price, "o": oders})

def cart(request):
    if len(theid) > 0: 
        orderid = theid[0]
    
    return render(request, 'cart.html')
