from datetime import datetime
from django.http import JsonResponse
from . import models
import json

# Create your views here.


def index(request):
    """Index for Polls."""
    if request.method == "GET":
        return list_questions(request)
    if request.method == "POST":
        return create_question(request)


def list_questions(request):
    questions = models.Question.objects.all().values()

    return JsonResponse(
        {
            "questions": list(questions),
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
