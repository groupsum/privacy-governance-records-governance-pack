# privacy-governance-records-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>privacy-governance-records-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for privacy records, consent receipts, notices, DPV processing records, and audit evidence.</p>
<p align="center">
<a href="https://pypi.org/project/privacy-governance-records-governance-pack/"><img alt="pypi: privacy-governance-records-governance-pack" src="https://img.shields.io/pypi/v/privacy-governance-records-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.1.1.dev1" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.1.1.dev1&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/privacy-governance-records-governance-pack/"><img alt="Monthly PyPI downloads: privacy-governance-records-governance-pack" src="https://img.shields.io/pypi/dm/privacy-governance-records-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/README.md"><img alt="README hits: privacy-governance-records-governance-pack" src="https://hits.sh/github.com/groupsum/privacy-governance-records-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/privacy-governance-records-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for privacy records, consent receipts, notices, DPV processing records, and audit evidence.

### Why This Package

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern privacy governance and consent records, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Privacy Governance And Consent Records.

### Features

**Included ADRs**

- [`adr:privacy-governance-record-source-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1001-privacy-governance-record-source-policy.yaml) — Privacy Governance Record Source Policy
- [`adr:iso-29100-privacy-framework-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1002-iso-29100-privacy-framework-policy.yaml) — ISO 29100 Privacy Framework Policy
- [`adr:iso-29184-privacy-notice-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1003-iso-29184-privacy-notice-policy.yaml) — ISO 29184 Privacy Notice Policy
- [`adr:iso-27560-consent-record-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1004-iso-27560-consent-record-policy.yaml) — ISO 27560 Consent Record Policy
- [`adr:kantara-consent-receipt-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1005-kantara-consent-receipt-policy.yaml) — Kantara Consent Receipt Policy
- [`adr:dpv-processing-record-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1006-dpv-processing-record-policy.yaml) — DPV Processing Record Policy
- [`adr:privacy-audit-evidence-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1007-privacy-audit-evidence-policy.yaml) — Privacy Audit Evidence Policy
- [`adr:iso-27701-pims-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1008-iso-27701-pims-policy.yaml) — ISO 27701 PIMS Policy
- [`adr:iso-27018-cloud-pii-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1009-iso-27018-cloud-pii-policy.yaml) — ISO 27018 Cloud PII Policy
- [`adr:privacy-record-retention-policy`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/adr/ADR-1010-privacy-record-retention-policy.yaml) — Privacy Record Retention Policy

**Included SPECs**

- [`spc:iso-29100-privacy-principles-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2001-iso-29100-privacy-principles-requirements.yaml) — ISO 29100 Privacy Principles Requirements
- [`spc:iso-29100-pii-role-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2002-iso-29100-pii-role-requirements.yaml) — ISO 29100 PII Role Requirements
- [`spc:iso-29184-notice-content-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2003-iso-29184-notice-content-requirements.yaml) — ISO 29184 Notice Content Requirements
- [`spc:iso-29184-notice-presentation-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2004-iso-29184-notice-presentation-requirements.yaml) — ISO 29184 Notice Presentation Requirements
- [`spc:iso-27560-consent-record-structure-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2005-iso-27560-consent-record-structure-requirements.yaml) — ISO 27560 Consent Record Structure Requirements
- [`spc:iso-27560-consent-lifecycle-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2006-iso-27560-consent-lifecycle-requirements.yaml) — ISO 27560 Consent Lifecycle Requirements
- [`spc:kantara-consent-receipt-core-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2007-kantara-consent-receipt-core-requirements.yaml) — Kantara Consent Receipt Core Requirements
- [`spc:kantara-consent-receipt-policy-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2008-kantara-consent-receipt-policy-requirements.yaml) — Kantara Consent Receipt Policy Requirements
- [`spc:dpv-processing-purpose-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2009-dpv-processing-purpose-requirements.yaml) — DPV Processing Purpose Requirements
- [`spc:dpv-personal-data-category-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2010-dpv-personal-data-category-requirements.yaml) — DPV Personal Data Category Requirements
- [`spc:dpv-rights-risk-measure-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2011-dpv-rights-risk-measure-requirements.yaml) — DPV Rights Risk Measure Requirements
- [`spc:iso-27701-pims-evidence-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2012-iso-27701-pims-evidence-requirements.yaml) — ISO 27701 PIMS Evidence Requirements
- [`spc:iso-27018-cloud-pii-evidence-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2013-iso-27018-cloud-pii-evidence-requirements.yaml) — ISO 27018 Cloud PII Evidence Requirements
- [`spc:privacy-record-retention-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2014-privacy-record-retention-requirements.yaml) — Privacy Record Retention Requirements
- [`spc:privacy-record-export-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2015-privacy-record-export-requirements.yaml) — Privacy Record Export Requirements
- [`spc:privacy-record-evidence-linkage-requirements`](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates/specs/SPEC-2016-privacy-record-evidence-linkage-requirements.yaml) — Privacy Record Evidence Linkage Requirements

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

If the desired PyPI release is a prerelease, use its exact version in the installer command.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add privacy-governance-records-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install privacy-governance-records-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add privacy-governance-records-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from ssot_pack_privacy_governance_records import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:privacy-governance-records"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:privacy-governance-records` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/examples/usage.py).

```python
"""Resolve and read a packaged specification without synchronizing it."""

from ssot_pack_privacy_governance_records import load_document_manifest, read_packaged_document_text

spec = next(row for row in load_document_manifest("spec") if row["id"] == "spc:iso-29100-privacy-principles-requirements")
document = read_packaged_document_text("spec", spec["filename"])
assert spec["id"] in document
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `privacy-governance-records-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect ssot_pack_privacy_governance_records
uv run ssot pack preflight . ssot_pack_privacy_governance_records --all
uv run ssot pack sync . ssot_pack_privacy_governance_records --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `ssot_pack_privacy_governance_records` in SSOT Registry. Review reservation owner `extension-pack:privacy-governance-records-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

The pack owns the Privacy Governance And Consent Records ADRs and SPECs listed under Features.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `ssot_pack_privacy_governance_records` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/privacy-governance-records-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/privacy-governance-records-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/src/ssot_pack_privacy_governance_records/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/privacy-governance-records-governance-pack)
- [Issues](https://github.com/groupsum/privacy-governance-records-governance-pack/issues)
- [Repository](https://github.com/groupsum/privacy-governance-records-governance-pack)
- [pypi: privacy-governance-records-governance-pack](https://pypi.org/project/privacy-governance-records-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/privacy-governance-records-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:privacy-governance-records`. The pack's reservation owner is `extension-pack:privacy-governance-records-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [ISO/IEC 29100 Privacy Framework](https://www.iso.org/standard/85938.html)
- [ISO/IEC 29184 Online privacy notices and consent](https://www.iso.org/standard/70331.html)
- [ISO/IEC TS 27560 Consent record information structure](https://www.iso.org/standard/80392.html)
- [Kantara Consent Receipt Specification](https://kantara.atlassian.net/wiki/spaces/archive/pages/3508790/Consent%2BReceipt%2BSpecification)
- [W3C Data Privacy Vocabulary](https://www.w3.org/community/reports/dpvcg/CG-FINAL-dpv-20240801/)
- [ISO/IEC 27701 Privacy Information Management System](https://www.iso.org/standard/27701)
- [ISO/IEC 27018 Public-cloud PII protection](https://www.iso.org/standard/27018)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/privacy-governance-records-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
