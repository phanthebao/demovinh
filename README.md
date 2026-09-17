# Web bất động sản – mẫu batdongsan03 (clone)

Website tĩnh 1 file, không cần build, không cần internet.

## Cách dùng
1. Giải nén thư mục `batdongsan03`.
2. Mở `index.html` bằng Chrome/Edge là chạy được ngay.
3. Upload cả thư mục (index.html + assets/) lên hosting / Netlify / Vercel / GitHub Pages là live.

## Cấu trúc
- `index.html` — toàn bộ HTML + CSS + JS (vanilla, không thư viện ngoài).
- `assets/` — 5 ảnh demo: `hero.jpg`, `canho.jpg`, `biethu.jpg`, `shophouse.jpg`, `noithat.jpg`.

## Các khối đã dựng
Topbar (hotline/email/giờ làm việc) → header sticky + menu 7 mục + nút "Ký gửi nhà đất" →
hero slider 3 slide (tự chạy 6s, có dots) → thanh tìm kiếm nổi (tab Bán / Cho thuê / Dự án + 4 bộ lọc) →
danh mục 6 loại hình → dự án đang mở bán (3 card overlay) → sản phẩm nổi bật (lọc Tất cả/Bán/Cho thuê, 6 card) →
dải số liệu (counter chạy số) → vì sao chọn chúng tôi (ảnh + badge 98% + 4 lợi thế) →
tin tức 3 bài → form "Yêu cầu gọi lại" → footer 4 cột + bottom bar.
Ngoài ra: nút nổi gọi/Zalo/back-to-top, popup đăng ký tư vấn, hiệu ứng reveal khi scroll, responsive 1280/1140/1080/960/640px.

## Chỗ cần sửa khi dùng thật
- Tìm & thay `0909 123 456`, `info@anphuland.vn`, địa chỉ, tên "AN PHÚ LAND".
- Thay ảnh trong `assets/` (giữ nguyên tên file là không cần sửa code).
- Form hiện chỉ hiện thông báo thành công ở client — muốn nhận data thì trỏ `#ctaForm` / `#modalForm` sang API, Google Form hoặc Formspree.
- Màu thương hiệu sửa ở khối `:root` đầu file (`--navy`, `--blue`, `--amber`...).
