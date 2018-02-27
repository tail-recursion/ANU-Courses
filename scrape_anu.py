import json, requests, time, random

# Web scraping library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

get_course_descriptions = False
browser = webdriver.Chrome()

base_url = 'http://programsandcourses.anu.edu.au/Search'

def execute_script(filename):
    '''' Injects Javascript into the browser and returns JSON
    :param filename: the name of the file containing Javascript to inject
    :return: JSON data - can be either a list or dictionary '''
    f = open(filename, 'r')
    json_string = browser.execute_script(f.read())
    f.close()
    json_data = json.loads(json_string)
    return json_data

def save_json(filename, data):
    ''' Saves data as a JSON file named filename
    :param filename: the name of the file to save
    :param data: a dictionary that will be encoded as a JSON string '''
    f = open(filename, 'w')
    json_string = json.dumps(data, indent=4, sort_keys=True)
    f.write(json_string)
    f.close()

browser.get(base_url)

# load courses
f = open('load_courses.js', 'r')
browser.execute_script(f.read())
f.close()

time.sleep(random.randint(15,20))

print("Scraping courses")

# scrape course data and save as JSON
courses = execute_script('scrape_courses.js')

save_json('courses.json', courses)

if get_course_descriptions:
    i = len(courses)
    for course in courses:
        print(str(i) + " " + course['title'])
        browser.get(course['url'])
        course_details = execute_script('scrape_course_details.js')
        course['introduction'] = course_details['introduction']
        save_json('courses.json', courses)
        time.sleep(random.randint(1,3))
        i -= 1
