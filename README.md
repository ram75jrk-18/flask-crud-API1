# flask-crud-API1
My python project code and CRUD Project
# Flask CRUD Mini Project

This is a REST API mini project built with **Flask** and **SQLite**. It satisfies the following weekly task requirements:

- Build REST API using Flask
- Implement CRUD operations
- Test APIs using Postman
- Implement error handling
- Maintain proper project structure
- Prepare a working mini project for GitHub submission

## Project Structure

```text
flask_crud_mini_project/
│── app/
│   ├── __init__.py
│   ├── errors.py
│   ├── extensions.py
│   ├── models.py
│   └── routes/
│       └── items.py
│── postman/
│   └── Item_API.postman_collection.json
│── config.py
│── requirements.txt
│── run.py
│── .gitignore
│── README.md
```

## Mini Project Description

This project manages **Items / Tasks**.

Each item has:
- `id`
- `title`
- `description`
- `status` (`pending`, `in_progress`, `completed`)
- `created_at`
- `updated_at`

## Setup Instructions

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python run.py
```

The app will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### Health Check
- `GET /health`

### Create Item
- `POST /api/items`

Sample JSON:
```json
{
  "title": "Complete weekly submission",
  "description": "Prepare Flask project and Postman collection",
  "status": "pending"
}
```

### Get All Items
- `GET /api/items`

### Get Single Item
- `GET /api/items/<id>`

### Update Item
- `PUT /api/items/<id>`

Sample JSON:
```json
{
  "title": "Complete weekly submission",
  "description": "Updated item details",
  "status": "completed"
}
```

### Delete Item
- `DELETE /api/items/<id>`

## Error Handling Implemented

- 400 Bad Request for invalid JSON or missing required fields
- 404 Not Found when item ID does not exist
- 500 Internal Server Error for unexpected exceptions

## Postman Testing

Import the file below into Postman:

```text
postman/Item_API.postman_collection.json
```

Then test all CRUD APIs.

## GitHub Submission Steps

1. Create a new GitHub repository.
2. Upload all project files.
3. Commit with message: `Initial Flask CRUD mini project`.
4. Add the repository link to your weekly report.

## Suggested GitHub Repository Name

```text
flask-crud-mini-project
```

## Example Git Commands

```bash
git init
git add .
git commit -m "Initial Flask CRUD mini project"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```
