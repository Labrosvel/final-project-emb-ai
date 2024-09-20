''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    payload = emotion_detector(text_to_analyze)

    # Check if dominant emotion is None indicating invalid input
    if payload['dominant_emotion'] == None:
        response = "Invalid text! Please try again!"
    # Formatting the response message
    else: 
        response = (
            f"For the given statement, the system response is 'anger': {payload['anger']}, "
            f"'disgust': {payload['disgust']}, 'fear': {payload['fear']}, "
            f"'joy': {payload['joy']} and 'sadness': {payload['sadness']}. "
            f"The dominant emotion is {payload['dominant_emotion']}."
        )
    
    # Output the formatted response
    return response
    
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)