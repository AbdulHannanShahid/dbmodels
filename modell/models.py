from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key="true")
    user_name= models.CharField(max_length=100,default="")

    def __str__(self):
        return self.user_name
class Posts(models.Model):
    posts_id = models.AutoField(primary_key="true")
    posts_caption = models.CharField(max_length=500,default="")
    posts_image = models.ImageField(upload_to="modell/images",default="")
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.posts_caption
class Bio(models.Model):
    bio_email = models.EmailField(max_length=75,default="")
    bio_password = models.CharField(max_length=30,default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.bio_email
class Comment(models.Model):
    comment_id = models.AutoField(primary_key="true")
    comment_content = models.CharField(max_length=500,default="")
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    def __str__(self):
        return self.comment_content
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
#class Reply(models.Model):
 #  reply_content = models.CharField(max_length=500,default="")
  #  created_on = models.DateTimeField(auto_now_add=True)
   # user = models.ForeignKey(User, on_delete=models.CASCADE)
    #posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    #comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    #def __str__(self):
     #   return str(self.reply_content)