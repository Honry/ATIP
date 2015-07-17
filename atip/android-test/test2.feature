Feature: Embedding api usecase tests
    Scenario: Check xwalk & api versions
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.sample" and "XWalkVersionAndAPIVersion" on android
        And I register watcher "ClearInfoWindow" when "Info" click "confirm"
        And I force to run all watchers
        Then I should see text "API Version: 5.0; XWalk Version: 15"
        And I remove all watchers
