from django.db import models as m
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.


class Profile(m.Model):
    user = m.OneToOneField(settings.AUTH_USER_MODEL, on_delete=m.CASCADE)
    date_of_birth = m.DateField(blank=True, null=True)
    photo = m.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self) -> str:
        return f"Profile of {self.user.username}"

class Contact(m.Model):
    user_from = m.ForeignKey('auth.User',
                             related_name='rel_from_set',
                             on_delete=m.CASCADE)
    user_to = m.ForeignKey('auth.User',
                           related_name='rel_to_set',
                           on_delete=m.CASCADE)
    created = m.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            m.Index(fields=['-created']),
        ]
        ordering = ['-created']
        
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'
    
user_model = get_user_model()
user_model.add_to_class('following',
                        m.ManyToManyField('self',
                                            through=Contact,
                                            related_name='followers',
                                            symmetrical=False))