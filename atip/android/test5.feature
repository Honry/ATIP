Feature: Embedding api usecase tests
    Scenario: Check xwalk pause & resume js time
        When I launch "usecase-embedding-android-test" with "org.xwalk.embedded.api.sample" and "PauseTimersActivity" on android
        And I register watcher "ClearInfoWindow" when "Info" click "confirm"
        And I force to run all watchers
        And I wait 3 seconds
        Then I click button "org.xwalk.embedded.api.sample:id/pause"
        Then I process "android.view.View" on the "down" side of view "A script on this page starts this clock:"
        Then I reload process result to temporary value "clock_pause"
        And I wait 3 seconds
		Then I reload process result to temporary value "clock_after_pause"
		Then I compare object "clock_pause" equal "clock_after_pause" on info "contentDescription"
		Then I click button "org.xwalk.embedded.api.sample:id/pause"
		And I wait 3 seconds
		Then I reload process result to temporary value "clock_onresume"
		Then I compare object "clock_after_pause" unequal "clock_onresume" on info "contentDescription"
        And I remove all watchers