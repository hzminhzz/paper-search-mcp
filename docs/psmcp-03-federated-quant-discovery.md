# PSMCP-03 Federated Quant-Paper Discovery

Verified on 2026-08-25 with the existing concurrent CLI search and deduplication path.

Providers exercised for every canary: `arxiv,openalex,crossref,semantic`, with `max_results=3` per provider.

## Canary results

| Query | arXiv | OpenAlex | Crossref | Semantic Scholar | Raw | Unique | Duplicates collapsed | Relevant raw | 429/errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `intraday momentum futures` | 3 | 3 | 3 | 0 | 9 | 9 | 0 | 7 | Semantic Scholar anonymous HTTP 429 |
| `dealer gamma hedging index futures` | 3 | 3 | 3 | 0 | 9 | 9 | 0 | 4 | Semantic Scholar anonymous HTTP 429 |
| `foreign exchange macro announcement momentum` | 3 | 3 | 3 | 0 | 9 | 9 | 0 | 4 | Semantic Scholar anonymous HTTP 429 |
| `limit order book adverse selection market making` | 3 | 3 | 3 | 0 | 9 | 8 | 1 | 6 raw / 5 unique | Semantic Scholar anonymous HTTP 429 |

`Relevant` is a conservative manual title/abstract screen for direct usefulness to the query, not a performance metric.

## Useful examples and provenance

The search output preserved provider, paper identifier, DOI when available, title, authors, and publication date/year. Examples:

- OpenAlex — `W3033849955`, **Intraday momentum in Chinese commodity futures markets**, DOI `10.1016/j.ribaf.2020.101278`, Zhang We / Pengfei Wang / Yi Li, 2020.
- OpenAlex — `W2972876854`, **Does intraday time-series momentum exist in Chinese stock index futures market?**, DOI `10.1016/j.frl.2019.09.007`, Yi Li / Dehua Shen / Pengfei Wang / Wei Zhang, 2019.
- OpenAlex — `W3106590193`, **Hedging demand and market intraday momentum**, DOI `10.1016/j.jfineco.2021.04.029`, Guido Baltussen / Zhi Da / Sten Lammers / Martin Martens, 2021.
- OpenAlex — `W3124772813`, **Micro Effects of Macro Announcements: Real-Time Price Discovery in Foreign Exchange**, DOI `10.3386/w8959`, Torben M. Andersen / Tim Bollerslev / Francis X. Diebold / Clara Vega, 2002.
- OpenAlex — `W2000903314`, **Adverse Selection and Competitive Market Making: Empirical Evidence from a Limit Order Market**, DOI `10.1093/rfs/14.3.705`, Patrik Sandås, 2001.
- Crossref — DOI `10.2139/ssrn.675769`, **Liquidity Supply and Adverse Selection in a Pure Limit Order Book Market**, Stefan Frey / Joachim Grammig, 2005.
- arXiv — `2510.27334v1`, **When AI Trading Agents Compete: Adverse Selection of Meta-Orders by Reinforcement Learning-Based Market Making**, Ali Raza Jafree / Konark Jain / Nick Firoozye, 2025.

## Deduplication and failure isolation

For the LOB query the providers returned 9 raw records and the existing CLI emitted 8 unique records, demonstrating that the current deduplication path collapsed one duplicate.

Semantic Scholar's anonymous connector encountered HTTP 429 on every canary. It retried and returned zero results; the federated command still returned successful arXiv/OpenAlex/Crossref results. The JSON `errors` map remained empty because the connector handles the rate limit internally and degrades to an empty result set.

This is classified as `UPSTREAM_PROVIDER_BLOCKED` for anonymous Semantic Scholar access, not a software defect. No provider-orchestration code was changed.
