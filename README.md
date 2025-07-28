# 📝 Flask To-Do List App

A simple web-based To-Do List application built using Flask and SQLite. It allows users to add, complete, and delete tasks with a clean and responsive user interface.

---

## 🚀 Features

- Add new tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Data stored persistently using SQLite
- HTML/CSS/JavaScript frontend

---

## 📂 Project Structure

```bash
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── index.html
├── todo.db  # auto-created SQLite database
├── app.py
├── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/flask-todo-app.git
cd flask-todo-app
```

2. **Create Virtual Environment (Optional)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the App**
```bash
python app.py
```
Visit `http://127.0.0.1:8000` in your browser.

---

## 🛠️ Requirements

- Python 3.7+
- Flask
- Flask_SQLAlchemy

You can generate `requirements.txt` using:
```bash
pip freeze > requirements.txt
```


## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
