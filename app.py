from flask import Flask
from flask_cors import CORS
from database import init_db
from routes import register_routes
from chatbot import IntelligentChatbot

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    init_db()
    chatbot = IntelligentChatbot()
    register_routes(app, chatbot)
    app.run()
