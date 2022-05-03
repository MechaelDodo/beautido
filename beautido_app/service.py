from beautido_app.models import *
from django.contrib.auth.models import User


def set_score(request, slug, score):
    girl = Girl.objects.get(slug=slug)
    user = request.user
    Score.objects.filter(user_id=user.id, girl_id=girl.id).delete()
    score = Score(user=user, girl=girl, score_number=score)
    score.save()
