from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    thumbnail=models.ImageField(blank=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title=models.CharField(max_length=200)
    subtext=models.TextField()
    thumbnail=models.ImageField()
    author=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug=slugify(self.title)
        super(Quiz, self).save(*args, **kwargs)




class Question(models.Model):
    type=models.CharField(max_length=200, choices=(('Text', 'Text'), ('Image', 'Image')))
    text=models.TextField()
    no=models.IntegerField()
    thumbnail=models.ImageField(null=True, blank=True)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Option(models.Model):
    img_option=models.ImageField(null=True, blank=True)
    text_option=models.TextField(null=True, blank=True)
    weight = models.CharField(max_length=200)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return '-> '+self.text_option + ' for '+self.question.text

class Answers(models.Model):
    min_score=models.IntegerField()
    max_score=models.IntegerField()
    name=models.TextField()
    thumbnail=models.ImageField()
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name












