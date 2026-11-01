from flask import render_template, request, jsonify
from database import log_conversation, get_conversations, get_faq

def register_routes(app, chatbot):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/chat', methods=['POST'])
    def chat():
        data = request.json
        user_message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        response_data = chatbot.get_response(user_message, session_id)
        log_conversation(session_id, user_message, response_data['response'], 
                        response_data.get('intent'), response_data.get('confidence'))
        
        return jsonify(response_data)

    @app.route('/conversations/<session_id>')
    def get_conversations_route(session_id):
        conversations = get_conversations(session_id)
        return jsonify({'conversations': conversations})

    @app.route('/faq')
    def get_faq_route():
        faqs = get_faq()
        return jsonify({'faqs': faqs})
