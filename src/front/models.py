from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=True)
    prep_time = models.CharField(max_length=150, blank=False, null=False)
    cook_time = models.CharField(max_length=150, blank=False, null=False)
    posted_at = models.DateField(auto_now_add=True, blank=False, null=False)
    stars = models.SmallIntegerField(
        blank=False, null=False, default=1,
        choices=[
            (1, 'One star'), (2, 'Two stars'), (3, 'Three stars'), (4, 'Four stars'), (5, 'Five stars')
        ]
    )

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    order = models.IntegerField(blank=False, null=False)
    recipe = models.ForeignKey(Recipe, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=500, blank=False, null=False)
    order = models.IntegerField(blank=False, null=False)
    recipe = models.ForeignKey(Recipe, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.CharField(max_length=100, blank=True, null=True)


class Blog(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    short_description = models.CharField(max_length=1000, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    posted_at = models.DateField(blank=False, null=False)
    author = models.ForeignKey(Author, blank=False, null=True, on_delete=models.SET_NULL)
    stars = models.SmallIntegerField(
        blank=False, null=False, default=1,
        choices=[
            (1, 'One star'), (2, 'Two stars'), (3, 'Three stars'), (4, 'four_stars'), (5, 'five stars')
        ]
    )

    def __str__(self):
        return self.title


class GetInTouch(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.CharField(max_length=150, blank=False, null=False)
    subject = models.CharField(max_length=150, blank=False, null=False)
    message = models.TextField(max_length=150, blank=False, null=False)
    sent_at = models.DateTimeField(blank=False, null=True)

    def __str__(self):
        return self.name


class Followers(models.Model):
    email = models.EmailField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.email
