# This Python file uses the following encoding: utf-8
import os, sys, json
from botocore.vendored import requests

def get_emoji_count():
  emojis = ['😁', '😂', '😃', '😄', '😅', '😆', '😉', '😊', '😒', '😨', '😡', '😢']
  emoji_count = {
    "😁": {},
    "😂": {},
    "😃": {},
    "😄": {},
    "😅": {},
    "😆": {},
    "😉": {},
    "😊": {},
    "😒": {},
    "😨": {},
    "😡": {},
    "😢": {}
  }
  
  for x in emojis:
    parameters = {
      "access_token": "" # add instagram access_token here
    }
  
    response = requests.get("https://api.instagram.com/v1/tags/"+x, params=parameters)
  
    data = response.json()
    emoji_count[x] = data["data"]
  
  return emoji_count



def response(message, status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
            },
        }

def lambda_handler(event, context):
    try:
        emoji_count = get_emoji_count()
        return response({
          'message': 'Success',
          'body': emoji_count
        }, 200)
    except Exception as e:
        return response({'message': e.message}, 400)
