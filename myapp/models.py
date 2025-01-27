from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Card(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='cards/', blank=True, null=True)


class Interpretation(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='interpretations')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='interpretations')
    description = models.TextField()
    def __str__(self):
        return f"{self.card.name} - {self.question.text}"


