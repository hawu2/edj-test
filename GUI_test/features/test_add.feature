Feature:  Add an event to database

  Scenario: Open landing page
    Given I open eventlist test page
    Then The page open


  Scenario: Open Events Manager Page
    Given I am already on the landing page
    When Click on Events link
    Then I can see Events Manager Page in the page


  Scenario: Add a event for today
    When Click on Add button to open Event Summary Dialog
    Then Input event data and save
    And Verify from GUI