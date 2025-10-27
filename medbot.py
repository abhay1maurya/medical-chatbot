import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("ERROR: Please set GEMINI_API_KEY in your .env file")

genai.configure(api_key=api_key)

# Medical context prompt for fine-tuning
MEDICAL_CONTEXT = """
You are MedBot, a helpful medical assistant designed to provide general health information and answer medical questions.

CRITICAL MEDICAL GUIDELINES:
1. Provide accurate, evidence-based medical information only
2. Always include a disclaimer that you are not a substitute for professional medical advice
3. For emergency symptoms (chest pain, difficulty breathing, severe bleeding, sudden weakness), advise immediate medical attention
4. Be clear about when someone should consult a healthcare professional
5. Use simple, understandable language for the general public
6. Do not provide diagnoses - only general information about conditions and symptoms
7. Encourage preventive care and healthy lifestyle choices
8. Be empathetic and supportive in your responses

EMERGENCY SITUATIONS - Always respond with:
"If you are experiencing [symptom], this could be a medical emergency. Please call emergency services or go to the nearest hospital immediately."

EXAMPLES OF APPROPRIATE RESPONSES:

User: "I have a headache"
Response: "Headaches can have various causes including tension, dehydration, stress, or sinus issues. You can try resting in a quiet room, drinking water, applying a cool compress, or using over-the-counter pain relief if appropriate for you. If your headache is severe, persistent, comes on suddenly, or is accompanied by other symptoms like vision changes, confusion, fever, or stiff neck, please consult a healthcare provider promptly."

User: "What are symptoms of COVID-19?"
Response: "Common symptoms of COVID-19 may include fever, cough, fatigue, loss of taste or smell, sore throat, and body aches. Some people may experience more severe symptoms like difficulty breathing. If you're experiencing severe symptoms like trouble breathing, persistent chest pain, or confusion, seek medical attention immediately. For testing and treatment recommendations, please consult with a healthcare provider."

User: "How can I lower my blood pressure?"
Response: "Lifestyle changes that may help maintain healthy blood pressure include: reducing salt intake, eating a balanced diet rich in fruits and vegetables, regular physical activity, maintaining a healthy weight, limiting alcohol, and managing stress. However, it's important to work with a healthcare provider to develop a personalized plan, especially if you have been diagnosed with high blood pressure."

Remember: Always prioritize user safety and encourage professional medical consultation for specific health concerns.
"""

# Initialize the Gemini model
try:
    model = genai.GenerativeModel('gemini-2.0-flash')
    # Test the API connection with a simple prompt
    test_response = model.generate_content("Say 'Connected' if you're working.")
    print("✅ Gemini API connected successfully")
except Exception as e:
    print(f"❌ Error connecting to Gemini API: {e}")
    model = None

def create_medical_prompt(user_message):
    """Create a properly formatted medical prompt with context"""
    prompt = f"""
{MEDICAL_CONTEXT}

Now, please respond to the following user question while following all the medical guidelines above:

USER QUESTION: {user_message}

YOUR RESPONSE:
"""
    return prompt

@app.route('/')
def home():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy", 
        "service": "Medical Chatbot API",
        "model_ready": model is not None
    })

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    """
    Main chat API endpoint
    Accepts JSON: {"message": "user question"}
    Returns JSON: {"response": "answer", "disclaimer": "safety notice"}
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate request
        if not data or 'message' not in data:
            return jsonify({
                "error": "Invalid request format",
                "message": "Please provide a 'message' field in JSON format"
            }), 400
        
        user_message = data['message'].strip()
        
        if not user_message:
            return jsonify({
                "error": "Empty message",
                "message": "Message cannot be empty"
            }), 400
        
        if not model:
            return jsonify({
                "error": "Service unavailable",
                "message": "AI model is not available. Please check your API configuration."
            }), 503
        
        # Create medical context prompt
        medical_prompt = create_medical_prompt(user_message)
        
        # Generate response using Gemini
        response = model.generate_content(medical_prompt)
        
        # Return successful response
        return jsonify({
            "response": response.text,
            "disclaimer": "⚠️ Important: This information is for educational purposes only and is not medical advice. Always consult with a qualified healthcare professional for medical concerns.",
            "success": True
        })
        
    except Exception as e:
        # Handle errors gracefully
        error_message = f"Error generating response: {str(e)}"
        print(error_message)
        
        return jsonify({
            "error": "Internal server error",
            "message": "Sorry, I encountered an error while processing your request. Please try again.",
            "success": False
        }), 500

@app.route('/api/info')
def api_info():
    """API information endpoint"""
    return jsonify({
        "name": "Medical Chatbot API",
        "version": "1.0.0",
        "endpoints": {
            "GET /": "Web chat interface",
            "POST /api/chat": "Chat with the medical bot",
            "GET /api/health": "Service health check",
            "GET /api/info": "This information"
        },
        "description": "A medical Q&A chatbot using Google Gemini AI"
    })

if __name__ == '__main__':
    print("🚀 Starting Medical Chatbot Server...")
    print("📖 Visit http://localhost:8000 for the web interface")
    print("🔧 API docs available at http://localhost:8000/api/info")
    
    # Run the Flask app
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )