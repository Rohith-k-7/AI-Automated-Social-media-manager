# AI Social Media Manager

An AI-powered web application that transforms **images and videos into complete social media campaigns** using multimodal AI.

---

## 🎯 Overview

This project automates social media content creation by analyzing uploaded media and generating:

- 📢 Engaging captions  
- #️⃣ Trending hashtags  
- 🎵 Music recommendations  
- ⏰ Optimal posting schedule  

It helps creators and businesses **save time and improve engagement**.

---

## ✨ Features

- 🖼️ Image + 🎥 Video support  
- 🤖 AI-powered content generation  
- 🧩 Multi-agent architecture  
- 🎯 Structured output (bullet points & chips UI)  
- 🌐 Direct posting links for:
  - Instagram  
  - Facebook  
  - LinkedIn  
  - X (Twitter)  

---

## 🧠 How It Works
Upload Media → Video Frame Extraction → AI Analysis → Content Generation → Web UI Output


---

## ⚙️ Tech Stack

- Python  
- Flask  
- Gemini AI (Multimodal)  
- OpenCV (Video processing)  
- HTML + CSS  

---

## 🧩 Architecture
User Input
↓
Media Processing (Image / Video)
↓
AI Agents:

Caption Agent
Hashtag Agent
Music Agent
Scheduler Agent
↓
Frontend UI (Flask)

## 📂 Project Structure

social-media-agent/
│
├── app.py
├── .env
├── requirements.txt
│
├── agents/
│   ├── caption_agent.py
│   ├── hashtag_agent.py
│   ├── music_agent.py
│   └── scheduler_agent.py
│
├── utils/
│   ├── gemini_api.py
│   └── video_processor.py
│
├── templates/
│   └── index.html
│
└── static/
    └── uploads/
