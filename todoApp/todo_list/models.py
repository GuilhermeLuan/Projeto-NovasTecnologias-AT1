from django.db import models

# Create y
# our models here.
class todo(models.Model):
    title = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " - " + self.created_at.strftime("%d/%m/%Y") + " - " + str(self.isCompleted)