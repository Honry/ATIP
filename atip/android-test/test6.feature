Feature: scroll & fling tests
    Scenario: settings
        When I launch "Settings" with "com.android.settings" and "Settings" on android
        Then I wait for 3 seconds
        Then I scroll to end
        Then I wait for 3 seconds
        Then I press "home" on android
        Then I fling "horiz" goto "forward"        
        Then I press "recent" on android
        Then I wait for 3 seconds
        Then I save "android.widget.ImageView" on the "right" side of text "Settings" to temporary value "settings_app"
        Then I click object "settings_app"
        Then I wait for 3 seconds
        Then I press "back" on android    
        Then I wait for 3 seconds
        Then I press "recent" on android
        Then I wait for 3 seconds
        Then I swipe object "settings_app" to "left"
        Then I press "power" on android
        Then I wait for 3 seconds
        Then I turn on device
        Then I wait for 3 seconds
        Then I turn off device
        Then I turn on device
