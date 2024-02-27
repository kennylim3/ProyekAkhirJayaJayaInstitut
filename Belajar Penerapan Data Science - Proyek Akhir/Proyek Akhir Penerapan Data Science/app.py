import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Displaced
from prediction import prediction

col = st.columns(5)

with col:
    st.header('Potential Dropout Students Predicting App (Prototype)')

data = pd.DataFrame()

col1, col2, col3 = st.columns(3)
with col1:
    Displaced = st.selectbox(label='Displaced', options=encoder_Displaced.classes_,
                                         index=1)
    data["Displaced"] = [Displaced]
with col2:
    Admission_grade = float(st.number_input(label='Admission grade', value=150.0))
    data["Admission_grade"] = Admission_grade

with col3:
    Age_at_enrollment = int(st.number_input(label='Age at enrollment', value=18))
    data["Age_at_enrollment"] = Age_at_enrollment


col1, col2, col3 = st.columns(3)
with col1:
    Curriculum_units_1st_sem_enrolled = int(st.number_input(label='Curriculum units 1st sem enrolled', value=10))
    data["Curriculum_units_1st_sem_enrolled"] = Curriculum_units_1st_sem_enrolled
with col2:
    Curriculum_units_1st_sem_approved = int(st.number_input(label='Curriculum units 1st sem approved', value=10))
    data["Curriculum_units_1st_sem_approved"] = Curriculum_units_1st_sem_approved

with col3:
    Curriculum_units_1st_sem_grade = float(st.number_input(label='Curriculum units 1st sem grade', value=13.4))
    data["Curriculum_units_1st_sem_grade"] = Curriculum_units_1st_sem_grade


col1, col2, col3 = st.columns(3)
with col1:
    Curriculum_units_2nd_sem_enrolled = int(st.number_input(label='Curriculum units 2nd sem enrolled', value=10))
    data["Curriculum_units_2nd_sem_enrolled"] = Curriculum_units_2nd_sem_enrolled
with col2:
    Curriculum_units_2nd_sem_approved = int(st.number_input(label='Curriculum units 2nd sem approved', value=10))
    data["Curriculum_units_2nd_sem_approved"] = Curriculum_units_2nd_sem_approved

with col3:
    Curriculum_units_2nd_sem_grade = float(st.number_input(label='Curriculum units 2nd sem grade', value=13.4))
    data["Curriculum_units_2nd_sem_grade"] = Curriculum_units_2nd_sem_grade


with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)


if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Credit Scoring: {}".format(prediction(new_data)))

