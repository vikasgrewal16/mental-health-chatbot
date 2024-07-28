# Mental Health Chatbot

This project is a simple mental health chatbot built with FastAPI. The chatbot uses a classification model to determine the sentiment of the text input provided by the user.

## Project Structure


- `app/`: Contains the main application code.
  - `data/`: Contains the dataset and serialized models.
  - `models/`: Contains the model-related code.
  - `utils/`: Contains utility functions.
  - `main.py`: The entry point for the FastAPI application.
- `Dockerfile`: Docker configuration file.
- `requirements.txt`: Lists the Python packages required to run the project.
- `test_imports.py`: Script to test the imports and setup.
- `README.md`: This file.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)
- `git` (version control system)
- Visual Studio Code (optional, for code editing)
- Anaconda or Miniconda (recommended for managing virtual environments)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vikasgrewal16/mental-health-chatbot/
   cd mental_health_chatbot

2. **Using Virtual Environment**

     ```bash
    python -m venv venv
    source venv/bin/activate    

3. **Install Requirements**
     
      ```bash
   pip install -r requirements.txt

4. **Test the Setup**

         pip install -r requirements.txt

5. **Start the FastAPI server:**

     ```bash
     uvicorn app.main:app --reload
    # This will start the server on http://127.0.0.1:8000

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

