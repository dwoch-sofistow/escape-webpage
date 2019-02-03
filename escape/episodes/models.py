from django.db import models

# Create your models here.
class Episode(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images')
    video = models.CharField(max_length=500)
    skin1 = models.ImageField(upload_to='images', blank=True, null=True)
    skin2 = models.ImageField(upload_to='images', blank=True, null=True)
    resource1 = models.TextField()
    resource2 = models.TextField()
    link = models.TextField()
    censorlink = models.TextField()

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title

    #Ta funkcja ogranicza długość tekstu na stronie wpisów, żeby nie było zbyt rozlegle i każdy mógł sobie wybrać...
    def summary(self):
        return self.body[:110]

    #Funkcja formatująca datę w ludzki sposób...
    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')

class HiddenEpisode(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images')
    video = models.CharField(max_length=500)
    skin = models.ImageField(upload_to='images', blank=True, null=True)
    resource1 = models.TextField()
    resource2 = models.TextField()
    link = models.TextField()

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title

    #Ta funkcja ogranicza długość tekstu na stronie wpisów, żeby nie było zbyt rozlegle i każdy mógł sobie wybrać...
    def summary(self):
        return self.body[:110]

    #Funkcja formatująca datę w ludzki sposób...
    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')
