Feature: orientation & freeze & screenshot tests
    Scenario: functions
        When I launch "Settings" with "com.android.settings" and "Settings" on android
        Then I press "home" hardware key
        Then I take screenshot as "home.png"
        Then I wait for 3 seconds
        Then I set orientation "n"
        Then I wait for 3 seconds
        Then I open notification
        Then I wait for 3 seconds
        Then I open quick settings
        Then I wait for 3 seconds
        Then I press "home" hardware key
