import streamlit as st
import pickle

# Load the trained model and scaler
with open('svm_classifier.pkl', 'rb') as f:
  svm_classifier = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
  ss_train_test = pickle.load(f)

# Define the main function
def main():
  # Set the title of the app
  st.title('SVM Classifier')

  # Get the user input
  age = st.number_input('Age', min_value=0, max_value=100)
  gender = st.selectbox('Gender', ['Male', 'Female'])
  height = st.number_input('Height (cm)', min_value=0, max_value=250)
  weight = st.number_input('Weight (kg)', min_value=0, max_value=200)
  submit = form.form_submit_button('Submit')
  # Preprocess the user input
  user_input = [[age, gender, height, weight]]
  user_input_scaled = ss_train_test.transform(user_input)

  # Make the prediction
  prediction = svm_classifier.predict(user_input_scaled)[0]

  # Display the prediction
 if submit:
    prediction = m.predict(scaledData)
    if prediction == 1 :
        result = 'Gizi Baik'
    elif prediction == 2 :
        result = 'Gizi Kurang => Stunting'
    elif prediction == 3 :
        result = 'Risiko Gizi Lebih'
    elif prediction == 4 :
        result = 'Gizi Lebih'
    else:
        result = 'Obesitas'
    st.success(f"{result}")
    
# Run the main function
if __name__ == '__main__':
  main()
