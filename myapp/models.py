from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib

PREDICTIONS = (
    ('bugs', 'bugs'),
    ('unpirated', 'unpirated'),
    ('pirated', 'pirated')
)


class Data(models.Model):
    software_name = models.CharField(max_length=50, null=True)
    uniq_Opnd = models.FloatField(
        validators=[MinValueValidator(0.8), MaxValueValidator(7.9)], null=True)
    total_Op = models.FloatField(
        validators=[MinValueValidator(2.0), MaxValueValidator(4.4)], null=True)
    total_Opnd = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(6.9)], null=True)
    branchCount = models.FloatField(
        validators=[MinValueValidator(-0.8), MaxValueValidator(2.5)], null=True)
    predictions = models.CharField(
        max_length=50, null=True, choices=PREDICTIONS, default='Status')
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/software_piracy_tracker.joblib')
        self.predictions = ml_model.predict(
            [[self.uniq_Opnd, self.total_Op, self.total_Opnd, self.branchCount]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.software_name
