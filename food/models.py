from django.db import models

class Receipe(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    prep_time = models.CharField(max_length=100, blank=False, null=False)
    cook_time = models.CharField(max_length=100, blank=False, null=False)
    stars = models.SmallIntegerField(
        blank=False, null=False, default=1,
        choices=[
            (1, 'One star'),(2, 'Two star'), (3, 'Three star'),(4, 'Four star'),(5, 'Five star')
        ]
    )
    posted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    order = models.IntegerField(blank=False, null=False)
    recipe = models.ForeignKey(Receipe, blank=False, null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    order = models.IntegerField(blank=False, null=False)
    receipe = models.ForeignKey(Receipe, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    author = models.CharField(max_length=300, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    posted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class GetInTouch(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    sent_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name