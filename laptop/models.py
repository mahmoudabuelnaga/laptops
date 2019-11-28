from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Inher(models.Model):
    name    = models.CharField(max_length=255)
    slug    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    # def save(self,*args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super(Category, self).save(*args, **kwargs)



class Category(Inher):
    img_cat = models.ImageField(upload_to='category', default='category_default.jpg')

    # def __str__(self):
    #     return self.name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)
    
class ScreenSize(Inher):
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(ScreenSize, self).save(*args, **kwargs)


class Color(Inher):
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Color, self).save(*args, **kwargs)

class ProcessorFamily(Inher):
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(ProcessorFamily, self).save(*args, **kwargs)

class HardDiskCapacity(Inher):
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(HardDiskCapacity, self).save(*args, **kwargs)

class GraphicsCardCapacity(Inher):
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(GraphicsCardCapacity, self).save(*args, **kwargs)


class OperatingSystem(Inher):
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(OperatingSystem, self).save(*args, **kwargs)

class RAMSize(Inher):
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(RAMSize, self).save(*args, **kwargs)

class Laptop(models.Model):
    name                   = models.CharField(max_length=255)
    slug                   = models.SlugField(null=True, blank=True,max_length=255)
    price                  = models.DecimalField(max_digits=10,decimal_places=2)
    img_lap                = models.ImageField(upload_to='laptops', default='laptop_default.jpg')
    category               = models.ForeignKey(Category, on_delete=models.CASCADE)
    screen_size            = models.ForeignKey(ScreenSize, on_delete=models.CASCADE)
    color                  = models.ForeignKey(Color, on_delete=models.CASCADE)
    processor_family       = models.ForeignKey(ProcessorFamily, on_delete=models.CASCADE)
    hard_disk_capacity     = models.ForeignKey(HardDiskCapacity, on_delete=models.CASCADE)
    graphics_card_Capacity = models.ForeignKey(GraphicsCardCapacity, on_delete=models.CASCADE)
    operating_System       = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    ram_size               = models.ForeignKey(RAMSize, on_delete=models.CASCADE)
    content                = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Laptop, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk, self.slug])
