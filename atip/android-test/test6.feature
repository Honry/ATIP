Feature: scroll & fling tests
    Scenario: settings
        When I launch "Settings" with "com.android.settings" and "Settings" on android
        And I sleep 3 seconds
        Then I scroll to end
        And I sleep 3 seconds
        Then I press "home" key
        Then I fling "horiz" goto "forward"        
        Then I press "recent" key
        And I sleep 3 seconds
        Then I save "android.widget.ImageView" on the "right" side of text "Settings" to temporary value "settings_app"
        Then I click object "settings_app"
        And I sleep 3 seconds
        Then I press "back" key    
        And I sleep 3 seconds
        Then I press "recent" key
        And I sleep 3 seconds
        Then I swipe object "settings_app" to "left"
        Then I press "power" key
        And I sleep 3 seconds
        Then I turn on device
        And I sleep 3 seconds
        Then I turn off device
        Then I turn on device
