## Created by msingh at 2023-04-04
#Feature: Verify is Book is Added and Deleted using Library API
#
#  @library
#  Scenario: Verify Add Book Functionality
#    Given the book details which need to be added to Library
#    When we execute AddBook PostAPI method
#    Then book is successfully added
#
#  @library
#  Scenario Outline: Verify Add Book Functionality
#    Given the book details which need to be added to Library
#    When we execute AddBook PostAPI method with <name> <aisle> <author>
#    Then book is successfully added
#    Examples:
#      |   name       |   aisle    |   author     |
#      |   Satinder   |   2345     |   Pratiksha  |
#      |   Nidhi      |   2456     |   Rahul      |