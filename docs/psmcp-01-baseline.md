# PSMCP-01 Fork Baseline

Baseline verified on 2026-08-25 before fork-specific production changes.

- Fork: `hzminhzz/paper-search-mcp`
- Origin: `https://github.com/hzminhzz/paper-search-mcp.git`
- Upstream: `https://github.com/openags/paper-search-mcp.git`
- Baseline HEAD: `234678ab231074a7977320978ee0496dcdaddd1f`
- `origin/main`: `234678ab231074a7977320978ee0496dcdaddd1f`
- `upstream/main`: `234678ab231074a7977320978ee0496dcdaddd1f`
- `uv sync`: PASS

## Untouched upstream test baseline

Command:

```text
uv run --extra dev pytest -q
```

Result:

```text
115 passed, 11 skipped, 1 failed, 1 error
```

Observed non-green cases:

1. `tests/test_biorxiv.py::TestBioRxivSearcher::test_download_and_read`
   - External bioRxiv PDF request returned HTTP 429 after retries.
   - Classified as upstream/provider behavior for this baseline; no production change made.
2. `tests/functional_test.py::test_platform`
   - Pytest collection treats helper `test_platform(name, fn, optional=False)` as a test and cannot resolve fixture `name`.
   - Pre-existing baseline test-layout defect; no production change made in PSMCP-01.

PSMCP-01 introduces no production-code behavior change, wrapper, transport, registry, service, or orchestration layer.
