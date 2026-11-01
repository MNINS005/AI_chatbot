import nltk
import sqlite3
import re
import random
from difflib import SequenceMatcher
from faq_data import SAMPLE_FAQS

class IntelligentChatbot:
    def __init__(self):
        self._setup_nltk()
        self._load_faq_data()
        self.context_memory = {}
        
    def _setup_nltk(self):
        packages = ['punkt', 'stopwords', 'averaged_perceptron_tagger']
        for package in packages:
            try:
                nltk.data.find(f'tokenizers/{package}' if package == 'punkt' else f'corpora/{package}' if package == 'stopwords' else f'taggers/{package}')
            except LookupError:
                nltk.download(package)
    
    def _load_faq_data(self):
        with sqlite3.connect('chatbot.db') as conn:
            cursor = conn.cursor()
            
            if cursor.execute('SELECT COUNT(*) FROM faq').fetchone()[0] == 0:
                self._add_sample_faq_data(cursor)
            
            self.faq_data = cursor.execute('SELECT question, answer, category, keywords FROM faq').fetchall()
    
    def _add_sample_faq_data(self, cursor):
        faq_tuples = [(faq['question'], faq['answer'], faq['category'], ', '.join(faq['keywords'])) for faq in SAMPLE_FAQS]
        cursor.executemany('INSERT INTO faq (question, answer, category, keywords) VALUES (?, ?, ?, ?)', faq_tuples)
    
    def preprocess_text(self, text: str) -> str:
        text = re.sub(r'[^a-zA-Z0-9\s?]', '', text.lower())
        tokens = [token for token in nltk.word_tokenize(text) if token not in set(nltk.corpus.stopwords.words('english'))]
        return ' '.join(tokens)
    
    def classify_intent(self, message: str) -> tuple:
        msg_lower = message.lower()
        intent_patterns = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon'],
            'question': ['?', 'how', 'what', 'when', 'where', 'why'],
            'complaint': ['problem', 'issue', 'wrong', 'broken', 'damaged'],
            'feedback': ['good', 'great', 'excellent', 'love', 'satisfied']
        }
        
        for intent, patterns in intent_patterns.items():
            if any(word in msg_lower for word in patterns):
                return intent, 0.9 if intent == 'greeting' else 0.8
        return 'other', 0.5
    
    def find_best_faq_match(self, message: str) -> tuple:
        best_match = best_question = None
        best_score = 0.0
        msg_lower = message.lower()
        
        for faq_question, faq_answer, *_ in self.faq_data:
            similarity = SequenceMatcher(None, msg_lower, faq_question.lower()).ratio()
            if similarity > best_score and similarity > 0.3:
                best_score, best_match, best_question = similarity, faq_answer, faq_question
        
        return best_match, best_score, best_question
    
    def generate_contextual_response(self, message: str, session_id: str) -> str:
        with sqlite3.connect('chatbot.db') as conn:
            history = conn.cursor().execute(
                'SELECT user_message, bot_response FROM conversations WHERE session_id = ? ORDER BY timestamp DESC LIMIT 3',
                (session_id,)
            ).fetchall()
        
        if history:
            msg_lower = message.lower()
            if any(word in msg_lower for word in ['what do you mean', 'clarify', 'explain', 'elaborate']):
                return "I'd be happy to clarify! Could you let me know which part of my previous response you'd like me to explain in more detail?"
            if any(word in msg_lower for word in ['thank', 'thanks', 'appreciate']):
                return "You're welcome! Is there anything else I can help you with today?"
        return None
    
    def get_response(self, message: str, session_id: str) -> dict:
        intent, confidence = self.classify_intent(message)
        
        if intent == 'greeting':
            return {
                'response': random.choice([
                    "Hello! How can I assist you today?",
                    "Hi there! What can I help you with?",
                    "Good day! How may I help you?",
                    "Welcome! What can I do for you?"
                ]),
                'intent': intent,
                'confidence': confidence,
                'type': 'greeting'
            }
        
        contextual_response = self.generate_contextual_response(message, session_id)
        if contextual_response:
            return {
                'response': contextual_response,
                'intent': intent,
                'confidence': confidence,
                'type': 'contextual'
            }
        
        faq_answer, faq_confidence, matched_question = self.find_best_faq_match(message)
        if faq_answer:
            return {
                'response': faq_answer,
                'intent': intent,
                'confidence': faq_confidence,
                'type': 'faq_match',
                'matched_question': matched_question
            }
        
        return {
            'response': random.choice([
                "I'm not sure I understand. Could you please rephrase your question?",
                "I don't have information about that. Would you like me to connect you with a human agent?",
                "That's an interesting question. Let me find the best way to help you with that.",
                "I'm still learning! Could you try asking in a different way?",
                "I don't have a specific answer for that, but I'd be happy to help with general questions about our services."
            ]),
            'intent': intent,
            'confidence': 0.3,
            'type': 'fallback'
        }
