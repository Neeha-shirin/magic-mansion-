from django import forms
from .models import Property, PropertyImage, Amenity

class PropertyForm(forms.ModelForm):
    amenities = forms.ModelMultipleChoiceField(
        queryset=Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    builder_logo = forms.ImageField(required=False)
    video_url = forms.URLField(required=False)

    class Meta:
        model = Property
        fields = [
            'title', 'description', 'price', 'location',
            'property_type', 'category', 'community',
            'area_min', 'area_max', 'bedrooms', 'bathrooms',
            'amenities', 'builder_name', 'builder_logo',
            'video_url', 'status', 'publish_status'
        ]
