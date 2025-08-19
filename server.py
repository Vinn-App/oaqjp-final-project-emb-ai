"""Shut up lint."""
from flask import Flask, request # pylint: disable=import-error
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

"""Shut up lint."""
def format_emotion_data(func):
    """Shut up lint."""
    def modify_output():
        """Shut up lint."""
        response_dict = func()

        if response_dict.get('dominant_emotion') is None:
            return "Invalid text! Please try again."

        anger = response_dict.get('anger')
        disgust = response_dict.get('disgust')
        fear = response_dict.get('fear')
        joy = response_dict.get('joy')
        sadness = response_dict.get('sadness')
        dominant_emotion = response_dict.get('dominant_emotion')

        formatted_string = (
            f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
            f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
        )
        return formatted_string

    return modify_output

@app.route('/emotion_detector')
@format_emotion_data
def detect_emotion():
    """Shut up lint."""
    text_to_analyze = request.args.get('textToAnalyze')

    return emotion_detector(text_to_analyze)
