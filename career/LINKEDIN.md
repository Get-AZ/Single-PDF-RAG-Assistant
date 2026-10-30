# LinkedIn Publication Pack

## Ready to post

I built a PDF question-answering assistant with Streamlit, local MiniLM embeddings,
FAISS and Gemini Flash-Lite.

The most useful lesson came from an answer the system could not find. The paper
stated the base Transformer's training hardware and schedule, but semantic retrieval
missed the relevant page. Inspecting the exact prompt showed that the model had
never received the evidence.

I added keyword retrieval alongside semantic search and expanded neighboring chunks.
The system then recovered the missing passage and answered with a page citation.
The initial manually reviewed test passed 11 of 12 questions. My full retest after
the retrieval change passed all 12, including three missing-information questions.
This is a small development/regression set on one PDF, not a general accuracy claim.

The app also saves its FAISS index and runs embeddings locally, avoiding repeated
cloud embedding calls. Gemini is used for answer generation, and retrieved evidence
is visible for review.

Source and technical documentation: https://github.com/Get-AZ/Single-PDF-RAG-Assistant
Portfolio: https://getamesay-ml-cloud-ai.getgad-uss.chatgpt.site

#RAG #GenerativeAI #Python #Streamlit #FAISS

## Project section

Name: Single PDF RAG Assistant
Date: October 2026
Role: Independent developer
Skills: Python; Retrieval Augmented Generation; Sentence Transformers; FAISS; Streamlit
URL: https://github.com/Get-AZ/Single-PDF-RAG-Assistant

Description: Built a single-PDF assistant with local MiniLM embeddings, persistent
FAISS indexing, hybrid semantic and keyword retrieval, neighbor expansion and
Gemini answers with page citations. Diagnosed a missing-evidence failure by inspecting
the exact prompt. A 12-question development test improved from 11/12 reviewed passes
to 12/12 in my reported retest; unseen-document performance remains unmeasured.

## Featured section

Title: Single PDF RAG Assistant with Evidence Based Answers
Description: Code, architecture, evaluation boundaries and a retrieval-debugging
case study using MiniLM, FAISS, Streamlit and Gemini Flash-Lite.
Link: https://github.com/Get-AZ/Single-PDF-RAG-Assistant

## Publishing notes

This file is publication copy, not proof of posting. Add the project URL as a
Featured link and use the attached project card as an optional cover illustration.
The card is a diagram, not a screenshot of the running app. A live app endpoint
has not been deployed. Avoid describing the 12-question result as general accuracy.
