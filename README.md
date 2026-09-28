Nama : Muhammad Wildan Firdaus

NPM : 2506595985

Kelas : PBP F

### Set-up
1. Download folder myportofolio, kemudian jalankan "cd myportofolio" dalam terminal untuk membuka foldernya
2. Jalankan "python -m venv env" pada Windows, atau "python3 -m venv env" pada Linux atau macOS untuk membuat Virtual Environment.
3. Jalankan "env\Scripts\activate" pada Windows, atau "source env/bin/activate" pada Linux atau macOS untuk mengaktifkan Virtual Environment
4. Jalankan "pip install -r requirements.txt", buat berkas .env dan isi dengan "PRODUCTION=False", lalu jalankan "python manage.py check" untuk memastikan apakah semua sudah benar.
5. Jalankan "python manage.py migrate" dan "python manage.py runserver" sebelum membuka website dengan membuka "http://localhost:8000/"
6. Untuk mematikan server, tekan Ctrl+C pada Windows atau Linux atau Control+C pada macOS.
7. Untuk mematikan Virtual Environment, jalankan "deactivate"

### Tugas 1
1. Iya saya menggunakan elemen semantik tersebut. Elemen seperti <section> membantu saya dalam mengelompokkan bagian-bagian website static portofolio saya.
2. Sejauh ini saya masih memprioritaskan fungsionalitas dikarenakan saya belum terpikir design overall dari website saya. Dalam membuat design (yang mungkin sementara) ini, saya beberapa kali mencoba mengubah beberapa hal dan melihat hasilnya (trial and error)
3. Sejauh ini, saya belum menghadapi kesulitan dalam menyajikan informasi di portofolio saya. Terkait dynamic website, saya tertarik dengan bagaimana fungsi-fungsi dinamis bisa memungkinkan saya untuk membuat portofolio somehow lebih interaktif

AI disclosure: Selama mengerjakan tugas 1, saya hanya menggunakan Copilot untuk auto-complete beberapa code repetitif. Saya menggunakan w3shools untuk mayoritas proses trial and error saya.

### Tugas 2
1. membuka url di browser, portofolio/urls.py menya,bungkan ke main/urls.py yang mencari "" lalu menjalankan 'show_main' method dari views. Method lalu mengirimkan context2 dan model kepada template yang lalu akan digunakan untuk ditampilkan.
2. Karena model memudahkan kita untuk mengupdate informasi baru dibandingkan dengan mengubah seluruh instance informasi tersebut muncul dalam web
3. 'makemigrations' akan membuat file migration baru dan 'migrate' akan mengaplikasikan file tersebut kedalam program. Salah satu saat dimana method ini digunakan adalah saat menambah model. di contoh saya, saat menambah class 'Education' saya membuat migration baru.

AI disclosure: Selama mengerjakan tugas 2, saya hanya menggunakan sedikit AI overview pada masalah-masalah yang saya alami, salah satunya saat saya lupa makemigrations.

### Tugas 3
1. karena ModelForm akan memudahkan kita dalam pembuatan web dengan menghubungkan form dengan database model. {% csrf_token %} wajib ditambahkan untuk memproteksi akses web dari pihak yang tidak berwenang.
2. karena bentuk file JSON lebih mudah dibaca mata manusia dan karena tidak adanya tag penutup, ukuran file JSON lebih kecil dibandingkan file XML yang akan mempersingkat waktu parsing
3. membuat object, misalnya 'projects', yang merupakan semua object 'Project' dalam database. Kemudian, serialization digunakan untuk mengubah bentuk object menjadi format JSON. Lalu mengirim respon dalam bentuk HTTP kepada client

AI disclosure: Saya menggunakan gemini untuk menjelaskan beberapa poin dalam tutorial 3, seperti implementasi JSON database

### Tugas 4
AI disclosure: Saya menggunakan beberapa dokumentasi dan juga Gemini untuk membantu saya dalam hal Django group dan permission. Saya tidak terlalu menggunakan AI dalam generate kode karena mayoritas memakai ulang kode yang sudah ada. Dokumentasi juga membantu saya dalam membuat group dan permission.