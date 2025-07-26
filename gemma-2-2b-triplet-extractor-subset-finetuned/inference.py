from transformers import AutoTokenizer, AutoModelForCausalLM
import sys

def main():
    hf_token = "Use a read token from hugginface"
    tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b-it")
    model = AutoModelForCausalLM.from_pretrained("i5-8300h/gemma-2-2b-triplet-extractor-subset-finetuned", trust_remote_code=False)
    prompt = (
        "Generate triplets from this sentence: "
        "Alan Turing developed the Turing machine to formalize the concept of computation."
    )
    inputs = tokenizer(prompt, return_tensors="pt", padding=True)
    outputs = model.generate(**inputs, max_new_tokens=50)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

if __name__ == "__main__":
    main()
