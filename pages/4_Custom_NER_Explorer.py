import streamlit as st
import spacy
from spacy import displacy

# --- Main App Function ---
def main():
    st.title("🎉 Welcome to the Custom NER Explorer! 🎉")
    st.write("""
        This application allows you to explore Named Entity Recognition (NER). 
        You can analyze text to see which words and phrases are automatically tagged as entities—
        and even add your own custom entity rules to tailor the analysis.
    """)

    # new text 
    st.markdown("### Need Help Understanding How to Use the App?")

    # Expandable section for explanation
    with st.expander("Click to Have the App Explained 👉"):
        st.markdown("""
                    This app is designed to give you hands-on experience with Named Entity Recognition (NER) using spaCy—
                     with an added twist: you can inject your own custom rules to detect entities that might not otherwise 
                    be captured by a general-purpose model.
                    
                     ### 1. Enter Your Text
                    In the main section, enter or paste text in the textbox to analyze.
                     
                     ### 2. Add Custom Entity Rules (Optional)
                    On the left-hand sidebar, you can specify your own rules for recognizing entities:
                    
                    **Entity Label:** Enter a custom label that describes the type of entity (for example, PRODUCT, BRAND, or LOCATION).
                    
                    **Pattern Text:** Input the exact word (or token) you want to detect. The app will match occurrences of this word (case-insensitive) in your text.
                    
                    **Adding a Rule:** Click the "Add Entity Rule" button to save your rule. Your current custom rules will be listed below, so you can review them before processing.
                    
                    ### 3. Process Your Text
                    Once you have entered your text and added any custom rules you’d like, click the "Process Text" button.
                    The app then uses spaCy’s language model along with your custom rules to analyze the text, tagging any matching tokens or phrases.
                    
                     ### 4. Review the Results
                     After processing, the app highlights detected entities directly within the text.
                    
                    **Entity Labels:** Each highlighted section shows the entity type. This lets you see which parts of the text the model recognized (or you defined) as entities.
                    
                    **Dynamic Updates:** Feel free to adjust your text or add new rules and process the text again to see how the analysis changes.
                    
                    """)

    st.markdown("---")

    # --- Sidebar: Custom Rules Input ---
    st.sidebar.header("Add Custom Entity Rule")
    custom_label = st.sidebar.text_input("Entity Label (e.g., PRODUCT, TECH)", key="label")
    custom_token = st.sidebar.text_input("Pattern Text (exact word to match)", key="token")
    
    if st.sidebar.button("Add Entity Rule"):
        if custom_label and custom_token:
            pattern = {"label": custom_label, "pattern": [{"LOWER": custom_token.lower()}]}
            if "patterns" not in st.session_state:
                st.session_state.patterns = []
            st.session_state.patterns.append(pattern)
            st.sidebar.success(f"Rule added: [{custom_label}] → '{custom_token}'")
        else:
            st.sidebar.error("Both Entity Label and Pattern Text are required.")

    st.sidebar.header("Current Custom Rules")
    if "patterns" in st.session_state and st.session_state.patterns:
        st.sidebar.json(st.session_state.patterns)
    else:
        st.sidebar.write("No custom rules added yet.")

    # --- Main Content: Text Input ---
    st.subheader("Input Text for Analysis")
    sample_text = "Apple is looking at buying U.K. startup for $1 billion."
    user_text = st.text_area("Enter text to analyze", value=sample_text, height=200)

    # --- Processing Button ---
    if st.button("Process Text"):
        nlp = spacy.load("en_core_web_sm")
        ruler = nlp.add_pipe("entity_ruler", before="ner", config={"overwrite_ents": True})

        if "patterns" in st.session_state and st.session_state.patterns:
            ruler.add_patterns(st.session_state.patterns)
        
        doc = nlp(user_text)
        html = displacy.render(doc, style="ent", jupyter=False)
        st.write("### Recognized Entities")
        st.markdown(html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

# new text 
st.markdown("### What do my Results Mean? ")

# Expandable section
with st.expander("# Click to Find Out 👉"):
    
    # Add spacing below image
    st.markdown("")

    st.image(
    "/Users/catherineparis/Documents/GitHub/Paris-Python-Portfolio/NERStreamlitApp/SC2.png", caption=" Here is a list of what SpaCy Named Entity Recognition labels mean ", use_container_width=True
    )


st.markdown("---")

# New text giving an example
st.write("""
         ## Need Inspiration for Your Custom Rules? 
         ### Here’s an Example Use Case
    """)

# to imput images
import streamlit as st
from PIL import Image

image_path = "/Users/catherineparis/Documents/GitHub/Paris-Python-Portfolio/NERStreamlitApp/Screenshot1.png"
image = Image.open(image_path)
st.image(image, caption="First, I imputed the sentence into the Custom NER Explorer app with no added entity labels or pattern text, to see what that output would look like. As you can see, the app (incorrectly) recognized Tesla as NORP (NORP is SpaCy’s classification for Nationalities or religious or political groups) ", use_container_width=True)

# adding text
st.write("""
    This kind of misclassification is actually pretty common with pre-trained spaCy models. Pre-trained spaCy models are trained on broad, general datasets and can struggle with domain-specific language, leading to misclassifications when encountering ambiguous or unfamiliar terms. They rely on statistical patterns, which might not capture nuanced meanings outside their training data.
    
    That’s why you want to add custom rules!
         
    """)

st.markdown("---")

# digression into seperate example
st.write("""
  ### ✋ Quick digression!
  Observe the how the accuracy improves as custom rules are added
    """)

# including images (using columns so they can be next to each other)
colx, coly = st.columns(2)

with colx:
    st.image(
    "https://dataknowsall.com/hs-fs/hubfs/image-png-1.png?width=1600&height=920&name=image-png-1.png", caption="Before adding custom rules ", use_container_width=True
    )

with coly:
    st.image(
    "https://dataknowsall.com/hs-fs/hubfs/image-png-2.png?width=1600&height=1000&name=image-png-2.png", caption="After adding custom rules ", use_container_width=True
    )
 
st.write("""
         Notice how much more accurate the second version is. 
         """)

st.markdown("---")

st.write("""
         ### Back to Our Example Use Case!

         Since our orginal Named Entity Recognition was not accurate for our sentence **I enjoyed a crisp apple from the orchard while walking past the Tesla showroom downtown.** Let's add some custom Entity Labels and Pattern Text using the sidebar tools
        """)

# including images (using columns so they can be next to each other)
col1, col2 = st.columns(2)

with col1:
    image_path = "/Users/catherineparis/Documents/GitHub/Paris-Python-Portfolio/NERStreamlitApp/Screenshot2.png"
    image = Image.open(image_path)
    st.image(image, caption="This rule will search for the word **apple** in the text. Every time it finds **apple** (ignoring case differences), it will tag it as a fruit. ", use_container_width=True)

with col2:
    image_path = "/Users/catherineparis/Documents/GitHub/Paris-Python-Portfolio/NERStreamlitApp/Screenshot3.png"
    image = Image.open(image_path)
    st.image(image, caption="This rule will look for the word **tesla** in the text. Every match will be classified under the CAR label, signifying that it represents a car brand ", use_container_width=True)

st.write("""
         ### Now Let's Re-Run the App!
        """)

image_path = "/Users/catherineparis/Documents/GitHub/Paris-Python-Portfolio/NERStreamlitApp/Screenshot4.png"
image = Image.open(image_path)
st.image(image, caption=" Now the app correctly identifies **apple** as a fruit and **tesla** as a car ", use_container_width=True)

st.write("""
        ## Now Try It Yourself!👆😃
        """)