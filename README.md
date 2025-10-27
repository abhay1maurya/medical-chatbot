

# 🩺 MedBot - Medical Chatbot

A fully functional medical chatbot built with Flask and Google's Gemini API, designed to provide general health information with proper safety guidelines.

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![Gemini](https://img.shields.io/badge/Gemini-2.0_Flash-orange.svg)

## ✨ Features

- 🏥 **Medical Safety Focus** - Built-in disclaimers and emergency guidance
- 💬 **Web Chat Interface** - Beautiful, responsive UI
- 🔌 **REST API** - Programmatic access to chatbot
- 🚀 **Fast Responses** - Powered by Gemini 2.0 Flash
- 📱 **Mobile Responsive** - Works on all devices
- 🔒 **Secure Configuration** - Environment-based API key management

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [Gemini API Key](https://makersuite.google.com/app/apikey)


### Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/abhay1maurya/medical-chatbot.git
   cd medical-chatbot
   ```

2. **Set up environment**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your Gemini API key:
   # GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```

5. **Run application**
   ```bash
   python medbot.py
   ```
   Visit: http://localhost:8000

## 🔌 API Usage

### Web Interface
- Access the chat interface at: http://localhost:8000

### REST API Endpoint
```bash
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What are common cold symptoms?"}'
```

### API Response Format
```json
{
  "response": "Common cold symptoms include...",
  "disclaimer": "⚠️ Important: This information is for educational purposes only...",
  "success": true
}
```

### Other Endpoints
- **Health Check**: `GET /api/health`
- **API Info**: `GET /api/info`

## 🎯 Example Questions

- "What are common flu symptoms?"
- "How can I lower my blood pressure naturally?"
- "When should I see a doctor for a fever?"
- "What are the symptoms of COVID-19?"
- "How to manage stress and anxiety?"
- "What is a healthy diet for heart health?"

## 📁 Project Structure

```
medical-chatbot/
├── medbot.py              # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── .gitignore            # Git exclusion rules
├── README.md             # Project documentation
├── templates/
│   └── index.html        # Web chat interface
└── static/
    └── style.css         # Styling
```

## ⚠️ Medical Disclaimer

**This chatbot provides general health information only and is NOT a substitute for professional medical advice.**

- 🚨 **For emergencies**: Call your local emergency services immediately
- 🏥 **For medical concerns**: Always consult qualified healthcare professionals
- 📋 **For diagnoses**: See a doctor for proper medical evaluation
- 💊 **For treatments**: Follow prescribed medical treatments from your healthcare provider

The AI provides educational information but cannot diagnose, treat, or provide personalized medical advice.

## 🔧 Configuration

### Environment Variables
Create a `.env` file with:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

### Model Configuration
- **Model**: `gemini-2.0-flash`
- **Temperature**: Default (balanced for medical accuracy)
- **Safety Settings**: Built-in medical guidelines and disclaimers

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `.env` file exists with correct API key
   - Verify key is active in [Google AI Studio](https://makersuite.google.com/app/apikey)

2. **Port Already in Use**
   - Change port in `medbot.py` (default: 8000)

3. **Module Not Found**
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt`

### Health Check
Verify service status:
```bash
curl http://localhost:8000/api/health
```

## 🔒 Security Notes

- API keys are stored in `.env` (never committed to Git)
- No personal health data is stored
- All conversations are transient
- Use HTTPS in production environments

## 🚀 Deployment

For production deployment:

1. Set `debug=False` in `medbot.py`
2. Use production WSGI server (Gunicorn, Waitress)
3. Configure reverse proxy (Nginx, Apache)
4. Set up SSL certificates

### Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 medbot:app
```

## 👥 For Contributors

### Setting Up Development Environment
```bash
git clone https://github.com/abhay1maurya/medical-chatbot.git
cd medical-chatbot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Add your API key to .env
python medbot.py
```

### Project Standards
- Follow PEP 8 coding standards
- Include type hints where possible
- Add comments for complex logic
- Update requirements.txt when adding dependencies

## 📄 License

This project is for educational purposes. Medical chatbot applications should comply with healthcare regulations in your jurisdiction.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**Remember**: This tool is for educational information only. Always consult healthcare professionals for medical advice and emergencies.

---

<div align="center">

**Built with ❤️ using Flask & Gemini AI**

[Report Bug](https://github.com/abhay1maurya/medical-chatbot/issues) · [Request Feature](https://github.com/abhay1maurya/medical-chatbot/issues)

</div>

