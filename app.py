import streamlit as st
        background-color: #00C853;
        color: white;
    }

    .negative {
        background-color: #D50000;
        color: white;
    }

    .neutral {
        background-color: #2962FF;
        color: white;
    }

    textarea {
        border-radius: 15px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open('SentimentAnalys.pkl', 'rb'))

# ---------------- LOTTIE ANIMATION ----------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ai = load_lottie("https://assets2.lottiefiles.com/packages/lf20_zrqthn6o.json")

# ---------------- HEADER ----------------
st.markdown('<div class="title">💬 AI Sentiment Analysis App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyze user emotions using Machine Learning & NLP</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st_lottie(lottie_ai, height=300, key="ai")

with col2:
    user_input = st.text_area(
        "✍ Enter Your Text Here",
        height=200,
        placeholder="Type your review, feedback, or message here..."
    )

    predict_btn = st.button("🚀 Predict Sentiment")

# ---------------- PREDICTION ----------------
if predict_btn:
    if user_input.strip() == "":
        st.warning("⚠ Please enter some text.")

    else:
        with st.spinner("Analyzing Sentiment..."):
            time.sleep(2)

            prediction = model.predict([user_input])[0]

            st.balloons()

            if str(prediction).lower() == "positive":
                st.markdown(
                    '<div class="result-box positive">😊 Positive Sentiment</div>',
                    unsafe_allow_html=True
                )

            elif str(prediction).lower() == "negative":
                st.markdown(
                    '<div class="result-box negative">😡 Negative Sentiment</div>',
                    unsafe_allow_html=True
                )

            else:
                st.markdown(
                    f'<div class="result-box neutral">📌 Prediction: {prediction}</div>',
                    unsafe_allow_html=True
                )

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<center>Made with ❤️ using Streamlit & Machine Learning</center>",
    unsafe_allow_html=True
)
