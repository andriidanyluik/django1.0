from django.db import models

class Article(models.Model):
	article_title = models.CharField("nazva statti", max_length = 200)
	article_text = models.TextField("text statti" )
	pub_date = models.DateTimeField()
class Comment(models.Model):
	author


