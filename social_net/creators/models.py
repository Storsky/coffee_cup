from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    follows = models.ManyToManyField(
                                    "self",
                                    related_name="followed_by",
                                    symmetrical=False,
                                    blank=True
                                    )
    avatar = models.ImageField(default='static/avatars/default.jpg', upload_to='static/avatars')
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    yt_link = models.URLField()
    created_ad = models.DateTimeField(auto_now_add=True)
    likes =  models.ManyToManyField(User, related_name='liked_posts')
    video_id = models.CharField(max_length=55, default='https://www.youtube.com/embed/dQw4w9WgXcQ')

    def save(self, *args, **kwargs):
        self.video_id = 'https://www.youtube.com/embed/' + self.yt_link[32:43]
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return (f'{self.owner}, {self.title}')