from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json

def main(request):
    
    return render(request, 'index.html')

def products(request):

    with open('products.json', 'r') as file:
        data = json.load(file)    
    
    if 'orders' in request.POST:
        orders = request.POST.get("orders") 
        data1 = orders.split()

        write_oders = {
            "orderid" : f"{data1[0]}", 
            "malli" : f"{data1[1]}", 
            "hinta" : f"{data1[2]}" 
        }
        # appends orders in json file
        with open("orders.json", "r+") as f:
            file_data = json.load(f)
            for key, value in file_data.items():
                for a in value:
                    if a["orderid"] == orders:
                        orders = ""
            
            if orders == "":
                pass
            else:
                file_data["orders"].append(write_oders)
                                
                f.seek(0)
                                
                json.dump(file_data, f, indent=4)     
    
    
    with open('orders.json', 'r') as file:
        ordersdata = json.load(file)    
    
    # for keyy, valuee in ordersdata.items():
    #     for xx in valuee:
    #         print(xx)


    return render(request, 'products.html',  {"json_data": data, "o_data": ordersdata})

def cart(request):

    return render(request, 'cart.html')
