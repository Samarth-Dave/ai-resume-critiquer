# 📃 AI Resume Critiquer

AI Resume Critiquer is a beginner-friendly Streamlit app that provides AI-powered feedback on resumes. It uses the LLaMA 3 model via Groq’s ultra-fast API to analyze resumes and give helpful suggestions to improve clarity, skill presentation, and relevance to job roles.

---

## ✨ Features

* 📄 Upload resume as PDF or TXT
* 🧠 AI-generated feedback using Meta’s LLaMA 3 (via Groq)
* 🎯 Tailored suggestions based on job role
* ⚡ Fast and free thanks to Groq's OpenAI-compatible API
* 🖥️ Clean and simple interface with Streamlit

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-resume-critiquer.git
cd ai-resume-critiquer
```

### 2. Install dependencies using `uv` (or pip)

```bash
uv pip install -r requirements.txt
```

Or, if you're using pip:

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the project folder and add your Groq API key like this:

```
API_KEY=your_groq_api_key_here
```

You can get a free API key from: [https://console.groq.com](https://console.groq.com)

---

### 4. Run the app

```bash
streamlit run app.py
```

Then open your browser at [http://localhost:8501](http://localhost:8501)

---

## 🧠 How It Works

1. You upload your resume (PDF or TXT).
2. The app extracts the text from your file.
3. It sends a prompt + resume content to Groq's LLaMA 3 model.
4. You receive structured feedback focused on clarity, skills, and experience.
5. All output is shown directly in your browser.

---

## 🗂️ Project Structure

```
📁 ai-resume-critiquer/
🔚🔹 app.py              # Main Streamlit app
🔚🔹 requirements.txt    # Python dependencies
🔚🔹 .env                # Your Groq API key (not tracked by Git)
🔚🔹 README.md           # Project documentation
```

---

## 🔧 Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python + Groq API (LLaMA 3)
* **File Handling**: PyPDF2, io
* **Environment Variables**: python-dotenv

---

## 🛆 requirements.txt (reference)

If you need it, your `requirements.txt` file should include:

```
streamlit
requests
python-dotenv
PyPDF2
```

(You can generate it via `uv pip freeze > requirements.txt`)

---

## 💡 Future Enhancements

* Add resume rating score
* Export feedback as PDF or DOCX
* Integrate job descriptions for better targeting
* Add voice or video summary using AI avatars

---

## 👨‍💻 Author

**Samarth Dave**
This is my first AI project — feedback is welcome and appreciated! 🙌

---

## 📄 License

This project is licensed under the **MIT License**. Feel free to use, modify, and share it.

---

## 🌐 Links

* Groq API: [https://console.groq.com](https://console.groq.com)
* Streamlit Docs: [https://docs.streamlit.io](https://docs.streamlit.io)
