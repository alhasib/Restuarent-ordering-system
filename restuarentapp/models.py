from django.db import models

class RestuarentInfo(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length = 50)
    restuarent = models.ForeignKey(RestuarentInfo, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='item_image/', blank=True)
    
    def __str__(self):
        return self.name

class CartItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.item)


class Cart(models.Model):
    cart_item = models.ManyToManyField(CartItem)
    active = models.BooleanField(default = True)
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    token_number = models.CharField(max_length = 20)
    table_number = models.ImageField()
    menu = models.ManyToManyField(MenuItem)
    quantity = models.IntegerField()

    def __str__(self):
        return self.token_number

    

    

    

    
