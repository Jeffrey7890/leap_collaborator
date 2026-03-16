# Collaborative LEAP Scenario Tracking Platform

A web platform for researchers to **track, compare, and collaborate on energy modeling scenarios** exported from LEAP. This project allows teams to **manage multiple projects, track scenario versions, upload results, and visualize trends** — all without violating LEAP licensing restrictions.

---

## 🚀 Features

* **User Authentication** – Register, login, and manage user roles (admin, editor, viewer).
* **Project Management** – Create and manage multiple energy modeling projects.
* **Scenario Management** – Track multiple scenarios per project with version history.
* **File Upload & Parsing** – Upload CSV/Excel files exported from LEAP and extract results automatically.
* **Scenario Comparison Dashboard** – Compare results across scenarios and visualize trends over time.
* **Collaboration & Activity Logs** – Multiple users per project with role-based permissions and activity history.

---

## 🛠 Tech Stack

**Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL
**Frontend:** React, Plotly / Chart.js for visualizations
**Infrastructure:** Docker for containerization, AWS / Render for deployment
**Utilities:** Pandas for data parsing, JWT for authentication

---

## 📁 Database Structure (Simplified)

**Tables:**

* `users` – platform users and roles
* `projects` – research projects
* `project_members` – collaborators and roles
* `scenarios` – LEAP scenarios per project
* `scenario_versions` – version history for each scenario
* `scenario_assumptions` – key scenario assumptions
* `scenario_files` – uploaded CSV/Excel files
* `scenario_results` – parsed scenario results
* `activity_logs` – tracks user actions

**Relationships:**

```
User
 │
 ├── Projects
 │     │
 │     ├── Project Members
 │     │
 │     └── Scenarios
 │           │
 │           └── Scenario Versions
 │                 │
 │                 ├── Assumptions
 │                 ├── Files
 │                 └── Results
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/leap-collab-platform.git
cd leap-collab-platform
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL database and update `app/core/config.py` with your database URL.

5. Run migrations (if using Alembic):

```bash
alembic upgrade head
```

6. Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

7. Open [http://localhost:8000/docs](http://localhost:8000/docs) to view API documentation.

---

## 💡 Usage

1. Create a user account
2. Create a project and invite collaborators
3. Add scenarios with version history
4. Upload LEAP-exported CSV/Excel files
5. View results and comparisons in the dashboard

---

## 🔮 Future Enhancements

* Automatic extraction of assumptions and variables from LEAP model files
* Advanced trend analytics and visualizations
* Notifications for scenario updates
* Role-based access control enhancements

---

## 📄 License

This project is for educational and research purposes. **Do not attempt to run LEAP scenarios automatically**, as it may violate licensing.

---

## 👤 Author

Jeffrey Ogwu
[GitHub](https://github.com/Jeffrey7890) | [Email](mailto:jeffrey.ogechi@gmail.com)

Do you want me to do that next?
