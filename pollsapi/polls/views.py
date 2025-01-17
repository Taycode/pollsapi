from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .serializers import PollSerializer
from .models import Poll

# Create your views here.


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = PollSerializer(polls, many=True)
    return JsonResponse(data)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
            "results":
                {
                    "question": poll.question,
                    "created_by": poll.created_by.created_by__username,
                    "pub_date": poll.pub_date
                }
            }
    return JsonResponse(data)



