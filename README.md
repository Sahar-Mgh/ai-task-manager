# AI-Powered Flask Task Manager

This project is a fully functional web-based task management application built with Python and Flask. It was developed to demonstrate a modern, AI-assisted software development workflow, from requirements gathering and code generation to testing, documentation, and containerization.

The application not only manages a to-do list with full CRUD (Create, Read, Update, Delete) functionality but also integrates a Natural Language Processing (NLP) model to intelligently parse task descriptions.

---

## Features

-   **View, Add, and Delete Tasks:** Standard, robust functionality to manage your to-do list.
-   **Mark Tasks as Complete:** Visually track your progress by marking tasks as done.
-   **Database Persistence:** All tasks are saved in a persistent SQLite database.
-   **Smart Task Parsing:** Automatically detects dates and times in task descriptions using a `spaCy` NLP model (e.g., "Finish report by Friday" will be saved with a note).
-   **Containerized:** The entire application is containerized with **Docker** for easy deployment and portability.

---

## Tech Stack

-   **Backend:** Python, Flask, Flask-SQLAlchemy
-   **Database:** SQLite
-   **NLP:** spaCy
-   **Testing:** pytest
-   **Containerization:** Docker

---

## Getting Started

You can run this project in two ways: locally with Python or using Docker.

### Option 1: Local Setup

1.  **Prerequisites:** Make sure you have Python 3 and `pip` installed.

2.  **Clone the Repository:**
    ```sh
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```

3.  **Create and Activate a Virtual Environment:**
    ```sh
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

4.  **Install Python Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5.  **Download the NLP Model:**
    ```sh
    python -m spacy download en_core_web_sm
    ```

6.  **Run the Application:**
    ```sh
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

---

### Option 2: Running with Docker

1.  **Prerequisites:** Make sure you have Docker installed and running on your machine.

2.  **Build the Docker Image:**
    From the root directory of the project, run:
    ```sh
    docker build -t task-manager .
    ```

3.  **Run the Docker Container:**
    ```sh
    docker run -p 5000:5000 task-manager
    ```
    The application will be available at `http://127.0.0.1:5000`.

---

## Running the Tests

This project includes a full suite of automated tests. To run them, make sure you have completed the local setup steps and then run the following command in your terminal:

```sh
pytest