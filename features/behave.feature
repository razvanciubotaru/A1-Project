Feature: Check page navigation
       Want to check page navigation

Scenario: Valid Intial Page
       When we go to initial page
       Then it should have title "A1 Digital"

Scenario: Choose english language
        When we select english language
        Then it should have title "A1 Digital - Drive digitization"

Scenario: Go to solutions page
        When we go to solutions page
        Then it should have title "Solutions"

Scenario: Go to virtual infrastructure page
        When we go to virtual infrastructure page
        Then it should have title "Virtual infrastructure in the cloud"

Scenario: Go to exoscale page
        When we go to exoscale page
        Then it should have title "Exoscale - The European Cloud Platform"




