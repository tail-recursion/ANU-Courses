// This has to be injected after load_courses.js
// You have to sleep for some time in between to allow courses to load

var table = document.getElementsByClassName('catalogue-search-results__table catalogue-search-results__table--courses table');

var table_class = 'catalogue-search-results__table catalogue-search-results__table--courses table';
var body = document.getElementsByClassName(table_class)[0].getElementsByTagName('tbody')[0];
var rows = body.getElementsByTagName('tr');

var courses = [];

for (var i=0; i < rows.length; i++) {
    var course = {};
    var td = rows[i].getElementsByTagName('td');
    course.code = td[0].textContent.trim()
    course.url = td[0].children[0].href;
    course.title = td[1].textContent.trim();
    course.term = td[2].textContent.trim();
    course.career = td[3].textContent.trim();
    course.units = td[4].textContent.trim();
    course.delivery = td[5].textContent.trim();
    courses.push(course);
}

return JSON.stringify(courses);
