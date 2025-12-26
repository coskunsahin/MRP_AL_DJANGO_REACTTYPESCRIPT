from django.db import models

class AIDecisionLog(models.Model):
    item = models.CharField(max_length=50)
    decision = models.CharField(max_length=10)
    confidence = models.FloatField()
    score = models.FloatField()
    purchase_cost = models.FloatField()
    production_cost = models.FloatField()
    capacity = models.FloatField()
    reason = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
