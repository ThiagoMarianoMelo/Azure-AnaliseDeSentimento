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

    value = ['Remotely worth or not? response: 90% of my company is remote and the office never closed. It’s the standard where allowed. Remote is awesome, but you have to be disciplined. Once I’m at my desk, I don’t really do other personal tasks during work time.Your setup needs to be as good as an office setting. Don’t try to work from a laptop at your kitchen table, you won’t be effective, invest in your tools: Monitors, microphone, camera, chair, Desk, office area, etc.']
    
    result = client.analyze_sentiment(value, show_opinion_mining=True)
    doc_result = [doc for doc in result if not doc.is_error]

    positive_reviews = [doc for doc in doc_result if doc.sentiment == "positive"]
    negative_reviews = [doc for doc in doc_result if doc.sentiment == "negative"]

    for document in doc_result:
        print("Document Sentiment: {}".format(document.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            document.confidence_scores.positive,
            document.confidence_scores.neutral,
            document.confidence_scores.negative,
        ))
        for sentence in document.sentences:
            print("Sentence: {}".format(sentence.text))
            print("Sentence sentiment: {}".format(sentence.sentiment))
            print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
                sentence.confidence_scores.positive,
                sentence.confidence_scores.neutral,
                sentence.confidence_scores.negative,
            ))
            for mined_opinion in sentence.mined_opinions:
                target = mined_opinion.target
                print("......'{}' target '{}'".format(target.sentiment, target.text))
                print("......Target score:\n......Positive={0:.2f}\n......Negative={1:.2f}\n".format(
                    target.confidence_scores.positive,
                    target.confidence_scores.negative,
                ))
                for assessment in mined_opinion.assessments:
                    print("......'{}' assessment '{}'".format(assessment.sentiment, assessment.text))
                    print("......Assessment score:\n......Positive={0:.2f}\n......Negative={1:.2f}\n".format(
                        assessment.confidence_scores.positive,
                        assessment.confidence_scores.negative,
                    ))
            print("\n")
        print("\n")


client = authenticate_client()
          
sentiment_analysis(client)