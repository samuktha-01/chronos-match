"""Tests for ChronosMatch project foundation setup and package initialization."""

import chronosmatch


def test_package_import() -> None:
    """Verify that the chronosmatch package can be imported successfully."""
    assert chronosmatch is not None


def test_package_version() -> None:
    """Verify that chronosmatch defines a valid non-empty semantic version."""
    assert hasattr(chronosmatch, "__version__")
    assert isinstance(chronosmatch.__version__, str)
    assert len(chronosmatch.__version__) > 0
    assert chronosmatch.__version__ == "0.1.0"


def test_package_exports() -> None:
    """Verify that __all__ defines the public package symbols."""
    assert hasattr(chronosmatch, "__all__")
    assert "__version__" in chronosmatch.__all__


def test_package_docstring() -> None:
    """Verify that the package has a descriptive module docstring."""
    assert chronosmatch.__doc__ is not None
    assert "ChronosMatch" in chronosmatch.__doc__
