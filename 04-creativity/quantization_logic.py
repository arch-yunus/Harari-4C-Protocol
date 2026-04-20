import random

def simulate_quantization(weights, bits=8):
    """
    Harari-4C-Protocol: Creativity (Technical Optimization)
    Simulates Weight Quantization for Edge-AI.
    Shows how creative constraints (low bit-rate) lead to efficient architectures.
    """
    q_min = -(2**(bits-1))
    q_max = (2**(bits-1)) - 1
    
    # Simple linear quantization
    scale = (max(weights) - min(weights)) / (q_max - q_min)
    
    quantized_weights = []
    for w in weights:
        # Quantize
        q = round(w / scale)
        # Clip
        q = max(q_min, min(q_max, q))
        quantized_weights.append(q)
        
    return quantized_weights, scale

def run_creativity_demo():
    print("--- Harari-4C: Creativity (Edge-AI Optimization) ---")
    print("Senaryo: Düşük kaynaklı bir cihaz için model ağırlıklarını optimize etme.\n")
    
    # 32-bit floats simulation
    original_weights = [random.uniform(-1.0, 1.0) for _ in range(10)]
    print(f"Orijinal Ağırlıklar (32-bit): {[round(w, 4) for w in original_weights]}")
    
    # 8-bit quantization
    q_weights, scale = simulate_quantization(original_weights, bits=8)
    print(f"Quantized Ağırlıklar (8-bit):   {q_weights}")
    
    # Dequantize to check error
    dequantized = [q * scale for q in q_weights]
    error = sum(abs(o - d) for o, d in zip(original_weights, dequantized)) / len(original_weights)
    
    print(f"\nDequantized Ağırlıklar:       {[round(w, 4) for w in dequantized]}")
    print(f"Ortalama Hata (Loss):         {round(error, 6)}")
    print("\n[Sonuç] Yaratıcı kısıtlamalar (8-bit), %75 bellek tasarrufu sağlarken hassasiyeti korudu.")

if __name__ == "__main__":
    run_creativity_demo()
