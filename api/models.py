from django.db import models

# Create your models here.

class ProjectForm(models.Model):
    description = [
        ("Yet to Review - 0",'0'),
        ('Projectmanager Inspected & Snags given to Programhead - 1','1'),
        ('Projectmanager Snags attended & Handed Over - 2','2'),
        ('Customer Intimated for inspection - 3','3'),
        ('Customer Snags Given to Architect - 4','4'),
        ('Customer Snags Attended & Handed over to Supervisor - 5','5'),
        ('Handed over to Customer - 6','6'),
    ]

    location        = models.CharField(max_length=100,default='Bengaluru')
    project_name    = models.CharField(max_length=150,default='paradise')
    tower           = models.CharField(max_length=50,default='')
    floor           = models.IntegerField(max_length=30,default='')
    unit_status     = models.IntegerField(max_length=10,default='0')
    created         = models.DateTimeField(auto_now_add=True)
    unit_desc       = models.CharField(max_length=200,choices = description,default='')

    class Meta:
        ordering = ['created']
