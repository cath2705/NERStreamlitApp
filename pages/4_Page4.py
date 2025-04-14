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
    st.markdown("## How to Use the App")

    # Expandable section for explanation
    with st.expander("The App Explained"):
        st.markdown("""
        
        This app is designed to give you hands-on experience with Named Entity Recognition (NER) using spaCy, 
        with an added twist: you can inject your own custom rules to detect entities that might not otherwise 
        be captured by a general-purpose model.

        ### 1. Enter Your Text
        In the main section, enter or paste text in the textbox to analyze.

        ### 2. Add Custom Entity Rules (Optional)
        Use the sidebar to add rules. Enter a label and the exact token to detect.

        ### 3. Process Your Text
        Click the "Process Text" button to analyze and visualize results.

        ### 4. Review the Results
        The app will highlight entities in the text and label them by type.
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
