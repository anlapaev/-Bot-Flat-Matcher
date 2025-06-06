# BotFlatMatcher

Telegram bot to match renters with property owners in Nizhny Novgorod. This repository contains
initial project structure and setup scripts.

## Structure
- `bot/` – application code
  - `main.py` – bot entry point
  - `handlers/` – command and callback handlers
  - `keyboards/` – custom keyboards
  - `states/` – FSM states
- `db/` – database models and connection helpers
- `utilities/` – common utilities

## Quick start
1. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
2. Export Telegram bot token as `BOT_TOKEN` environment variable.
3. Run the bot:
   ```bash
   python -m bot.main
   ```

This is a work in progress.
