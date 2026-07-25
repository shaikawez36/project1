import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(
    page_title="Marketing Assistant",
    page_icon="📈"
)

st.title("Marketing Assistant AI")
st.write("This is an AI Marketing Assistant that helps with marketing strategies and content creation.")

st.write("Ask anything related to marketing")

question = st.text_area(
    "Enter Your Marketing Question"
)

if st.button("Ask AI"):
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
        - SEO (Search Engine Optimization)
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

        If the user asks anything outside marketing,
        reply:

        "Sorry, I only answer marketing-related questions."

        Question:
        {question}

        Provide:
        1. Simple Explanation
        2. Step-by-step guidance
        3. Best Practices
        4. Tips and Common Mistakes to Avoid
        """
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "question": question
        }
    )

    st.success(response.content)