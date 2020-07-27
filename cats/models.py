from django.db import models
from django.urls import reverse

class Brend(models.Model):
	# бренд товара
	name = models.CharField('Бренд', max_length=30, unique=True)
	url = models.SlugField(max_length=130, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Бренд'
		verbose_name_plural = 'Бренды'
		ordering = ['name']

class Category(models.Model):
	# представление товара, питание, гигиена
	name = models.CharField('Категория', max_length=160, unique=True)
	url = models.SlugField(max_length=130, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['name']

class AddCategory(models.Model):
	# какой это продукт, сухой корм, игрушка, шампунь
	name = models.CharField('Представление продукта', max_length=150, unique=True)
	url = models.SlugField(max_length=130, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Представление о продукте'
		verbose_name_plural = 'Представление о продуктах'
		ordering = ['name']

class Product(models.Model):
	title = models.ManyToManyField(Brend, verbose_name='Бренд', related_name='product_name')
	categories = models.ManyToManyField(Category, verbose_name='Категория товара', related_name='categories_name')
	addcategories = models.ManyToManyField(AddCategory, verbose_name='Представление товара', related_name='addcategories_name')
	tagtitle = models.CharField('Название продукта', max_length=150, unique=True)
	description = models.TextField('Описание')
	price = models.PositiveIntegerField('Цена', default='', help_text='цена указывается в тенге')
	poster = models.ImageField('Изображение', upload_to='cat_images/')
	url = models.SlugField(max_length=150, unique=True)
	draft = models.BooleanField('Черновик', default=False)

	def __str__(self):
		return self.tagtitle

	def get_absolute_url(self):
		return reverse('product_detail', kwargs={'slug': self.url})

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'
		ordering = ['tagtitle']