# FastAPI Backend with Machine Learning

This backend serves two endpoints:

1. **POST /learn**: Accepts a CSV file to train a RandomForest model and stores the trained model for later use.
2. **GET /ask**: Accepts a question and returns a response based on the trained model.

## Setup Instructions

### Prerequisites
- Python 3.x
- Install the required Python dependencies with `pip install -r requirements.txt`.

### Running the Backend

1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
