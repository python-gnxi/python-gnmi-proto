def pytest_addoption(parser):
    parser.addoption(
        "--skip-integration",
        action="store_true",
        dest="skip_integration",
        default=False,
        help="skip integration tests",
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "integration: mark integration tests")

    if config.option.skip_integration:
        setattr(config.option, "markexpr", "not integration")
