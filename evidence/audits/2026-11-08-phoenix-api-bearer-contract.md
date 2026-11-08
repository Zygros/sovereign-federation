# Phoenix API Bearer-Token Contract for Preserved Archive Copies

**Recorded:** 2026-11-08  
**Source PR:** [CONZETIAN-UNIFIED-INTELLIGANCE #1](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/pull/1)  
**Scope:** Two preserved \`ZYGROS-PRIME/Downloaded/\` Phoenix API source snapshots  
**State:** Test and evidence additions are on the open PR branch; the PR remains unmerged.

## 1. Implementation under review

The PR branch \`fix/aikido-security-code-audit-97973653-bqra\` removes the hardcoded bearer-token fallback from both archived API copies:

- \`source-repositories/ZYGROS-PRIME/Downloaded/phoenix_api.py\`
- \`source-repositories/ZYGROS-PRIME/Downloaded/phoenix_api-1.py\`

The branch now contains:

- \`API_SECRET = os.getenv("API_SECRET")\` with no default credential.
- A fail-closed startup guard that prints a fatal configuration message and exits with status 1 when the secret is missing or empty.
- \`secrets.compare_digest()\` for bearer-token comparison instead of ordinary string equality.

The two archived copies are byte-identical on the PR branch.

## 2. Verification added and executed

A new AST-based contract suite and a dedicated GitHub Actions workflow were added. The tests do not import or start FastAPI; they execute only the extracted startup-gate AST nodes and verifier function with controlled fixtures.

Final PR-head checks:

- [Phoenix API Bearer Token Contract Tests #42521467851](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42521467851): **3/3 unittest methods passed** on Python 3.11.18. The tests check both source copies, missing/empty secret startup exit, configured-secret startup, and constant-time verifier behavior including 401 rejection.
- [Phoenix Audit #42521467889](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42521467889): **16 pytest tests and 7 subtests passed**; compilation and credential-pattern scan passed.
- [Conzetian Contract Verification #42521467842](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGIANCE/actions/runs/42521467842): **2 tests passed**.
- [Phoenix API Key Policy #42521467934](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42521467934): passed.

### Reproducible artifact

[Phoenix API bearer contract artifact 13633577075](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42521465734/artifacts/13633577075)

- ZIP size: 1,587 bytes.
- GitHub-reported ZIP SHA-256: \`3ef80ed1c2ca5b06224fda3d2daa0444a453900ef232c064d2311901a18b3357\`.
- Independent download recalculation: exact match.
- Internal SHA-256 manifest: both listed file digests matched the extracted files.
- Receipt: three unittest methods passed; two archive copies recorded; Python 3.11.18; source and tested commit \`6fff7cb9650c0c8aae0fc52402fea81d1774669c\`.
- GitHub retention: 90 days, expiring 2027-02-06.

## 3. Promotion and runtime boundary

PR #1 is **open, non-draft, mergeable, and unmerged**. The current default branch still contains the old \`API_SECRET = os.getenv("API_SECRET", "phoenix-api-secret")\` fallback in both archived files because the PR has not been merged. The change is therefore not yet present on the default branch.

These files are under the preserved \`Downloaded/\` archive. The passing tests establish the source-level contract of the PR branch only. They do not establish that either file is an active deployed service, that a production API was started, or that any real credential was read, rotated, or revoked. The test secret is a fixture. No production service, external API, or credential provider was contacted.
