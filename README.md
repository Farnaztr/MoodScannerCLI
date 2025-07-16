<div align="center">


# MoodScannerCLI  
*A simple and powerful command-line sentiment analysis tool using free public API*

[![GitHub](https://img.shields.io/badge/GitHub-farnaz--tarabi-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/farnaztr)


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


## How It Works

User inputs a sentence → MoodScannerCLI sends a POST request to text-processing.com API with the sentence →  
API returns a JSON response with sentiment label and probability scores →  
The app parses the response and clearly displays the sentiment label along with positive, negative, and neutral percentages in the console.

---

## Usage

Make sure Python 3 is installed, then install `requests` library:

```bash
pip install requests
```
***Run the program***

```python Text_Analysis.py
Enter your sentence: I love coding in Python!
Label: Pos  
Positive: 85.34%  
Negative: 5.12%  
Neutral: 9.54%
```
