from django.db import models

class theBlog(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    # content = models.TextField()
class Card(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    card_image = models.ImageField(upload_to='card_images/')
    author_image = models.ImageField(upload_to='author_images/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Blogs Section'


        
class PortfolioPost(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    post_image = models.ImageField(upload_to='card_images/')

    def __str__(self):
        return self.title
    
class Meta:
    verbose_name_plural = 'Portfolio Section'
    
class theTeam(models.Model):
    team_name = models.CharField(max_length=20)
    team_position = models.CharField(max_length=50)
    team_content = models.TextField()
    team_image = models.ImageField(upload_to='author_images/')
    team_twitter = models.URLField(blank=True)
    team_facebook = models.URLField(blank=True)
    team_intagram = models.URLField(blank=True)
    
    def __str__(self):
        return self.team_name
    
    class Meta:
        verbose_name_plural = 'Teams Section'
