# Python News Headlines Scraper

A beginner-friendly Python project that scrapes the **latest top news headlines** from [India Today](https://www.indiatoday.in/) using `requests` and `BeautifulSoup`, and saves them into both a `.txt` file and an optional `.html` file.


##  Tech Stack
- Python 3
- `requests` (for fetching web content)
- `BeautifulSoup` (for parsing HTML)
- File handling (to save output)



##  Files in this Repo

| File | Description |
|------|-------------|
| `news_scraper.py` | The main Python script that does the scraping |
| `headlines.txt`   | The saved news headlines in plain text |
| `news.html` *(optional)* | Pretty HTML version of the headlines *(if added)* |



##  How It Works

1. Sends a request to India Today homepage
2. Parses the HTML to find all headlines (`<h2>` and `<h3>` tags)
3. Extracts clean text from those tags
4. Saves them into `headlines.txt` with numbering
5. *(Optional)* Also creates a `news.html` file for browser view



##  Output Example

1. Download App
2. Black box data downloaded in Air India crash probe breakthrough
3. LIVE: Dragon spacecraft with India's Shubhanshu Shukla to dock shortly
4. Rajnath Singh refuses to sign SCO document as Pak-China snub Pahalgam
5. Snake oil seller to 100% communist. Why Mamdani is facing backlash tsunami
6. Like baby learning to walk: Shubhanshu Shukla describes his space debut in call
7. Roti, kapda, but no makaan? The disappearing dream of affordable housing
8. Disclose all social media handles from past 5 years for visa: US Embassy in India
9. Who's Kerala's Arya Rajendran, cited by NYC's Mamdani in now-viral post
10. England vs India
11. How Ben Duckett and Ollie Pope neutralised Jasprit Bumrah in 1st Test
