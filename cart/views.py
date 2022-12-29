import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action

from cart import models
from cart.serializers import CartInfoSerializer


class CartVeiwSet(viewsets.ModelViewSet):
    """
    API 添加商品到购物车
    """

    @action(methods=['POST'], detail=False, url_path='cart/to_cart/')
    def addToCart(self, request):
        """
        比对数据库中的用户信息
        """
        goodsData = json.loads(request.body.decode('utf-8'))
        print(goodsData)
        goods_count = int(goodsData.get("goods_count"))
        goods_cover_img = goodsData.get("goods_cover_img")
        goods_id_id = goodsData.get("goods_id_id")
        selling_price = goodsData.get("selling_price")
        user_id_id = goodsData.get("user_id_id")
        goods_name = goodsData.get("goods_name")
        count = models.Cart.objects.filter(user_id_id=user_id_id, goods_id_id=goods_id_id).first()

        if count:
            goods_count += int(count.goods_count)
            res = models.Cart.objects.filter(goods_id_id=goods_id_id, user_id_id=user_id_id).update(goods_count=goods_count)
        else:
            res = models.Cart.objects.create(
                goods_count=goods_count,
                goods_cover_img=goods_cover_img,
                goods_id_id=goods_id_id,
                selling_price=selling_price,
                user_id_id=user_id_id,
                goods_name=goods_name,
            )

        if res != '':
            return JsonResponse({'status': 200, 'message': "商品添加成功"}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '注册失败'})

    @action(methods=['GET'], detail=False, url_path='cart/get_cart/')
    def getCart(self, request):
        """
        比对数据库中的用户信息
        """
        user_id = request.GET.get('id')
        # print(request.GET)
        queryset = models.Cart.objects.filter(user_id_id=user_id, goods_count__gt=0)
        cartList = CartInfoSerializer(queryset, many=True)
        # print(cartList.data)

        if cartList != '':
            return JsonResponse({'status': 200, 'message': "获取购物车列表成功", 'data': cartList.data}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '购物车获取失败'})

    @action(methods=['PUT'], detail=False, url_path='cart/update_cart/')
    def updateCart(self, request):
        """
        更改数据库中的购物车信息
        """
        cartData = json.loads(request.body.decode('utf-8'))

        item_id = cartData.get("cart_item_id")
        # item_is_deleted = cartData.get("is_deleted")
        item_count = cartData.get("goods_counts")
        # print(item_count)
        cartItem = models.Cart.objects.filter(cart_item_id=item_id).first()
        res = None
        if item_count == 0:
            res = models.Cart.objects.filter(cart_item_id=item_id).update(goods_count=item_count)
        elif item_count != cartItem.goods_count:
            res = models.Cart.objects.filter(cart_item_id=item_id).update(goods_count=item_count)

        if res != '':
            return JsonResponse({'status': 200, 'message': "购物车更新成功"}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '购物车更新失败'})