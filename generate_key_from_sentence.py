import key_list
import get_best_key

def generate_key_from_sentence(sentence):
    return get_best_key(generate_candidate_keys(generate_key_list(sentence)),sentence)

print(generate_key_from_sentence("In plants, vascular tissues conduct food and water from one part of the plant to other plants"))
