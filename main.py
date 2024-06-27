import pickle
import streamlit as st
import pandas as pd


smart_model = pickle.load(open('LR_2variabel_new.sav', 'rb'))

container1 = st.container()


with container1:

    prediksi_harga_penawaran = ''

    st.title('Prediksi harga penawaran minyak')

    bursa = st.number_input("Masukkan harga bursa minyak")

    ringgit = st.number_input("Masukkan nilai ringgit")


    if st.button('Predict harga penawaran minyak'):
        prediksi_harga_penawaran = smart_model.predict([[bursa, ringgit]])                          
        
        # st.subheader(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: ")
        prediksi_include = round(prediksi_harga_penawaran[0], 2)
        max_nego = prediksi_include-277.18
        st.success(f"Prediksi harga penawaran dari bursa `{bursa}` adalah: Rp. {prediksi_include},-")
        st.success(f"Perkiraan Maksimal negosiasi yang dapat dilakukan adalah: Rp. {max_nego},-")
