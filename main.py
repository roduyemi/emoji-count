# This Python file uses the following encoding: utf-8
import os, sys, requests, json
import requests
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

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
      "access_token": os.getenv("ACCESS_TOKEN")
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
        print("value1 = " + event['key1'])
        print("value2 = " + event['key2'])
        emoji_count = get_emoji_count()
        return response({
          'message': 'Success',
          'body': emoji_count
        }, 200)
    except Exception as e:
        return response({'message': e.message}, 400)