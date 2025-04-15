import streamlit as st

#Set up page 
st.title("🔍 How Named Entity Recognition Works")
st.write("But **HOW** is a machine actually able to identify and understand entities in text?")

import streamlit as st

#making quick quiz 
st.markdown("---")
st.markdown("### Quick: Which of these is a date?")

# if else statement based off answer to quiz
answer = st.radio(
    "Select the correct option:",
    ["5 ducks", "January 27th", "1st Place", "Winter Time"]
)

if answer == "January 27th":
    st.success("🎉 Correct! 'January 27th' is a date")
    st.markdown("""
We are able to recognize which of these options is a date because we intuitively understand what a date looks like — and perhaps more importantly, we have a strong grasp of context.

Even when multiple options contain numbers, we can quickly distinguish between a calendar date ("January 27th") and something like a race result ("1st Place"), or a quantity ("5 ducks").

This ability comes naturally to us because we’ve spent a lifetime learning the structure and meaning of language.

But for a machine, this is far from simple.

So how can a computer — with no real-world experience or intuition — learn to do the same?
""")
else:
    st.error("❌ Not quite.")


#inserting text to explain NER
st.markdown("---")
st.markdown("### Let's Dive In!")
st.markdown("""
Named Entity Recognition (NER) operates through a multi-step process that enables a computer to extract and categorize specific pieces of information—such as names, organizations, locations, and more—from written language.

At a high level, NER typically involves two main stages:

**Entity Identification** – Detecting potential named entities within a body of text.

**Entity Classification** – Categorizing those identified entities into predefined types (e.g., Person, Organization, Location).

The intricacies of this process can be further broken down into the following steps:
""")

# Explaining NER
st.markdown("""
#### 1. Tokenization
            """)
st.markdown("""
            Before identifying entities, the system must first divide the text into smaller components known as tokens. These are usually individual words or meaningful units.

            For example, the sentence:

            “Steve Jobs co-founded Apple”

            …would be tokenized as:

            ["Steve", "Jobs", "co-founded", "Apple"]
""")

st.markdown("""
#### 2. Entity Identification
            """)
st.markdown("""
            Once the text is tokenized, the system applies linguistic rules or statistical models to detect potential named entities. These may include recognizing patterns such as capitalization, common name structures, or standard formats (e.g., dates or numerical values).
""")

st.markdown("""
#### 3. Entity Classification
            """)
st.markdown("""
            After identification, each entity is classified into a specific category using machine learning models trained on annotated datasets. For example:

“Steve Jobs” → Person

“Apple” → Organization
            
""")

st.markdown("""
#### 4. Contextual Analysis
            """)
st.markdown("""
           To improve accuracy, NER systems often consider the surrounding context of each token. For instance, in the sentence “Apple released a new iPhone,” the context allows the system to determine that “Apple” refers to a company rather than the fruit.
""")

st.markdown("""
#### 5. Post-Processing
            """)
st.markdown("""
            Finally, post-processing steps may be applied to refine the output. These include resolving ambiguities, combining multi-token entities (e.g., “New York City”), or consulting external knowledge bases to validate and enrich the extracted data.

""")

# New Text Section to talk about challanges 
st.markdown("---")
st.markdown("### Even Still, Challenges Remain")
st.markdown("""
Despite advances in technology, machines still face several challenges when performing Named Entity Recognition. 
Two of the most significant are **ambiguity** and **context dependency**:

**Ambiguity**
Words can be inherently deceptive. A single term may have multiple meanings, and without sufficient context, it can be difficult—even for humans—to disambiguate.
For example, the word “Amazon” might refer to a major tech company or the world’s largest river. Determining the correct interpretation requires an understanding of the broader context in which the word appears.
            """)

# including images (using columns so they can be next to each other)
col1, col2 = st.columns(2)

with col1:
    st.image("https://images.nationalgeographic.org/image/upload/v1638890315/EducationHub/photos/amazon-river-basin.jpg")

with col2:
    st.image("https://static01.nyt.com/images/2021/10/29/business/29AMAZON-EARNINGS-1/merlin_187804479_f67d2a88-abe4-4d62-92d1-1adebe78f6bf-superJumbo.jpg")            

st.markdown("""
**Context Dependency**
The meaning of a word is often shaped by its surrounding text. Consider the word “Apple”. In a technology article, it most likely refers to the company. In a recipe, it almost certainly means the fruit.
Machines must be able to account for such contextual cues in order to accurately identify and classify entities.
""")

# Adding Image 
st.image(
    "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/MSNBC/Components/Photo/_new/091015-pcw-appbeat-hmed.jpg",
    use_container_width=True
)

st.markdown("---")
st.markdown("""
            👉 Now, head to the sidebar to use a Custom Named Entity Recognizer!
           
            """)