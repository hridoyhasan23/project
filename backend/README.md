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



---

### **Step 3: Frontend (`ml-fastapi-nextjs-project/frontend`)**

1. **Create `frontend/pages/upload.js`**

```javascript
import { useState } from "react";
import axios from "axios";

export default function Upload() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:8000/learn", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Error training model.");
    }
  };

  return (
    <div>
      <h1>Upload CSV to Train Model</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
