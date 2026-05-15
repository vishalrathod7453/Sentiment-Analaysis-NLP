import streamlit as st
import pickle
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Sentiment Analyzer", 
    page_icon="✨", 
    layout="centered"
)

# ==========================================
# 2. CUSTOM CSS & ANIMATIONS
# ==========================================
st.markdown("""
<style>
    /* Animated Gradient Title */
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .title-anim {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 5s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
    }
    /* Stylized Text Area */
    .stTextArea textarea {
        border-radius: 15px;
        border: 2px solid #e73c7e;
        padding: 15px;
        font-size: 16px;
    }
    /* Stylized Button */
    .stButton>button {
        border-radius: 25px;
        width: 100%;
        background-image: linear-gradient(to right, #FF512F 0%, #F09819  51%, #FF512F  100%);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: 0.5s;
        background-size: 200% auto;
        padding: 10px;
    }
    .stButton>button:hover {
        background-position: right center; /* Change the direction of the gradient */
        color: #fff;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. LOAD MODELS (CACHED FOR SPEED)
# ==========================================
@st.cache_resource
def load_ml_components():
    try:
        # Load your Naive Bayes model
        with open('SentimentAnalys.pkl', 'rb') as file:
            model = pickle.load(file)
            
        # IMPORTANT: Uncomment and load your vectorizer below!
        # with open('vectorizer.pkl', 'rb') as file:
        #     vectorizer = pickle.load(file)
            
        return model, None # Change 'None' to 'vectorizer' when you add it
    except Exception as e:
        st.error(f"Error loading model files: {e}")
        return None, None

model, vectorizer = load_ml_components()

# ==========================================
# 4. APP FRONTEND
# ==========================================
# Header
st.markdown('<p class="title-anim">AI Sentiment Analyzer</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 18px;'>Type a sentence below to discover the emotion behind the text.</p>", unsafe_allow_html=True)
st.write("---")

# User Input
user_input = st.text_area("✍️ Enter your text here:", placeholder="e.g. I absolutely loved this product! Highly recommended...", height=150)

# Analyze Button
if st.button("🔮 Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing the emotional tone..."):
            time.sleep(1.2) # Adding a slight delay for dramatic effect
            
            try:
                # ---------------------------------------------------------
                # REAL PREDICTION LOGIC (Uncomment when you have your vectorizer)
                # ---------------------------------------------------------
                # 1. Transform text to numbers using the vectorizer
                # input_data = vectorizer.transform([user_input])
                # 2. Make prediction
                # prediction = model.predict(input_data)[0] 
                
                # ---------------------------------------------------------
                # PLACEHOLDER LOGIC (Remove this block when using actual model)
                # ---------------------------------------------------------
                # This is just so the app doesn't crash before you add the vectorizer
                prediction = 'positive' if any(word in user_input.lower() for word in ['good', 'great', 'love', 'awesome', 'amazing', 'best']) else 'negative'
                # ---------------------------------------------------------

                st.write("---")
                # Display animated results based on the prediction output
                if prediction == 'positive':
                    st.balloons() # Triggers floating balloons animation
                    st.success("### ✨ Result: Positive Sentiment! ✨")
                    st.info("The AI detected positive and uplifting emotions in your text.")
                elif prediction == 'negative':
                    st.snow() # Triggers falling snow animation
                    st.error("### 🌧️ Result: Negative Sentiment. 🌧️")
                    st.info("The AI detected frustrated or negative emotions in your text.")
                    
            except Exception as e:
                st.error("Prediction failed. Did you remember to load your vectorizer? Check the code comments!")
