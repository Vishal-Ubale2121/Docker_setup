from django.db import models
from datetime import datetime

Movie_Choice = (
    ('DR.KABIR SINGH','Dr.Kabir_Singh'),
    ('DR.AJAY MITTAL', 'Dr.Ajay Mittal'),
    ('DR.VISHAL PANDE','Dr.Vishal Pandy')
)

Test_Choice = (
    ('BLOOD','Blood'),
    ('URINE', 'Urine'),
    ('GLUCOUSE','Glucouse'),
    ('PREGNANCY','Pregnancy')
)

class Mood(models.Model):

    name = models.CharField(max_length=120)
    mno = models.IntegerField()
    test = models.CharField(max_length=100, choices= Test_Choice, default='Select')
    amt = models.IntegerField()
    dr = models.CharField(max_length=100, choices= Movie_Choice, default='Select')
    time = models.DateTimeField()



    class Meta:  
        db_table = "mood"