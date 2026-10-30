# Setup and Troubleshooting

Use README.md for the Python 3.12 Windows commands. In VS Code select the .venv
interpreter. Start with python -m streamlit run app.py, not python app.py.

- Missing module: install requirements through the same .venv Python executable.
- PowerShell blocks activation: use .venv\Scripts\python.exe directly; activation is optional.
- First run is slow: MiniLM downloads weights; later calls reuse the local model cache.
- 429 from generation: inspect the API error and current quota; do not retry in a tight loop.
  Embeddings are local in this version, so old Google embedding errors suggest an old app.
- 504: the service did not complete in time; retry later or verify model availability.
  Increasing timeouts is not a guarantee of completion.
- No text: scanned files need OCR; encrypted or damaged PDFs may need separate handling.
- Wrong/missing answer: inspect exact retrieved text before editing the prompt.
- Old results: save app.py, restart Streamlit and rerun the question. There should be one
  retrieve function. Reprocessing is needed for embedding/chunk changes, not prompt edits.
- Cache mismatch: the content/settings key selects a new index; do not mix embedding spaces.

## Demo script

1. Start the app and upload the Transformer PDF.
2. Process it and show the chunk count.
3. Ask how many encoder layers there are; show page 3 evidence.
4. Ask Q7; show page 7 evidence and explain the retrieval debugging story.
5. Ask the electricity-cost question; show the appropriate abstention.
6. Restart and demonstrate reuse of the saved index.

Record only actual app output in demo screenshots. Do not portray a mockup or
illustration as a live application screenshot. Do not expose API keys or private PDF text.
