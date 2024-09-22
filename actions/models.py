from django.db import models as m
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Action(m.Model):
    user = m.ForeignKey('auth.User',
                        related_name='actions',
                        on_delete=m.CASCADE)
    verb = m.CharField(max_length=55)
    created = m.DateTimeField(auto_now_add=True)
    target_ct = m.ForeignKey(ContentType,
                             blank=True,
                            null=True,
                            related_name='target_obj',
                            on_delete=m.CASCADE)
    target_id = m.PositiveIntegerField(null=True,
                                       blank=True)
    target = GenericForeignKey('target_ct', 'target_id')
    class Meta:
        indexes = [
            m.Index(fields=['-created']),
            m.Index(fields=['target_ct', 'target_id'])
        ]
        ordering = ['-created']
