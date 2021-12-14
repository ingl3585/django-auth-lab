from django.db import models
from django.contrib.auth import get_user_model

class Comment(models.Model):
  blog = models.ForeignKey(
      'Blog',
      on_delete=models.CASCADE
  )
  author = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  content = models.CharField(max_length=400)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    # This must return a string
    return f"Created at: {self.created_at} by {self.author} - Updated at: {self.updated_at} - Title: {self.blog} - Content: {self.content}"
