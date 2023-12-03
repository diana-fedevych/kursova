from django.db import models

class Texts(models.Model):
    title = models.CharField('Text title', max_length=50)
    full_text = models.TextField('Full text')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'