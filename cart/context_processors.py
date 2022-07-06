from . models import Cart,CartItem
from . views import cart_id


def counter(request):
    item_count=0
    if 'admin' in request.path:
        return  {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=cart_id(request))
            car_item=CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in car_item:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)


