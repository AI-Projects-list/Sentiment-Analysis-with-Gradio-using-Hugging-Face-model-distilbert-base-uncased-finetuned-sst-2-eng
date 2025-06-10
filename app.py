import gradio as gr
from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Define the prediction function
def analyze_sentiment(text):
    result = classifier(text)[0]
    return f"Label: {result['label']}, Score: {result['score']:.2f}"

# Create Gradio interface
demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=2, placeholder="Enter text here..."),
    outputs="text",
    title="Sentiment Analysis App",
    description="Enter a sentence to analyze its sentiment (positive/negative)."
)

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)
