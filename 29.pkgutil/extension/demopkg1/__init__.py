# extension/demopkg1/__init__.py
import pkgutil

# Keep path extension consistent
__path__ = pkgutil.extend_path(__path__, __name__)

