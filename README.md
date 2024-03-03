# Friendly chat bot
## About
This bot was created special for the one chat, where bad words are strictly prohibited. Well, in the future this bot can be easily modified to something bigger.

## Admin privileges
There are admin privileges available in the bot. You can also modify answer texts in src/texts.json

### How to add new admins?
**File .env** you should add new telegram ID to ```ADMINS``` variable, separating by whitespace.

You can get telegram ID from the [special telegram bot](https://t.me/getmyid_bot).

Example:

```python
# Two admins with telegram ID's
ADMIN = "123456 468267"
```

### Admin commands
```/add_stop_word``` — add word to the stop list<br>
```/check_stop_word``` — check if word is in the stop list

## Contributing
Bot was written in **Python 3.8.10** using [aiogram](https://github.com/aiogram/aiogram)

All the files, but **words.txt**, in this bot are under the MIT License, so if you want, you can contribute in it.

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
