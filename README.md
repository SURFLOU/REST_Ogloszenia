# REST_Ogloszenia
This is a Django project for a simple bulletin board application with REST API endpoints for adding, editing, and displaying announcements.

## Setup
To set up and run this project, follow these steps:

### 1. Clone the Repository
Clone the repository using the following command:

```
git clone https://github.com/SURFLOU/REST_Ogloszenia.git
```

### 2. Navigate to the Project Directory
Navigate to the project directory:

```
cd REST_Ogloszenia
```

### 3. Create a Virtual Environment
Create a virtual environment using Python's built-in venv module. If you already have a virtual environment in the venv folder, you can skip this step.

```
python3 -m venv venv
```

### 4. Activate the Virtual Environment
Activate the virtual environment. On Windows:

```
venv\Scripts\activate
```

On macOS and Linux:

```
source venv/bin/activate
```

### 5. Install Dependencies
Install the project dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```

### 6. Migrate the Database
Run the Django migrations to create the necessary database tables:

```
python manage.py migrate
```

### 7. Run the Development Server
Start the Django development server:

```
python manage.py runserver
```

The development server will start running at http://127.0.0.1:8000/.
