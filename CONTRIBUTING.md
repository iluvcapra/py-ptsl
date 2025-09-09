# Contributing

Contributions to this project in the form of issue submissions, discussion posts, and code are welcome!

## Notes about submitting issues

When submitting issues please take care to note the version of Pro Tools you are using.

## Notes for submitting code contributions or PRs

If you would like to submit code fixes or new features, please follow these guidelines:

1. Please create a pull request and fully fill-out the PR form.
2. Please base all PRs on the master branch.
3. New features should also have [tests](#unit-tests) implemented.
4. Any new code to be contributed should pass flake8 using the settings in the `.flake8` file
  in the root directory.
5. The documentation and README should be updated to reflect all changes.

## Unit Tests

Unit tests should fully exercise any new feature you add to either the Engine or the Client
class. Tests should only test the class and feature they're targeting, while mocking the behavior
of any other class.

If you add a new test to the Engine, it should mock the underlying client (using
the provided `open_engine_with_mock_client()` method. New features or tests added to the client
should likewise mock the underlying protocol stub.

At this time there are no tests that specifically require Pro Tools to be running and installed
on the host, though it probably would be a good idea to have some of these at some point.
