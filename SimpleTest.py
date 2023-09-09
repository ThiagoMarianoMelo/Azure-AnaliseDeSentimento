import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
load_dotenv()

endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
key = os.environ["AZURE_LANGUAGE_KEY"]

text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

documents = [
    {"id": "1", "language": "pt", "text": "Gostei muito do filme porque é engraçado"}
]

response = text_analytics_client.analyze_sentiment(documents)

print(response)