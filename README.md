# AI Chatbot — Gemini API

A lightweight terminal-based chatbot powered by Google's Gemini 1.5 Flash model. Built to demonstrate clean API integration, secure credential handling, and a simple conversational loop in Python.

---

## Tech Stack

- **Python 3**
- **Google Generative AI SDK** (`google-generativeai`)
- **python-dotenv** for environment variable management

---

## Features

- Real-time conversation with Gemini 1.5 Flash via API
- Secure API key handling through environment variables (no secrets in source code)
- Minimal, readable codebase — easy to extend or adapt

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-chatbot-api.git
cd ai-chatbot-api
```

### 2. Create and activate a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Copy the example env file and add your Gemini API key:

```bash
cp .env.example .env
```

Then open `.env` and replace the placeholder:

```
GEMINI_API_KEY=your_api_key_here
```

> You can get a free API key at [https://aistudio.google.com](https://aistudio.google.com)

### 5. Run the chatbot

```bash
python main.py
```

---

## Usage

```
AI Chatbot (Gemini) - press Ctrl+C to quit

You: What is the speed of light?

Bot: The speed of light in a vacuum is approximately 299,792,458 meters per second...
```

---

## Project Structure

```
ai-chatbot-api/
├── main.py           # Core chatbot logic
├── .env.example      # Environment variable template
├── .gitignore        # Excludes .env and other sensitive files
├── requirements.txt  # Python dependencies
└── README.md
```

---

## Notes

- The `.env` file is listed in `.gitignore` and will never be committed to version control.
- This project uses `gemini-1.5-flash`, a fast and cost-efficient model suitable for conversational tasks.
