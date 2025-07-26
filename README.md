# LLM-Fine-Tuning-Experiments
Showcasing some of my experiments finetuning LLMs and other transformer based models
This repository contains my personal experiments with fine-tuning transformer models on custom tasks like triplet extraction, emotion classification etc. The finetuned models are not particularly performant, and they remain as testing grounds where I learned about model finetuning.

The models themselves are hosted on HuggingFace: https://huggingface.co/i5-8300h

Model List:

1- llama-sft-triplets : This is a finetune of Llama 3.1 8B on the XAlign dataset. The goal was to optimize the LLM to generate triplets (in subject, relation, object format) from a sentence. The finetune did not result in optimal behaviour, but I learnt about resource management - I was using my RTX 3050Ti 4GB.

2- gemma-2-2b-triplet-extractor-subset-finetuned : The goal with this finetune was to realign the model towards generating triplets strictly from the semantic information present in the sentence, and not from the pre-trained knowledge. The finetune resulted in minor improvements to the outputs, but the key takeaway for me was that finetuning a model on a subset of a large dataset is a good way to estimate the performance that a full finetune would result in.

3- bert-base-emotion-06july and bert-base-emotion-07july : The goal here was to finetune a model for the task of sentiment analysis on user prompts and to classify them into the categories of ["laidback", "concerned", "stressed", "overwhelmed", "desperate"] . The dataset used was go_emotions from google=research-datasets. Testing showed that accuracy was subpar, and the experiment was abandoned.

4- distilbert-emotion-05july : Same task as above. The validation accuracy measured was 71.82%, which did not represent a significant benefit from finetuning.

All these finetuning experiments were conducted on my Acer Swift X SFX14-R1SG, with a Ryzen 7 5800u and RTX 3050Ti 4GB. Managing VRAM usage was the main challenge, and I experimented with techniques like SFT, LoRA and PeFT.
I aim to take the learnings from my experiments and use them to develop finetuned models for my ongoing projects, and also to create some tools that will make my daily life easier :D

I appreciate any feedback, critiques or discussion on these experiments.

Do email me on ramsundar289@gmail.com!
