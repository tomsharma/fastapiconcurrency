# This is now in github
# Adding a url
from fastapi import FastAPI
import requests
import time
from httpx import AsyncClient  # Install with: pip install httpx
import asyncio

app = FastAPI()

def fetch_url(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return f"URL: {url}, Error: {response.status_code}"
    except Exception as e:
        return f"URL: {url}, Error: {str(e)}"

    duration_ms = int((time.time() - start_time) * 1000)
    return f"URL: {url}, Execution Time: {duration_ms} ms"


@app.get("/")
async def read_root():
    urls = ["https://www.example.com", "https://www.google.com", "https://www.github.com"]
    return [fetch_url(url) for url in urls]


# to run python fastapi version in terminal window type uvicorn main:app --reload
# for the GO lang version of this go to /Users/ks-01/gocode and then execute gocode % go run .
"""
Python results
[
  "URL: https://www.example.com, Execution Time: 51 ms",
  "URL: https://www.google.com, Execution Time: 357 ms",
  "URL: https://www.github.com, Execution Time: 194 ms"

]



Go results

(base) ks-01@Toms-MacBook-Pro gocode % go run .
URL: https://www.example.com, Execution Time: 69 ms
URL: https://www.google.com, Execution Time: 318 ms 
URL: https://www.github.com, Execution Time: 134 ms
"""
