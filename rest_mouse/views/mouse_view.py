from io import BytesIO

from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from rest_mouse.models.mouse_model import MouseModel
from rest_mouse.mouse_movement import mouse_get, mouse_post
from rest_mouse.serializers.mouse_serializer import MouseSerializer


class MouseResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs['content_type'] = 'application/json'
        content = JSONRenderer().render(data)
        super().__init__(content, **kwargs)

@csrf_exempt
def mouse_view(request: HttpRequest):
    if request.method == "GET":
        mouse = mouse_get()
        serializer = MouseSerializer(mouse)
        return MouseResponse(serializer.data)

    if request.method == "POST":
        #return HttpResponse(repr(request))
        data = JSONParser().parse(request)
        serializer = MouseSerializer(data=data)
        if serializer.is_valid():
            mouse_post(data)
            return MouseResponse(serializer.errors)
        return MouseResponse(serializer.errors, status=400)


