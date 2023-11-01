from django.shortcuts import render
import requests

def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": "Bearer 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"}
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    except:
        return "NO INTERNET CONNECTION"
# Create your views here.
def index(request):
    if request.method=="POST":
      value=request.POST["sentence"]
      output = query({
    "inputs": value,
})

# Extract and print the summary_text
      if output:
          summary_text = output[0]['summary_text']
          print(summary_text)
          return render(request,"index.html",{"data":summary_text})
      else:
          print("No output or invalid response.")
    return render(request,"index.html")