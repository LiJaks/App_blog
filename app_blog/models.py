from django.db import models

class BlogRecordModel(models.Model):
    description = models.TextField(max_length=5000)
    date_creation = models.DateField(auto_now_add=True)
    user = models.ForeignKey('auth.User', default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'db_record'

class BlogImgModel(models.Model):
    blog_record = models.ForeignKey('BlogRecordModel', default=None, null=True, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images_blogs/')

    class Meta:
        db_table = 'db_img'

class UploadRecord(models.Model):
    file = models.FileField(upload_to='upload_record/')
