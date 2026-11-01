# Intelligent Customer Support Chatbot

A Flask-based intelligent customer support chatbot that uses Natural Language Processing (NLP) to provide automated customer service with FAQ matching, intent classification, and contextual responses.

## Features

- **Intelligent Response System**: Uses NLTK for text preprocessing and intent classification
- **FAQ Matching**: Automatically matches user questions with predefined FAQ database
- **Contextual Awareness**: Maintains conversation history for contextual responses
- **Intent Classification**: Identifies user intents (greeting, question, complaint, feedback)
- **Session Management**: Tracks conversations by session ID
- **Modern Web Interface**: Clean, responsive chat interface
- **SQLite Database**: Stores conversations and FAQ data

## Project Structure

```
chatbot/
├── app.py            
├── chatbot.py           
├── routes.py           
├── database.py         
├── faq_data.py         
├── templates/
│   └── index.html      
├── requirements.txt   
└── README.md          
```

## Technology Stack

- **Backend**: Flask 2.3.3
- **NLP**: NLTK 3.8.1
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **CORS**: Flask-CORS 4.0.0

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd chatbot
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Unix/MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the chatbot**:
   Open your browser and navigate to `http://localhost:5000`


## API Endpoints

### Chat Endpoint
- **URL**: `/chat`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "message": "Your message here",
    "session_id": "unique_session_id"
  }
  ```
- **Response**:
  ```json
  {
    "response": "Bot response",
    "intent": "detected_intent",
    "confidence": 0.95,
    "type": "response_type",
    "matched_question": "FAQ question (if applicable)"
  }
  ```

### Conversation History
- **URL**: `/conversations/<session_id>`
- **Method**: GET
- **Response**: Conversation history for the specified session

### FAQ Data
- **URL**: `/faq`
- **Method**: GET
- **Response**: All FAQ questions and answers

## Chatbot Capabilities

### Intent Classification
The chatbot can identify the following intents:
- **Greeting**: Hello, hi, hey, etc.
- **Question**: Questions containing what, how, when, where, why
- **Complaint**: Issues, problems, broken items
- **Feedback**: Positive feedback and satisfaction

### Response Types
1. **Greeting**: Personalized greeting responses
2. **FAQ Match**: Direct answers from FAQ database
3. **Contextual**: Responses based on conversation history
4. **Fallback**: Generic responses when no match is found

### NLP Features
- Text preprocessing and tokenization
- Stop word removal
- Similarity matching using SequenceMatcher
- Keyword-based intent detection

## Database Schema

### Conversations Table
- `id`: Primary key
- `session_id`: Session identifier
- `user_message`: User input
- `bot_response`: Chatbot response
- `timestamp`: Conversation timestamp
- `intent`: Detected intent
- `confidence`: Intent confidence score

### FAQ Table
- `id`: Primary key
- `question`: FAQ question
- `answer`: FAQ answer
- `category`: Question category
- `keywords`: Search keywords

## Configuration

### Adding Custom FAQ Data
Edit `faq_data.py` to add new FAQ entries:

```python
SAMPLE_FAQS = [
    {
        'question': 'Your question here?',
        'answer': 'Your answer here.',
        'category': 'Category Name',
        'keywords': ['keyword1', 'keyword2']
    }
]
```






