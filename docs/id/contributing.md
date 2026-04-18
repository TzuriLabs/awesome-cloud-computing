# Kontribusi

Kontribusi selalu diterima.

## Panduan

- Tambahkan sumber daya ke file markdown yang sesuai di direktori `docs/en/`.
- Gunakan format tabel: `| [Nama](https://example.com) | Deskripsi singkat. |`
- Jaga deskripsi tetap ringkas dan faktual.
- Pastikan tautan berfungsi dan mengarah ke sumber daya yang sah.
- Gunakan URL bersih tanpa garis miring di akhir untuk beranda: `https://example.com` bukan `https://example.com/`
- Tambahkan bagian baru hanya jika diperlukan.

## Pull Request

- Jaga PR tetap fokus: satu perubahan logika utama per PR.
- Gunakan judul yang jelas, misalnya: `Add Terraform to infrastructure tools`.
- Uji perubahan Anda secara lokal jika memungkinkan menggunakan `just dev`.

## Organisasi Konten

- **Konten utama** ada di direktori `docs/en/`
- **Website** dibangun dari file markdown ini
- **README.md** berfungsi sebagai halaman arahan yang mengarah ke website
- Perubahan ke `docs/en/` secara otomatis memperbarui website

## Isu

- Gunakan isu untuk melaporkan tautan rusak, kesalahan, atau saran.
- Berikan deskripsi yang singkat dan jelas.

## Pengaturan Pengembangan

Pengaturan lokal hanya diperlukan jika Anda ingin melihat pratinjau situs atau mengerjakan perubahan yang lebih besar.

### Prasyarat

- Instal [`uv`](https://docs.astral.sh/uv) (manajer paket Python):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Instal [`lychee`](https://github.com/lycheeverse/lychee) (pemeriksa tautan)

```bash
cargo install lychee
```

> **Catatan**: Anda perlu menginstal `cargo` terlebih dahulu: `curl https://sh.rustup.rs -sSf | sh`
> Atau baca [panduan](https://doc.rust-lang.org/cargo/getting-started/installation.html).

### Pengaturan

**1. Fork dan clone repositori:**

```bash
git clone https://github.com/YOUR_USERNAME/awesome-cloud-computing.git && cd awesome-cloud-computing
```

**2. Atur lingkungan Python (Python 3.13):**

Opsi A - Otomatis (Direkomendasikan):

```bash
uv sync --extra dev
```

Opsi B - Lingkungan virtual manual:

```bash
uv venv --python 3.13
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

**3. Mulai server pengembangan:**

```bash
uv run mkdocs serve
```

Situs akan tersedia di `http://127.0.0.1:8000`

### Opsional: Instal justfile untuk perintah yang lebih mudah

Jika Anda ingin menggunakan task runner untuk kenyamanan:

```bash
# On macOS: brew install just
# On Linux: cargo install just
# Atau kunjungi: https://github.com/casey/just#installation

# Kemudian Anda dapat menggunakan:
just dev              # Mulai server pengembangan
just lint             # Jalankan pemeriksaan kualitas (cepat, tanpa pemeriksaan tautan)
just check-links      # Periksa tautan rusak saja
just check-all        # Jalankan semua pemeriksaan termasuk tautan (lebih lambat)
just create-lang <code_lang> # Buat struktur bahasa baru
just install-hooks    # Instal pre-commit hooks
```

### Perintah Manual

Tanpa justfile, Anda dapat menjalankan perintah secara langsung:

```bash
# Mulai server pengembangan
uv run mkdocs serve
```

```bash
# Jalankan semua pemeriksaan kualitas (termasuk linting markdown)
uv run pre-commit run --all-files
```

```bash
# Periksa tautan rusak saja
lychee docs/en/**/*.md
```

```bash
# Buat bahasa baru
uv run python scripts/create-language.py <code_lang>
```

### Pre-commit Hooks (Opsional)

Untuk menjalankan pemeriksaan kualitas secara otomatis sebelum setiap commit:

```bash
# Instal pre-commit hooks
uv run pre-commit install
```

```bash
# Jalankan semua pemeriksaan (kecuali pemeriksaan tautan untuk performa)
uv run pre-commit run --all-files
```

Pre-commit hooks akan secara otomatis:

- Memperbaiki spasi di akhir baris dan masalah akhir file
- Memeriksa format markdown dengan markdownlint
- Memformat kode Python dengan ruff
- Memformat file lain dengan prettier

**Catatan**: Pemeriksaan tautan ditangani secara terpisah melalui `just check-links` untuk performa yang lebih baik.

### Pengaturan Alternatif

Jika Anda tidak ingin menggunakan uv:

```bash
# Buat lingkungan virtual
python -m venv venv
source venv/bin/activate  # Di Windows: venv\Scripts\activate

# Instal dependensi
pip install -e ".[dev]"

# Mulai server pengembangan
mkdocs serve
```

## Menambahkan Terjemahan

Untuk menambahkan bahasa baru:

```bash
just create-lang es
just sync-langs

# Atau secara manual

python scripts/create-language.py es
python scripts/sync-languages.py
```

## Pemeriksaan Kualitas

```bash
just lint
just check-links

# Atau secara manual

markdownlint README.md docs/**/*.md
lychee README.md docs/en/**/*.md
```
