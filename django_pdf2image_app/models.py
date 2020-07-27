from django.db import models

class City(models.Model):
    cityid =models.AutoField(primary_key=True)
    name = models.CharField( max_length=50)

    class Meta:
        verbose_name = ("City")
        verbose_name_plural = ("Cities")

    def __str__(self):
        return self.name
        
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    ab = instance.date.strftime("%Y/%m/%d")
    return 'pdf/{0}/{1}/{2}'.format(instance.city.name,ab, filename)

class Images (models.Model):
    imageid =models.AutoField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date =models.DateField(auto_now=False, auto_now_add=False)
    page1  = models.FileField(upload_to=user_directory_path)

    class Meta:
        verbose_name = ("Image")
        verbose_name_plural = ("Images")

    def __str__(self):
        return self.city.name

