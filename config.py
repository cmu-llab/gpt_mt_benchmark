"""Various configuration options for the chatbot task.

This file is intended to be modified. You can go in and change any
of the variables to run different experiments.
"""
#TODO create a map  of langcode to lang_name
from __future__ import annotations

import transformers

from zeno_build.evaluation.text_features.exact_match import avg_exact_match, exact_match
from zeno_build.evaluation.text_features.length import (
    chat_context_length,
    input_length,
    label_length,
    output_length,
)
from zeno_build.evaluation.text_metrics.critique import (
    avg_bert_score,
    avg_chrf,
    avg_length_ratio,
    bert_score,
    chrf,
    length_ratio,
)
from zeno_build.experiments import search_space
from zeno_build.models.dataset_config import DatasetConfig
from zeno_build.models.lm_config import LMConfig
from zeno_build.prompts.chat_prompt import ChatMessages, ChatTurn

# Define the space of hyperparameters to search over.
space = search_space.CombinatorialSearchSpace(
    {
        "dataset_preset": search_space.Constant("local-fra"),
        "model_preset": search_space.Categorical(
            [
                "gpt-3.5-turbo",
            ]
        ),
        "prompt_preset": search_space.Discrete(
            ["tt-def"]
        ),
        "temperature": search_space.Discrete([0.3]),
        "context_length": search_space.Discrete([-1]),
        "max_tokens": search_space.Constant(500),
        "top_p": search_space.Constant(1.0),
    }
)

# The number of trials to run
num_trials = 1

# The details of each dataset
dataset_configs = {
    "dstc11": DatasetConfig(
        dataset="gneubig/dstc11",
        split="validation",
        data_column="turns",
        data_format="dstc11",
    ),
    "flores200": DatasetConfig(
        dataset=("facebook/flores", "swh_Latn-eng_Latn"),
        split="devtest",
        data_column="sentence_swh_Latn",
        data_format="flores",
    ),
    "local-fra": DatasetConfig(
        dataset="fra_Latn",
        split="devtest",
        data_column="sentence_fra_Latn",
        data_format="local",
    ),
    "local-swh": DatasetConfig(
        dataset="swh_Latn",
        split="devtest",
        data_column="sentence_swh_Latn",
        data_format="local",
    ),
    "local-fin": DatasetConfig(
        dataset="fin_Latn",
        split="devtest",
        data_column="sentence_swa_Latn",
        data_format="local",
    ),
    "local-amh": DatasetConfig(
        dataset="amh_Ethi",
        split="devtest",
        data_column="sentence_amh_Latn",
        data_format="local",
    ),
    "local-lao": DatasetConfig(
        dataset="lao_Laoo",
        split="devtest",
        data_column="sentence_lao_Latn",
        data_format="local",
    ),
    "local-luo": DatasetConfig(
        dataset="luo_Latn",
        split="devtest",
        data_column="sentence_luo_Latn",
        data_format="local",
    ),
    "local-pap": DatasetConfig(
        dataset="pap_Latn",
        split="devtest",
        data_column="sentence_pap_Latn",
        data_format="local",
    ),
    "local-tam": DatasetConfig(
        dataset="tam_Taml",
        split="devtest",
        data_column="sentence_tam_Latn",
        data_format="local",
    ),
    "local-tgl": DatasetConfig(
        dataset="tgl_Latn",
        split="devtest",
        data_column="sentence_tgl_Latn",
        data_format="local",
    ),
    "local-tur": DatasetConfig(
        dataset="tur_Latn",
        split="devtest",
        data_column="sentence_tur_Latn",
        data_format="local",
    ),
    "local-zho": DatasetConfig(
        dataset="zho_Hans",
        split="devtest",
        data_column="sentence_zho_Hans",
        data_format="local",
    ),
    "local-sat": DatasetConfig(
        dataset="sat_Olck",
        split="devtest",
        data_column="sentence_sat_Latn",
        data_format="local",
    )
}

# The details of each model
model_configs = {
    "text-davinci-003": LMConfig(provider="openai", model="text-davinci-003"),
    "gpt-3.5-turbo": LMConfig(provider="openai_chat", model="gpt-3.5-turbo"),
    "cohere-command-xlarge": LMConfig(
        provider="cohere", model="command-xlarge-nightly"
    ),
    "gpt2": LMConfig(
        provider="huggingface",
        model="gpt2",
        model_cls=transformers.GPT2LMHeadModel,
    ),
    "gpt2-xl": LMConfig(
        provider="huggingface",
        model="gpt2-xl",
        model_cls=transformers.GPT2LMHeadModel,
    ),
    "llama-7b": LMConfig(
        provider="huggingface",
        model="decapoda-research/llama-7b-hf",
        tokenizer_cls=transformers.LlamaTokenizer,
    ),
    "llama-13b": LMConfig(
        provider="huggingface",
        model="decapoda-research/llama-13b-hf",
        tokenizer_cls=transformers.LlamaTokenizer,
    ),
    "alpaca-7b": LMConfig(
        provider="huggingface",
        model="chavinlo/alpaca-native",
    ),
    "alpaca-13b": LMConfig(
        provider="huggingface",
        model="chavinlo/alpaca-13b",
    ),
    "vicuna-7b": LMConfig(
        provider="huggingface",
        model="eachadea/vicuna-7b-1.1",
        name_replacements={
            "system": "ASSISTANT",
            "assistant": "ASSISTANT",
            "user": "HUMAN",
        },
    ),
    "vicuna-13b": LMConfig(
        provider="huggingface",
        model="eachadea/vicuna-13b-1.1",
        name_replacements={
            "system": "ASSISTANT",
            "assistant": "ASSISTANT",
            "user": "HUMAN",
        },
    ),
    "mpt-7b-chat": LMConfig(
        provider="huggingface",
        model="mosaicml/mpt-7b-chat",
        model_loader_kwargs={"trust_remote_code": True},
    ),
}

# The details of the prompts
prompt_messages: dict[str, ChatMessages] = {
    "tt-def": ChatMessages(
        messages=[
            ChatTurn(
                role="user",
                content="",
            ),
        ]
    ),
    "tt-zero": ChatMessages(
        messages=[
            ChatTurn(
                role="user",
                content='',
            ),
        ]
    ),
    "tt-one": ChatMessages(
        messages=[
            ChatTurn(
                role="user",
                content='',
            ),
        ]
    ),
    "tt-three": ChatMessages(
        messages=[
            ChatTurn(
                role="system",
                content='',
            ),
        ]
    ),
    "tt-five": ChatMessages(
        messages=[
            ChatTurn(
                role="system",
                content='',
            ),
        ]
    ),
}

# The functions to use to calculate scores for the hyperparameter sweep
sweep_distill_functions = [chrf]
sweep_metric_function = avg_chrf

# The functions used for Zeno visualization
zeno_distill_and_metric_functions = [
    output_length,
    input_length,
    label_length,
    chat_context_length,
    chrf,
    length_ratio,
    bert_score,
    exact_match,
    avg_chrf,
    avg_length_ratio,
    avg_bert_score,
    avg_exact_match,
]