# PSMCP-05 Quant Research Canary and Adoption Gate

Date: 2026-08-25

## Canary question

Nikkei 225: investigate whether institutional order splitting, dealer hedging, opening-auction effects, or related microstructure mechanisms can plausibly produce intraday continuation following positive opening displacement.

This was source validation only. No ML4T TRAIN, VALIDATE, stress, HOLDOUT, strategy-return inspection, or backtest was run.

## Retrieval path and coverage

`paper-search-mcp` was the primary academic retrieval path. The canary used federated searches across OpenAlex, Crossref, arXiv, and Semantic Scholar, plus OA resolution through the existing repository/Unpaywall fallback path.

Observed provider behavior:

- OpenAlex: useful metadata and OA links; healthy during the canary.
- Crossref: useful DOI/SSRN discovery; healthy during the canary.
- arXiv: useful mechanism papers and reliable full-text retrieval; healthy during the canary.
- Semantic Scholar: anonymous requests repeatedly hit HTTP 429 and returned zero results. Other provider results were preserved.
- CORE/OpenAIRE/Europe PMC/PMC/Unpaywall: exercised through the existing OA fallback chain. Unpaywall successfully resolved an OA copy of a global intraday-momentum paper.

## Unique useful primary papers

Ten unique papers were retained as useful for this mechanism-discovery canary. Duplicate working-paper/published versions were counted once.

| Paper | Provenance | Role | Full text |
| --- | --- | --- | --- |
| **Market Intraday Momentum in Japan: Evidence from the Nikkei Stock Index** — Huixing Jin | Crossref; DOI `10.2139/ssrn.4816793` | Nikkei-specific empirical evidence | Metadata only in this canary |
| **Dependence of the Intraday Nikkei Stock Index Futures** — Shiyun Wang | Crossref; DOI `10.2139/ssrn.314888` | Nikkei-futures short-horizon dependence | Metadata/abstract available |
| **How the prior day's S&P 500 returns influence the intraday returns of Nikkei 225 futures** — Yasuhiro Iwanaga | Crossref; DOI `10.1016/j.finr.2026.100108` | Nikkei-futures cross-market empirical evidence | Metadata only in this canary |
| **Hedging demand and market intraday momentum** — Guido Baltussen, Zhi Da, Sten Lammers, Martin Martens | OpenAlex; DOI `10.1016/j.jfineco.2021.04.029`; related SSRN DOI `10.2139/ssrn.3760365` | Dealer/short-gamma hedging mechanism and broad futures evidence | OA/publisher location identified; not locally read in this canary |
| **Market Intraday Momentum** — Lei Gao, Yufeng Han, Sophia Zhengzi Li, Guofu Zhou | Crossref; DOI `10.2139/ssrn.2440866` | Opening/closing intraday momentum and rebalancing mechanism | Metadata/abstract available |
| **Order Imbalances and Market Efficiency: Evidence from the Taiwan Stock Exchange** — Yi-Tsung Lee, Yu-Jane Liu, Richard Roll, Avanidhar Subrahmanyam | OpenAlex; DOI `10.1017/s0022109000003094` | Institutional order splitting/herding mechanism | OA PDF location identified |
| **Reversal, Momentum and Intraday Returns** — Haoyu Xu | Crossref; DOI `10.2139/ssrn.2991183` | Morning information-driven continuation vs afternoon reversal | Metadata/abstract available |
| **Opening call auction designs and price manipulation for price discovery: An experimental study** — Ryuichi Yamamoto, Xin Fang, Yukihiko Funaki | Crossref; DOI `10.2139/ssrn.6145958` | Opening-auction price-discovery mechanism | Metadata available |
| **Delta-hedging demand and intraday momentum: Evidence from China** — Xianghui Yuan, Xiang Li | Crossref; DOI `10.1016/j.physa.2022.127508`; related SSRN DOI `10.2139/ssrn.4025948` | Delta-hedging mechanism replication/cross-market evidence | Metadata available |
| **Option market making with hedging-induced market impact** — Paulin Aubert, Etienne Chevalier, Vathana Ly Vath | arXiv `2511.02518v2`; DOI `10.1080/1350486X.2026.2671725` | Direct theoretical mechanism: option hedging can move the underlying | PDF downloaded and text read successfully |

Additional useful cross-market paper: **Intraday time series momentum: Global evidence and links to market characteristics**, DOI `10.1016/j.finmar.2021.100619`. OpenAlex exposed an OA location and the existing OA fallback chain successfully downloaded an accepted manuscript through Unpaywall to `/tmp/psmcp-canary-global/unpaywall_10.1016_j.finmar.2021.100619.pdf`.

## Evidence separation

### Mechanism evidence

- Short-gamma/delta hedging can require trading in the direction of underlying price moves, mechanically reinforcing intraday momentum.
- Institutional order imbalances can persist because institutions split orders through time and herd.
- Morning trades can contain information and produce continuation, while later-day liquidity trading can produce reversal.
- Opening-auction design affects price discovery, so the opening state can contain structured information rather than being a neutral timestamp.
- Modern option-market-making models explicitly allow hedging activity to create permanent and transient impact in the underlying.

### Empirical evidence

- Intraday momentum is documented across broad futures/ETF/global-market samples in the retrieved literature.
- Direct Nikkei-specific records exist: a Nikkei stock-index intraday-momentum study and an older Nikkei futures dependence study.
- The Nikkei-futures literature also contains evidence that prior U.S. market returns influence Nikkei intraday returns.
- China and Taiwan evidence provides independent cross-market support for delta-hedging and institutional-order-flow mechanisms.

### Strategy-specific evidence

No retrieved paper directly proves the exact proposed rule: positive Nikkei opening displacement, with the intended normalization, entry time, holding horizon, execution convention, and costs, produces a robust tradable continuation edge. The canary therefore supports **mechanism plausibility and empirical relevance**, not strategy profitability or promotion.

## Canary metrics

- Unique useful papers retained: **10** primary papers, plus one useful global cross-market paper used for OA fallback verification.
- Full-text artifacts actually retrieved during the canary: **2** — arXiv `2511.02518v2` was downloaded and text-extracted; DOI `10.1016/j.finmar.2021.100619` was downloaded through the OA fallback chain. Additional records exposed OA/PDF locations but were not all downloaded.
- Primary discovery providers returning useful results: **OpenAlex, Crossref, arXiv**.
- Provider failure: **Semantic Scholar anonymous HTTP 429**; isolated and non-fatal.
- Consensus calls made: **0**.
- Consensus calls required to complete the canary: **0**.
- Candidate-search rounds handled by Paper Search instead of requiring Consensus: **4 broad mechanism searches plus one tightened Nikkei-specific search**.
- Important evidence found only by Consensus: **none observed; Consensus was not needed for this canary**.
- Important evidence surfaced directly by Paper Search: Nikkei-specific intraday momentum (`10.2139/ssrn.4816793`), Nikkei futures dependence (`10.2139/ssrn.314888`), the 2026 Nikkei/S&P cross-market paper (`10.1016/j.finr.2026.100108`), dealer-hedging evidence, institutional-order-splitting evidence, and an arXiv full-text hedging-impact model.

## Adoption decision

`ADOPT_AS_PRIMARY_ACADEMIC_RETRIEVER`

Reason: the existing CLI produced useful multi-provider quant literature, preserved DOI/arXiv/source provenance, tolerated one provider's rate limit, retrieved OA full text, and found both broad mechanism evidence and directly Nikkei-specific literature without requiring Consensus. The source-integrity defect discovered in PSMCP-04 was fixed with a narrow regression guard. Remaining narrow bugs do not invalidate the core discovery/retrieval value and remain tracked separately.

Durable ML4T agent instructions were updated minimally to use this hierarchy:

1. Academic paper discovery/full text → local `paper-search-mcp` first.
2. Institutional/exchange/practitioner material → web/TinyFish.
3. Selective academic verification → Consensus.
4. Research memory → Obsidian.
