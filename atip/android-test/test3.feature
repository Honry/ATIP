Feature: Embedding api usecase tests
    Scenario: Check xwalk activity
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.sample" and "XWalkViewWithLayoutActivity" on android
        And I register watcher "ClearInfoWindow" when "Info" click "confirm"
        And I register watcher "ClearAttentionWindow" when "Attention" click "OK"
        And I force to run all watchers
        And I sleep 10 seconds
        Then I should see web "百度一下"
        And I remove all watchers
