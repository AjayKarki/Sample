from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Item(models.Model):
    name = models.CharField(max_length=100, default="Butter")
    quantity = models.IntegerField()


class Transaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()


@receiver(post_save, sender=Transaction, dispatch_uid="update_items")
def update_items(sender, instance, **kwargs):
    instance.item.quantity -= instance.quantity_sold
    instance.item.save()


@receiver(post_delete, sender=Transaction, dispatch_uid="update_items_delete")
def increase_items(sender, instance, **kwargs):
    instance.item.quantity += instance.quantity_sold
    instance.item.save()
