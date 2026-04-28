from getter import rawGetter
from bs4 import BeautifulSoup
import os
import csv
import sys
import re

def get_start_prefix(base_url):
    html_content = rawGetter(base_url)
    if not html_content:
        return 1
    
    soup = BeautifulSoup(html_content, 'html.parser')
    prefixes = []
    for a in soup.find_all('a'):
        href = a.get('href', '')
        # Check if it ends in 6 digits
        match = re.search(r'(\d{6})$', href)
        if match:
            prefixes.append(int(match.group(1)[:3]))
    
    if prefixes:
        return min(prefixes)
    return 1

def append_to_list(tail, list_scraped):
    list_questions = list()
    list_answer_tuple = list()
    list_right_tuple = list()
    
    i_html = rawGetter(tail)
    html = BeautifulSoup(i_html, 'html.parser')

    if(html != None):
        questions = html.find_all(attrs={"class": "bix-td-qtxt"})
        right = html.find_all("input", attrs={"class": "jq-hdnakq"})
        if(questions != [] and right != []):
            for td in questions:
                list_questions.append(td.text.strip())
            for ans in right:
                list_right_tuple.append(ans.get("value", "").strip())
        
        iteration = 0
        table = html.find_all(attrs={"class":"bix-div-container"})
        for td in table:
            newcsv = list()
            newcsv.append("")
            newcsv.append("")
            newcsv.append("")
            newcsv.append(list_questions[iteration])
            newcsv.append("")
            newcsv.append("")
            newcsv.append("")
            newcsv.append("")
            
            d = td.find_all(attrs={"class": "bix-td-option-val"})
            answer_count = 0
            for din in d:
                answer_count = answer_count + 1
            newcsv.append(answer_count)
            
            right_answer = list_right_tuple[iteration]
            if right_answer=="A": newcsv.append("1")
            elif right_answer=="B": newcsv.append("2")
            elif right_answer=="C": newcsv.append("3")
            elif right_answer=="D": newcsv.append("4")                
            elif right_answer=="E": newcsv.append("5")
            else: newcsv.append("")
            
            for din in d:
                newcsv.append(din.text.strip())
            
            # Pad answers up to 5 options so explanation is in the same column
            while len(newcsv) < 15:
                newcsv.append("")
            
            explanation_div = td.find(attrs={"class": "bix-ans-description"})
            explanation_text = explanation_div.text.strip() if explanation_div else ""
            newcsv.append(explanation_text)
            
            iteration = iteration + 1
            print('[APPEND]: ',newcsv)
            list_scraped.append(newcsv)

def run_scraper(index, mode, sections=0, pages=0, specific_pages=[]):
    """
    Run scraper and return a list of rows to be converted into a CSV.
    Mode can be: 'auto', 'manual', 'single'
    """
    list_final = [['subject_id', 'topic_id', 'question_type', 'question', 'marks',
    'time_to_spend','difficulty_level', 'hint', 'total_answers', 'correct_answer', 
    'answer 1', 'answer 2', 'answer 3', 'answer 4', 'answer 5', 'explanation']]
    
    list_scraped = list()
    
    if mode == 'auto':
        start_prefix = get_start_prefix(index)
        for s in range(start_prefix, start_prefix + sections):
            for p in range(1, pages + 1):
                page_code = f"{s:03d}{p:03d}"
                print(f"[FETCHING] {index}{page_code}")
                append_to_list(index + page_code, list_scraped)
    elif mode == 'manual':
        for ip in specific_pages:
            append_to_list(index + str(ip), list_scraped)
    else:
        # single
        append_to_list(index, list_scraped)
        
    list_final.extend(list_scraped)
    return list_final


if __name__ == "__main__":
    input_file_name = input("[NAME] Output to save: ")
    index = input("[PASTE, should end with / ] url to crawl: ")
    inquiry = input("[AUTO-CRAWL] Do you want to automatically scrape multiple sections and pages? [y/n]: ")
    
    mode = 'single'
    sections = 0
    pages = 0
    specific_pages = []
    
    if inquiry.lower() == 'y':
        try:
            sections = int(input("Enter the number of Sections (e.g., 2): "))
            pages = int(input("Enter the number of Pages per Section (e.g., 10): "))
            mode = 'auto'
        except ValueError:
            print("Invalid input. Please enter integer numbers.")
            sys.exit(1)
    else:
        inquiry2 = input("[MANUAL-CRAWL] Do you want to enter specific child page codes manually? [y/n]: ")
        if inquiry2.lower() == "y":
            latter = input("[001001 001002 001003] Please enter the sub urls to crawl: \n").split()
            specific_pages = latter
            mode = 'manual'
            
    list_final = run_scraper(index, mode, sections, pages, specific_pages)
    
    with open(input_file_name+ '.csv', 'w', newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(list_final)
        
    try:
        os.system("start excel "+input_file_name+".csv && exit")
    except:
        pass