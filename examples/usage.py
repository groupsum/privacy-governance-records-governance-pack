"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_privacy_governance_records import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:iso-29100-privacy-principles-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-iso-29100-privacy-principles-requirements.yaml"
