from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.CharField(max_length=500, blank=True, null=True)
    skin1 = models.ImageField(upload_to='images', blank=True, null=True)
    skin2 = models.ImageField(upload_to='images', blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    censorlink = models.TextField(blank=True, null=True) #Tu wpisz HiddenEpisode_ID - zwykły integer
    # Można by dodać jeszcze ze dwa pola na linki (1 normalny i 1 cenzurowany)
    # Można tu dodać pole na skina (albo 2 jeśli chcemy tu coś ukrywać.)


    #Ta funkcja pokazuje tytuł postu na stronie admina. Zawsze używaj ___str___ żeby wrzucić coś w górę do adminów.
    def __str__(self):
        return self.title

    #Ta funkcja ogranicza długość tekstu na stronie wpisów, żeby nie było zbyt rozlegle i każdy mógł sobie wybrać...
    def summary(self):
        return self.body[:110]

    #Funkcja formatująca datę w ludzki sposób...
    def pubdate_short(self):
        return self.pubdate.strftime('%a %d %b %Y')
