```markdown
# My Flask API (With pyenv and Docker)

This repository contains a simple Flask API that returns a list of properties as JSON.  
We provide two ways to run it:

1. **Locally** (using a Python virtual environment, e.g. with [pyenv](https://github.com/pyenv/pyenv) / [pyenv-win](https://github.com/pyenv-win/pyenv-win)).
2. **Inside a Docker container**.

---

## 1. Running Locally with a Virtual Environment

> **Note for Windows Users**:  
> - If you want to use `pyenv` on Windows, please check out [pyenv-win](https://github.com/pyenv-win/pyenv-win).  
> - If you just need a simple virtual environment, you can use the built-in `venv` module as shown below.

### (Optional for Linux/Mac) Use devbox:
```bash
devbox shell
```
*(This step is optional and Linux/Mac-specific.)*

### Steps

1. **Create a virtual environment** (works on Windows, Mac, or Linux):
   ```bash
   python -m venv venv
   ```
   - **Linux/Mac**: `source venv/bin/activate`
   - **Windows (Command Prompt)**: `venv\Scripts\activate.bat`
   - **Windows (PowerShell)**: `venv\Scripts\Activate.ps1`

2. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   python app.py
   ```
   - The Flask server will start on port `5009`.  
   - Visit [http://localhost:5009/api/properties](http://localhost:5009/api/properties) to see the JSON response.

---

## 2. Running in Docker

### 2.1. Build the Docker Image
From the project root folder (where `Dockerfile` is located):
```bash
docker build -t macher-app .
```
- Uses `python:3.9-slim` as the base image.
- Installs dependencies from `requirements.txt`.
- Copies `app.py` into the container.

### 2.2. Run the Docker Container
```bash
docker run -p 5009:5009 macher-app
```
- Binds container port 5009 to your local machine’s port 5009.
- Visit [http://localhost:5009/api/properties](http://localhost:5009/api/properties) to see the JSON data.

### 2.3. Live Development (Optional)
If you want to see code changes without rebuilding:

- **Mac/Linux**:
  ```bash
  docker run -p 5009:5009 -v "$(pwd)":/app my-flask-app
  ```
- **Windows (CMD)**:
  ```cmd
  docker run -p 5009:5009 -v "%cd%":/app my-flask-app
  ```
- **Windows (PowerShell)**:
  ```powershell
  docker run -p 5009:5009 -v "${pwd}:/app" my-flask-app
  ```
- This mounts your local project folder into the container.  
- You may need to restart the container or use Flask’s auto-reload feature for changes to take effect immediately.

---

## Additional Notes

- If you add more Python packages, add them to `requirements.txt`.
- If you change your Python version (e.g., via pyenv or pyenv-win), reinstall dependencies in your (new) virtual environment:
  ```bash
  pip install -r requirements.txt
  ```
- This setup removes any references to ngrok or other unnecessary tools.
- Port `5009` is exposed by default in `app.py`; you can change it if you wish.
```