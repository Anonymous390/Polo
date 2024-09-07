# POLO - Vacation Finder

Welcome to **POLO - Vacation Finder**, a web application that helps users find perfect vacation spots based on their preferences for adventure, safety, weather, and luxury. 

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

---

## Features

- Users can input their preferences for **adventure**, **safety**, **weather**, and **luxury**.
- A beautiful and user-friendly UI with a dynamic image gallery of popular Indian vacation spots.
- Responsive design with animations for better user experience.

---

## Installation

Follow the steps below to set up the project on your local machine.

### Prerequisites

- **Python**: Make sure you have Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).
- **Flask**: Flask is the web framework used in this project. It will be installed with other dependencies.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/polo-vacation-finder.git
cd polo-vacation-finder
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
```
  Activate the virtual environment:
  - On Windows:
    ```bash
    venv\\Scripts\\activate
    ```
  - On Mac:
    ```bash
    source venv/bin/activate
    ```
### 3. Install Dependencies
  Make sure you have `pip` installed, then run:
  ```bash
  pip install -r requirements.txt
  ```
  This will install all the required Python libraries, including Flask.

### Running the Project
  Once the dependencies are installed, follow these steps to run the application:
  ### 1. Start the Flask Application
  ```bash
  flask run
  ```
  By default, the Flask server will run at `http://127.0.0.1:5000/`.
  ### 2. Open in Your Browser
  Go to your web browser and navigate to:
  ```bash
  http://127.0.0.1:5000
  ```
  You should see the homepage of the POLO - Vacation Finder.

### Usage
  - Navigate to the homepage.
  - Enter your preferences for adventure, safety, weather, and luxury.
  - Submit the form to receive vacation suggestions based on your preferences.
  - Browse through the gallery to see images of the vacation spots.

### Technologies Used
  - Python: Programming language.
  - Flask: Web framework.
  - HTML/CSS: For frontend design.
  - Unsplash: For high-quality images in the gallery.
  - Google Fonts: To style the fonts.
