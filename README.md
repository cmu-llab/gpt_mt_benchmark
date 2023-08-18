# Benchmarking Large Language Models (GPT) for Machine Translation
## Overview
In this work, we investigate the translation capabilities of GPT models across 203 diverse languages from [FLORES 200 dataset](https://github.com/facebookresearch/flores/blob/main/flores200/README.md)

Read more about it in the paper [to be updated]

We have outputs for 3 systems:
  - tt-zero (GPT-3.5-turbo): Zero-shot prompt
  - tt-five (GPT-3.5-turbo): Five-shot prompt
  - GPT-4-(On a subset of 20 languages)- Five shot prompt
We also added NLLB outputs (it is our baseline) for comparison
  
## Reproducing the work
We used _gpt-3.5-turbo-0613_  and *gpt-4-0613* in July and August 2023. 
Find instructions below on how to use our codebase.

### Outputs and inputs
We release the outputs in the folder system_outputs. Each tsv contains 3 columns:
- messages : Contains the prompts
- label : Is the reference
- predictions : The predictions from Open AI.

###  Querying OpenAI
This section has instructions on how to use our codebase to run the experiments.
- You will need to install Zeno and OpenAI libraries. Install them and other requirements by running `pip install -r requirements.txt`
- config.py contains the configuration for the models; GPT-3.5-turbo aand GPT-4
- Modelling.py
- Have a file called `langs.txt` that contains the languages you want to generated. 
- Your source folders should be named [prompt]/[lang]/
- run.sh
- Finally run `bash run.sh`
### Evaluation
`python eval_runs.py --results_dir [folder] --langs_file [a file with line searated languages to be evaluated]  --tokenizer [tokenizer-this is optional]`

## License