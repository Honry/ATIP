Feature: scroll & fling tests
    Scenario: settings
        When I launch "Settings" with "com.android.settings" and "Settings" on android
        Then I wait for 3 seconds
        Then I scroll to end
        Then I wait for 3 seconds
        Then I press "home" hardware key
        Then I wait for 3 seconds
        Then I fling "horiz" goto "forward"        
        Then I press "recent" hardware key
        Then I wait for 3 seconds
        Then I save "android.widget.ImageView" on the "right" side of text "Settings" to temporary value "settings_app"
        Then I click object "settings_app"
        Then I wait for 3 seconds
        Then I press "back" hardware key
        Then I wait for 3 seconds
        Then I press "recent" hardware key
        Then I wait for 3 seconds
        Then I swipe object "settings_app" to "left"
        Then I press "power" hardware key
        Then I wait for 3 seconds
        Then I turn on screen
        Then I wait for 3 seconds
        Then I turn off screen
        Then I turn on screen
