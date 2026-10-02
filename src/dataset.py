import json


def load_dataset(path):
    samples = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                samples.append(json.loads(line))

    return samples


def get_text(sample):
    return sample["doc"]["input"]


samples = load_dataset("data/len_500.jsonl")

text = get_text(samples[0])

print(text)