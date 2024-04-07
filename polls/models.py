from django.db import models

# Create your models here.
# database schemas/models


class Question(models.Model): 
    # inheritance models.Model
    # id is automatically created by django
    question_text = models.CharField(max_length=200) # character
    pub_date = models.DateTimeField("date published") # datetime - timestamp
    
    # dunder methods
    def __str__(self): 
        return self.question_text  # returns question_text in Question.objects.all()

class Choice(models.Model):
    # inheritance models.Model -> Parent class
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # linking a column from another table, foreign key 
    choice_text = models.CharField(max_length=200, null=False) # character 
    votes = models.IntegerField(default=0) # Integer field
    
    def __str__(self):
        return self.choice_text
    
    
# to update in db, if you are doing it first time, 


# >>> from polls.models import Question, Choice
# >>> from django.utils import timezone
# >>> q = Question(question_text="What's new?", pub_date=timezone.now())# instance of Question, q is an isntance
# >>> q.save()
# >>> Question.objects.all()
# <QuerySet [<Question: Question object (1)>]>
# >>> Question.objects.all() # returns all  rows in Question Table 
# <QuerySet [<Question: Question object (1)>]>
# >>> q1 = Question(question_text="What's old?", pub_date=timezone.now())# instance of Question, q is an isntance
# >>> q1.save()
# >>> Question.objects.all()
# <QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>
# >>> 
# now exiting InteractiveConsole...


# to creat choices two ways Foreign Key Relation
#  Question --- Choices
#  q1           c1 - q1     # Choice --> Question
#                             Question --> Choice,   choice_set, <foreign_key_class>_set