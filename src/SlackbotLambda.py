import json
#import nltk
#import numpy as np

def lambda_handler(event, context):
    print("Hi CLoudWatch!")
    print ("I am a handler")
    text = event.get('text', 'No event given')
#    tokenized = nltk.word_tokenize(text)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('THIS IS A FRESH DEPLOY 12-19. I got a body for u and it comes from an S3 ZIP!!!\n Plus I\'ve been testing. My event is '+text), #err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
        #'body': json.dumps('Hello from Lambda!')
    }

if __name__ == "__main__":

    lambda_handler({'text':'event test'}, '')
