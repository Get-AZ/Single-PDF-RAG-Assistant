# Single PDF RAG Assistant

## Overview

A document assistant that lets a user upload one PDF, ask a question and inspect
page-linked evidence. Local MiniLM embeddings and a persistent FAISS index support
retrieval; Gemini Flash-Lite generates the answer from the selected passages.

## Engineering challenge

A hardware-and-training question failed even though the answer appeared in the PDF.
The exact prompt revealed that semantic retrieval selected other pages and omitted
the hardware section. Increasing context and changing wording did not consistently
recover it. The fix combined term-rarity-weighted keyword candidates with semantic
candidates, then included same-page neighbors.

## Outcome

Baseline: 11/12 manually reviewed questions passed. After the retrieval change,
the developer reported 12/12 on the same one-PDF development/regression set,
including all three missing-information tests. The final Q7 answer was shared;
the complete final transcript and final local source were not supplied for
independent reproduction. This is not a production or generalization benchmark.

## My contributions

PDF extraction and chunking; normalized local embeddings; persistent vector storage;
hybrid retrieval and deduplication; prompt construction; API integration; evidence
inspection; manual evaluation; documented failure analysis.

## Technology

Python, Streamlit, pypdf, Sentence Transformers, all-MiniLM-L6-v2, NumPy, FAISS,
Google Gen AI SDK and Gemini Flash-Lite.

## Status and next steps

Local application with a documented release candidate. No hosted inference service.
Next: exact-source retest, unseen-PDF questions, bounded context/reranking and stronger
citation checks.

## Links

Source and documentation: https://github.com/Get-AZ/Single-PDF-RAG-Assistant
Professional portfolio: https://getamesay-ml-cloud-ai.getgad-uss.chatgpt.site
