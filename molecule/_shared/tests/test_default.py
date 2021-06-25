def test_service(host):
    """Validate consul service."""
    consul = host.service('consul')

    assert consul.is_running
    assert consul.is_enabled
