from django.db import models


class ContactInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    last_name = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    email = models.EmailField(
        max_length=50,
        blank=False,
        null=False
    )
    verify_email = models.EmailField(
        max_length=50,
        blank=False,
        null=False
    )
    message = models.TextField(
        max_length=500,
        blank=False,
        null=False,
        help_text="Maximum allowed: 500 characters"
    )
