Feature: Embedding api usecase tests
    Scenario: Check xwalk contact extension
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.sample" and "ContactExtensionActivity" on android
        And I register watcher "ClearInfoWindow" when "Info" click "confirm"
        And I force to run all watchers
        And I wait 3 seconds
        Then I edit index "0" text to input "jacky"
        Then I edit index "1" text to input "10010"
        Then I click "Write Contact"
        And I wait 1 seconds
        Then I click "Read Contact"
        And I wait 1 seconds
        Then I should see view "passed"
        And I remove all watchers