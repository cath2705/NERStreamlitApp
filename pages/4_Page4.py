import streamlit as st
import spacy
from spacy import displacy

# --- Main App Function ---
def main():
    st.title("Custom NER Application with spaCy")
    st.write(
        "This application allows you to explore Named Entity Recognition (NER) "
        "by adding custom rules using spaCy’s EntityRuler. You can enter your own text "
        "or use the provided sample text, define custom entities, and visualize the detected entities."
    )

    # --- Sidebar: Custom Rules Input ---
    st.sidebar.header("Add Custom Entity Rule")
    custom_label = st.sidebar.text_input("Entity Label (e.g., PRODUCT, TECH)", key="label")
    custom_token = st.sidebar.text_input("Pattern Text (exact word to match)", key="token")
    
    if st.sidebar.button("Add Entity Rule"):
        if custom_label and custom_token:
            pattern = {"label": custom_label, "pattern": [{"LOWER": custom_token.lower()}]}
            # Initialize session state list if not present
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
        # Load the spaCy model
        nlp = spacy.load("en_core_web_sm")
        # Add the EntityRuler pipeline component before the standard NER
        ruler = nlp.add_pipe("entity_ruler", before="ner", config={"overwrite_ents": True})
        
        # Add any custom patterns from session state (if they exist)
        if "patterns" in st.session_state and st.session_state.patterns:
            ruler.add_patterns(st.session_state.patterns)
        
        # Process the text
        doc = nlp(user_text)
        
        # Render the visualization using spaCy's displacy
        html = displacy.render(doc, style="ent", jupyter=False)
        st.write("### Recognized Entities")
        st.markdown(html, unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()