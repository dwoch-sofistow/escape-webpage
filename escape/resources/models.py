from django.db import models

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.CharField(max_length=500, blank=True, null=True)
    file = models.TextField(blank=True, null=True)

    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title

    #Ta funkcja ogranicza długość tekstu na stronie wpisów, żeby nie było zbyt rozlegle i każdy mógł sobie wybrać...
    def summary(self):
        return self.body[:110]

    #Funkcja formatująca datę w ludzki sposób...
    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')

class HiddenResource(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.CharField(max_length=500, blank=True, null=True)
    file = models.TextField(blank=True, null=True)


    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title

    #Ta funkcja ogranicza długość tekstu na stronie wpisów, żeby nie było zbyt rozlegle i każdy mógł sobie wybrać...
    def summary(self):
        return self.body[:110]

    #Funkcja formatująca datę w ludzki sposób...
    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')
