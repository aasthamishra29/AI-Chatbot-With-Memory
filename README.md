# AI Chatbot With Memory

A Generative AI chatbot built using Python and Google's Gemini API. The chatbot maintains conversation history during a session, enabling contextual responses.

## Features
- Conversation memory
- Google Gemini API integration
- Environment variable support using `.env`
- Python-based implementation

## Technologies Used
- Python
- Google Gemini API
- python-dotenv

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

Run the project:

```bash
py chatbot.py
```

## Note

The `.env` file is intentionally excluded from the repository to protect the API key.
