# Detailed CV Project Entry

## Single PDF RAG Assistant

Getamesay Zegeye | Independent AI portfolio project | October 2026

### Project objective

Developed a local document-question-answering application that retrieves evidence
from an uploaded PDF and generates answers with page citations. Designed the
workflow to support inspection of the source passages behind each response.

### Implementation contributions

- Implemented a single-file Streamlit interface with processing status, question entry,
  answer display and expandable source evidence.
- Extracted text page by page and applied 120-word windows with 25-word overlap.
- Generated normalized 384-dimensional MiniLM embeddings locally on CPU and stored
  vectors in FAISS IndexFlatIP with JSON metadata.
- Added content-and-settings cache keys so unchanged PDFs reuse saved indexes.
- Combined semantic candidates and term-rarity-weighted keyword candidates, expanded
  same-page neighbors and removed duplicate chunks before generation.
- Integrated Gemini Flash-Lite through Google's SDK with a request timeout and one
  attempt, while separating local retrieval from external answer generation.

### Evaluation and problem solving

- Reviewed direct-answer, synthesis and missing-information questions on the
  Transformer paper; baseline passed 11 of 12 questions.
- Inspected the exact generation prompt to establish that a failed hardware question
  lacked page 7 evidence, avoiding an unsupported diagnosis of model reasoning failure.
- Recovered the missing evidence using hybrid retrieval; the developer's full retest
  reported 12 of 12 passes on the same development/regression set.
- Separated source citations, answer completeness, unsupported additions and
  appropriate abstention in manual review.
- Replaced cloud embeddings after a quota interruption; local embeddings remove that
  quota dependency while retaining the external generation API.

### Scope and transferable skills

Applied information retrieval, NLP embeddings, data preprocessing, API integration,
cache design, evaluation design and failure analysis. Local educational application;
no production-scale service, unseen-document benchmark or measured business impact
is claimed. The packaged source is reconstructed from recorded changes and requires
an exact-source acceptance retest before an evaluated release is tagged.

### Links

GitHub project: https://github.com/Get-AZ/Single-PDF-RAG-Assistant
Portfolio: https://getamesay-ml-cloud-ai.getgad-uss.chatgpt.site
