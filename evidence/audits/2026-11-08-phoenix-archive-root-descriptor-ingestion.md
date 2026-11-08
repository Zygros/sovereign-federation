# Phoenix Archive-Root Descriptor-Bound Ingestion

**Recorded:** 2026-11-08  
**Source PR:** [CONZETIAN-UNIFIED-INTELLIGANCE #17](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/pull/17)  
**Superseded proposal:** [CONZETIAN-UNIFIED-INTELLIGANCE #2](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/pull/2), left unchanged because its branch remains non-mergeable  
**Scope:** Preserved \`ZYGROS-PRIME/Downloaded/phoenix_node_genesis.py\` snapshot  
**State:** Clean current-main branch, draft PR, all final-head checks passed, unmerged.

## 1. Implementation

The new branch \`security/archive-root-descriptor-read-2026-11-08\` was created from current \`main\` commit \`e4e378e4b6d76d7ed9f1726fd2a50a923f08707f\`.

The preserved Phoenix node snapshot now:

- Accepts optional \`ARCHIVE_ROOT\`; if absent or invalid, path-based ingestion is disabled.
- Canonicalizes paths and enforces \`realpath\` + \`commonpath\` containment.
- Rejects group/world-writable archive roots, descendant directories, and files.
- Revalidates both requested paths and discovered files in \`walk_paths\`.
- Opens an accepted file once, checks regular-file status and descriptor/path device+inode identity, and reads bytes through that descriptor.
- Revalidates the path after the read and compares file identity, size, mtime, and ctime before/after reading.
- Passes the already-read bytes to PDF/DOCX parsers through \`io.BytesIO\`, avoiding a second pathname open.
- Treats a single string/path argument as one path rather than iterating its characters.
- Adds \`archive_root\` and \`path_ingestion_enabled\` to the authenticated status response.

The existing Flask/ChromaDB structure and API-key security checks were preserved. The new \`ARCHIVE_ROOT\` gate is limited to path-based ingestion.

## 2. Final-head verification

Source head: \`84f883237dc98b700f6aa0b14e8af05361329b6e\`  
Base: \`e4e378e4b6d76d7ed9f1726fd2a50a923f08707f\`  
Tested pull-request merge commit: \`2d32634e30d436b436f17514bcb681593e865f4d\`

- [Phoenix Archive Root Descriptor Tests #42522100248](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42522100248): **7/7 unittest methods passed** on Python 3.11.18. Coverage includes valid read, outside/traversal/symlink rejection, writable root/nested/file rejection, path replacement after open, symlink swap after open, missing-root behavior, and single-string path handling.
- [Phoenix Audit #42522100286](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42522100286): **20 pytest tests and 3 subtests passed**; source-discovery checks passed.
- [Conzetian Contract Verification #42522100261](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42522100261): passed.
- [Phoenix API Key Policy #42522100249](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42522100249): passed.

The tests extract the path/reader helpers from the source AST and use temporary filesystem fixtures. They do not import Flask or ChromaDB, start a server, contact a database, or access production credentials.

## 3. Reproducible evidence artifact

[Phoenix archive-root descriptor evidence artifact 13633916996](https://github.com/Zygros/CONZETIAN-UNIFIED-INTELLIGANCE/actions/runs/42522100248/artifacts/13633916996)

- ZIP size: 1,576 bytes.
- GitHub-reported ZIP SHA-256: \`07305d12e36050ed4178c0e62d05805b33e81d10a079b2e3d5661e471be17639\`.
- Independent download recalculation: exact match.
- Internal SHA-256 manifest: all listed file digests matched the extracted files.
- Receipt binds source head, tested merge commit, base commit, Python 3.11.18, seven test methods, and source/test/docs/workflow hashes.
- GitHub retention: 90 days, expiring 2027-02-06.

## 4. Promotion and runtime boundary

PR #17 is **open, draft, mergeable, and unmerged**. The default branch was not modified. The older PR #2 remains open and non-mergeable; it was not force-updated or merged.

The target file is under the preserved \`Downloaded/\` archive. These checks establish the proposed source behavior, not that this file is an active or deployed service. No Flask/ChromaDB server was started, no production API was contacted, and no Android/Termux files or permissions were changed. The descriptor-bound read narrows pathname replacement exposure but does not sandbox the application process.
