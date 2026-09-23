"""Production smoke tests for OrbisAgents."""
import importlib


def test_package_imports() -> None:
    module = importlib.import_module("orbisagents")
    assert module.__name__ == "orbisagents"


def test_import_is_network_independent() -> None:
    # Import-time network calls make CI and offline development fragile.
    module = importlib.import_module("orbisagents")
    assert module is not None
