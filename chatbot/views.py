#-*-coding: utf-8 -*-
from random import randint
from main.settings import WebhookParser_token, LineBotApi_token
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi(LineBotApi_token)
parser = WebhookParser(WebhookParser_token)

@csrf_exempt
def line_callback(request):
    if request.method == 'POST':
        # get X-Line-Signature header value
        signature = request.META.get('HTTP_X_LINE_SIGNATURE')

        # get request body as text
        body = request.body.decode('utf-8')

        # handle webhook body
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        messages = ["hi there", "hi here"]
        for event in events:
            if isinstance(event, MessageEvent):
                index =  randint(0, messages.__len__())
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=messages[index]))
        return JsonResponse({"status": 200})
    else:
        return HttpResponseBadRequest()