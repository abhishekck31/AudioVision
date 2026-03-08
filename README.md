# 🎧 AudioVision – Audio Feature Visualization

AudioVision is an interactive web application built with **Streamlit** that allows users to upload audio files and visualize important audio features such as **waveforms, spectrograms, and MFCCs**.

The project demonstrates **audio preprocessing, feature extraction, and visualization techniques** commonly used in speech recognition and audio analysis.

---

## 🚀 Features

* Upload `.wav` audio files
* Play uploaded audio directly in the app
* Visualize **Audio Waveform**
* Generate **Spectrogram**
* Extract and visualize **MFCC (Mel-Frequency Cepstral Coefficients)**
* Interactive UI built using **Streamlit**

---

## 🛠 Technologies Used

* **Python**
* **Streamlit**
* **Librosa**
* **NumPy**
* **Matplotlib**

---

## 📂 Project Structure

```
AudioVision
│
├── app.py              # Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── sample_audio/       # Optional example audio files
```

---

## ⚙️ Installation & Setup (Run Locally)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abhishekck31/AudioVision.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd AudioVision
```

### 3️⃣ Create a Virtual Environment (Recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

### 6️⃣ Open the Application

After running the command, Streamlit will start a local server.

Open your browser and go to:

```
http://localhost:8501
```

---

## 📊 How to Use

1. Upload a `.wav` audio file.
2. The app will automatically:

   * Play the audio
   * Display waveform visualization
   * Generate a spectrogram
   * Show MFCC feature visualization

---

## 🌐 Live Demo

Deployed using **Streamlit Cloud**

```
https://audiovision.streamlit.app
```

---

## 📚 Applications

Audio feature visualization is widely used in:

* Speech Recognition Systems
* Voice Assistants
* Emotion Detection
* Music Information Retrieval
* Audio Signal Processing

---

## ⭐ Contributing

Contributions, suggestions, and improvements are welcome.
Feel free to fork the repository and submit a pull request.

---

