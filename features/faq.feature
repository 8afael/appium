@android
Feature: Corelogic tests
  @current
  Scenario: login 
    Given authentication
    Given click in FAQ
    Then text should be in the results

#  Scenario: Share a movie with Email
#    When user search for movie: "Matrix"
#    And user clone ad banner
#    Then movie: "Matrix" should be in the results
#    Then user should be able to send email to: "8afael@gmail.com"