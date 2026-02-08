### Versi 1: Dasar (Generic AI)
* **Prompt:** `Buatlah kalimat pembuka email untuk perusahaan {company} berdasarkan berita {news}.`
* **Evaluasi:** Output terlalu kaku, menggunakan jargon pemasaran Amerika (seperti "game-changer"), dan tidak memiliki "jiwa" lokal Singapura sehingga mudah diabaikan oleh eksekutif senior.

### Versi 2: Penambahan Persona (Expert Tone)
* **Prompt:** `Anda adalah pakar bisnis Singapura. Buatlah hook profesional untuk {company} menggunakan berita {news}. Hindari istilah pemasaran berlebihan.`
* **Evaluasi:** Nada bicara membaik, namun AI seringkali melewatkan detail penting seperti lokasi spesifik (misal: Pulau Jurong) atau target tahun pemerintah, sehingga kurang memiliki otoritas sebagai konsultan lokal.

### Versi 3: Final (Persona-Driven & Logic-Guided)
* **System Message:** `You are a senior business consultant in Singapore. You specialize in hyper-personalized B2B outreach.`
* **User Prompt:** ```text
    Role: You are an expert B2B Consultant at Magna Pacific Bridge, Singapore.
    Context: {company} is involved in: {news}.
    Task: Write a 1-sentence 'Smart-Hook' for a professional email.
    Guidelines:
    - Use formal Singaporean business etiquette (direct, professional, value-driven).
    - Reference specific locations or national goals (e.g., Jurong Island, Singapore Green Plan 2030).
    - Output ONLY the sentence.
    ```
* **Alasan Efektivitas:** Pemisahan instruksi sistem dan panduan spesifik (Guidelines) pada model Llama-3.3-70b berhasil menciptakan output yang memiliki "Data Anchor" kuat, sangat relevan dengan pasar Singapura tahun 2026, dan lolos filter spam AI.