from huggingface_hub import InferenceClient
import keys

model_id = "facebook/mbart-large-50-many-to-many-mmt"   
client = InferenceClient(model=model_id, token= keys.HUGGINGFACE_KEY)

english_text = "What did you learn about AI?"
prefixed_text = ">>te_IN<< " + english_text

# Run translation
response = client.translation(prefixed_text)

print("Telugu:", response.generated_text)