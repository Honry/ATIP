Feature: Embedding api usecase tests
    Scenario: Check xwalk pause & resume js time
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.sample" and "PauseTimersActivity" on android
        And I register watcher "ClearInfoWindow" when "Info" click "confirm"
        And I force to run all watchers
        And I wait 3 seconds
        Then I click "org.xwalk.embedded.api.sample:id/pause"
        And I remove all watchers