from .manager import PluginManager
from .builtin import BasicAuthPlugin, DigestAuthPlugin
from ..output.formatters.headers import HeadersFormatter
from ..output.formatters.json import JSONFormatter
from ..output.formatters.colors import ColorFormatter


plugin_manager = PluginManager()


# Register all built-in plugins.
plugin_manager.register(
    BasicAuthPlugin,
    DigestAuthPlugin,
    HeadersFormatter,
    JSONFormatter,
    ColorFormatter,
)
