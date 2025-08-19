# Simple Flask Task Manager

A lightweight web application for managing a to-do list, built with Python and the Flask framework. This project demonstrates full CRUD (Create, Read, Update, Delete) functionality for managing tasks.

---

## Features

- **Add a Task:** Quickly add new items to your list.
- **View All Tasks:** See a clean, organized list of all your current tasks.
- **Mark a Task as Done:** Visually mark tasks as complete to track your progress.
- **Delete a Task:** Permanently remove tasks that are no longer needed.

---

## Installation and Usage

1.  **Prerequisites:** Make sure you have Python 3 and pip installed.

2.  **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```

3.  **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Download the NLP Model:** (This is the new step)
    ```sh
    python -m spacy download en_core_web_sm
    ```

5.  **Run the app:**
    ```sh
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.