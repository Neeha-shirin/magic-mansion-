from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import Property, PropertyImage
from .forms import PropertyForm, PropertyImageFormSet

def property_list(request):
    properties = Property.objects.filter(deleted_at__isnull=True)
    return render(request, 'dashboard/property_list.html', {'properties': properties})


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        formset = PropertyImageFormSet(request.POST, request.FILES, queryset=PropertyImage.objects.none())

        if form.is_valid() and formset.is_valid():
            property_instance = form.save()
            for image_form in formset:
                if image_form.cleaned_data:
                    PropertyImage.objects.create(
                        property=property_instance,
                        image=image_form.cleaned_data.get('image')
                    )
            return redirect('property_list')
    else:
        form = PropertyForm()
        formset = PropertyImageFormSet(queryset=PropertyImage.objects.none())

    return render(request, 'dashboard/add_property.html', {'form': form, 'formset': formset})


def edit_property(request, pk):
    property_instance = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        formset = PropertyImageFormSet(request.POST, request.FILES, queryset=property_instance.images.all())

        if form.is_valid() and formset.is_valid():
            form.save()
            for image_form in formset:
                if image_form.cleaned_data:
                    PropertyImage.objects.create(
                        property=property_instance,
                        image=image_form.cleaned_data.get('image')
                    )
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property_instance)
        formset = PropertyImageFormSet(queryset=property_instance.images.all())

    return render(request, 'dashboard/edit_property.html', {'form': form, 'formset': formset, 'property': property_instance})


def delete_property(request, pk):
    property_instance = get_object_or_404(Property, pk=pk)
    property_instance.deleted_at = now()
    property_instance.save()
    return redirect('property_list')


def toggle_property_status(request, pk):
    property_instance = get_object_or_404(Property, pk=pk)
    property_instance.status = 'inactive' if property_instance.status == 'active' else 'active'
    property_instance.save()
    return redirect('property_list')
