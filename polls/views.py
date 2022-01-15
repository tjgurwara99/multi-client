from datetime import datetime
from django.http import JsonResponse
from . import models
import json


def list_questions(request):
    questions = models.Question.objects.all()

    return JsonResponse(
        {
            "questions": [question.question for question in questions],
        }
    )


def create_question(request):
    """Create request for creating a new poll."""
    question = json.loads(request.body).get("question")
    pub_date = datetime.now()
    q = models.Question(question=question, publish_date=pub_date)
    q.save()
    ret_obj = q.__dict__.copy()
    ret_obj.pop("_state")
    return JsonResponse({"saved_object": ret_obj})


handlers = {
    "GET": list_questions,
    "POST": create_question,
}


def index(request):
    """Index for Polls."""
    handler = handlers.get(request.method)
    if not handler:
        return JsonResponse({"error": "Method not found."})
    return handler(request)
