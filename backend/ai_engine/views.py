from django.http import JsonResponse
from .models import AIDecisionLog
import json, random

def make_or_buy_bulk(request):
    items = json.loads(request.body)
    results = []
    for item in items:
        score = (item["purchase_cost"] - item["production_cost"]) + item["capacity"] * 5
        decision = "MAKE" if score > 0 else "BUY"
        confidence = min(abs(score) / 5, 1) * 100

        AIDecisionLog.objects.create(
            item=item["item"],
            decision=decision,
            confidence=confidence,
            score=score,
            purchase_cost=item["purchase_cost"],
            production_cost=item["production_cost"],
            capacity=item["capacity"],
            reason="AI score",
        )

        results.append({
            "item": item["item"],
            "decision": decision,
            "confidence": round(confidence,1),
        })

    return JsonResponse(results, safe=False)

def decision_logs(request):
    logs = AIDecisionLog.objects.order_by("-created_at")[:50]
    return JsonResponse([
        {
            "item": l.item,
            "decision": l.decision,
            "confidence": l.confidence,
            "score": l.score,
            "created_at": l.created_at.strftime("%Y-%m-%d %H:%M")
        } for l in logs
    ], safe=False)
