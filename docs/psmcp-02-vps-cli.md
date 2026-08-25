# PSMCP-02 VPS CLI Verification

Verified on 2026-08-25 using the fork's existing `paper-search` command surface.

## Installation and configuration

- Installed directly from the fork checkout with `uv tool install --force /home/quant/dev/mcp/paper-search-mcp`.
- No launcher, wrapper, daemon, proxy, HTTP transport, or alternate interface was added.
- Optional configuration used the supported environment-variable mechanism outside Git.
- `PAPER_SEARCH_MCP_UNPAYWALL_EMAIL` was supplied as a shell environment variable for the verification commands.
- CORE and Semantic Scholar keys were intentionally left unset to prove the free-first path.
- Google Scholar proxy, Sci-Hub, IEEE, and ACM were not required.

## Fresh-shell / working-directory independence

Commands were run from `/tmp`, not from the repository.

`paper-search sources` succeeded and exposed the installed free-first providers, including arXiv, OpenAlex, Crossref, Semantic Scholar, CORE, OpenAIRE, Zenodo, HAL, SSRN, and Unpaywall.

Representative federated search:

```text
paper-search search "intraday momentum futures" -s arxiv,openalex,crossref,semantic -n 3
```

Result:

- arXiv: 3 results
- OpenAlex: 3 results
- Crossref: 3 results
- Semantic Scholar: 0 results after anonymous HTTP 429 rate limiting
- Total deduplicated results: 9
- Command exit: success; one provider's rate limit did not discard other provider results.

## Download and read

Verified against arXiv identifier `2605.17724v1`:

```text
paper-search download arxiv 2605.17724v1 -o /tmp/psmcp-downloads
paper-search read arxiv 2605.17724v1 -o /tmp/psmcp-downloads
```

Download returned `status=ok` with `/tmp/psmcp-downloads/2605.17724v1.pdf`.
Text extraction returned the paper title and body text, beginning with `Sequential Structure in Intraday Futures Data: LSTM vs Gradient Boosting on MNQ`.

PSMCP-02 required no production-code changes.
