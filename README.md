# Quote Scraper & Guessing Game

**Quote Scraper & Guessing Game** is a Python mini-project that scrapes quotes from a public website and lets players guess the author in a fun, interactive way.

---

## Features
- Scrapes all quotes from [quotes.toscrape.com](http://quotes.toscrape.com) across multiple pages.
- Stores each quote, its author, and a link to the author's biography.
- Randomly selects a quote for the player to guess the correct author.
- Gives players 4 attempts to get it right.

---

## Tech Stack
- **Python 3.x**
- **requests** (HTTP library)
- **BeautifulSoup4** (HTML parsing)

---

## Screenshots/Diagrams
![image](https://github.com/user-attachments/assets/75cd88c5-88bd-41a2-9205-d04f67634987)

---
## How to Install/Run

### 1. Clone the Repository

```bash
git clone https://github.com/deberry-code/quotes-scraper-guessing-game.git
cd quotes-scraper-guessing-game

```

### 2. Set up a Python Virtual Environment (optional but recommended)

```bash
python3 -m venv env
source env/bin/activate

```

### 3. Install Requirements

```bash
pip install requests beautifulsoup4

```

### 4. Run the App

```bash
python3 quote_guessing_game.py

```

---

## Future Improvements

- Add hints (e.g., first letter of author's name, birth year).
- Display author's biography link if the player loses.
- Add multiple rounds or score tracking.
- Timer for each guess to increase difficulty.
- Export all scraped quotes to a CSV file.
