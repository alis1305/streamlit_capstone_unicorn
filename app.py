import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# Load the trained model
model = load_model('model')

# Define the Streamlit app
def main():
    st.title("Company Success Prediction")

    # User input for each feature
    #company = st.text_input("Company Name")
    fintech = st.selectbox("Fintech", [0, 1])
    web3 = st.selectbox("Web3", [0, 1])
    ecommerce = st.selectbox("E-commerce", [0, 1])
    consumer_others = st.selectbox("Consumer Others", [0, 1])
    edtech = st.selectbox("EdTech", [0, 1])
    esg = st.selectbox("ESG", [0, 1])
    enterprise_saas = st.selectbox("Enterprise SaaS", [0, 1])
    others = st.selectbox("Others", [0, 1])
    business_model = st.text_input("Business Model")
    glassdoor_rating = st.slider("Glassdoor Rating", 0.0, 5.0, 3.5)
    sucessranking_four_gdranking = st.slider("Success Ranking Four (GD Ranking)", 0, 10, 5)
    glassdoor_total_employees = st.number_input("Glassdoor Total Employees", min_value=0, step=1)
    sucessranking_three_employees = st.slider("Success Ranking Three (Employees)", 0, 10, 5)
    glassdoor_recommend_percentage = st.slider("Glassdoor Recommend Percentage", 0, 100, 50)
    valauation_divide_vdminusyf = st.number_input("Valuation Divide VD minus YF", min_value=0.0)
    sucessranking_two_valdivideyear = st.slider("Success Ranking Two (Val Divide Year)", 0, 10, 5)
    similar_businessmodel_overseas = st.selectbox("Similar Business Model Overseas", [0, 1])
    year_operating = st.number_input("Year Operating", min_value=0)
    years_to_unicorn = st.number_input("Years to Unicorn", min_value=0)
    exit = st.selectbox("Exit", [0, 1])
    country = st.text_input("Country")
    patent = st.selectbox("Patent", [0, 1])
    pivot = st.selectbox("Pivot", [0, 1])
    subsidiary_corporatespinoff = st.selectbox("Subsidiary / Corporate Spinoff", [0, 1])
    firsttime_founder = st.selectbox("First-time Founder", [0, 1])
    tech_founder = st.selectbox("Tech Founder", [0, 1])
    foundersage_when_started = st.number_input("Founder's Age When Started", min_value=0)
    graduated_overseas_uni = st.selectbox("Graduated Overseas University", [0, 1])
    sg_uni = st.selectbox("SG University", [0, 1])
    india_uni = st.selectbox("India University", [0, 1])
    us_uk_uni = st.selectbox("US/UK University", [0, 1])
    sea_uni = st.selectbox("SEA University", [0, 1])
    china_uni = st.selectbox("China University", [0, 1])
    aust_uni = st.selectbox("Aust University", [0, 1])
    no_graduate = st.selectbox("No Graduate", [0, 1])
    investor_vertex = st.selectbox("Investor Vertex", [0, 1])
    investor_500global = st.selectbox("Investor 500 Global", [0, 1])
    investor_eastvc = st.selectbox("Investor East VC", [0, 1])
    investor_sequoia = st.selectbox("Investor Sequoia", [0, 1])
    investor_yc = st.selectbox("Investor YC", [0, 1])
    investor_insignia = st.selectbox("Investor Insignia", [0, 1])
    investor_ggv = st.selectbox("Investor GGV", [0, 1])
    investor_wavemaker = st.selectbox("Investor Wavemaker", [0, 1])
    investor_openspace = st.selectbox("Investor Openspace", [0, 1])
    investor_alphajwc = st.selectbox("Investor Alpha JWC", [0, 1])
    investor_jungle = st.selectbox("Investor Jungle", [0, 1])
    investor_cyberagentcapital = st.selectbox("Investor CyberAgent Capital", [0, 1])

    # Create a dictionary with the inputs
    input_data = {
        #'company': company,
        'fintech': fintech,
        'web3': web3,
        'ecommerce': ecommerce,
        'consumer_others': consumer_others,
        'edtech ': edtech,
        'esg': esg,
        'enterprise_saas': enterprise_saas,
        'others ': others,
        'business_model': business_model,
        'glassdoor_rating': glassdoor_rating,
        'sucessranking_four_gdranking': sucessranking_four_gdranking,
        'glassdoor_total_employees': glassdoor_total_employees,
        'sucessranking_three_employees': sucessranking_three_employees,
        'glassdoor_recommend_percentage': glassdoor_recommend_percentage,
        'valauation_divide_vdminusyf': valauation_divide_vdminusyf,
        'sucessranking_two_valdivideyear': sucessranking_two_valdivideyear,
        'similar_businessmodel_overseas': similar_businessmodel_overseas,
        'year_operating': year_operating,
        #'years_to_unicorn': years_to_unicorn,
        'exit': exit,
        'country': country,
        'patent': patent,
        'pivot': pivot,
        'subsidiary _corporatespinoff': subsidiary_corporatespinoff,
        'firsttime_founder': firsttime_founder,
        'tech_founder': tech_founder,
        'foundersage_when_started': foundersage_when_started,
        'graduated_overseas_uni': graduated_overseas_uni,
        'sg_uni': sg_uni,
        'india_uni': india_uni,
        'us_uk_uni': us_uk_uni,
        'sea_uni': sea_uni,
        'china_uni': china_uni,
        'aust_uni': aust_uni,
        'no_graduate': no_graduate,
        'investor_vertex': investor_vertex,
        'investor_500global': investor_500global,
        'investor_eastvc': investor_eastvc,
        'investor_sequoia': investor_sequoia,
        'investor_yc': investor_yc,
        'investor_insignia': investor_insignia,
        'investor_ggv': investor_ggv,
        'investor_ wavemaker': investor_wavemaker,
        'investor_openspace': investor_openspace,
        'investor_alphajwc': investor_alphajwc,
        'investor_jungle': investor_jungle,
        'investor_ cyberagentcapital': investor_cyberagentcapital,
    }

    # Convert the dictionary to a DataFrame
    input_df = pd.DataFrame([input_data])

    # Make predictions
    if st.button("Predict"):
        prediction = predict_model(model, data=input_df)
        
        if int(prediction['prediction_label']) == 1:
            predicted_outcome = "Low"
        else:
            predicted_outcome = "High"            
        
        st.write("Predicted Startup Success is: ", predicted_outcome)

if __name__ == '__main__':
    main()
