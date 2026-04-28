from flask import Flask, render_template, request, Response, send_file
import csv
import io
from scrapper import run_scraper

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/scrape', methods=['POST'])
def scrape():
    data = request.json
    base_url = data.get('base_url', '').strip()
    mode = data.get('mode', 'single') # 'auto', 'manual', 'single'
    sections = int(data.get('sections', 0))
    pages = int(data.get('pages', 0))
    specific_pages = data.get('specific_pages', [])
    
    if not base_url:
        return {"error": "Base URL is required."}, 400
        
    try:
        # Run scraper logic
        list_final = run_scraper(base_url, mode, sections, pages, specific_pages)
        
        # Write CSV output to a string buffer
        si = io.StringIO()
        cw = csv.writer(si)
        cw.writerows(list_final)
        
        output = io.BytesIO(si.getvalue().encode('utf-8'))
        output.seek(0)
        
        return send_file(
            output,
            mimetype="text/csv",
            as_attachment=True,
            download_name="scraped_data.csv"
        )
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    # Run the app locally
    app.run(debug=True)
