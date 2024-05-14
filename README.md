# Benchmarking Large Language Models (GPT) for Machine Translation

Software for: [ChatGPT MT: Competitive for High- (but Not Low-) Resource Languages](https://aclanthology.org/2023.wmt-1.40/) (WMT 2023)

## Overview
In this work, we investigate the translation capabilities of GPT models across 203 diverse languages from [FLORES 200 dataset](https://github.com/facebookresearch/flores/blob/main/flores200/README.md)

Read more about it in [our paper](https://arxiv.org/abs/2309.07423) (accepted to [WMT 2023](http://www2.statmt.org/wmt23/))

Also see our [Zeno browser](https://hub.zenoml.com/project/cabreraalex/GPT%20MT%20Benchmark), with interactive visualizations of our results.

We have outputs for 5 systems:
  - ChatGPT (0-shot prompts) (GPT-3.5-turbo): 203 target languages
  - ChatGPT (5-shot prompts) (GPT-3.5-turbo): 203 target languages
  - GPT-4 (5-shot prompts): 20 target languages
  - NLLB-MOE: 201 target languages
  - Google Translate: 115 target languages

All model outputs can be found on [Zenodo](https://zenodo.org/records/8286649)
  
## Reproducing the work
We used _gpt-3.5-turbo-0613_  and *gpt-4-0613* in July and August 2023. 
Find instructions below on how to use our codebase.

### Outputs and inputs
The outputs and inputs from this work can be found [here]()(will be updated) . We  will release the outputs in a folder system_outputs.  Each tsv contains 3 columns:
- messages : Contains the prompts
- label : Is the reference
- predictions : The predictions from Open AI.

###  Querying OpenAI
This section has instructions on how to use our codebase to run the experiments.
- You will need to install Zeno and OpenAI libraries. Install them and other requirements by running `pip install -r requirements.txt`
- config.py contains the configuration for the models; GPT-3.5-turbo aand GPT-4
- modelling.py: This script contains utilities. An important one is the call to `generate_from_chat_prompt` function. You may want to reduce the `requests_per_minute` parameter value especially for n-shot and non-latin scripts so as not to max out and get empty returns from the API.
- flores200_utils.py : Contains data processing utilities.
- Have a file called `langs.txt` that contains the languages you want to generated. 
- Your source folders should be named [prompt]/[lang]/
- Within each lang, have a file with the prompt. 
- run.sh: This is the bash script that launches main.py
- Finally run `bash run.sh`

### Evaluation
We have a script `eval_runs.py` that handles evaluation for BLEU, chrF, SLR and TER.
`python eval_runs.py --results_dir [folder] --langs_file [a file with line searated languages to be evaluated]  --tokenizer [tokenizer-this is optional]`
### Notebooks
*langid_classifier.ipynb* - for classifying the langauge of the predictions

*zeno_browser.ipynb* - This notebook shows how to use the Zeno library to analyze the results from our experiments.

## Citation

Please cite:

```
@inproceedings{robinson-etal-2023-chatgpt,
    title = "{C}hat{GPT} {MT}: Competitive for High- (but Not Low-) Resource Languages",
    author = "Robinson, Nathaniel  and
      Ogayo, Perez  and
      Mortensen, David R.  and
      Neubig, Graham",
    editor = "Koehn, Philipp  and
      Haddow, Barry  and
      Kocmi, Tom  and
      Monz, Christof",
    booktitle = "Proceedings of the Eighth Conference on Machine Translation",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.wmt-1.40",
    doi = "10.18653/v1/2023.wmt-1.40",
    pages = "392--418",
    abstract = "Large language models (LLMs) implicitly learn to perform a range of language tasks, including machine translation (MT). Previous studies explore aspects of LLMs{'} MT capabilities. However, there exist a wide variety of languages for which recent LLM MT performance has never before been evaluated. Without published experimental evidence on the matter, it is difficult for speakers of the world{'}s diverse languages to know how and whether they can use LLMs for their languages. We present the first experimental evidence for an expansive set of 204 languages, along with MT cost analysis, using the FLORES-200 benchmark. Trends reveal that GPT models approach or exceed traditional MT model performance for some high-resource languages (HRLs) but consistently lag for low-resource languages (LRLs), under-performing traditional MT for 84.1{\%} of languages we covered. Our analysis reveals that a language{'}s resource level is the most important feature in determining ChatGPT{'}s relative ability to translate it, and suggests that ChatGPT is especially disadvantaged for LRLs and African languages.",
}
```

## License
MIT
