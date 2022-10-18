from django.db import models

# Create your models here.

class Guest(models.Model):
    # myno = models.AutoField(auto_created=True, primary_key=True) # 이렇게 하면 id가 생기지 않는다.
    title = models.CharField(max_length=50)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    # 정렬
    class Meta:
        # ordering = ('title', ) <,붙이기>
        # ordering = ('title', 'id')
        ordering = ('-id',)

