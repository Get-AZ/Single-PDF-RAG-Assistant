# Single PDF RAG Assistant Technical Report

## Objective

Make a PDF searchable through natural-language questions while showing the evidence
used to answer. The implementation is an educational document assistant and a
portfolio demonstration of retrieval debugging, rather than a production service.

## Implementation decisions

Streamlit provides file upload, question entry and evidence inspection. pypdf keeps
page metadata during extraction. Fixed word windows are easy to explain and debug;
120 words with 25 overlap balances short passages and continuity, although token
length varies. MiniLM produces compact 384-dimensional sentence embeddings locally.
FAISS stores normalized vectors in an exact inner-product index. Exact search suits
a small document and avoids approximate-search tuning.

The Google SDK calls Gemini Flash-Lite directly for generation. This path followed
successful local testing after another Gemini configuration repeatedly timed out.
Because both client and model changed, the original timeout cannot be attributed
to either factor alone. Google embedding requests later exhausted a reported daily
free-tier limit; replacing embeddings with MiniLM removed that external embedding
quota dependency. Generation still depends on Google's service and quota.

## Retrieval investigation

A baseline answered 11 of 12 questions in the single-PDF development test. The
hardware-and-schedule question produced a false abstention. A DEBUG view of the
actual prompt revealed passages from pages 5, 8 and 9 but not page 7, which contains
the eight P100 GPUs and base-model schedule. This established missing evidence at
retrieval time, rather than proving a language-model reasoning failure.

Neighbor expansion alone could not recover a page with no selected seed chunk.
Adding keyword candidates weighted by term rarity brought distinctive hardware
and schedule wording into the candidate set. Combining candidates and expanding
same-page neighbors recovered the relevant evidence. The developer supplied a
correct Q7 answer and subsequently reported that all 12 questions passed.

## Evaluation interpretation

The baseline was manually reviewed from shared responses. The final 12/12 is a
self-reported retest aggregate, not an independent benchmark execution. The same
questions informed system tuning; therefore the final figure describes regression
performance. No confidence interval or generalization claim is justified by this
small, selected test. No user study or production adoption was measured.

## Limitations

Research papers with columns, tables and formulas can be extracted incorrectly.
Small word windows can still exceed MiniLM's token limit for technical text.
Keyword ranking is not semantic reasoning and can overemphasize exact words.
Document-order context can bury strong evidence among many expanded chunks.
Prompts reduce but do not eliminate unsupported claims or prompt injection risks.
Missing-answer tests need a clear distinction between absence from supplied context
and absence from the full document. Source citations need manual validation.

## Next experiments

Freeze source, dependency versions and model revision. Evaluate new questions on
a different PDF without tuning to them. Log retrieved chunk IDs, page coverage,
answer text, elapsed time, model ID and prompt version. Compare semantic-only,
keyword-only and hybrid methods with the same context budget. Consider BM25 or
rank fusion, a reranker, token-aware chunking, OCR, and bounded neighbor expansion.
Add authentication and data isolation before offering a shared hosted service.
