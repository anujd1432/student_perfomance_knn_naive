import streamlit as st
import joblib
import pandas as pd

# Load the trained model pipeline
# The pipeline includes StandardScaler and GaussianNB
model_pipeline = joblib.load('model.pkl')

# Assuming the feature names are consistent with the training data
# We can get these from the X dataframe used for training the naive bayes model
# If X is not available, we would need to manually define them or save them with the model.
# From the notebook state, X (from naive bayes training) is available.
# It also aligns with the features saved in model_bundle.pkl (excluding 'GradeClass').
features = ['Age', 'Gender', 'Ethnicity', 'ParentalEducation', 'StudyTimeWeekly',
            'Absences', 'Tutoring', 'ParentalSupport', 'Extracurricular', 'Sports',
            'Music', 'Volunteering', 'GPA']

# Streamlit App Title
st.title('Student Grade Class Prediction App')
st.write('Enter the student details to predict their Grade Class.')

# Input widgets for each feature
with st.form('prediction_form'):
    st.header('Student Information')

    age = st.slider('Age', min_value=15, max_value=18, value=17)
    gender = st.selectbox('Gender', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
    ethnicity = st.selectbox('Ethnicity', options=[0, 1, 2, 3], help='0: Group A, 1: Group B, 2: Group C, 3: Group D')
    parental_education = st.selectbox('Parental Education', options=[0, 1, 2, 3, 4], help='0: None, 1: Primary, 2: Secondary, 3: High School, 4: University')
    study_time_weekly = st.number_input('Study Time Weekly (hours)', min_value=0.0, max_value=20.0, value=10.0, step=0.1)
    absences = st.slider('Absences', min_value=0, max_value=29, value=10)
    tutoring = st.selectbox('Tutoring', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    parental_support = st.selectbox('Parental Support', options=[0, 1, 2, 3, 4], help='0: None, 1: Low, 2: Medium, 3: High, 4: Very High')
    extracurricular = st.selectbox('Extracurricular Activities', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    sports = st.selectbox('Sports', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    music = st.selectbox('Music', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    volunteering = st.selectbox('Volunteering', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    gpa = st.number_input('GPA', min_value=0.0, max_value=4.0, value=2.5, step=0.01)

    submitted = st.form_submit_button('Predict Grade Class')

    if submitted:
        # Create a DataFrame from the input values
        input_data = pd.DataFrame([[age, gender, ethnicity, parental_education, study_time_weekly,
                                    absences, tutoring, parental_support, extracurricular, sports,
                                    music, volunteering, gpa]], columns=features)

        # Make prediction
        prediction = model_pipeline.predict(input_data)

        # Map the GradeClass integer to a descriptive string if needed, based on problem definition
        # Assuming GradeClass values are 0, 1, 2, 3, 4 as seen in df['GradeClass'].value_counts()
        grade_class_map = {
            0: 'Grade A (Excellent)',
            1: 'Grade B (Very Good)',
            2: 'Grade C (Good)',
            3: 'Grade D (Pass)',
            4: 'Grade E (Fail/Retake)'
        }
        predicted_class_label = grade_class_map.get(int(prediction[0]), 'Unknown Grade Class')

        st.subheader('Prediction Result:')
        st.success(f'The predicted Grade Class is: {predicted_class_label}')


