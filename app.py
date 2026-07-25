import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Marketing Assistant AI",
    page_icon="📈",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background:#F5F7FA;
    color:black;
}

/* Main Card */
.main-box{
    background:white;
    padding:30px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.15);
    color:black;
}

/* Title */
.title{
    font-size:42px;
    font-weight:bold;
    text-align:center;
    color:#1565C0;
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:black;
    font-size:18px;
    margin-bottom:25px;
}

/* AI Response */
.response{
    background:#E3F2FD;
    padding:20px;
    border-radius:12px;
    border-left:6px solid #1976D2;
    color:black !important;
    font-size:17px;
}

/* Make all text black */
label,
p,
span,
div,
h2,
h3,
h4,
h5,
h6{
    color:black !important;
}

/* Text Area */
textarea{
    color:black !important;
    background:white !important;
}

/* Input Labels */
.stTextArea label,
.stTextInput label,
.stSelectbox label,
.stNumberInput label,
.stSlider label{
    color:black !important;
}

/* Info Box */
[data-testid="stAlert"]{
    color:black !important;
}

/* Caption */
[data-testid="stCaptionContainer"]{
    color:black !important;
}

/* Button */
.stButton>button{
    background:#1976D2;
    color:white !important;
    height:55px;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    background:#0D47A1;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown(
    "<div class='title'>📈 Marketing Assistant AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Get AI-powered marketing strategies, SEO tips, branding ideas, and campaign guidance.</div>",
    unsafe_allow_html=True
)

# ---------------- MAIN CARD ---------------- #

st.markdown("<div class='main-box'>", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:

    question = st.text_area(
        "💬 Enter Your Marketing Question",
        height=180,
        placeholder="Example: How can I increase Instagram engagement?"
    )

with col2:

    st.info("""
### 💡 You can ask about

✅ SEO

✅ Social Media

✅ Branding

✅ Email Marketing

✅ Content Marketing

✅ Advertising

✅ Market Research

✅ Lead Generation
""")

st.write("")

ask = st.button(
    "🚀 Ask AI",
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- AI RESPONSE ---------------- #

if ask:

    with st.spinner("Generating marketing advice..."):

        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.3
        )

        prompt = ChatPromptTemplate.from_template(
            """
You are a Marketing Expert.

Your job is to answer ONLY marketing-related questions.

Topics include:

- Digital Marketing
- Social Media Marketing
- Content Marketing
- SEO
- Email Marketing
- Branding
- Advertising Campaigns
- Marketing Strategy
- Market Research
- Target Audience
- Customer Engagement
- Lead Generation
- Influencer Marketing
- Product Launch
- Sales Funnel
- Marketing Analytics
- Copywriting
- Marketing Automation

If the question is not related to marketing reply:

"Sorry, I only answer marketing-related questions."

Question:
{question}

Provide:

1. Simple Explanation

2. Step-by-step guidance

3. Best Practices

4. Common Mistakes

5. Final Recommendation
"""
        )

        chain = prompt | llm

        response = chain.invoke(
            {
                "question": question
            }
        )

    st.write("")

    st.subheader("📊 AI Marketing Advice")

    st.markdown(
        f"""
<div class="response">

{response.content}

</div>
""",
        unsafe_allow_html=True
    )

st.write("")
st.caption("Built with ❤️ using Streamlit + LangChain + Groq")
