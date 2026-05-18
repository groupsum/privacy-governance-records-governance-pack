<div align="center">

# privacy-governance-records-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/privacy-governance-records-governance-pack.svg)](https://pypi.org/project/privacy-governance-records-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/privacy-governance-records-governance-pack.svg)](https://pypi.org/project/privacy-governance-records-governance-pack/)
[![License](https://img.shields.io/pypi/l/privacy-governance-records-governance-pack.svg)](https://pypi.org/project/privacy-governance-records-governance-pack/)
[![Publish](https://github.com/groupsum/privacy-governance-records-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/privacy-governance-records-governance-pack/actions/workflows/publish.yml)

</div>

Installable SSOT governance pack for privacy records, consent receipts, notices, DPV processing records, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `privacy-governance-records-governance-pack` is an installable SSOT governance pack for Privacy Governance And Consent Records. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern privacy governance and consent records, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`privacy-governance-records-governance-pack`](https://pypi.org/project/privacy-governance-records-governance-pack/)
- GitHub package repository: [`groupsum/privacy-governance-records-governance-pack`](https://github.com/groupsum/privacy-governance-records-governance-pack)
- Import package: `ssot_pack_privacy_governance_records`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:privacy-governance-records`
- PyPI package: `privacy-governance-records-governance-pack`
- Import package: `ssot_pack_privacy_governance_records`
- GitHub repository: [groupsum/privacy-governance-records-governance-pack](https://github.com/groupsum/privacy-governance-records-governance-pack)
- Reservation owner: `extension-pack:privacy-governance-records-governance-pack`

## Domain Focus

Privacy Governance And Consent Records

## Authority Sources

- [ISO/IEC 29100 Privacy Framework](https://www.iso.org/standard/85938.html)
- [ISO/IEC 29184 Online privacy notices and consent](https://www.iso.org/standard/70331.html)
- [ISO/IEC TS 27560 Consent record information structure](https://www.iso.org/standard/80392.html)
- [Kantara Consent Receipt Specification](https://kantara.atlassian.net/wiki/spaces/archive/pages/3508790/Consent%2BReceipt%2BSpecification)
- [W3C Data Privacy Vocabulary](https://www.w3.org/community/reports/dpvcg/CG-FINAL-dpv-20240801/)
- [ISO/IEC 27701 Privacy Information Management System](https://www.iso.org/standard/27701)
- [ISO/IEC 27018 Public-cloud PII protection](https://www.iso.org/standard/27018)

## Included ADRs

- [`adr:privacy-governance-record-source-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1001-privacy-governance-record-source-policy.yaml) - Privacy Governance Record Source Policy
- [`adr:iso-29100-privacy-framework-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1002-iso-29100-privacy-framework-policy.yaml) - ISO 29100 Privacy Framework Policy
- [`adr:iso-29184-privacy-notice-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1003-iso-29184-privacy-notice-policy.yaml) - ISO 29184 Privacy Notice Policy
- [`adr:iso-27560-consent-record-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1004-iso-27560-consent-record-policy.yaml) - ISO 27560 Consent Record Policy
- [`adr:kantara-consent-receipt-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1005-kantara-consent-receipt-policy.yaml) - Kantara Consent Receipt Policy
- [`adr:dpv-processing-record-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1006-dpv-processing-record-policy.yaml) - DPV Processing Record Policy
- [`adr:privacy-audit-evidence-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1007-privacy-audit-evidence-policy.yaml) - Privacy Audit Evidence Policy
- [`adr:iso-27701-pims-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1008-iso-27701-pims-policy.yaml) - ISO 27701 PIMS Policy
- [`adr:iso-27018-cloud-pii-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1009-iso-27018-cloud-pii-policy.yaml) - ISO 27018 Cloud PII Policy
- [`adr:privacy-record-retention-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1010-privacy-record-retention-policy.yaml) - Privacy Record Retention Policy

## Included SPECs

- [`spc:iso-29100-privacy-principles-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2001-iso-29100-privacy-principles-requirements.yaml) - ISO 29100 Privacy Principles Requirements
- [`spc:iso-29100-pii-role-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2002-iso-29100-pii-role-requirements.yaml) - ISO 29100 PII Role Requirements
- [`spc:iso-29184-notice-content-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2003-iso-29184-notice-content-requirements.yaml) - ISO 29184 Notice Content Requirements
- [`spc:iso-29184-notice-presentation-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2004-iso-29184-notice-presentation-requirements.yaml) - ISO 29184 Notice Presentation Requirements
- [`spc:iso-27560-consent-record-structure-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2005-iso-27560-consent-record-structure-requirements.yaml) - ISO 27560 Consent Record Structure Requirements
- [`spc:iso-27560-consent-lifecycle-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2006-iso-27560-consent-lifecycle-requirements.yaml) - ISO 27560 Consent Lifecycle Requirements
- [`spc:kantara-consent-receipt-core-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2007-kantara-consent-receipt-core-requirements.yaml) - Kantara Consent Receipt Core Requirements
- [`spc:kantara-consent-receipt-policy-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2008-kantara-consent-receipt-policy-requirements.yaml) - Kantara Consent Receipt Policy Requirements
- [`spc:dpv-processing-purpose-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2009-dpv-processing-purpose-requirements.yaml) - DPV Processing Purpose Requirements
- [`spc:dpv-personal-data-category-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2010-dpv-personal-data-category-requirements.yaml) - DPV Personal Data Category Requirements
- [`spc:dpv-rights-risk-measure-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2011-dpv-rights-risk-measure-requirements.yaml) - DPV Rights Risk Measure Requirements
- [`spc:iso-27701-pims-evidence-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2012-iso-27701-pims-evidence-requirements.yaml) - ISO 27701 PIMS Evidence Requirements
- [`spc:iso-27018-cloud-pii-evidence-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2013-iso-27018-cloud-pii-evidence-requirements.yaml) - ISO 27018 Cloud PII Evidence Requirements
- [`spc:privacy-record-retention-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2014-privacy-record-retention-requirements.yaml) - Privacy Record Retention Requirements
- [`spc:privacy-record-export-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2015-privacy-record-export-requirements.yaml) - Privacy Record Export Requirements
- [`spc:privacy-record-evidence-linkage-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2016-privacy-record-evidence-linkage-requirements.yaml) - Privacy Record Evidence Linkage Requirements

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

- GitHub package repository: [groupsum/privacy-governance-records-governance-pack](https://github.com/groupsum/privacy-governance-records-governance-pack)
- PyPI package: [privacy-governance-records-governance-pack](https://pypi.org/project/privacy-governance-records-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
