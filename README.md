Nama: Anindya Raihani Hassan

NPM: 2506553295

Kelas: PBP B

### Tugas 1

1. Ya, saya menggunakan elemen semantik di struktur html. Elemen yang saya gunakan antara lain:

- `<header>` untuk navigation bar,
- `<main>` untuk seluruh konten utama,
- `<section>` untuk tiap bagian besar halaman (hero, services, experience),
- `<article>` untuk item dalam section seperti card di services dan experience, dan
- `<footer>` di paling bawah halaman.

Elemen semantik ini membantu saya karena memberi struktur yang jelas sehingga saya bisa menemukan dan mengedit ulang suatu item.

2. Tantangan tata letak responsif yang saya temui ada pada dua komponen utama:

- Bagian Hero: Pada tampilan desktop,tata letak berformat samping-sampingan (teks di kiri dan foto di kanan). Pada layar mobile, tata letak ini kurang efektif. Oleh karena itu, saya memindahkan posisi foto ke atas teks (order: -1) sehingga terlihat lebih natural.

- Bagian Services Card: Penggunaan CSS Grid awal sempat membuat tampilan kurang stabil pada ukuran layar desktop menengah/kecil. Saya menggantinya ke flexbox dengan flex-wrap: wrap agar kartu dapat terlihat menurun saat lebar tampilan mengecil.

3. Batasan dari static web adalah kurangnya fleksibilitas dalam manajemen konten. Ketika saya ingin menambahkan data seperti riwayat di bagian experience atau skill di services, saya harus menambahkannya di html secara manual. Oleh karena itu, di iterasi proyek selanjutnya saya ingin mengintegrasikan database yang nantinya menyimpan data-data yang sering di-update. Dengan begitu, data bisa dipanggil otomatis ke halaman web tanpa perlu edit html satu per satu.

### Alur Pengerjaan & Penggunaan AI Pada Tugas 1

link figma: https://www.figma.com/proto/AXqN1DCBqLUiTjETsTN8tg/Untitled?node-id=105-6601&t=tAFQbkDSLBSeoBXY-0&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&fuid=1569677707401958808

1. Desain pertama saya buat sendiri di Figma. Kemudian dengan plugin Figma to Framer, saya mendapatkan kode mentah HTML-nya.
2. Karena kode dari Framer belum sepenuhnya rapi dan sesuai keinginan saya, saya merevisi dengan menggunakan Claude untuk memisahkan file HTML dan CSS-nya.
3. Agar saya tetap memahami struktur kode, saya meminta Claude untuk memberi lokasi kode dan item korespondennya. Berdasarkan hal ini, barulah saya mengubah bagian-bagian yang perlu direvisi.
4. Salah satu keterbatasan AI yang saya jumpai: Claude sempat kesulitan me-render logo Figma pada card dengan proporsi yang benar (dicoba 2 kali, hasilnya tetap tidak sesuai bentuk aslinya). Saya akhirnya memutuskan untuk mengunduh langsung icon dari Figma dan menaruhnya di folder `img/`, sehingga yang sebelumnya berupa SVG hasil generate Claude, sekarang jadi file PNG asli.
5. Keterbatasan lain: saat meminta animasi hover yang mengubah warna icon, saran awal Claude menggunakan `filter: invert(1)` ternyata tidak menghasilkan warna spesifik yang saya inginkan (invert cuma balik nilai RGB, bukan ganti ke warna tertentu). Solusi akhirnya menggunakan teknik `mask-image` di CSS, yang memisahkan bentuk icon dari warnanya, sehingga warna hover bisa diatur presisi lewat `background-color`.
   ![1](static/img/screenshots/ai-hover.png)
   ![2](static/img/screenshots/ai-invert.png)

### Tutorial 2

Terdapat beberapa penyesuaian yang saya lakukan di Tutorial 2 (tidak mengikuti template sepenuhnya):

- **Menghapus `EXPERIENCE_CHOICES`** sejak awal desain portofolio ini tidak menggunakan kategori pengalaman, dan diganti dengan field `institution` (nama penyelenggara/instansi) yang dirasa lebih relevan.
- **Navigation bar di halaman utama** berfungsi untuk _scroll_ ke bagian terkait di halaman yang sama. Halaman baru `experience.html` diakses lewat tombol **"View More"**, bukan lewat item navbar.

### Tugas 2

1. Alur website

Misalnya, ketika pengguna mengakses sebuah URL `/experience`, Django akan mengecek `urls.py` proyek. Karena path-nya kosong (`""`), maka masuk ke `main.url` atau dengan kata lain lanjut ke `urls.py` yang ada di `main`. Di sana, path `experience/` dicocokkan dengan fungsi `show_experience` yang ada di `views.py`.

Di dalam `views.py`, fungsi `show_experience` mengambil data dari model `Experience` melalui `Experience.objects.all()`, lalu memasukkannya ke sebuah `context`. Setelah itu, baru memanggil `render()` untuk menggabungkan data tersebut dengan `experience.html` yang akhirnya dikirim sebagai response dan ditampilkan di browser pengguna. Hal yang sama juga terjadi untuk fitur service.

2. Data portfolio bisa berubah-ubah dan bertambah seiring waktu. Jika data ditulis langsung di template(hardcode), maka setiap kali ada perubahan, developer akan kesusahan untuk mengedit file HTML secara manual dan beresiko mengubah kode yang tidak diinginkan.

Dengan menyimpan data di model, terdapat satu sumber data yang terstruktur dan konsisten. Template melalukan for loop terhadap data tersebut sehingga:

- Penambahan/pengubahan data cukup dilakukan lewat Django Admin tanpa perlu mengakses kode di HTML-nya.
- Struktur tampilan tiap item akan konsisten karena memiliki patokan yang sama.
- Kode lebih mudah dikembangkan dan dijaga karena tempat penyimpanan data dan tampilan website dipisah.

3. `makemigrations` melihat perubahan yang diterapkan pada `models.py` dan membuat file migrasi yang berisi perubahan tersebut. Namun, file ini belum diterapkan ke database. Saat kita menjalankan `migrate`, baru perubahan tersebut diimplementasikan ke database.

Contohnya: di awal saya mengikuti template untuk memiliki field `category`, tetapi saya menghapus field ini dan menggantinya dengan field `institution`. Perubahan pada kode di `models.py` ini menyebabkan saya harus menjalankan kedua perintah tersebut untuk menerapkan perubahan skema tersebut ke database.

### Alur Pengerjaan & Penggunaan AI Pada Tugas 2

Perintah tugas 1 kurang lebih sama dengan apa yang saya lakukan di tutorial/tugas sebelumnya. Oleh karena itu, sebagian besar pekerjaan dilakukan dengan menyalin kode yang sudah ada lalu menyesuaikannya dengan kebutuhan baru. Misalnya, karena di tutorial 2 saya sudah membuat halaman `experience`, di tugas 2 saya hanya perlu menyalin kode tersebut (model, views, template, urls) kemudian diganti dengan fields dan elemen-elemen yang ada di `service`. Selain itu, karena saat ini halaman utama (main) dan halaman khusus per section desainnya sama, styling CSS pun juga disalin dan disesuaikan.

Selama pengerjaan tugas, saya menggunakan Claude sebagai alat bantu belajar, debugging, dan diskusi alur website.

- Saya menggunakan AI untuk memahami alur desain navigasi yang baik. Salah satu hasilnya adalah, keputusan membuat navigation bar di halaman utama yang hanya mengarah ke section preview (di halaman yang sama). Akses menuju page `experience.html` dan `service.html` disediakan lewat button `View more` di masing-masing bagian.
- Membantu bagaimana unit test bekerja dan debugging test yang gagal akibat perubahan model dan konten di template.

### Tugas 3

1. `ModelForm` digunakan karena `ModelForm` secara otomatis men-generate field input berdasarkan struktur model yang sudah didefinisikan (`Service`), termasuk validasi tipe data tanpa perlu ditulis ulang secara manual. Selain itu, `ModelForm` juga menyediakan method `.save()` yang langsung menyimpan data ke database sesuai model terkait, sehingga mengurangi risiko kesalahan penulisan dan duplikasi kode antara struktur form dan struktur model.

`{% csrf_token %}` wajib ditambahkan pada form karena Django menerapkan proteksi _Cross-Site Request Forgery_ (CSRF) secara default untuk setiap request yang mengubah data (POST, PUT, DELETE). Tag ini menghasilkan token unik yang disisipkan sebagai _hidden input_ pada form, lalu diverifikasi oleh server saat form disubmit. Tanpa token ini, server akan menolak request dengan error 403 Forbidden, karena tidak bisa memastikan request tersebut benar-benar berasal dari pengguna yang sah, bukan dari situs pihak ketiga yang mencoba mengeksekusi aksi atas nama pengguna tanpa sepengetahuannya.

2. JSON lebih disukai dibandingkan XML dalam pengembangan aplikasi web modern karena beberapa alasan. Pertama, JSON memiliki struktur yang lebih ringkas (tanpa closing tag yang berulang seperti XML), sehingga ukuran datanya lebih kecil. Kedua, JSON dapat langsung di-parse menjadi objek JavaScript tanpa proses parsing tambahan, sehingga lebih efisien digunakan pada aplikasi web yang berjalan di browser. Ketiga, hampir seluruh bahasa pemrograman modern (termasuk Python melalui modul `json`) memiliki dukungan bawaan untuk membaca dan menulis JSON, membuatnya menjadi format pertukaran data yang lebih universal dan mudah diintegrasikan dibandingkan XML yang cenderung lebih kompleks.

3. Pertama, _view_ mengambil data dari database melalui Django ORM (`Service.objects.all()`), yang hasilnya berisi objek-objek Python. Objek-objek ini tidak bisa langsung dikirim sebagai response HTTP karena format aslinya adalah objek Python, bukan teks. Oleh karena itu, dilakukan proses _serialization_ menggunakan `serializers.serialize("json", ...)`, yang mengubah setiap objek model menjadi representasi teks dalam format JSON (memuat nama model, primary key, dan nilai setiap field). Hasil serialisasi ini kemudian dikembalikan sebagai `HttpResponse` dengan `content_type="application/json"`. Pada `show_service`, teks JSON ini kemudian diambil kembali dan diubah balik menjadi objek Python melalui `serializers.deserialize`, sehingga datanya dapat diproses dan ditampilkan kembali di template menggunakan sintaks seperti `{{ service.title }}`.

### Tugas 4

Log Chat AI: https://claude.ai/share/8dac07a3-20c6-4a4e-b368-f13e1e24648d

#### Apa saja yang dikerjakan:

Menerapkan manajemen authorization, menambahkan peran editor via Django Admin, membatasi hak akses sesuai 4 role yang ada, menambah fitur `starred_by`, mengedit JSON supaya tetap sesuai ketentuan, dan menyesuaikan styling css untuk fitur-fitur baru yang ditambahkan

#### Penggunaan AI:

Untuk penerapan authentication, authorization, dan cookies di Django, saya berpatokan pada tutorial 4. Saya menggunakan generative AI (Claude) untuk membantu membuat fitur `starred_by` dan memahami tujuan di tugas 4 seperti membuat role editor, menambahkannya melalui admin, dan membantu debugging styling di css. Selain itu, supaya hasil yang diberikan AI sesuai kebutuhan, saya meminta AI untuk mengonfirmasi pemahamannya terlebih dahulu sebelum memberi solusi. Jika terdapat kekurangan informasi, maka saya bisa memberi konteks tambahan (ex: potongan kode, preferensi pribadi). Jika

## Bagian yang dibantu AI

1. Implementasi role editor menggunakan objek bawaan { perms }
2. Debugging masalah pada UI

## Keterbatasan AI

1. Beberapa saran AI tidak saya pakai, misalnya cara menyembunyikan tombol add/edit/delete dari role tertentu. Setelah saya coba tulis sendiri langsung di HTML, ternyata cara tersebut sudah cukup berjalan dengan baik, sehingga saya tidak jadi memakai saran AI.
2. Meski sudah saya minta untuk tidak membuat asumsi, AI kadang tetap memberi asumsi yang kurang sesuai karena kurangnya konteks yang saya berikan. Misalnya, saat membuat role admin, AI berasumsi editor juga bisa melakukan add/delete, padahal seharusnya editor hanya memiliki izin `can_change_service`. Karena itu, saya hanya mengambil bagian saran yang relevan dan menyesuaikan sisanya secara manual.
