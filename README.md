# Multi-Modal-Assistant-
Build an assistant capable of answering queries based on both text and images
---
title: Multi-Modal Assistant (LLaVA via Ollama) --- Project
  Documentation
---

# 1. Project Overview

This project builds a Multi-Modal Assistant capable of answering user
queries based on both text and images. It uses the LLaVA model running
locally via Ollama and provides a clean, user-friendly interface with
Streamlit.\
\
- No cloud APIs or internet connection required.\
- Fully local inference with privacy.\
- Upload an image, ask a question about it, get contextual answers.

# 2. How It Works

The application allows users to upload an image and ask questions
related to the content of that image. When a user submits a question,
the image is encoded in base64 format and sent along with the question
to the local Ollama server running the LLaVA model. LLaVA is a
multi-modal language model capable of understanding and reasoning about
both text and images.\
\
The Ollama server processes the request and returns a text-based answer
that is contextually relevant to the uploaded image and the user's
question. This response is then displayed in the Streamlit interface.
Users can repeat this process with new images and questions, enabling
interactive multi-modal querying.

# 3. Technologies Used

  -----------------------------------------------------------------------
  Technology                          Purpose
  ----------------------------------- -----------------------------------
  Python                              Main programming language

  Streamlit                           Web app framework for UI

  Ollama                              Local LLM serving platform

  LLaVA model                         Multi-modal vision-language model

  Requests lib                        HTTP client to communicate with
                                      Ollama API

  Base64                              Encoding images for sending via API
  -----------------------------------------------------------------------

# 4. Prerequisites

• Python 3.7 or later installed\
• Streamlit installed (pip install streamlit)\
• Requests library installed (pip install requests)\
• Ollama installed and configured on your system (https://ollama.com)\
• LLaVA model available via Ollama (ollama run llava)

# 5. Project Setup & Running

Step 1: Clone or Download the Project

Save the main code as app.py in a folder.

Step 2: Install Dependencies

pip install streamlit requests

Step 3: Run LLaVA Model Locally

Open a terminal and start LLaVA with Ollama:

ollama run llava

Make sure this terminal stays open while running the Streamlit app.

Step 4: Run the Streamlit Application

Run the app using the command:

streamlit run app.py

# 6. Application Usage

• Upload an image using the uploader.\
• Type a question related to the uploaded image.\
• Click the \'Get Answer\' button to get the response from the
assistant.\
• After getting the answer, click \'Upload Another Image\' to start over
with a new image.\
• All processing happens locally; no external API keys or internet
connection required.

# 7. Notes

• Ensure Ollama is running with the LLaVA model before launching the
Streamlit app.\
• The application communicates with the local Ollama server via HTTP
requests.\
• The interface is designed to be minimalistic and user-friendly.\
• Streamlit\'s rerun functionality is used to reset the app state when
uploading new images.
