### Walmart Content Refiner with Compliance Guardrails

This project makes it super easy to create product listings for Walmart. It takes a CSV with brand, product type, attributes, and current details, and automatically generates:

* Walmart-safe title
* HTML key features (<ul><li>)
* Product description (120-160 words)
* Meta title (≤70 characters) & meta description (≤160 characters)

It follows all of Walmart’s rules—no banned words, keeps bullet points short (≤85 chars), and makes sure the keywords are spot on. Plus, any violations are logged in the output CSV so you can easily fix them. Super simple and saves time!

Sure! Here's how you can write the README section with code structure:

---

### Project Overview

This project is built using **FastAPI** for its lightweight and fast performance, with **LangChain** for interacting with GPT, and **OpenAI** as the primary model.

---

### Prerequisites

* Python 3.10 or higher
* **UV** package (For package manager)

---

### Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:

    ```bash
    source venv/bin/activate
    ```

4. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

### FastAPI Endpoints

* **Endpoint:** `/refine`

  This endpoint handles the product content refinement process.

---

### Testing the API

You can use any API tool like **Postman** or simply visit `http://localhost:8080/docs` in your browser to interact with the backend and explore the endpoints.
