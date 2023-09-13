# Person API Documentation

## Overview

The Person API provides endpoints for managing person records. You can perform CRUD (Create, Read, Update, Delete) operations on individual person records.

## Base URL
```http

https://stage2-bkvm.onrender.com
```


## Endpoints

### 1. Get All Persons

**Endpoint:**
```bash
GET /api
```

**Description:**

Retrieve a list of all persons.

**Example Request:**

```http
GET /api
```
**Example Response:**
```json
[
    {
        "id": 1,
        "name": "Kenny",
        "created_at": "2023-09-11T14:58:29.134956Z",
        "updated_at": "2023-09-12T20:50:24.663014Z"
    },
    {
        "id": 2,
        "name": "Captain Jack Sparrow",
        "created_at": "2023-09-11T14:58:57.098872Z",
        "updated_at": "2023-09-11T14:58:57.098872Z"
    },
    {
        "id": 3,
        "name": "Ariel",
        "created_at": "2023-09-11T15:04:59.754652Z",
        "updated_at": "2023-09-11T15:04:59.754652Z"
    }
]
```
### 2. Get Person by ID
**Endpoint:**
```bash
GET /api/{id}
```

**Description:**

Retrieve a person by their ID.

**Example Request:**

```http
GET /api/1
```
**Example Response:**

```json
{
    "id": 1,
    "name": "John Doe",
    "created_at":"2023-09-11T14:58:29.134956Z",
    "updated_at":"2023-09-12T20:50:24.663014Z"
}
```
### 3. Create Person
**Endpoint:**

```bash
POST /api
```
**Description:**

Create a new person record.

**Example Request:**

```http
POST /api
Content-Type: application/json

{
    "name": "Alice Doe",
}
```
**Example Response:**

```json
{
    "message": "Person created"
}
```
### 4. Update Person
**Endpoint:**

```bash
PUT /api/{id}
```
**Description:**

Update an existing person record by their ID.

**Example Request:**

```http
PUT /api/3
Content-Type: application/json

{
    "name": "Alice Brown",
}
```
**Example Response:**

```json
{
    "message":"Person Alice Brown updated"
}
```
### 5. Delete Person
**Endpoint:**

```bash
DELETE /api/{id}
```
**Description:**

Delete a person record by their ID.

**Example Request:**

```http
DELETE /api/3
```
**Example Response:**

```json
{
    "message":"Alice Brown deleted"
}
```
### Unsuccessful Response
All unsuccessful responses have the following format:

```json
{
    "detail":"Not found."
}
```