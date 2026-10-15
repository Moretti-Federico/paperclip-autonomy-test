# TextKit roadmap

Owner authorization of Phase F and a Board-created Paperclip kickoff are prerequisites to starting these tasks. Codex reads this roadmap, creates one implementation issue at a time and supplies the native policy: GLM executor, Claude review, Codex approval, maxReviewRounds=2. Codex must omit responsibleUserId from agent-created issue payloads and verify inheritance from the kickoff run.

## T1 — Normalize whitespace

- [ ] Implement `textkit.normalize_whitespace(text: str) -> str`.
- Leading and trailing whitespace is removed; every consecutive sequence of Unicode whitespace becomes one ASCII space.
- Empty and whitespace-only strings return an empty string. Punctuation and letter case are preserved.
- Add tests for empty input, tabs/newlines, repeated spaces and Unicode whitespace.
- Acceptance: CI passes; the PR contains implementation and meaningful tests; independent review and native approval complete before merge.

## T2 — Generate deterministic slugs

- [ ] Implement `textkit.slugify(text: str) -> str`, reusing the normalization from T1 where appropriate.
- Use only the standard library. Convert accented Latin letters to their ASCII equivalents, lowercase the result, replace runs of non-ASCII-alphanumeric characters with one hyphen and strip leading/trailing hyphens.
- Empty or punctuation-only input returns an empty string.
- Add tests for accents, case, punctuation, repeated separators and empty input. Preserve T1 behavior.
- Acceptance: all tests and required CI pass; native Claude review and Codex approval complete before merge.

## T3 — Summarize text using the implemented utilities

- [ ] Implement `textkit.summarize_text(text: str) -> dict`, returning exactly `normalized`, `slug` and `word_count`.
- `normalized` equals `normalize_whitespace(text)`; `slug` equals `slugify(text)`; `word_count` is the number of space-delimited words in the normalized text, or zero for empty text.
- Reuse the existing functions and add end-to-end tests, including multiline input and accents. Update README with working examples.
- Acceptance: all regression and integration tests pass; CI is green; independent review is complete; Codex merges, closes the issue and records roadmap completion.
