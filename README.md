#  Text Summarizer Projects

Two Python-based text summarizers demonstrating different approaches to automatic text summarization.

##  Project Overview

This repository contains two implementations of text summarization:

1. ** AI-Powered Summarizer** (`AITextSum.py`) - Uses Facebook's BART model for abstractive summarization
2. ** Simple Summarizer** (`TextSum.py`) - Lightweight extractive summarization without external dependencies

## Comparison

| Feature | AI Summarizer | Simple Summarizer |
|---------|---------------|------------------|
| **Approach** | Abstractive (generates new text) | Extractive (selects existing sentences) |
| **Dependencies** | transformers, torch | None |
| **Speed** | Slower (requires model loading) | Instant |
| **Output Quality** | Human-like, creative | Direct, factual |
| **Best For** | Professional use, longer texts | Quick summaries, learning |

##  Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/text-summarizers.git
   cd text-summarizers
