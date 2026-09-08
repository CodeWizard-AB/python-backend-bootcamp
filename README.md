# Python Backend Engineering Bootcamp

A structured, self-maintained knowledge base for a university bootcamp on
Python backend engineering — covering Git & GitHub, Python, PostgreSQL, and
FastAPI, built out through hands-on projects across 3-hour weekly sessions.

This repo holds every class's notes, cheatsheets, code examples, practice
exercises, and quizzes in one place, organized so any topic can be found
and reviewed in seconds — during the course and afterward.

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
- [Class 1](./01-git-github/)

### 02 — Python (12 classes)
- [Class 1](./02-python/)  ← add a link per class as sessions happen

### 03 — PostgreSQL (12 classes)
- [Class 1](./03-postgresql/)

### 04 — FastAPI (12 classes)
- [Class 1](./04-fastapi/)

### Projects (12 sessions)
- [Project 1](./projects/)

## Workflow

1. Right after each class, spend 5–10 minutes filling `notes.md` and `cheatsheet.md` for that session — don't batch it later.
2. Complete `practice.py`/`practice.sql` a day or two after class, without looking at notes first.
3. Commit after every session so the repo tracks progress class-by-class.
4. Quizzes for a module live in that module's `quizzes/` folder.

## Author

**Anunay Argha** — Full Stack Developer, Software Development Community Lead at Shanto-Mariam University of Creative Technology (SMUCT)
