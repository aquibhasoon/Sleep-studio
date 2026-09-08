from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('mattress', 'Mattress'),
        ('pillow', 'Pillow'),
        ('bedsheet', 'Bedsheet'),
        ('cover', 'Cover'),
    ]

    COLLECTION_CHOICES = [
        ('premium', 'Premium'),
        ('standard', 'Standard'),
    ]

    name = models.CharField(max_length=200)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    collection = models.CharField(
        max_length=20,
        choices=COLLECTION_CHOICES,
        blank=True,
        null=True
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    size = models.CharField(
        max_length=100,
        blank=True
    )

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name