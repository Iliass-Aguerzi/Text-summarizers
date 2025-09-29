"""
AITextSum: AI-Powered Text Summarizer
Uses Facebook's BART model for abstractive summarization.
Generates new sentences that capture the essence of the text.
"""

from transformers import pipeline

ai_summarizer = None


def initialize_ai_model():
    """
    Initializes the AI summarization model.
    This will download the model on first run (may take several minutes).
    """
    global ai_summarizer
    if ai_summarizer is None:
        print("Loading AI model... (this may take a moment on first run)")
        ai_summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            device=-1
        )
        print("AI model loaded successfully!")
    return ai_summarizer


def ai_summarize_text(text):
    """
    Generates an AI-powered summary using Facebook's BART model.
    """
    try:
        summarizer = initialize_ai_model()
        if len(text.split()) < 50:
            return "Text is too short for AI summarization. Please provide a longer text."
        summary = summarizer(
            text,
            max_length=150,
            min_length=40,
            do_sample=False,
            num_beams=4,
            early_stopping=True
        )
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error generating summary: {str(e)}"


def main():
    """
    Main function that handles user input and AI summarization.
    """
    print(" AI Text Summarizer")
    print("Paste your text below and press Enter when finished:")
    print("-" * 50)
    user_input = input()
    if user_input.strip():
        print("\n⏳ Generating AI summary...")
        summary = ai_summarize_text(user_input)
        print("\n" + "=" * 60)
        print("AI SUMMARY:")
        print("=" * 60)
        print(summary)
        print("=" * 60)
    else:
        print("No text was provided.")


if __name__ == "__main__":
    main()
