from transformers import pipeline

print("Loading the AI model... (this may take a moment on first run)")
model_name = "t5-small"
summarizer = pipeline("summarization", model=model_name,
                      tokenizer=model_name, framework="pt")
print("Model loaded successfully!")


def summarize_text(long_text):
    if len(long_text.split()) < 30:
        return "Text is too short. Please provide a longer paragraph."
    words = long_text.split()
    if len(words) > 1024:
        long_text = ' '.join(words[:1024])
        print("Note: Text was too long and was truncated.")
    summary = summarizer(
        long_text,
        max_length=150,
        min_length=40,
        do_sample=False
    )
    return summary[0]['summary_text']


def main():
    print("\nPaste your text below and press Enter when finished:")
    user_input = input()
    if user_input.strip():
        print("\nGenerating summary...")
        result = summarize_text(user_input)
        print("\n" + "="*50)
        print("SUMMARY:")
        print("="*50)
        print(result)
        print("="*50)
    else:
        print("No text was provided.")


if __name__ == "__main__":
    main()
