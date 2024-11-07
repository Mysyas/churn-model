import streamlit as st
import backend

if 'result' not in st.session_state:
    st.session_state.result="Résultat :"

st.set_page_config(layout="wide")
with open('front.css','r') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    
st.markdown("<h1>Prédiction du churn</h1>",unsafe_allow_html=True)
st.markdown('<p id="info"><strong>Remplissez dument les informations</strong></p>',unsafe_allow_html=True)
with st.form('churn_form'):
    st.write('<strong>Abonnement service téléphone<i>*</i></strong>',unsafe_allow_html=True)
    phone=st.radio('Utilises-t-il/elle un abonnement téléphonique ?',['Oui','Non'])
    col1,col2 = st.columns([1,3])
    with col1:
        st.write('<strong>Genre<i>*</i></strong>',unsafe_allow_html=True)
    with col2:
        gender=st.selectbox('',options=['Masculin','Féminin'])
    st.write('<strong>Situation matrimoniale<i>*</i></strong>',unsafe_allow_html=True)
    married=st.radio('Est-il/elle marrié(e) ?',['Oui','Non'])
    col1_1,col1_2 = st.columns([1,3])
    with col1_1:
        st.write('<strong>Score de satisfaction<i>*</i></strong>',unsafe_allow_html=True)
    with col1_2:
        satisfaction=st.selectbox('',options=[i for i in range(1,6)])
    st.write('<strong>Abonnement service internet<i>*</i></strong>',unsafe_allow_html=True)
    internet=st.radio('Est-il/elle souscrit(e) au service internet ?',['Oui','Non'])
    col_1,col_2=st.columns([1,2])
    with col_1:
        st.write('<strong>Utilisation moyenne de connexion internet en GB<i>*</i></strong>',unsafe_allow_html=True)
    with col_2:
        download=st.number_input('',step=1)
    btn=st.form_submit_button('Lancer la prédiction')
    if btn:
        phone_val = 1 if phone == "Oui" else 0
        gender_val=1 if gender=="Masculin" else 0
        married_val = 1 if married == "Oui" else 0
        internet_val = 1 if internet == "Oui" else 0
        st.session_state.result=f"Résultat : {backend.predict(phone_val,gender_val,married_val,satisfaction,internet_val,download)}"
    
st.write(st.session_state.result)

