# 🐍 Chan Study FastAPI Project

Welcome to the **Chan Study** project!  
This project is a Python web application using [FastAPI](https://fastapi.tiangolo.com/) and is configured for easy debugging and development.

## 🚀 Features

- **FastAPI** backend for building APIs quickly and efficiently.
- Debugging support via VSCode and `debugpy`.
- Hot-reload enabled for rapid development (`uvicorn --reload`).

## 📚 Purpose

The purpose of this project is to practice and understand how to implement an ORM using SQLAlchemy and to create an API using FastAPI..


## 🛠️ Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [VSCode](https://code.visualstudio.com/) (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GabrielSoaCassi/chan_study.git
   cd chan_study

2. **Create a VENV:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
    ```bash
    fastapi dev main.py
    ```

### 🪳 Debugging

This project includes a VSCode launch configuration for debugging with debugpy.
To start debugging:

Open the project in VSCode.
Go to the Run and Debug panel.
Select Python Debugger: FastAPI and click Start Debugging.

### 📁 Project Structure
```chan_study/
├── main.py
├── application/
│   └── services/
│       ├── thread_service.py
│       └── post_service.py
├── config/
│   └── config.py
├── data/
│   └── repositories/
│       ├── thread_repository.py
│       └── post_repository.py
├── packages/
│   └── models/
│       ├── base.py
│       ├── post.py
│       └── thread.py
├── db/
│   └── my_chan.db/
├── web/
│   └── routers/
│       ├── post_controller.py
│       └── thread_controller.py
├── requirements.txt
├── .vscode/
│   └── launch.json
└── README.md
```
### 📝 License
This project is licensed under the MIT License.