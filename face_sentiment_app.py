# face_sentiment_app.py
import gradio as gr
from fer import FER
import numpy as np

# FER detector
detector = FER(mtcnn=False)

def analyze_face(frame):
    """
    frame: numpy array (BGR)
    return: frame, dominant emotion string
    """
    result = detector.detect_emotions(frame)
    if result:
        top_emotion, score = detector.top_emotion(frame)
        return frame, f"{top_emotion} ({score:.2f})"
    return frame, "No face detected"

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Face Sentiment Analysis (Snapshot Based)")
    cam_output = gr.Image(label="Camera", type="numpy")
    emotion_output = gr.Textbox(label="Dominant Emotion")
    cam_input = gr.Camera(label="Show your face")
    cam_input.change(fn=analyze_face, inputs=cam_input, outputs=[cam_output, emotion_output])

demo.launch()
