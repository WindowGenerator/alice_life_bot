# Alice Life Bot

## Description:

While the bot is considered purely for polling users in chat rooms for specialization in IT

## Roadmap

- [x] Inject linters formatters + Makefile
- [x] Implement ways to run and build the project, and describe them in README.md
- [x] Write configs + main.py
- [ ] Write a prototype with cli without a database
- [ ] Separate business logic and interfaces to manage the application + Think about special cases 
- [ ] Inject sqlite3
- [ ] Replace commands with keyboard

## Development:

## Install dependencies:
1. [Install poetry](https://python-poetry.org/docs/) + Install make for your platform
2. Install deps: 
```bash
poetry install
```

## Run project:
```bash
make -f Makefile start
```

## Other:
- Linting and testing:
```bash
make -f Makefile
```
- Linting:
```bash
make -f Makefile lint
```
- Formating:
```bash
make -f Makefile format
```
- Run tests:
```bash
make -f Makefile test
```
