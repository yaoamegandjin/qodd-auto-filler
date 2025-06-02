# 🎯 QODD Auto-Filler: Residence Hall Trivia Automation
This project automates submissions to my university residence hall’s **Question of the Day (QODD)** form. Correct answers earn points toward a semester-end prize drawing. You can also submit your own trivia questions — if your question is picked and you answer it correctly, you earn **even more points.**

This Python program uses web automation to submit **50 trivia questions and answers every morning** — maximizing your chances of earning points daily.

# 🚀 Features
- 🔁 Automatically submits 50 questions and answers each morning
- 📩 Submits both answers and original trivia questions
- 🧠 Questions are pulled from a public Trivia API
- ⏰ Executes daily using Windows Task Scheduler
- 📄 Logs all submissions in questionsAndAnswers.txt

# 🛠️ Technologies Used
- **Python**
- **Selenium** - for browser automation
- **Trivia API** - to fetch trivia questions and answers
- **Windows Task Scheduler** - to automate script execution
- **PowerShell / Batch scripting** - for local automation setup

# 🧪 Setup & Usage
1. **Clone the Repository**
```bash
git clone git@github.com:yaoamegandjin/qodd-auto-filler.git
cd qodd-auto-filler
```
2. **Set Up Virtual Environment**
```powershell
python -m venv myenv
myenv\Scripts\Activate.ps1
```
3. **Install Dependencies**
```bash
pip install selenium requests
```

4. **Run the Script Manually**
```bash
python qoddAutoFiller.py
```

# ⚡Automate Daily Runs with Task Scheduler
**Batch File:** ==QODDAutoFiller.bat==
```batch
@echo off
set "venv_path=path_to_venv"
set "script_path=path_to_script"

"%venv_path%\Scripts\python.exe" "%script_path%"
```

# Set Up Task Scheduler

1. Open **Task Scheduler** on Windows.
2. Create a new basic task with a daily trigger (e.g., 8:00 AM).
3. In the **Action** step, select *Start a Program* and point it to ==QODDAutoFiller.bat==.
4. Save and test your task.

# 📌 Notes
- You may need to update element selectores in qoddAutoFiller.py to match your specific form's HTML structure.
- This script maintains a log of submitted questions and answers in ==questionsAndAnswers.txt==.




