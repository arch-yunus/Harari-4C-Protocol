import re

class BiasAnalyzer:
    """
    Harari-4C-Protocol: Critical Thinking Module
    Simple heuristic-based bias and logical fallacy detector.
    """
    
    BIAS_PATTERNS = {
        "Confirmation Bias": [r"herkes biliyor ki", r"her zaman olduğu gibi", r"kanıtlamaya gerek yok"],
        "Bandwagon Effect": [r"çoğunluk", r"herkes böyle yapıyor", r"trend"],
        "Appeal to Authority": [r"uzmanlar diyor ki", r"bilim insanları kanıtladı", r"otorite"],
        "False Dichotomy": [r"ya ... ya da", r"başka seçenek yok"],
        "Ad Hominem": [r"zaten o kişi", r"onun karakteri", r"aptalca"],
    }

    def __init__(self):
        pass

    def analyze(self, text):
        findings = []
        text_lower = text.lower()
        
        for bias_name, patterns in self.BIAS_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    findings.append({
                        "type": bias_name,
                        "matched": pattern,
                        "suggestion": f"Bu ifade '{bias_name}' riski taşıyor olabilir. Mantıksal temelleri tekrar kontrol edin."
                    })
        
        return findings

if __name__ == "__main__":
    analyzer = BiasAnalyzer()
    sample_text = "Herkes biliyor ki bu teknoloji en iyisidir, ya bizimle olursunuz ya da geri kalırsınız."
    results = analyzer.analyze(sample_text)
    
    print("--- Harari-4C: Critical Thinking Analysis ---")
    print(f"Girdi: {sample_text}\n")
    if not results:
        print("Belirgin bir safsata bulunamadı.")
    for result in results:
        print(f"[!] {result['type']}: '{result['matched']}'")
        print(f"    Öneri: {result['suggestion']}")
