# SecretKey Voice Assistant 🎙️🤖

This project demonstrates how to build an **intelligent voice assistant** using **OpenAI's GPT-3.5**, **speech recognition**, and **text-to-speech synthesis**. The bot can answer questions naturally and achieves **real-time response** with human-like interaction.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technical Architecture](#technical-architecture)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Results](#results)

---

## Project Overview
The goal of this project is to create a voice assistant named **SecretKey** that can:
- Understand natural speech questions
- Provide intelligent responses using AI
- Speak answers aloud in natural voice

The project involves:
1. **Speech Recognition**: Converting voice to text using Google's Speech-to-Text API
2. **Natural Language Processing**: Generating responses with OpenAI's GPT-3.5
3. **Voice Synthesis**: Converting text responses to speech using pyttsx3
4. **Error Handling**: Robust failure recovery for all components

---

## Features
- **Voice Interaction**: Real-time speech recognition and response
- **Predefined Q&A**: Curated responses for common questions
- **AI Generation**: Dynamic answers for unexpected questions
- **Multi-platform**: Works on Windows, macOS, and Linux
- **Privacy Focused**: No data collection or storage

---

## Technical Architecture
The voice assistant is built using:

1. **Speech Recognition**:
   - `speech_recognition` library with Google Web Speech API
   - Noise cancellation and timeout handling

2. **Natural Language Processing**:
   - OpenAI GPT-3.5-turbo model
   - Custom system prompt for consistent personality
   - Fallback to predefined responses

3. **Voice Synthesis**:
   - pyttsx3 for offline text-to-speech
   - Adjustable speech rate and voice selection

4. **Core Logic**:
   ```mermaid
   graph TD
     A[Microphone Input] --> B[Speech-to-Text]
     B --> C{Predefined Question?}
     C -->|Yes| D[Return Cached Answer]
     C -->|No| E[Query OpenAI API]
     E --> F[Text-to-Speech]
     F --> G[Speaker Output]
