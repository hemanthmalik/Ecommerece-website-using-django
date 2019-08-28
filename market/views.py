from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order, OrderUpdate
import json
# Create your views here.


def index(request):
    product = Product.objects.values("category")
    categories = {i["category"] for i in product}
    listings = []
    for j in categories:
        catItems = Product.objects.filter(category=j)
        listings.append(catItems)
    return render(request, "market/index.html", {"listings": listings})


def about(request):
    return HttpResponse("this is the about page.")


def contact(request):
    return HttpResponse("this is the contact us page.")


def tracker(request):
    status = {}
    if request.method=="POST":
        order_id = request.POST.get("orderId", 0)
        email = request.POST.get('email', "")
        try:
            orderTrack = Order.objects.get(order_id=order_id, email=email)
        except:
            orderTrack = None
        if orderTrack:
            try:
                status=OrderUpdate.objects.get(order_id=order_id)
                status = {"order_status": status.order_status, "timestamp": status.timestamp, "itemsJson": orderTrack.itemsJson}
            except Exception as e:
                status = {}
        status=json.dumps(status, default=str)
        return HttpResponse(status)
    return render(request, "market/tracker.html", {"status": status})


def productview(request, pId):
    productData = Product.objects.get(id = pId)
    return HttpResponse("this is the productview page."+ productData.subcategory + str(productData))


def search(request):
    if request.method == "POST":
        searchVal = request.POST.get('search')
        items = Product.objects.all()
        searchRes = []
        for item in items:
            if searchVal in item.desc or searchVal in item.product_name:
                searchRes.append(item)

        return render(request, "market/search.html", {"search" : searchRes})
    else:
        return HttpResponse("Sorry! Page is not found.")


def checkout(request):
    saved = 0
    if request.POST.get('hello'):
        return HttpResponse("shit is fucked up")
    if request.method == "POST":
        # if request.POST.get('cartItems'):
        #     cartData = []
        #     for i in json.loads(request.POST.get('cartItems')):
        #         cartData.append(Product.objects.get(id = int(i)))
        #     return render(request, 'market/checkout.html', {"cartData": cartData})
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address1 = request.POST.get('address1', "")
        address2 = request.POST.get('address2', "")
        state = request.POST.get('state', "")
        city = request.POST.get('city', "")
        zip = request.POST.get('zip_code', "")
        itemsJson = request.POST.get('itemsJson', "")
        order = Order(name=name, email=email, address1=address1, address2=address2, state=state, city=city, zip=zip, itemsJson=itemsJson)
        order.save()
        saved = 1
        tracker_set=OrderUpdate(order_id=order.order_id)
        tracker_set.save()
    return render(request, 'market/checkout.html', {"saved": saved})

def testpage(request):
    return HttpResponse("testpage")
