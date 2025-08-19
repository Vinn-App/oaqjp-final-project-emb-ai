import requests

def emotion_detector(text_to_analyze):
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": { "text": text_to_analyze }
    }

    response = requests.post(
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        headers=headers,
        json=payload
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        
    return format_emotion_data(response.json())

def format_emotion_data(json_data):
    if json_data is None:
        return None

    try:
        emotion_scores = json_data['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        result = {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }

        return result
        
    except (KeyError, IndexError) as e:
        print(f"You f'd up on: {e}")
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
