const protocolDetails = {
    critical: {
        title: "Critical Thinking (Eleştirel Düşünme)",
        body: "Gerçeklik ile algı arasındaki boşluğu yönetir. Bu modül; bias tespiti, mantıksal safsatalardan arınma ve veri odaklı karar alma süreçlerini içerir. '01-critical-thinking' dizinindeki araçlarla desteklenir."
    },
    communication: {
        title: "Communication (İletişim)",
        body: "Bilginin en az kayıpla aktarılmasını sağlar. Prompt engineering standartları ve teknik dokümantasyon protokolleri ile sistemlerin (insan ve makine) senkronizasyonunu optimize eder."
    },
    collaboration: {
        title: "Collaboration (İş Birliği)",
        body: "Tekil zekayı, kolektif bir güce dönüştürür. Sürü zekası simülasyonları ve açık kaynak katkı protokolleri ile ekosistem içindeki enformasyon akışını yönetir."
    },
    creativity: {
        title: "Creativity (Yaratıcılık)",
        body: "Mevcut kalıpların ötesine geçer. Ontolojik veri modelleme ve Security-by-Design yaklaşımları ile belirsizliğe karşı esnek mimariler inşaa eder."
    }
};

// Connection mapping showing interdependence
const connections = {
    critical: ['communication', 'creativity'],
    communication: ['collaboration'],
    collaboration: ['creativity'],
    creativity: ['critical']
};

const cards = document.querySelectorAll('.c-card');
const modal = document.getElementById('modal');
const modalTitle = document.getElementById('modal-title');
const modalBody = document.getElementById('modal-body');
const closeBtn = document.getElementById('close-modal');

cards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        const id = card.getAttribute('data-id');
        const linkedIds = connections[id];
        linkedIds.forEach(linkedId => {
            const linkedCard = document.querySelector(`.c-card[data-id="${linkedId}"]`);
            if (linkedCard) linkedCard.style.borderColor = 'rgba(34, 211, 238, 0.4)';
        });
    });

    card.addEventListener('mouseleave', () => {
        cards.forEach(c => c.style.borderColor = '');
    });

    card.addEventListener('click', () => {
        const id = card.getAttribute('data-id');
        const details = protocolDetails[id];
        
        modalTitle.innerText = details.title;
        modalBody.innerText = details.body;
        
        modal.classList.add('active');
    });
});

closeBtn.addEventListener('click', () => {
    modal.classList.remove('active');
});

// Close modal on background click
modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.classList.remove('active');
    }
});

// Protocol Pulse - System Heartbeat
setInterval(() => {
    console.log("%c[Protocol Pulse] System stable. Cognitive load: Optimal.", "color: #22d3ee; font-weight: bold;");
}, 5000);

console.log("Harari-4C Dashboard v1.1 Initialized with Connection Logic.");
