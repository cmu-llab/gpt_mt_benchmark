import subprocess
import pandas as pd

langs = ["fra_Latn", "zho_Hans", "fin_Latn", "tur_Latn", "tgl_Latn", "tam_Taml", "swh_Latn", "amh_Ethi", "pap_Latn",
         "lao_Laoo", "luo_Latn", "sat_Olck"]
prompt_datasets = ["tp3", "tt-zero", "tt-one", "tt-three", "tt-five"]
name_prefix = "gpt-3.5-turbo tt-def temperature=0.3 context_length=-1"

bleu_across_prompts = {}
chrf_across_prompts = {}
ter_across_prompts = {}

metrics_tuple = ((bleu_across_prompts, "BLEU"), (chrf_across_prompts, "chrF2++"), (ter_across_prompts, "TER"))

for lang in langs:
    for item in metrics_tuple:
        item[0][lang] = {}


def populate_metrics_across_prompts(metrics_name, metrics_xp_dict, prompt_name, prompt_dict):
    for key in metrics_xp_dict.keys():
        metrics_xp_dict[key][prompt_name] = prompt_dict[key][metrics_name]


for prompt in prompt_datasets:
    results = {}
    for lang in langs:
        fname = f"tsv_results/{prompt}/{name_prefix}_{prompt}_{lang}.tsv"
        out_file = open("metrics.txt", "w")
        subprocess.call(["python", "score.py", fname], stdout=out_file)
        out_file.close()
        output = open("metrics.txt", "r").read()
        bleu = float(output.split("BLEU = ")[1].split()[0])
        chrf = float(output.split("chrF2++ = ")[1].split()[0])
        ter = float(output.split("TER = ")[1].split()[0])

        results[lang] = {"BLEU": bleu, "chrF2++": chrf, "TER": ter}
    df = pd.DataFrame(results)
    df.to_csv(prompt + "_scores.tsv", sep="\t")
    populate_metrics_across_prompts("BLEU", bleu_across_prompts, prompt, results)
    populate_metrics_across_prompts("chrF2++", chrf_across_prompts, prompt, results)
    populate_metrics_across_prompts("TER", ter_across_prompts, prompt, results)

for item in metrics_tuple:
    df = pd.DataFrame(item[0])
    df.to_csv(item[1] + "_scores.tsv", sep="\t")
