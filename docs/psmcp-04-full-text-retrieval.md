# PSMCP-04 Paper-to-Full-Text Verification

Verified on 2026-08-25 using existing source-native retrieval plus the existing OA fallback components.

## Successful full-text retrieval

### arXiv

Identifier: `2605.17724v1`

- `paper-search download arxiv 2605.17724v1` returned a real PDF.
- `paper-search read arxiv 2605.17724v1` extracted readable text beginning with **Sequential Structure in Intraday Futures Data: LSTM vs Gradient Boosting on MNQ**.

### Non-arXiv OA

IACR identifier: `2026/1628`

- `paper-search download iacr 2026/1628` returned `/tmp/psmcp-downloads/iacr_2026_1628.pdf`.
- `paper-search read iacr 2026/1628` extracted page-level text for **Lattice-based Signature Schemes for Bitcoin**.
- Extracted text includes title, authors, publication date, abstract, and body text sufficient for source-grounded LLM analysis.

## OA fallback evidence

Unpaywall was exercised with the configured email against DOI `10.1111/jofi.12186` and resolved the OA PDF URL:

```text
http://www.federalreserve.gov/pubs/ifdp/2009/980/ifdp980.pdf
```

A fabricated DOI `10.0000/not-a-real-doi` resolved to `None`, not fabricated content.

Attempting direct `paper-search download unpaywall ...` returns an explicit error explaining that Unpaywall is metadata/OA-location only and that the returned URL must be used through fallback/source-native retrieval.

## Failure semantics and defects discovered

Three narrow defects were discovered and split into dedicated bug issues:

- #6 — HAL and Zenodo CLI search serialization fails on string-valued dates.
- #7 — arXiv download can report success for an invalid identifier/non-PDF response.
- #8 — repository fallback could accept an unrelated search hit solely because it exposed a `pdf_url`.

#8 was source-integrity critical and practical to repair immediately. `_try_repository_fallback` now requires the candidate DOI or normalized title to match the requested paper before accepting its PDF URL. A regression test proves unrelated repository hits are never downloaded. Existing numeric-paper-id fallback regression coverage remains intact.

Targeted verification:

```text
uv run --extra dev pytest tests/test_fallback.py -q
5 passed
```

No generic retry, caching, retrieval framework, or new orchestration abstraction was added.
