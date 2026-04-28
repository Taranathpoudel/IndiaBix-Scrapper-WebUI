# Implementing a Web UI for IndiaBix Scraper

This plan details the addition of a premium, state-of-the-art Web UI to the IndiaBix Scraper project, allowing users to effortlessly configure operations and download the scraped CSS from their browser, replacing the terminal interaction.

## User Review Required

> [!IMPORTANT]
> The Web UI will be powered by **Flask**. I will add `flask` to the `requirements.txt`. This ensures the backend remains simple, lightweight, and entirely in Python.
> Please review the design choices before I proceed.

## Proposed Changes

### Refactoring the Scraper
The current `scrapper.py` gets its inputs directly from `input()` prompts in the global scope and modifies global state.
#### [MODIFY] [scrapper.py](file:///f:/1.%20Don't%20Overwhelm/indiabix-scraper-gurkha-branch/scrapper.py)
- Encapsulate the global list definitions (`list_questions`, `list_right_tuple`, `list_scraped`) and the `append` function into a class or a robust function `scrape_data(config)`.
- Replace the interactive `input()` and `os.system("start excel")` lines with an interface that accepts parameters (base URL, counts, paths) and returns the generated CSV data or path.
- Keep backwards CLI compatibility using `if __name__ == "__main__":` so terminal fans can still run the script interactively.

### The Backend Application
#### [NEW] [app.py](file:///f:/1.%20Don't%20Overwhelm/indiabix-scraper-gurkha-branch/app.py)
- A lightweight Flask server with two routes:
  - `GET /` to render the Web UI.
  - `POST /api/scrape` to receive JSON scraping configurations from the UI, execute the `scrapper.py` logic, and return the generated CSV file as an attachment for the browser to download.

#### [MODIFY] [requirements.txt](file:///f:/1.%20Don't%20Overwhelm/indiabix-scraper-gurkha-branch/requirements.txt)
- Add `flask` to the list of project dependencies.

### The Frontend (Web UI)
Focusing heavily on **Premium Design Aesthetics**, dynamic interfaces, modern layout, and clean typography.
#### [NEW] [templates/index.html](file:///f:/1.%20Don%20't%20Overwhelm/indiabix-scraper-gurkha-branch/templates/index.html)
- Standard HTML5 structure importing an elegant Google Font (e.g., Inter or Outfit).
- Javascript logic to dynamically change the form options based on whether the user selects "Auto-Crawl", "Manual", or "Single URL".
- AJAX setup to hit the `POST /api/scrape` backend, process the response, and automatically trigger the browser file download.
#### [NEW] [static/styles.css](file:///f:/1.%20Don't%20Overwhelm/indiabix-scraper-gurkha-branch/static/styles.css)
- Sleek dark mode design.
- Glassmorphism effects for the central interactive form container.
- Smooth transitions and vibrant hover animations on buttons and input fields to wow the user.
- A beautiful loading state/spinner for when the scraping is actively running on the backend.

## Verification Plan

### Automated Tests
- Run `pip install -r requirements.txt` to ensure Flask installs.
- Start `python app.py` and ensure the server runs on port 5000.

### Manual Verification
- Ask the user to open `http://localhost:5000` in their browser, fill in the options for an "Auto-Crawl" using section `1` and page `2`, and verify that the downloading CSV has the valid scraped data inside of it.
