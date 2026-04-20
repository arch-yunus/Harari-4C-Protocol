# Teknik Dokümantasyon Standardı (21. Yüzyıl Mühendisi İçin)

Harari-4C-Protocol, iletişimi sadece bilgi aktarımı değil, **bilişsel yükü minimize etme sanatı** olarak görür. Bu dökümantasyon standardı, karmaşık sistemlerin en şeffaf şekilde temsil edilmesini amaçlar.

## 1. Mimari Hiyerarşisi (Top-Down)
Her döküman en tepeden en aşağıya doğru yapılandırılmalıdır:
1.  **Görsel Özet:** Mermaid.js veya benzeri bir araçla sistem akış diyagramı.
2.  **Yüksek Düzeyli Amaç:** Bu sistem neden var? Hangi sorunu çözüyor?
3.  **Bileşen Detayları:** Modüller, API'lar ve veri yapıları.

## 2. "Readability First" Prensibi
-   **Kısa Cümleler:** Teknik metinler edebi değil, işlevsel olmalıdır.
-   **Bullet Points:** Sıralı liste kullanımı okunabilirliği %50 artırır.
-   **Kritik Uyarılar:** Önemli notlar için standart Markdown uyarı kutuları (Note, Warning, Caution) kullanılmalıdır.

## 3. Kod ve Örnek Entegrasyonu
-   **Copy-Paste Ready:** Örnek kodlar terminalde doğrudan çalıştırılabilir olmalıdır.
-   **Yorum Satırları:** Kodun içinde "ne" yapıldığından ziyade "neden" yapıldığına odaklanılmalıdır.

## 4. İnsan-Makine Arayüzü (Prompting)
Dökümantasyon, AI sistemleri tarafından kolayca dizinlenebilir (indexable) olmalıdır.
-   **Metadata:** Dosya başında meta verileri (Versiyon, Yazarlar, Kapsam) eklenmelidir.
-   **Anlamlı İsimlendirme:** `utils.py` yerine `data_transformer_logic.py` gibi betimleyici isimler kullanılmalıdır.

---

### Standart Şablon (Harari-4C-v1)
```markdown
# [Sistem Adı]

## 🎯 Amaç
[Projenin/Sistemin temel amacı]

## 🧱 Bileşenler
- **Modül A:** [Açıklama]
- **Modül B:** [Açıklama]

## 🚀 Hızlı Başlangıç
`run_command --args`

## ⚠️ Dikkat Edilmesi Gerekenler
[Riskler ve kısıtlamalar]
```
