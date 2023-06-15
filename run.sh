#!/bin/bash

langs=("fra_Latn" "zho_Hans" "fin_Latn" "tur_Latn" "tgl_Latn" "tam_Taml" "swh_Latn" "amh_Ethi" "pap_Latn" "lao_Laoo" "luo_Latn" "sat_Olck")
prompt_datasets=("tp3" "tt-zero" "tt-one" "tt-three" "tt-five")

for prompt in "${prompt_datasets[@]}"
do
    for lang in "${langs[@]}"
    do
        python main.py --dataset "fewshot_texts/$prompt/$lang" --dataset_config_preset "local-${lang:0:3}"
    done
done
