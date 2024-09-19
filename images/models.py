from django.db import models as m
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Image(m.Model):
    user = m.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name="images_created", 
        on_delete=m.CASCADE
    )
    title = m.CharField(max_length=200)
    slug = m.SlugField(max_length=200)
    url = m.URLField(max_length=2000)
    image = m.ImageField(upload_to="images/%Y/%m/%d/")
    description = m.TextField(blank=True)
    created = m.DateField(auto_now_add=True)
    users_like = m.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='images_liked',
                                   blank=True)

    class Meta:
        indexes = [m.Index(fields=["-created"])]
        ordering = ["-created"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("images:detail", args=[self.id, self.slug])
    
