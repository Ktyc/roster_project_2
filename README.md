# AI Staff Roster Engine
An automated rostering engine built using Google OR-Tools to assign staff to shifts based on constraints that were given.

## Key Features
1. Ensures fairness in shift assignment using a point based system
2. Constraint Based
- Assigns staffs to shifts based on their roles.
- Staff will not be able to work the next shift following a PM shift for safety reasons.
- Staff will be entitled to take blackout dates where they would not be assigned a shift.
- Staff will be able to bid for specific Public Holiday shifts which they would want to work on.
- Staff will be taken out of pool for Public Holiday shifts if the shift is within 300 days of their last worked Public Holiday, unless they bidded for it.

## Tech Stack
- **Language:** Python 3.14+
- **Optimisation:** Google OR-Tools (CP-SAT Solver)
- **Interface:** Streamlit
- **Data Handling:** Pandas, Openpyxl

## Installation & Setup
To get this project running on your local machine, follow these steps:
<pre>
Bash
</pre>
<pre>
# Clone the repo
git clone https://github.com/Ktyc/roster_project_2.git

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt


To generate test file:
<pre>
Bash
</pre>
<pre>
```bash
python generate_data.py```
</pre>

To launch dashboard interface:
<pre>
Bash
</pre>
<pre>
streamlit run app.py
</pre>

## File Structure
```text
roster_project_main/
├── src/                # Core logic (engine, models)
├── data/               # Example Excel files
├── tests/              # Unit tests for constraints
├── app.py              # Streamlit UI
├── generate_data.py    # Script to generate test staff data
└── requirements.txt    # Python dependencies```
