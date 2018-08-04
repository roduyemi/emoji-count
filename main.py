# This Python file uses the following encoding: utf-8
import os, sys, requests, json
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

emojis = ['😁', '😂', '😃', '😄', '😅', '😆', '😉', '😊', '😒', '😨', '😡', '😢']
emoji_count = {
  # "😁": "\U0001f601",
  # "😂": "\U0001f602",
  # "😃": "\U0001f603",
  # "😄": "\U0001f604",
  # "😅": "\U0001f605",
  # "😆": "\U0001f606",
  # "😉": "\U0001f609",
  # "😊": "\U0001f60a",
  # "😒": "\U0001f612",
  # "😨": "\U0001f628",
  # "😡": "\U0001f621",
  # "😢": "\U0001f622"

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

print(emoji_count)

#https://api.instagram.com/v1/tags/search?q=%F0%9F%98%80&access_token=5717177908.afb9dd2.4cd8bfb23d374cf79fe94ea9ae2251b9