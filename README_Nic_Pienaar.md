## Nic Pienaar

## Files
First.py - scripts to get required information
query.py - script to test the factorial of a number

## QA Requirements for you to implement

1. Write a locator (CSS selector/XPath) for the red form validation styling
2. Find the console message printed
3. Write a Selenium script to test that the factorial of 7 is 5040
4. Figure out the API call being made along with the headers and parameters sent
5. Write a bug report
6. Document a test case
7. Include test coverage
8. Add any documentation that might be necessary to explain your process, include this in a file in the repo.

## Response

1. You will need to activate the styling and then get the css value
red_form_locator = driver.find_element("id", "number")
print("Style: " + red_form_locator.value_of_css_property('border'))
2. You will need to activate the message first and the look it up
console_message = driver.find_element("id", "resultDiv").text
3. 
4. API calls are shown in the spreadsheet attached (https://docs.google.com/spreadsheets/d/1TOr5vcn1YLpEw0M6AUJxZYBON-asLRzdDPF5SDUffHc/edit?usp=sharing)
5. Bug report can be found in the spreadsheet attached (https://docs.google.com/spreadsheets/d/1TOr5vcn1YLpEw0M6AUJxZYBON-asLRzdDPF5SDUffHc/edit?usp=sharing)
6. Test case can be found in spreadsheet attached (https://docs.google.com/spreadsheets/d/1TOr5vcn1YLpEw0M6AUJxZYBON-asLRzdDPF5SDUffHc/edit?usp=sharing)
7. My apologies, I'm not 100% sure what is required here
