import gradio as gr
from sentiment_analysis_eng_az import predict_sentiment
from face_sentiment_app import analyze_face

# Text sentiment funksiyası
def run_text(text):
    sentiment, confidence = predict_sentiment(text, threshold=70)
    return f"{sentiment} ({confidence:.2f}%)"

# Camera sentiment funksiyası
def run_camera(frame):
    img, emotion = analyze_face(frame)
    return img, emotion

# İstifadəçi seçim funksiyası
def user_choice(choice, text=None, frame=None):
    if choice == "Text sentiment":
        if text:
            return run_text(text), None
        else:
            return "Please enter text.", None
    elif choice == "Camera sentiment":
        if frame is not None:
            return None, run_camera(frame)
        else:
            return None, "Please show your face."
    else:
        return "Select an option.", None

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Sentiment Analysis App")

    choice = gr.Radio(
        choices=["Text sentiment", "Camera sentiment"],
        label="Select mode"
    )

    txt_input = gr.Textbox(label="Enter text (if Text sentiment selected)")
    cam_input = gr.Camera(label="Show your face (if Camera sentiment selected)")
    
    txt_output = gr.Textbox(label="Sentiment Result")
    cam_output = gr.Image(label="Camera")
    cam_emotion = gr.Textbox(label="Dominant Emotion")

    btn = gr.Button("Run")

    btn.click(
        fn=user_choice,
        inputs=[choice, txt_input, cam_input],
        outputs=[txt_output, (cam_output, cam_emotion)]
    )

demo.launch()
