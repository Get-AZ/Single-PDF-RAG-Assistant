# Q7 Retrieval Diagnostic

Original question: What hardware and training schedule were used for the base Transformer?

Expected answer: 8 NVIDIA P100 GPUs, 100,000 steps, approximately 12 hours (PDF page 7).

Observed failure: the model said the information was missing. Inspecting the actual
prompt showed passages from pages 5, 8 and 9, with no page 7. This is direct evidence
of missing retrieval coverage for this request.

After semantic-plus-keyword candidates and neighbor expansion, the developer shared:

> The base models were trained on one machine with 8 NVIDIA P100 GPUs for a total
> of 100,000 steps or 12 hours (Passage 5, page 7; Passage 6, page 7).

This individual retest passes the content rubric. The developer then reported all
12 passed. Complete final answer logs and final local source were not supplied;
the reported aggregate is preserved separately from independently executed checks.
