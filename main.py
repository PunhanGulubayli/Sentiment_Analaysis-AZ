import gradio as gr
from sentiment_analysis_eng_az import predict_sentiment
from face_sentiment_app import analyze_face

# Text sentiment tab
def run_text(text):
    sentiment, confidence = predict_sentiment(text, threshold=70)
    return f"{sentiment} ({confidence:.2f}%)"

# Camera sentiment tab
def run_camera(frame):
    img, emotion = analyze_face(frame)
    return img, emotion

with gr.Blocks() as demo:
    gr.Markdown("## Sentiment Analizi Web App")
    
    # Tab 1: Text sentiment
    with gr.Tab("Text sentiment"):
        txt_input = gr.Textbox(label="Mətni daxil edin")
        txt_output = gr.Textbox(label="Nəticə")
        txt_btn = gr.Button("Analiz et")
        txt_btn.click(fn=run_text, inputs=txt_input, outputs=txt_output)
    
    # Tab 2: Camera sentiment
    with gr.Tab("Camera sentiment"):
        cam_output = gr.Image(label="Kamera", type="numpy")
        emotion_output = gr.Textbox(label="Dominant Emotion")
        cam_input = gr.Camera(label="Üzünü göstər")
        cam_input.change(fn=run_camera, inputs=cam_input, outputs=[cam_output, emotion_output])

demo.launch()
