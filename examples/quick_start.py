"""Inspect the installed pack identity."""

from ssot_pack_privacy_governance_records import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:privacy-governance-records"
print(metadata["origin"]["id"])
