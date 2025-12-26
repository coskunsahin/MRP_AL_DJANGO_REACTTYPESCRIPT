from django.urls import path
from ai_engine.views import make_or_buy_bulk, decision_logs

urlpatterns = [
    path("api/ai/make-or-buy-bulk/", make_or_buy_bulk),
    path("api/ai/decision-logs/", decision_logs),
]
