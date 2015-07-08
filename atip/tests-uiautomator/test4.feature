Feature: Embedding api usecase tests
    Scenario: Check xwalk contact extension
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.sample" and "ContactExtensionActivity"
        And I register watcher "ClearInfoWindow" when "Info" click "confirm"
        And I force to run all watchers
        And I wait 3 seconds
        Then I edit first text to input "jacky"
        Then I edit second text to input "10010"
        Then I click "Write Contact" by "description"
        And I wait 1 seconds
        Then I click "Read Contact" by "description"
        And I wait 1 seconds
        Then I should see view "passed"
        And I remove all watchers