# ssot-pack-privacy-governance-records

Installable SSOT governance pack for privacy records, consent receipts, notices, DPV processing records, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:privacy-governance-records`
- Priority: `P0.3`
- PyPI package: `ssot-pack-privacy-governance-records`
- Import package: `ssot_pack_privacy_governance_records`
- GitHub repository: `groupsum/privacy-governance-records-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-privacy-governance-records`

## Domain Focus

Privacy Governance And Consent Records

## Authority Sources

- ISO/IEC 29100 Privacy Framework
- ISO/IEC 29184 Online privacy notices and consent
- ISO/IEC TS 27560 Consent record information structure
- Kantara Consent Receipt Specification
- W3C Data Privacy Vocabulary
- ISO/IEC 27701 Privacy Information Management System
- ISO/IEC 27018 Public-cloud PII protection

## Included ADRs

- `adr:privacy-record-authority-boundary` - Privacy Record Authority Boundary
- `adr:consent-receipt-and-dpv-governance` - Consent Receipt And DPV Governance

## Included SPECs

- `spc:consent-record-contract` - Consent Record Contract
- `spc:privacy-notice-contract` - Privacy Notice Contract
- `spc:dpv-processing-record-contract` - DPV Processing Record Contract
- `spc:privacy-audit-evidence-contract` - Privacy Audit Evidence Contract

## Install With uv

```bash
uv add ssot-pack-privacy-governance-records
uv add ssot-registry ssot-pack-privacy-governance-records
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-privacy-governance-records
uvx --from ssot-registry ssot pack sync . ssot-pack-privacy-governance-records
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_privacy_governance_records import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/privacy-governance-records-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-privacy-governance-records/
- SSOT Registry: https://pypi.org/project/ssot-registry/
