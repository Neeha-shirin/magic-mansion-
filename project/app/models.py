from django.db import models

class PropertyType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PropertyCategory(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Community(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Property(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    PUBLISH_STATUS = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=255)

    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(PropertyCategory, on_delete=models.SET_NULL, null=True)
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True, blank=True)

    area_min = models.PositiveIntegerField(help_text="Minimum area in sqft")
    area_max = models.PositiveIntegerField(help_text="Maximum area in sqft")
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField(null=True, blank=True)

    amenities = models.ManyToManyField(Amenity, blank=True)

    builder_name = models.CharField(max_length=150)
    builder_logo = models.ImageField(upload_to='builder_logos/', blank=True, null=True)

    video_url = models.URLField(blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    publish_status = models.CharField(max_length=10, choices=PUBLISH_STATUS, default='draft')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)  # Soft delete field

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.title}"
