# Person API Documentation

## Introduction

The Person API provides endpoints for managing person records. You can perform CRUD (Create, Read, Update, Delete) operations on individual person records.


## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Authentication](#authentication)
7. [Error Handling](#error-handling)
8. [Contributing](#contributing)
9. [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python [3.10.5]
- Django [4.2.5]
- [Database System, e.g., PostgreSQL, MySQL]

## Installation

1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/BobadeKenny/stage2api.git
    ```
2. **Change into the directory:**

   ```bash
   cd stage2api
   ```
3. **Create a virtual environment:**

   ```bash
   virtualenv venv
   ```
4. **Activate the virtual environment:**

   ```bash
   venv\Scripts\activate
    ```
5. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
    ```
6. **Apply database migrations:**

   ```bash
   python manage.py migrate
    ```
7. **Run the application:**

   ```bash
   python manage.py runserver
    ```
## API Endpoints
The full documentation for the API endpoints can be found [here](https://github.com/BobadeKenny/stage2api/blob/main/DOCUMENTATION.md).
- GET /api: Retrieve a list of all persons.
- GET /api/{id}: Retrieve a person by ID.
- POST /api: Create a new person.
- PUT /api/{id}: Update an existing person.
- DELETE /api/{id}: Delete a person by ID.

## Testing
To run the tests, run the following command:

```bash
python manage.py test
```
The tests are located in the `tests.py` file in the `api` directory.

