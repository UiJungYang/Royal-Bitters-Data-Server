from django.db import models

<<<<<<< Updated upstream
# Create your models here.
class AlcoholImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=100, null=True)
=======


class AlcoholImage(models.Model):
    id = models.AutoField(primary_key=True)
    alcoholImage = models.CharField(max_length=100, null=True)
>>>>>>> Stashed changes

    class Meta:
        db_table = 'alcohol_image'
        app_label = 'alcohol'
<<<<<<< Updated upstream


    def getImage(self):
        return self.image
=======
>>>>>>> Stashed changes
