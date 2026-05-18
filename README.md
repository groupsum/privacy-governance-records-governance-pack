# privacy-governance-records-governance-pack

Installable SSOT governance pack for privacy records, consent receipts, notices, DPV processing records, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:privacy-governance-records`
- Priority: `P0.3`
- PyPI package: `privacy-governance-records-governance-pack`
- Import package: `ssot_pack_privacy_governance_records`
- GitHub repository: `groupsum/privacy-governance-records-governance-pack`
- Reservation owner: `extension-pack:privacy-governance-records-governance-pack`

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

- `adr:privacy-governance-record-source-policy` - Privacy Governance Record Source Policy
- `adr:iso-29100-privacy-framework-policy` - ISO 29100 Privacy Framework Policy
- `adr:iso-29184-privacy-notice-policy` - ISO 29184 Privacy Notice Policy
- `adr:iso-27560-consent-record-policy` - ISO 27560 Consent Record Policy
- `adr:kantara-consent-receipt-policy` - Kantara Consent Receipt Policy
- `adr:dpv-processing-record-policy` - DPV Processing Record Policy
- `adr:privacy-audit-evidence-policy` - Privacy Audit Evidence Policy
- `adr:iso-27701-pims-policy` - ISO 27701 PIMS Policy
- `adr:iso-27018-cloud-pii-policy` - ISO 27018 Cloud PII Policy
- `adr:privacy-record-retention-policy` - Privacy Record Retention Policy

## Included SPECs

- `spc:iso-29100-privacy-principles-requirements` - ISO 29100 Privacy Principles Requirements
- `spc:iso-29100-pii-role-requirements` - ISO 29100 PII Role Requirements
- `spc:iso-29184-notice-content-requirements` - ISO 29184 Notice Content Requirements
- `spc:iso-29184-notice-presentation-requirements` - ISO 29184 Notice Presentation Requirements
- `spc:iso-27560-consent-record-structure-requirements` - ISO 27560 Consent Record Structure Requirements
- `spc:iso-27560-consent-lifecycle-requirements` - ISO 27560 Consent Lifecycle Requirements
- `spc:kantara-consent-receipt-core-requirements` - Kantara Consent Receipt Core Requirements
- `spc:kantara-consent-receipt-policy-requirements` - Kantara Consent Receipt Policy Requirements
- `spc:dpv-processing-purpose-requirements` - DPV Processing Purpose Requirements
- `spc:dpv-personal-data-category-requirements` - DPV Personal Data Category Requirements
- `spc:dpv-rights-risk-measure-requirements` - DPV Rights Risk Measure Requirements
- `spc:iso-27701-pims-evidence-requirements` - ISO 27701 PIMS Evidence Requirements
- `spc:iso-27018-cloud-pii-evidence-requirements` - ISO 27018 Cloud PII Evidence Requirements
- `spc:privacy-record-retention-requirements` - Privacy Record Retention Requirements
- `spc:privacy-record-export-requirements` - Privacy Record Export Requirements
- `spc:privacy-record-evidence-linkage-requirements` - Privacy Record Evidence Linkage Requirements

## Install With uv

```bash
uv add privacy-governance-records-governance-pack
uv add ssot-registry privacy-governance-records-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install privacy-governance-records-governance-pack
uvx --from ssot-registry ssot pack sync . privacy-governance-records-governance-pack
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
- PyPI package: https://pypi.org/project/privacy-governance-records-governance-pack/
- SSOT Registry: https://pypi.org/project/ssot-registry/
