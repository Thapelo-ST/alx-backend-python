# Unit Testing and Integration Testing

By Jacob Schmitt, Senior Technical Content Marketing Manager Unit testing and integration testing are two fundamental types of software testing that are crucial for successful software development. While they serve different yet related purposes, one replace the other. complement each other nicely.

## Unit Testing

Unit testing is a software development process in which the smallest testable parts of an application, called units, are individually and independently scrutinized for proper operation. Unit testing is a component of test-driven development (TDD), a pragmatic methodology that takes a meticulous approach to building a product by means of continual testing and revision. Test-driven development requires that developers first write failing unit tests. Then they write code and refactor the application until the test passes.

Unit testing involves only those characteristics that are vital to the performance of the unit under test. This encourages developers to modify the source code without immediate concerns about how such changes might affect the functioning of other units or the program as a whole.

## Integration Testing

Integration testing is a type of software testing that focuses on testing how parts of the application work together as a whole. Unlike unit testing, integration testing considers side effects from the beginning. These side effects may even be desirable.

For example, an integration test could use the connection to a database (a dependency in unit testing) to query and mutate the database as it usually would. You would need to prepare the database and read it out afterward correctly. DevOps often "mocks away" these external resources the way mocking is used in unit tests. This results in obscuring the failures caused by APIs beyond their control.

Integration testing helps find issues that are not obvious by examining the application's or a specific unit's implementation. Integration testing discovers defects in the interplay of several application parts. Sometimes, these defects can be challenging to track or reproduce.

## Conclusion

Unit testing and integration testing are both important parts of successful software development. While writing unit tests is often faster, the reliability of integration tests tends to build more confidence for key stakeholders. Use both test strategies to ensure that your application is working today and continues to work tomorrow. Use your CI/CD tools to run your team's tests automatically, triggered when something changes, at regular intervals, or on demand. More tests mean more data, and more ways to make sure your team's software applications remain stable in production.
