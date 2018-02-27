import json

def process():
    f = open('2017.json')
    all_courses = json.loads(f.read())
    f.close()
    courses = []

    first = 'First Semester'
    second = 'Second Semester'
    for course in all_courses:
        if 'term' in course:
            if course['term'][:len(first)] == first:
                if '2017' in course['term']:
                    course['echo'] = course['code'] + '_Sem1_2017'
                    courses.append(course)
                elif '2016' in course['term']:
                    course['echo'] = course['code'] + '_Sem1_2016'
                    courses.append(course)
            elif course['term'][:len(second)] == second:
                course['title'] = course['title']
                if '2017' in course['term']:
                    course['echo'] = course['code'] + '_Sem2_2017'
                    courses.append(course)
                elif '2016' in course['term']:
                    course['echo'] = course['code'] + '_Sem2_2016'
                    courses.append(course)
    f = open('processed.json', 'w')
    json_string = json.dumps(courses, indent=4, sort_keys=True)
    f.write(json_string)
    f.close()

def search_introduction(text):
    all_courses = []
    f = open('2018.json')
    all_courses = json.loads(f.read())
    f.close()
    for course in all_courses:
        if text.lower() in course['introduction'].lower():
            print(course['code'] + ' ' + course['title'])
