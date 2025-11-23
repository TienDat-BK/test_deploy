import gradio as gr
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive 😃"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Tạo giao diện Gradio
with gr.Blocks() as demo:
    gr.Markdown("# 📝 Sentiment Analyzer Demo")
    gr.Markdown("Nhập một câu và xem sentiment của nó.")
    
    with gr.Row():
        text_input = gr.Textbox(label="Enter your text here", placeholder="Type something...")
        output = gr.Label(label="Sentiment")
    
    text_input.submit(analyze_sentiment, inputs=text_input, outputs=output)
    # Hoặc dùng nút bấm
    btn = gr.Button("Analyze")
    btn.click(analyze_sentiment, inputs=text_input, outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)
