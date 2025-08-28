Sentiment Analysis Web App
=========================

English Version
---------------

This web application performs Sentiment Analysis in two ways:

1. Text Sentiment Analysis
   - Input text in Azerbaijani.
   - Automatically translates text to English.
   - Predicts sentiment using a Logistic Regression model.
   - Outputs: Positive, Negative, Neutral with confidence score.

2. Face Emotion Analysis
   - Uses camera snapshot to detect your face.
   - Analyzes emotions using FER (Facial Expression Recognition).
   - Outputs: Dominant emotion with confidence score.

How to Run Locally:
1. Clone the repository:
   git clone <your-repo-url>
   cd <your-repo-folder>

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app:
   python main.py

4. Open the link in your browser and select the desired tab:
   - Text sentiment
   - Camera sentiment

Deployment:
- Recommended: Hugging Face Spaces (Gradio).
- Upload repository and select Python/Gradio template.


Azərbaycan Versiyası
-------------------

Bu veb tətbiqi Sentiment Analizini iki üsulla həyata keçirir:

1. Mətn Sentiment Analizi
   - Mətninizi Azərbaycan dilində daxil edin.
   - Mətn avtomatik olaraq İngiliscəyə tərcümə olunur.
   - Sentiment Logistic Regression modeli ilə təxmin edilir.
   - Nəticə: Positive, Negative, Neutral və confidence faizi.

2. Üz Emosiya Analizi
   - Kamera snapshot-u vasitəsilə üzünüzü tanıyır.
   - Emosiyaları FER (Facial Expression Recognition) ilə analiz edir.
   - Nəticə: Dominant emotion və confidence faizi.

Lokal İstifadə Qaydası:
1. Repository-i klonlayın:
   git clone <repo-link>
   cd <repo-folder>

2. Tələb olunan paketləri quraşdırın:
   pip install -r requirements.txt

3. Tətbiqi işə salın:
   python main.py

4. Brauzerdə açılan linkdə istədiyiniz tab-ı seçin:
   - Text sentiment
   - Camera sentiment

Deploy (İctimai İstifadə):
- Tövsiyə olunur: Hugging Face Spaces (Gradio).
- Repository-i yükləyin və Python/Gradio şablonunu seçin.
