#Feature: Github API Validation
#
#
#  Scenario: Session management check
#    Given I have a github auth credentials
#    When  I hit getRepo API of github
#    Then status code of response should be 200