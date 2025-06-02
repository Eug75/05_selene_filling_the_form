from selene import browser, be

def test_browser_open(browser_options):
    browser.open('https://demoqa.com/automation-practice-form')

def test_filling_first_name():
    browser.element('#firstName').type('Ivan')
    browser.element('#firstName').should(be.not_.blank)

def test_filling_last_name():
    browser.element('#lastName').type('Petrov')
    browser.element('#lastName').should(be.not_.blank)

def test_filling_email():
    browser.element('#userEmail').type('ivan.petrov@mail.ru')
    browser.element('#userEmail').should(be.not_.blank)

def test_filling_sex():
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#gender-radio-1').should(be.selected)

def test_filling_phone():
    browser.element('#userNumber').type('9012345678')
    browser.element('#userNumber').should(be.not_.blank)

def test_filling_date_of_birth():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="0"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="2000"]').click()
    browser.element('div[aria-label="Choose Monday, January 31st, 2000"]').click()
    browser.element('#dateOfBirthInput').should(be.not_.blank)

def test_filling_subjects():
    browser.element('#subjectsInput').type('Maths').press_enter()

def test_filling_hobby():
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('.custom-control-input').should(be.selected)

def test_filling_file_upload():
    browser.element('#uploadPicture').send_keys('D:\photo_2025-06-01_15-49-01.jpg')

def test_filling_address():
    browser.element('#currentAddress').type(
        'Mahatma Gandhi Rd, Srinagar - Kanyakumari Hwy, P and T Colony,\
         P&T Colony, Civil Lines, Delhi, 110054, India')
    browser.element('#currentAddress').should(be.not_.blank)

def test_filling_state_and_city():
    browser.element('.css-1wa3eu0-placeholder').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('.css-1wa3eu0-placeholder').click()
    browser.element('#react-select-4-option-0').click()

def test_submit_form():
    browser.element('#submit').click()
