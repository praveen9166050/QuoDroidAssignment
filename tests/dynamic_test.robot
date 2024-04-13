*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open google.com
    Open Browser    browser=chrome
    Go To    url=https://google.com
Login with correct Username and Password
    Open Browser    browser=chrome
    Go To    url=https://the-internet.herokuapp.com/login
    Input Text    username    tomsmith
    Input Text    password    SuperSecretPassword!
    Click Button     class:radius
    Element Should Contain    id=flash    You logged into a secure area!
    Click Link    Logout
    Close Browser
