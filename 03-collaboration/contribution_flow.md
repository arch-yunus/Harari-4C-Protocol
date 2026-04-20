# Katkı Protokolü (Collaboration Protocol)

Harari-4C-Protocol, projeye katkı sağlamayı bireysel bir başarı değil, **sürü zekasının (swarm intelligence)** bir uzantısı olarak görür. Bu protokol, merkeziyetsiz ekiplerin uyum içinde çalışmasını sağlar.

## 1. Dal (Branch) Stratejisi
-   `main`: Sadece stabil ve üretim hazır kod.
-   `feat/`: Yeni özellikler için aktif geliştirme dalları.
-   `fix/`: Hata düzeltmeleri.
-   `doc/`: Sadece dökümantasyon güncellemeleri.

## 2. Pull Request (PR) Standartları
Her PR şu bileşenleri içermelidir:
-   **Özet:** Yapılan değişikliğin 4C (Critical Thinking, Communication, Collaboration, Creativity) prensiplerinden hangisini güçlendirdiği belirtilmelidir.
-   **Test Sonuçları:** Değişikliğin sistemin geri kalanını bozmadığına dair kanıt.
-   **Kritik Gözden Geçirme:** En az bir "Eleştirel Düşünme" analizi yapılmış olmalıdır.

## 3. İletişim ve Senkronizasyon
-   **Asenkron Önceliği:** Bilgi, herkesin her an erişebileceği şekilde dokümante edilmelidir (`02-communication` standartlarına uygun).
-   **Swarm Code Reviews:** Kod incelemeleri sadece hataları bulmak için değil, kolektif bilgiyi artırmak için yapılır.

## 4. Karar Alma Mekanizması (Consensus)
-   Projeyle ilgili kritik kararlar, teknik kanıtlara dayalı rasyonel optimizasyon ile alınır. Eğer bir karar "Eleştirel Düşünme" süzgecinden geçemiyorsa reddedilir.

---

### Hızlı Katkı Adımları
1.  Depoyu forklayın.
2.  `feat/yeniozellik` adında bir branch açın.
3.  Kodunuzu ve dökümantasyonunuzu ekleyin.
4.  `bias_analyzer.py` ile kodunuzdaki/metninizdeki mantıksal tutarlılığı test edin.
5.  PR açın ve sürüye katılın!
    
