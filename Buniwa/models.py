from django.db import models

<<<<<<< HEAD
class theBlog(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    # content = models.TextField()
=======
class Card(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    content = models.TextField()
>>>>>>> 2a242e0ccc7c1ec90306a6f34bff775db59f3b49
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    card_image = models.ImageField(upload_to='card_images/')
    author_image = models.ImageField(upload_to='author_images/')

    def __str__(self):
        return self.title
<<<<<<< HEAD
    
    class Meta:
        verbose_name_plural = 'Blogs Section'
=======
>>>>>>> 2a242e0ccc7c1ec90306a6f34bff775db59f3b49


        
class PortfolioPost(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    post_image = models.ImageField(upload_to='card_images/')

    def __str__(self):
        return self.title
    
<<<<<<< HEAD
    class Meta:
        verbose_name_plural = 'Portfolio Section'
    
=======
>>>>>>> 2a242e0ccc7c1ec90306a6f34bff775db59f3b49

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
    
<<<<<<< HEAD
    class Meta:
        verbose_name_plural = 'Teams Section'
    
=======
>>>>>>> 2a242e0ccc7c1ec90306a6f34bff775db59f3b49

