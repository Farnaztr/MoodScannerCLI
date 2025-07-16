<div align="center">


# MoodScannerCLI  
*A simple and powerful command-line sentiment analysis tool using free public API*

[![Built With](https://img.shields.io/badge/built%20with-Python-green.svg)](https://www.python.org/)
[![API](https://img.shields.io/badge/API-text-processing.com-yellow.svg)](https://text-processing.com/docs/sentiment.html)

</div>

---

## Overview

**MoodScannerCLI** is a lightweight command-line tool that analyzes the sentiment of your text input.  
By sending your sentences to a free public sentiment analysis API, it returns whether your text is positive, negative, or neutral — along with detailed probability scores.

Perfect for:  

- ✍️ Writers and bloggers for sentiment checking  
- 📊 Quick sentiment insights in terminal  
- 🤖 Chatbots and personal assistants  
- 🧠 Emotional data collection and research  

---

## Demo

<p align="center">
  <img src="https://img.icons8.com/ios-filled/100/000000/sentiment.png" width="150" alt="MoodScannerCLI Demo">
</p>

---

## How It Works

User inputs a sentence → MoodScannerCLI sends the text to the [text-processing.com](https://text-processing.com) API →  
API responds with sentiment label and probabilities → Results are shown clearly in the console.

---

## Usage

1. **Install dependencies**  

Make sure Python 3 is installed, then install `requests` library:

```bash
pip install requests
