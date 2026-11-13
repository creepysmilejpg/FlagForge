# FlagForge

## Executive Summary

Flag Forge is a Capture The Flag (CTF) hosting platform. As a student in Cybersecurity, and president of the Cybersecurity student organization on campus, I regularly participate in CTF competitions. This application is being built to facilitate the need to host a CTF competition of our own. 

This platform allows users to practice security skills by solving challenges and submitting flags. Players can browse through available challenges, submit their answers, and earn points when a flag is correctly identified! 

Administrators can create and manage challenges through the built in administrative interface. FlagForge provides a basic foundation for hsoting cyber challenges and encouraging hands on learning.

## Installation

### Requirements

- Python 3.10 or newer
- pip
- Django

#### 1. Clone the repository

```
git clone https://github.com/creepysmilejpg/FlagForge.git
cd FlagForge
```

#### 2. Create and activate virtual environment

```
python -m venv .venv
```

Windows:
```
.venv\Scripts\activate
```

Mac/Linux:
```
source .venv/bin/activate
```

#### 3. Install dependencies

```
pip install -r requirements.txt
```

#### 4. Set up database

```
python manage.py makemigrations competitions
python manage.py migrate
```

#### 5. Create admin account

```
python manage.py createsuperuser
```
Follow the prompts to create admin account

## Getting Started

### Start the application

```
python manage.py runserver
```

Open application in your browser:

http://127.0.0.1:8000/

#### Administrator

Navigate to

http://127.0.0.1:8000/admin/

Log in with the admin account created during installation

#### Players

http://127.0.0.1:8000/accounts/login/

Account must be created by administrator

#### Leaderboard

http://127.0.0.1:8000/leaderboard/

Leaderboard displays player scores and number of challenges solved

# License

MIT License Copyright (c) 2026 FlagForge

Permission is hereby granted, free of charge, to any person obtaining a copy of this software, to use, copy, modify, and distribute it.

The software is provided "as is," without warranty of any kind.
