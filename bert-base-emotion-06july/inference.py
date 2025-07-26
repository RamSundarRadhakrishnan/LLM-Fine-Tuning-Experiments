from transformers import AutoTokenizer, AutoModelForSequenceClassification
import sys

def main():
    model_name = "i5-8300h/bert-base-emotion-06july"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    text = "Today is a great day!"
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    pred_id = logits.argmax(dim=-1).item()
    labels = getattr(model.config, "id2label", None)
    if labels:
        print(labels[pred_id])
    else:
        print(pred_id)

if __name__ == "__main__":
    main()
