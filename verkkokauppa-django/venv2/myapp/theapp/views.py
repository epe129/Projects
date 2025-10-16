from django.template import loader
from django.shortcuts import render
import json

def main(request):
    return render(request, 'index.html')

def products(request):
    total_price = 0
    orders_count = 0

    with open('products.json', 'r') as file:
        data = json.load(file)

    if 'orders' in request.POST:
        orders = request.POST.get("orders")
        data1 = orders.split() 

        new_order = {
            "id": data1[0],
            "malli": data1[1],
            "hinta": data1[2]
        }

        with open("orders.json", "r+") as f:
            file_data = json.load(f)

            if "orders" not in file_data:
                file_data["orders"] = []

            file_data["orders"].append(new_order)

            f.seek(0)
            json.dump(file_data, f, indent=4)
            f.truncate()

    with open('orders.json', 'r') as file:
        ordersdata = json.load(file)["orders"]

    for item in ordersdata:
        total_price += float(item["hinta"])
        orders_count += 1

    return render(request, 'products.html', {"json_data": data, "total": total_price, "o": orders_count})

def cart(request):

    with open('orders.json', 'r') as file:
        ordersdata = json.load(file)
    
        for key, value in ordersdata.items(): 
            for x in value: 
                print(x["id"])
                print(x["malli"])
                print(x["hinta"])

    return render(request, 'cart.html', {"orders": ordersdata})