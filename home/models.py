from django.db import models

# Create your models here. 
# NOTE: These are your db tables, right?

# you can link models together, can have parent and child models, its OOP for your application
# i.e., a polls app will require what? a question and choices.

# Question:
# Question_text
# Publish_date

# Choice:
# Choice_text
# Number_of_votes
# Link #need to link your choices to the right questions

class Question(models.Model):
    # Example: what system have you updated?
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # Example: what was your TA3 System? What was your dataset? Completed?
    ## IDEA: sqlite table has row for that particular ta3 and dataset, when completed we switch to 1 
    # TODO: if this works, also add way to record timestamp and username?

    # OLD: choice_text = models.CharField(max_length=200)
    choice_text_TA3 = models.CharField(max_length=200)
    choice_text_DATASET = models.CharField(max_length=200)
    # OLD: votes = models.IntegerField(default=0)
    completed = models.IntegerField(default=0)
    #### NOTE: these next two will have a default stored value that gets overwritten
    completed_date = models.DateTimeField('date completed')
    user_name = models.CharField(max_length=200)
    # now we give choice class a new parameter - pass in question, has to be a foreign key of this q object and on delete, intiiatlize cascade (for 1 to 1 relationship)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text_TA3