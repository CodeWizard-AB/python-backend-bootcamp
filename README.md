# CodeForge: Python Backend Engineering Bootcamp

![VSCode](https://skillicons.dev/icons?i=vscode)
![Postman](https://skillicons.dev/icons?i=postman)
![Python](https://skillicons.dev/icons?i=py)
![FastAPI](https://skillicons.dev/icons?i=fastapi)
![PostgreSQL](https://skillicons.dev/icons?i=postgres)
![Git](https://skillicons.dev/icons?i=git)
![GitHub](https://skillicons.dev/icons?i=github)

A structured, production-grade knowledge base and code repository for the **CodeForge: Python Backend Engineering Bootcamp**. This repository documents 49 comprehensive sessions covering version control, advanced Python idioms, relational database design, asynchronous REST API engineering with FastAPI, and end-to-end capstone implementations.

Every session is maintained as an isolated laboratory containing theoretical notes, concise syntax references, annotated implementation patterns, and independent challenge solutions.

## Course structure

| Module | Classes | Duration | Format |
|---|---|---|---|
| Git & GitHub | 1 | 3 hrs | Version control fundamentals & workflow |
| Python | 12 | 3 hrs each | Language fundamentals through advanced topics |
| PostgreSQL | 12 | 3 hrs each | Relational database design & querying |
| FastAPI | 12 | 3 hrs each | REST API development with a modern async framework |
| Projects | 12 | 3 hrs each | Applied, end-to-end builds combining all modules |

**49 sessions total**, each session logged as its own dated entry inside the
relevant module folder.

## Repo structure

Every topic folder follows the same layout, so navigating any module feels
the same regardless of subject:

```
python-backend-bootcamp/
├── 01-git-github/
│   ├── notes.md            # theory, explained in plain language
│   ├── cheatsheet.md        # fast syntax/command reference
│   └── practice/            # hands-on exercises
├── 02-python/
│   ├── class-01-<topic>/
│   │   ├── notes.md
│   │   ├── cheatsheet.md
│   │   ├── examples.py      # heavily commented, runnable code
│   │   └── practice.py      # exercises, solved independently
│   ├── ...
│   └── quizzes/
├── 03-postgresql/
│   └── ...same pattern (examples/practice as .sql)
├── 04-fastapi/
│   └── ...same pattern
└── projects/
    ├── project-01-<name>/
    └── ...
```

Each subtopic folder contains:
- **`notes.md`** — theory and concepts explained in my own words, with
  real-world analogies where useful
- **`cheatsheet.md`** — a terse, scannable syntax/command reference (no prose)
- **`examples.py` / `.sql`** — working, heavily commented code
- **`practice.py` / `.sql`** — exercises to complete without referring back
  to notes

## Tech stack

- **Language:** Python 3
- **Database:** PostgreSQL
- **Framework:** FastAPI
- **Version control:** Git & GitHub

## Class index

### 01 — Git & GitHub (1 class)
### 02 — Python (12 classes)
### 03 — PostgreSQL (12 classes)
### 04 — FastAPI (12 classes)
### 05 - Projects (12 sessions)

## Workflow

1. Right after each class, spend 5–10 minutes filling `notes.md` and `cheatsheet.md` for that session — don't batch it later.
2. Complete `practice.py`/`practice.sql` a day or two after class, without looking at notes first.
3. Commit after every session so the repo tracks progress class-by-class.
4. Quizzes for a module live in that module's `quizzes/` folder.

## Author

**Anunay Argha** — Full Stack Developer, Software Development Community Lead at Shanto-Mariam University of Creative Technology (SMUCT)
