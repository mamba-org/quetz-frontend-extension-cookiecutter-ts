
import json
import quetz
from pathlib import Path

from ._version import __version__

HERE = Path(__file__).parent.resolve()

with (HERE / "labextension" / "package.json").open() as fid:
    data = json.load(fid)

@quetz.hookimpl
def js_plugin_paths():
    return [{
        "src": "labextension",
        "dest": data["name"]
    }]
