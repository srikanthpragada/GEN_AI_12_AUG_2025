from transformers import pipeline

client = pipeline("translation",         
                       model="Helsinki-NLP/opus-mt-en-hi")

text = "How are you?"
prompt = f"""
    Translate the following English text to simple Hindi:
    
    {text}                
    """
hindi = client(prompt)
print(hindi[0]['translation_text'])



     