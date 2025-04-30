# Destek Talep Sistemi (Frontend Only)

Bu proje, tamamen frontend tabanlı bir destek talep sistemi uygulamasıdır. Kullanıcılar destek talepleri oluşturabilir, uzmanlar ise bu taleplere yanıt verebilir. Herhangi bir backend ya da veritabanı entegrasyonu bulunmamaktadır.

## Özellikler

- 🧑‍💻 Giriş / Kayıt Sayfaları (Login / Register)
- 📝 Destek Talebi Oluşturma (Create Ticket)
- 📋 Talep Listesi Görüntüleme (Index / Dashboard)
- 🔍 Talep Detaylarını Görüntüleme
- 🛠️ Talep Düzenleme (Edit Ticket)
- 🧑‍⚖️ Admin Paneli
- 👨‍🔧 Uzman Paneli (Taleplere yanıt verme)
- 🎨 Farklı renk temaları ve tasarımlar (Tailwind CSS veya Bootstrap ile)

## Teknolojiler

- HTML5
- CSS3
- [Tailwind CSS](https://tailwindcss.com/) (veya) [Bootstrap](https://getbootstrap.com/)
- Tamamen statik frontend mimarisi

## Klasör Yapısı

/proje-klasoru 
│ 
├── index.html # Talep listesi ana sayfa 
├── login.html # Kullanıcı girişi 
├── register.html # Kullanıcı kaydı 
├── create.html # Talep oluşturma sayfası 
├── edit.html # Talep düzenleme sayfası 
├── admin.html # Admin paneli 
├── uzman.html # Uzman paneli 
├── dashboard.html # Kullanıcı dashboard'u 
├── base.html # Ortak layout (header/footer) (projemde şuanda ortak layout bulunmuyor ilerleyen zamanda kullanmak için eklendi)
├── css/ 
│ 
└── style.css # Proje stilleri (Tailwind/Bootstrap dahil) 
└── README.md # Bu dosya

