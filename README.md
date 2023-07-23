# Gambling App - Number Generator Game

## Overview

This is a simple gambling app that includes a number generator game. Users can register, log in, and play the Number Generator Game to guess a random number between 1 and 10. For each correct guess, they earn 1 point (equivalent to 1 gold coin). The points are stored in a database for each user, and they can view their wallet to check their balance.

## Prerequisites

1. Python 3.x
2. SQLite3

## Installation and Setup

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/stoodlesz/pygamblingapp.git
   cd gambling-app
   ```

## Install the required Python packages:

```bash
pip install bcrypt
```

## Create the SQLite database and set up the user table by running the following commands in your terminal:

```bash
sqlite3 gambling_app.db
```

In the SQLite shell:

```bash
-- Create the user table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    points INTEGER DEFAULT 0
);
.exit
```

## Usage

1. Run the app by executing the main Python script:

```bash
python main.py
```

2. You will see a menu with the following options:

   - Register: Create a new account with a unique username and password.
   - Login: Log in to your existing account.
   - Play: Guess the correct number between 1 and 10 to earn points (gold coins).
   - View Wallet: Check your current wallet balance (number of gold coins).
   - Exit: Quit the gambling app.

3. Follow the on-screen instructions to interact with the app. You can register, log in, and play the Number Generator Game to earn points. Your points will be stored in the database, and you can view your wallet balance at any time.

## Contributor

Stella
