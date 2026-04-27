import streamlit as st
import pandas as pd
from model import calculate_lead_score, get_priority
from data_processing import preprocess_data

# Set page configuration
st.set_page_config(
    page_title="Lead Scoring System",
    page_icon="🎯",
    layout="centered"
)

# Custom CSS for premium look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        border: none;
        color: white;
    }
    .score-card {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        color: white;
    }
    .high-priority {
        background-color: #28a745;
    }
    .medium-priority {
        background-color: #ffc107;
        color: black;
    }
    .low-priority {
        background-color: #dc3545;
    }
    h1 {
        color: #1e293b;
        text-align: center;
        font-weight: 700;
    }
    .subtitle {
        text-align: center;
        color: #64748b;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.markdown("<h1>Lead Scoring System 🎯</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Predict and prioritize your business leads efficiently</p>", unsafe_allow_html=True)

    with st.container():
        st.subheader("Lead Information")
        col1, col2 = st.columns(2)

        with col1:
            industry = st.selectbox(
                "Industry",
                ["Technology", "Finance", "Healthcare", "Manufacturing", "Retail", "Education", "Other"]
            )
            company_size = st.selectbox(
                "Company Size",
                ["1-10", "11-50", "51-200", "201-500", "501-1000", "1000+"]
            )
            demo_requested = st.radio("Demo Requested?", ["No", "Yes"])

        with col2:
            visits = st.slider("Website Visits", 0, 50, 5)
            pricing_time = st.slider("Time on Pricing Page (mins)", 0, 30, 2)
            email_clicks = st.slider("Email Clicks", 0, 20, 1)

    # Clean the input data using the data_processing module
    # (Though it's single input, we follow the structure)
    input_data = pd.DataFrame([{
        'Industry': industry,
        'Company Size': company_size
    }])
    input_data = preprocess_data(input_data)
    
    # We use the cleaned data (though minimal for this simple logic)
    clean_industry = input_data['Industry'][0]

    if st.button("Calculate Lead Score"):
        score = calculate_lead_score(pricing_time, demo_requested, visits, email_clicks)
        priority = get_priority(score)
        
        # Color logic
        priority_class = ""
        if priority == "High":
            priority_class = "high-priority"
        elif priority == "Medium":
            priority_class = "medium-priority"
        else:
            priority_class = "low-priority"

        st.markdown(f"""
            <div class="score-card {priority_class}">
                <h2>Score: {score}/100</h2>
                <h3>Priority: {priority}</h3>
                <p>Industry: {clean_industry.capitalize()} | Company Size: {company_size}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Additional Insights
        st.info(f"Based on the input, this lead from the **{industry}** industry has a **{priority}** conversion probability.")

if __name__ == "__main__":
    main()
