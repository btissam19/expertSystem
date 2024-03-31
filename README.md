# Expert System - PC Diagnostic

This application is a web-based expert system designed to diagnose potential issues with a PC based on user-selected symptoms.

## Setup Instructions

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install Flask using pip if not already installed:
    ```
    pip install Flask
    ```
4. Run the Flask app:
    ```
    python app.py
    ```
5. Open a web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the application.

## Description

This expert system employs a rule-based approach to diagnose PC issues. The rules are stored in a file named `base.txt`, where each line represents a rule in the format `symptom:affected_component`. The application allows users to select multiple symptoms from a list, and upon clicking the "Perform Diagnosis" button, it analyzes the selected symptoms against the stored rules to determine potential faulty components.

## Files

### `app.py`

This file contains the Flask application that serves the web interface and handles the diagnosis logic.

### `index.html`

This HTML file defines the structure and appearance of the web interface for symptom selection and diagnosis.

### `base.txt`

This text file contains the rules used by the expert system for diagnosis. Each line represents a rule in the format `symptom:affected_component`.

## Technologies Used

- Flask: A micro web framework for Python used to develop the web application.
- HTML/CSS/JavaScript: Frontend technologies used for designing and implementing the user interface.
- JSON: Used for data exchange between the frontend and backend.
