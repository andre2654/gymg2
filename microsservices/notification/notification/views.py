from django.http import HttpResponse
from .producer import publish


def notify(request):
    publish()
    return HttpResponse("Mensagem enviada para a fila RabbitMQ!")
