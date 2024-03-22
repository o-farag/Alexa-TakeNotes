import base64

import json


import boto3


runtime = boto3.client("bedrock-runtime")

# Get image encoded in base64
with open("test.png", "rb") as image_file:
    image_bytes = image_file.read()
encoded_image = base64.b64encode(image_bytes).decode("utf-8")

# Audio transcription
audio_transcript = '''
One of the properties we want for a cipher text is confusion or obscuring of the relationship between plain text and the cipher text. So an attacker, if they know that your message is in the English language, for example, they know that the letter E has a certain percentage. So they can is it the letter E composes a certain percentage of the human language so they can look for whatever cipher text has that same percentage of usage in the cipher text. So that's that, that's why I think coding should be nonlinear or the encoding of the message and message one, message two should not be equal to the encoding of them separately.
'''

#Create JSON body for API request
body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            { # Request to process slide
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": encoded_image,
                        },
                    },
                    {"type": "text", "text": "Provide a transcription of these lecture notes"},

                ],
            },
            {
                "role": "assistant",
                "content": [{"type": "text","text": "Provide a transcription of these lecture notes"}],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": "Here's an audio transcription of these lecture notes:\n" + audio_transcript},
                ],
            },
            {
                "role": "assistant",
                "content": [{"type": "text","text": "Here's an audio transcription of these lecture notes"}],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": "Combine these 2 sources and generate a well-formatted markdown file summarizing it"},
                ],
            },
            {
                "role": "assistant",
                "content": [{"type": "text","text": "Combine these 2 sources and generate a well-formatted markdown file summarizing it"}],
            },
        ],
    }
)

#Make API Call to Claude 3
response = runtime.invoke_model(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    body=body
)


response_body = json.loads(response.get("body").read())
print(response_body)