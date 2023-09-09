import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
load_dotenv()

key = os.environ.get('AZURE_LANGUAGE_KEY')
endpoint = os.environ.get('AZURE_LANGUAGE_ENDPOINT')

def authenticate_client() -> TextAnalyticsClient:
    credential = AzureKeyCredential(key)
    return TextAnalyticsClient(
            endpoint=endpoint, 
            credential=credential)


def sentiment_analysis(client: TextAnalyticsClient):

    value = [
        "A comida estava péssima, totalmente fria."
    ]
    
    result = client.analyze_sentiment(value, show_opinion_mining=True)
    
    print(result)


client = authenticate_client()
          
sentiment_analysis(client)