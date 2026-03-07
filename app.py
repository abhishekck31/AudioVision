
import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

st.title("AudioVision - Audio Feature Visualization")
st.audio(uploaded_file)

uploaded_file = st.file_uploader("Upload an audio file", type=["wav"])

if uploaded_file is not None:
    
    signal, sr = librosa.load(uploaded_file)

    st.write("Sampling Rate:", sr)

    # Waveform
    st.subheader("Waveform")
    fig, ax = plt.subplots()
    librosa.display.waveshow(signal, sr=sr, ax=ax)
    st.pyplot(fig)

    # Spectrogram
    st.subheader("Spectrogram")
    spectrogram = librosa.stft(signal)
    spectrogram_db = librosa.amplitude_to_db(abs(spectrogram))

    fig, ax = plt.subplots()
    img = librosa.display.specshow(spectrogram_db, sr=sr, x_axis="time", y_axis="hz", ax=ax)
    fig.colorbar(img, ax=ax)
    st.pyplot(fig)

    # MFCC
    st.subheader("MFCC Features")
    mfcc = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13)

    fig, ax = plt.subplots()
    img = librosa.display.specshow(mfcc, x_axis="time", ax=ax)
    fig.colorbar(img, ax=ax)
    st.pyplot(fig)
