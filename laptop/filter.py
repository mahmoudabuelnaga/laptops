import django_filters
from . import models
from django import forms

class LaptopFilter(django_filters.FilterSet):

    category = django_filters.ModelMultipleChoiceFilter(
        queryset = models.Category.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )

    screen_size = django_filters.ModelMultipleChoiceFilter(
        queryset = models.ScreenSize.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )
    
    color = django_filters.ModelMultipleChoiceFilter(
        queryset = models.Color.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )

    processor_family = django_filters.ModelMultipleChoiceFilter(
        queryset = models.ProcessorFamily.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )

    hard_disk_capacity = django_filters.ModelMultipleChoiceFilter(
        queryset = models.HardDiskCapacity.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )

    graphics_card_Capacity = django_filters.ModelMultipleChoiceFilter(
        queryset = models.GraphicsCardCapacity.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )

    operating_System = django_filters.ModelMultipleChoiceFilter(
        queryset = models.OperatingSystem.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )

    ram_size = django_filters.ModelMultipleChoiceFilter(
        queryset = models.RAMSize.objects.all(),
        widget = forms.CheckboxSelectMultiple,
    )

    # price = django_filters.ModelMultipleChoiceFilter(
    #     queryset = models.Laptop.objects.all().filter(price = price__gte  price__lte),
    #     widget = forms.NumberInput,
    # )
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = models.Laptop
        fields = [
        'category', 
        'screen_size', 
        'color', 
        'processor_family', 
        'hard_disk_capacity', 
        'graphics_card_Capacity', 
        'operating_System', 
        'ram_size', 
        'price__gte', 
        'price__lte',
        ]