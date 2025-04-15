# NERStreamlitApp
This repository will include a custom Named Entity Recognition (NER) application using Python, spaCy, and Streamlit.
______________________________________________________________________________________________________________________________________________________________________________________________________________________________
                                                                                      Named Entity Recognition (NER) Streamlit App

Overview
______________________________________________________________________________________________________________________________________________________________________________________________________________________________
This Streamlit web application is a fully interactive, educational platform designed to help users understand and engage with Named Entity Recognition (NER), a core task in Natural Language Processing (NLP). The app introduces the concept of NER, explains how it works, walks users through the steps machines take to identify entities in text, and even allows users to explore NER hands-on using a custom-built entity recognition tool powered by spaCy.
______________________________________________________________________________________________________________________________________________________________________________________________________________________________
Goals of the Project

The app is designed to meet the following educational and functional goals:

1. Demystify Named Entity Recognition for beginners through accessible explanations.
2. Illustrate how NER works step-by-step from tokenization to classification.
3. Provide interactive NER experiences, where users can input and analyze text.
4. Allow for custom rule-based entity matching using spaCy's EntityRuler.
5. Encourage exploration and critical thinking with embedded quiz questions, animations, and visual storytelling.
______________________________________________________________________________________________________________________________________________________________________________________________________________________________
Overview of the App
The app is composed of 4 pages that each serve a different informational purpose. 
Here is an overview of the folder structure:

<img width="431" alt="Screenshot 2025-04-14 at 10 46 46 PM" src="https://github.com/user-attachments/assets/a969dd9f-0bf9-4b29-b03c-fd10f0b2b1c8" />

Here is a description of what each page does: 

1. Welcome Page:
- Introduces the concept of NER in simple language.
- Combines markdown, emojis, and visuals for engaging storytelling.
- Displays images and examples (e.g., Barack Obama being tagged as a PERSON).
- Includes an interactive quiz to let users guess what constitutes a named entity.
- Uses Streamlit Expander widgets to deliver optional deeper learning moments.

2. How Ner Works Page:
- Describes the NER pipeline in five intuitive steps: Tokenization, Entity Identification, Entity Classification, Contextual Analysis, Post-Processing
- Embeds real-world illustrations and text to demonstrate complex topics.
- Discusses ambiguity and context dependency, showcasing challenges in NLP.
- Uses side-by-side columns to compare interpretations visually

3. Basic Named Entity Recognizer:
- Loads a base spaCy model (en_core_web_sm).
- Allows user to: Upload a .txt file or input custom text
- Text is analyzed using pre-defined rule patterns from a local JSON file.
- Uses a custom-built highlight_entities function for colorful entity tagging.
- Prompts users to reflect on what the model got right/wrong (including with ambiguity).
- Features Lottie animations to maintain engagement.

4. Custom NER Explorer Page:
- Gives users full control to: Enter custom entity labels (e.g., PRODUCT, BRAND), Enter patterns (e.g., words/phrases to match), Dynamically build and save rules
- spaCy’s EntityRuler integrates the user-defined patterns in real time.
- Text is analyzed with both base model + custom patterns.
- Visual feedback shows where rules are applied.
- Empowers users to simulate how rule-based NLP systems work.
______________________________________________________________________________________________________________________________________________________________________________________________________________________________
🔍 Key Features & Interactivity
Here is an explaination of some of the main features I used to make my app interactive 

1. Quiz Widget
- The How This Works page includes an interactive quiz created with st.radio() and an if/else statement:
- This lets users test their intuition before diving into how machines process similar patterns.
  <img width="577" alt="Screenshot 2025-04-14 at 10 48 03 PM" src="https://github.com/user-attachments/assets/08997e82-37d0-428e-9583-fc12b0ed960e" />

2. Expander Widgets
- Used throughout the app (like on the Welcome and Custom NER pages) to hide large blocks of text until the user is ready. This keeps the interface clean.
- This structure uses Streamlit's context manager (with) to create collapsible content regions.
  <img width="586" alt="Screenshot 2025-04-14 at 10 49 03 PM" src="https://github.com/user-attachments/assets/9d497137-eecf-44e4-926a-f350b843a11f" />

3. Side-by-side Layouts with st.columns
- Used across pages to align text explanations with visuals (like diagrams or Lottie).
 <img width="580" alt="Screenshot 2025-04-14 at 10 50 59 PM" src="https://github.com/user-attachments/assets/8f372782-4af3-467f-a4d2-6d4b0185cd69" />

4. Lottie Animations
- Streamlit doesn’t natively support Lottie JSON animations, so I imported the streamlit-lottie package and fetching animation JSON from a public URL using requests.get().
 <img width="581" alt="Screenshot 2025-04-14 at 10 49 54 PM" src="https://github.com/user-attachments/assets/3b64825d-9abb-4f65-a6c0-aeca05c8c462" />

6. spaCy’s EntityRuler for Custom Patterns
- The Custom NER Explorer page uses spaCy's EntityRuler to let users define custom entity types like "BRAND", "PRODUCT", etc.
- I loaded patterns from a .json file like this:
<img width="599" alt="Screenshot 2025-04-14 at 10 50 28 PM" src="https://github.com/user-attachments/assets/69eba3f3-c134-455a-9a68-914f8d654a19" />
<img width="576" alt="Screenshot 2025-04-14 at 10 50 44 PM" src="https://github.com/user-attachments/assets/e7cc6296-4c2a-4c62-a69c-a3152285922f" />

_______________________________________________________________________________________________________________________________________________
Technical Stack
- Language: Python 3.10+
- Framework: Streamlit
- NLP Library: spaCy

Additional Modules:
- requests (for loading Lottie animations)
- json (to handle user-created rule sets)
- os (file management)
_______________________________________________________________________________________________________________________________________________
Educational Design Philosophy

This app is built with approachability and interactivity in mind:
- Non-technical users can still follow explanations
- Learners build intuition with examples, visuals, and play
- Developers can explore advanced customization through spaCy's EntityRuler

By blending text analysis with user-driven control, this app bridges the gap between abstract NLP concepts and hands-on understanding.
_______________________________________________________________________________________________________________________________________________

How to Run the App

Clone the repository:
- git clone https://github.com/yourusername/NERStreamlitApp.git
- cd NERStreamlitApp

Create a virtual environment and activate it:
- python -m venv ner_env
- source ner_env/bin/activate  # On Windows: ner_env\Scripts\activate

Install dependencies:
- pip install -r requirements.txt

Run the app:
- streamlit run Welcome.py
_______________________________________________________________________________________________________________________________________________
Credits

Developed by Catherine for an educational NLP visualization project at the University of Notre Dame.
Inspired by Streamlit’s interactive tools and spaCy’s flexible NLP pipelines.
