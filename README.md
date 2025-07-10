# VOX Awards Scoring App

This is a lightweight Streamlit app designed to help PRSA Memphis judges evaluate VOX Award submissions using a structured rubric. The app scores entries based on:

- **Research** (20 points)
- **Planning** (30 points)
- **Implementation** (20 points)
- **Evaluation** (20 points)
- **Creativity Bonus** (10 points)
- **Normalized Score** (adjusted based on team size and budget)

---

## 📦 Files Included

- `vox_awards_scoring_app.py`: Main Streamlit app
- `requirements.txt`: Required packages to run the app

---

## 🚀 How to Run the App

### ✅ Option 1: Run Locally

1. Install [Python](https://www.python.org/downloads/)
2. Open a terminal and navigate to the folder with these files
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the app:
   ```bash
   streamlit run vox_awards_scoring_app.py
   ```

### ✅ Option 2: Deploy via [Streamlit Cloud](https://streamlit.io/cloud)

1. Push these files to a GitHub repo
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New App**
4. Select your repo and enter:
   - **Main file path**: `vox_awards_scoring_app.py`
5. Click **Deploy**

You’ll receive a public link like:
```
https://your-app-name.streamlit.app
```

---

## 🙋‍♀️ How to Use

1. Paste a submission's text into the form
2. Enter the campaign’s budget and team size
3. Click **Score Submission**
4. Review the rubric breakdown and normalized score

---

## 📬 Questions?
Email [yourname@example.com] or file an issue on this GitHub repository.
