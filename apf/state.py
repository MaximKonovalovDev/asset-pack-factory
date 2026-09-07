"""apf state: brief load + provenance fields."""
from __future__ import annotations
import yaml

PROV = ["seed","prompt","promptFamily","lane","model","providerVersion","sha256","license","source","date","routerHealth"]

def load_brief(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)
