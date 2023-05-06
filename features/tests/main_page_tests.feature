Feature: CureSkin Search Page feature


  Scenario: Top logo takes to the main page
    Given Open search results page Search: 18 results found for "cure"
    When  Click on CureSkin logo in the header
    Then Verify user is taken to the main page


  Scenario: User can verify UI elements on a Product Results Page
    Given Open cureskin homepage
    When Search for facewash
    And  Click on the product from Search Results
    Then Verify UI elements present: image, price, reviews, quantity, add to cart, buy it now button


  Scenario: Verify Footer Links
    Given Open cureskin homepage
    Then Identify the footer links: Terms of Service, Refund Policy, Privacy Policy, shipping policy and Verify each link navigates to correct pages


