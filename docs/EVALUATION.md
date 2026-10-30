# Evaluation

## Scope and results

The development set uses one PDF, Attention Is All You Need, and 12 questions:
seven direct, two synthesis and three missing-information questions. A pass requires
a correct and sufficiently complete answer, no material unsupported additions,
and accurate supporting page citations where an answer is available. Missing-answer
questions pass when the model avoids inventing the requested fact.

Baseline: 11/12 (91.7%) from manually reviewed shared answers. Q7 failed.
Final hybrid retrieval: 12/12 (100%) reported by the developer after a full retest.
The final Q7 answer was supplied and reviewed; the full final transcript was not.
Do not describe the reported aggregate as independently certified or general accuracy.

## Reproduce against this release candidate

1. Install and run the app; record exact package versions and source commit.
2. Upload your copy of Attention Is All You Need; record its SHA-256 and page count.
3. Record embedding model revision, generation model ID, prompt and retrieval k.
4. Ask each original question from evaluation/questions.csv without paraphrasing.
5. Save actual answers, final retrieved chunks/pages, and per-question elapsed time.
6. Grade completeness, factual support and page-citation correctness separately.
7. Repeat on an unseen PDF and new questions before making generalization claims.

The repo CSV is a question/expected-answer fixture, not an automatically executed
benchmark. The summary contains reported counts; it does not manufacture raw final
outputs. The source was reconstructed from the starter plus recorded patches and
needs an exact-source retest before attaching the reported evaluation to a release tag.

## Observed issues

Q7 demonstrated missing page coverage. Earlier outputs also produced malformed
mathematics, irrelevant extra benchmark claims and wrong page references. The
original PDF itself has inconsistent English-French BLEU values between prose
and Table 2; those should be flagged rather than silently reconciled.

## Next evaluation

Hold k and context budget constant across methods, track retrieval evidence coverage
on the nine answerable questions, and record appropriate-abstention rate on the three
missing questions. Do not compute retrieval hit rate from citations alone. Larger
context sets may improve recall while increasing latency, cost and distraction.
