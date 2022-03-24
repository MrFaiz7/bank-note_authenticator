import joblib
import streamlit as st

classifier = joblib.load('classifier.pkl')
id_to_category = {0: 'Genuine', 1: 'Fake'}


def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return prediction


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", "Type Here")
    skewness = st.text_input("skewness", "Type Here")
    curtosis = st.text_input("curtosis", "Type Here")
    entropy = st.text_input("entropy", "Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        if result == 0:
            st.success("Note is Genuine")
        else:
            st.success("Note is Fake")

    if st.button("About"):
        st.text("Bank Note Authentication:")
        st.text(
            'Data were extracted from images that were taken from genuine and forged banknote-like specimens.' 
             'For digitization, an industrial camera usually used for print inspection was used.' 
              'The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained.'
               'Wavelet Transform tool were used to extract features from images.')
        st.text("Built with Streamlit")
        st.text("Author: Mr. Faiz")


if __name__ == '__main__':
    main()
