## PRTS电商系统后端

#### 使用Django-rest-framework搭建

​		包含用户，商品，订单，购物车，地址等API接口

​		API返回数据格式为JSON

```json
{
"status":"200",
"message":"获取商品数据成功",
"data":"[{...数据}]",
"code":"1000"
}
```



##### 	权限校验

​		使用JWT进行用户权限的校验

​		相比与传统的Session、Token方式，JWT不需要将验证信息存入数据库中，减少了对服务器端的压力，也防止用户受到CSRF攻击
