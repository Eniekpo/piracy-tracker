from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.hashers import make_password
# from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib

PREDICTIONS = (
    ('', 'Status'),
    ('Bugs', 'Bugs'),
    ('Genuine', 'Genuine'),
    ('Pirated', 'Pirated')
)


class Data(models.Model):
    software_id = models.CharField(max_length=50, null=True)
    license_key = models.CharField(max_length=50, blank=True)
    hashvalue = models.CharField(max_length=256, null=True)
    branchCount = models.FloatField(
        validators=[MinValueValidator(-0.8), MaxValueValidator(2.5)], null=True)
    predictions = models.CharField(
        max_length=50, blank=True, choices=PREDICTIONS, default='Status')
    tested_at = models.DateField(auto_now_add=True)

    # FUNCTION TO MAKE PREDICTIONS
    # def save(self, *args, **kwargs):
    #     ml_model = joblib.load('ml_model/software_piracy_tracker.joblib')
    #     self.predictions = ml_model.predict(
    #         [[self.unique_Opnd, self.branchCount, self.total_Op, self.total_Opnd]])
    #     return super().save(*args, **kwargs)

    # FUNCTION TO GENERATE HASH VALUE

    def save(self, *args, **kwargs):
        some_salt = 'some_salt'
        hashvalue = make_password(self.hashvalue, some_salt)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-tested_at']
        verbose_name = 'data'
        verbose_name_plural = 'data'

    def __str__(self):
        return self.software_id

# PREDICTIONS MODEL


class Predictions(models.Model):
    softwarename = models.CharField(max_length=50, null=True)
    licensekey = models.CharField(max_length=50, null=True)
    Hashvalue = models.CharField(max_length=50, null=True)

    branchCount = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(30)], null=True)
    Predictions = models.CharField(max_length=50, blank=True)
    Tested_at = models.DateField(auto_now_add=True)

    # FUNCTION TO MAKE PREDICTIONS
    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/piracy_tracker.joblib')
        self.Predictions = ml_model.predict(
            [[self.branchCount]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-Tested_at']
        verbose_name = 'predictions'
        verbose_name_plural = 'predictions'

    def __str__(self):
        return self.softwarename
