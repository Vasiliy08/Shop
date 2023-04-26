from .models import Product, Category
from modeltranslation.translator import register, TranslationOptions
from orders.models import OrderItem, Order


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ['name', 'slug']


@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ['first_name', 'last_name', 'address', 'city']


@register(OrderItem)
class OrderItemTranslationOptions(TranslationOptions):
    fields = ['product', ]