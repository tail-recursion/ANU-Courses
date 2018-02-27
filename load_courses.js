// Select courses
document.getElementsByClassName('catalogue-search-button catalogue-search-button--courses')[0].click()

// Check undergraduate
document.getElementById('Careers[0]').click()

// Select 2016
document.getElementById('program-commencement-year').selectedIndex = 2;

// Click search
document.getElementById('btnSearchCatalogue').click()

// Show all results
document.querySelectorAll('a[href][data-template="course-template"]')[0].click()
