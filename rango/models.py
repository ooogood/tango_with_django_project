from django.db import models
# chapter 6
from django.template.defaultfilters import slugify
# Create your models here.
# chapter 5
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	# chapter 6
	slug = models.SlugField(unique=True)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Categories'
	def __str__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	def __str__(self):
		return self.title