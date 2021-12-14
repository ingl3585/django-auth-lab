# Django Auth Lab

Let's build a blog API with django!

## Version 1

### Models

- User model

### Routes

| Verb   | URI Pattern            | Token    |  Response |
|--------|------------------------|----------|-----------|
| POST   | `/sign-up`             |          | 201 user object |
| POST   | `/sign-in`             |          | 201 user object with token|
| PATCH  | `/change-password`     | required | 204  |
| DELETE | `/sign-out`            | required | 204 |

## Version 2

### Models

- User model

- Blog model
  - title : string
  - content : string
  - author : user reference
  - updated_at/created_at


### Routes

| Verb   | URI Pattern            | Token    |  Response |
|--------|------------------------|----------|-----------|
| POST   | `/sign-up`             |          | 201 - user object |
| POST   | `/sign-in`             |          | 201 - user object with token|
| PATCH  | `/change-password`     | required | 204  |
| DELETE | `/sign-out`            | required | 204 |
| GET | `/blogs` | required | 200 - array of blogs created by that user |
| POST | `/blogs` | required | 201 - blog object |
| GET | `/blogs/:id` | required | 200 - blog object |
| DELETE | `/blogs/:id` | required | 204  |
| PATCH | `/blogs/:id` | required | 200 - blog object |

## Version 3

### Models

- User model

- Blog model
  - title : string
  - content : string
  - author : user reference
  - updated_at/created_at

- Comment Model
  - content : string
  - blog : blog reference
  - author : user reference
  - updated_at/created_at

### Routes


| Verb   | URI Pattern            | Token    |  Response | Note |
|--------|------------------------|----------|-----------|---|
| POST   | `/sign-up`             |          | 201 - user object | |
| POST   | `/sign-in`             |          | 201 - user object with token| |
| PATCH  | `/change-password`     | required | 204  | |
| DELETE | `/sign-out`            | required | 204 | |
| GET | `/blogs` | required | 200 - array of blogs created by that user and its comments | |
| POST | `/blogs` | required | 201 - blog object | |
| GET | `/blogs/:id` | required | 200 - blog object and its comments | |
| DELETE | `/blogs/:id` | required | 204  | |
| PATCH | `/blogs/:id` | required | 200 - blog object and its comments | |
| POST | `/comments` | required | 201 - comment object | include blog id in body of request |
| DELETE | `/comments/:id` | required | 204  | |
| PATCH | `/comments/:id` | required | 200 - comment | |

