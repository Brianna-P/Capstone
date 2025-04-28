## NL2Esgish2 README
Convert ISS Stoxx formal query language: Esgish2 to natural language and vice versa.

### Description
NL2Esgish2 is a NLP-based tool which converts human-readable text input into the query language Esgish2, with the intent of streamlining non-technical user's interactions with the ISS Stoxx database.

### Features
The scope of this project is an API program capable of conversion to and from Esgish2. This means there are two main functions that will be syncretically developed.

Esgish2 -> Natural Language conversion. (FOCUS OF SPRINT 1) This is the first focus of NL2Esgish2, as training a model during Sprint 2 will require a large dataset of Esgish2 to English translations. This will be done using a local LLM, namely Mistral 7B Instruct, which takes each Esgish2 query, extracts related metadata and grammar information, and fetches an equivalent English translation.

Back-and-forth translations. (FOCUS OF SPRINT 2) This is the main focus of the NL2Esgish2 project, allowing for users to translate input from Esgish2 to English and vice versa. This will done by doing holdout training on a model, such as Flan T5 Base or Flan T5 Small, using 17k lines of Esgish2 to English translations. 

### How to Use Translate_to_English To Translate Esgish2 Queries to English
1. Install Jupyter Notebook and open the application
2. Download the file mistral-7b-instruct-v0.1.Q4_K_M.gguf from https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF to ensure local LLM use
3. Open Translate_to_English.ipynb in Jupyter Notebook
4. Edit the model path in the cell 2 of Translate_to_English.ipynb to match the model's local location
5. Ensure metadata.json is in the same directory (or, edit the file path in line 4, cell 3) as Translate_to_English.ipynb
6. Edit lines 6 and 7 of the cell 5 of Translate_to_English.ipynb to an the target Excel file that you want translations created for
7. Run the Jupyter Notebook

### How to Use Model_Training
1. Open application in Jupyter Notebook
2. Run the first cell, it installs the required libraries
3. Run the next cell which allows the use of the GPU
4. Authenticate with HuggingFace using next cell
5. Load in Flan-T5-Base model from HuggingFace and to the device
6. Then format the data for English to Esgish translations and vice versa
7. Run the trainer
8. When finished, save the model with the desired name
9. You can now load the model and use it to generate outputs
