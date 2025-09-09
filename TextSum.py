"""
TextSum: A Simple Text Summarizer
A lightweight Python tool that extracts key sentences from longer texts.
Uses basic extractive summarization without external dependencies.
"""

def simple_summarizer(text, max_sentences=3):
    """
    Extracts key sentences from text to create a summary.
    This function uses a simple extractive approach:
    - First sentence: Usually contains the main topic/thesis
    - Middle sentence: Often contains supporting details or examples  
    - Second to last sentence: Typically contains conclusions or solutions
    """
    # Split the text into sentences using period+space as delimiter
    sentences = text.split('. ')

    # If the text is already shorter than our target, return it unchanged
    if len(sentences) <= max_sentences:
        return text

    # Select the most important sentences for the summary
    summary_sentences = []
    summary_sentences.append(sentences[0])  
    if len(sentences) > 3:
        summary_sentences.append(sentences[len(sentences)//2])
    summary_sentences.append(sentences[-2])
    # Rejoin the selected sentences into a coherent summary
    return '. '.join(summary_sentences) + '.'  


def main():
    print("Paste your text and press Enter when finished:")
    user_input = input()

    if user_input.strip():
        summary = simple_summarizer(user_input)  
        print("\nSummary:")
        print(summary)
    else:
        print("No text was provided.")

if __name__ == "__main__":
    main()
