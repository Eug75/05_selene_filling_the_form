import os.path

from selene import browser, have

def test_filling_the_form(browser_options):
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Ivan')

    browser.element('#lastName').type('Petrov')

    browser.element('#userEmail').type('ivan.petrov@mail.ru')

    browser.element('label[for="gender-radio-1"]').click()

    browser.element('#userNumber').type('9012345678')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="0"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="2000"]').click()
    browser.element('div[aria-label="Choose Monday, January 31st, 2000"]').click()

    browser.element('#subjectsInput').type('Maths').press_enter()

    browser.element('label[for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('spanners.jpg'))

    (browser.element('#currentAddress').type
    ('Mahatma Gandhi Rd, Srinagar - Kanyakumari Hwy, P and T Colony, P&T Colony, Civil Lines, Delhi, 110054, India'))

    browser.element('.css-1wa3eu0-placeholder').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('.css-1wa3eu0-placeholder').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').click()

    browser.element('tr:nth-child(1) > td:nth-child(2)').should(have.exact_text("Ivan Petrov"))
    browser.element('tr:nth-child(2) > td:nth-child(2)').should(have.exact_text("ivan.petrov@mail.ru"))
    browser.element('tr:nth-child(3) > td:nth-child(2)').should(have.exact_text("Male"))
    browser.element('tr:nth-child(4) > td:nth-child(2)').should(have.exact_text("9012345678"))
    browser.element('tr:nth-child(5) > td:nth-child(2)').should(have.exact_text("31 January,2000"))
    browser.element('tr:nth-child(6) > td:nth-child(2)').should(have.exact_text("Maths"))
    browser.element('tr:nth-child(7) > td:nth-child(2)').should(have.exact_text("Reading"))
    browser.element('tr:nth-child(8) > td:nth-child(2)').should(have.exact_text("spanners.jpg"))
    browser.element('tr:nth-child(9) > td:nth-child(2)').should(have.exact_text
    ("Mahatma Gandhi Rd, Srinagar - Kanyakumari Hwy, P and T Colony, P&T Colony, Civil Lines, Delhi, 110054, India"))
    browser.element('tr:nth-child(10) > td:nth-child(2)').should(have.exact_text("NCR Delhi"))

    browser.element('#closeLargeModal').click()
