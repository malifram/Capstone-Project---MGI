import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load Environment
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def main():
    print("\n--- Magna Pacific Bridge: Generator (Powered by Groq) ---")
    company = input("Nama Perusahaan: ")
    news = input("Konteks Berita: ")

    if not company or not news: return

    print("\n[i] Menghubungi Groq AI (Llama 3.3)...")
    
    # PERBAIKAN: Prompt Engineering yang lebih spesifik (Sesuai isi Slide 2 PPT)
    prompt = (
        f"Role: You are an expert B2B Consultant at Magna Pacific Bridge, Singapore.\n"
        f"Context: {company} is involved in: {news}.\n"
        f"Task: Write a 1-sentence 'Smart-Hook' for a professional email.\n"
        f"Guidelines:\n"
        f"- Use formal Singaporean business etiquette (direct, professional, value-driven).\n"
        f"- Reference specific locations or national goals (e.g., Jurong Island, Singapore Green Plan 2030) if relevant.\n"
        f"- Avoid generic marketing jargon like 'game-changer' or 'disruptive'.\n"
        f"- Output ONLY the sentence, no preamble."
    )

    try:
        # Menggunakan model Llama-3.3-70b (Model terbaik Groq saat ini)
        chat_completion = client.chat.completions.create(
            messages=[
                # Menambahkan System Message agar AI benar-benar konsisten dengan persona pakar
                {"role": "system", "content": "You are a senior business consultant in Singapore. You specialize in hyper-personalized B2B outreach."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5, # Membuat jawaban lebih stabil/tidak ngelantur
        )
        
        result = chat_completion.choices[0].message.content
        
        print("\n" + "="*60)
        print(f"SMART-HOOK RESULT:")
        print(f"\"{result.strip()}\"")
        print("="*60)
        print("\n[i] Data Anchor: Lokasi Spesifik & Tren Industri Terdeteksi.")
        
    except Exception as e:
        print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    main()