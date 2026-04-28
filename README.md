# IndiaBix Scraper Suite

A powerful, autonomous Python scraping suite designed to extract educational materials (multiple-choice questions, options, and correct answers) directly from **indiabix.com**. 

It features a beautiful web-based dashboard for easy operation and file downloads, alongside a lightweight, fully functional command-line interface (CLI) for advanced usage. All exported data is neatly formatted into a single, spreadsheet-readable CSV file.

## Features
- **Modern Web Dashboard**: An easy-to-use graphical interface to configure your scraping options directly from your browser.
- **Autonomous Crawling**: Configure the scraper to sequentially fetch multiple sections and pages entirely on its own.
- **Precision Targeting**: Specify exact URLs or child page codes to scrape specific quiz banks.
- **Dual Interfaces**: Use the intuitive Flask-powered Web UI or stick to the lightning-fast CLI menu.
- **CSV Export Engine**: Formats questions, answers, and choices beautifully into CSV files ready to be imported into any database, flashcard app, or Excel.

### Output Format
The generated CSV will organize the data structurally:

| Question  | Answer | Option A | Option B | Option C | Option D | Option E |
| --------- | ------ | -------- | -------- | -------- | -------- | -------- |
| Example Question? | 2 | Value 1 | Value 2 | Value 3 | Value 4 | Value 5 |

*(Note: "Answer" contains the numeric value of the right option, e.g., 2 corresponds to Option B).*

---

## 🚀 Installation & Setup

1. **Install Prerequisites**: Ensure you have Python 3 installed.
2. **Clone the Project**:
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 How to Use (Web Interface)

The most user-friendly way to use the IndiaBix Scraper is through its built-in Web Interface.

1. Start the web server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://127.0.0.1:5000/`.
3. Fill out the **Base URL** (e.g., `https://www.indiabix.com/civil-engineering/building-materials/` - ensuring it ends with a `/`).
4. Select your crawl mode:
   - **Auto-Crawl**: Set the number of sections and pages and let the scraper generate the URLs.
   - **Manual Pages**: Pass manually picked child URLs.
   - **Single URL**: Scrape just the provided Base URL.
5. Hit **Start Scraping**! The server will process the inputs and a `.csv` file will automatically download to your computer.

---

## ⌨️ How to Use (Command Line)

If you prefer using the terminal, a lightweight CLI interface is still available!

1. Run the scraper core file:
   ```bash
   python scrapper.py
   ```
2. Follow the on-screen prompts:
   - Provide a file name to save as.
   - Provide your IndiaBix base URL.
   - Answer `y` or `n` to configure Auto-Crawling or manual pagination exactly like the Web Interface!
