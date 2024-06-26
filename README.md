# Friendly chat bot for the school chat

## About
This bot was created special for the one chat, where bad words are strictly prohibited. Well, in the future this bot can be easily modified to something bigger.

Bot deletes all the messages, where he could find "*" symbol or a word from the "words.txt" file.

Works only in one chat. You can set that in the **.env** file.

## Admin privileges
There are admin privileges available in the bot. You can also modify answer texts in src/texts.json

### How to add new admins?
**File .env** you should add new telegram ID to ```ADMINS``` variable, separating by whitespace.

You can get telegram ID from the [special telegram bot](https://t.me/getmyid_bot).

Example:

```python
# Two admins with telegram ID's
ADMINS = "123456 468267"
```

## Contributing
Bot was written in **Python 3.8.10** using [aiogram](https://github.com/aiogram/aiogram)

All the files, but **words.txt**, in this bot are under the MIT License, so if you want, you can contribute in it.

Before start, create ```/src/config/words.txt``` with some words, that will be filtered by the bot.

### How to create virtual environment
```bash
cd src

# activating environment and updating pip
./venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# starting application
python app.py
```

### How to start from Docker
```bash
docker compose build app
docker compoes up
```

## Contact author
My contacts are available in the profile — [@uw935](https://github.com/uw935)
