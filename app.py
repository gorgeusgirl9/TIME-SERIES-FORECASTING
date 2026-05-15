import streamlit as st
import pandas as pd
import joblib
import datetime as dt

# Başlık ve Açıklama
st.set_page_config(page_title="Netflix Trend Tahmincisi", page_icon="📈")
st.title("📈 Netflix (NFLX) Hisse Senedi Trend Tahmini")
st.write("Bu uygulama, geçmiş veriler üzerinden eğitilen bir modelle Netflix hissesinin trendini tahmin eder.")

# Modeli Yükle
@st.cache_resource
def load_model():
    return joblib.load('netflix_trend_model.pkl')

model = load_model()

# Kullanıcı Girişi
st.subheader("Tahmin Almak İstediğiniz Tarihi Seçin")
target_date = st.date_input("Tarih Seçin", value=dt.date.today())

# Tahmin Butonu
if st.button("Tahmini Gör"):
    # Tarihi ordinal formata çevir (Modelimiz bu formatta eğitildi)
    ordinal_date = dt.datetime.combine(target_date, dt.datetime.min.time()).toordinal()
    
    # Tahmin yap
    prediction = model.predict([[ordinal_date]])[0]
    
    # Sonucu göster
    st.success(f"📅 {target_date} tarihindeki tahmini hisse değeri: **${prediction:.2f}**")
    st.info("Not: Bu bir trend analizidir, kesin yatırım tavsiyesi değildir.")