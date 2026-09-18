# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/data/bcons_v2')
from shared import *

def proj_page(title, loc, price, status, badge_color, body_html, pfx='../'):
    sidebar = SIDEBAR
    page_body = f'''
<div class="ph">
  <div class="con">
    <p class="bc"><a href="{pfx}index.html">Trang chu</a> &raquo; <a href="index.html">Du An</a> &raquo; {title}</p>
    <h1>{title}</h1>
    <p>{loc} &nbsp;|&nbsp; <span style="background:{badge_color};padding:3px 12px;border-radius:12px;font-size:.85rem;color:#fff">{status}</span> &nbsp;|&nbsp; <strong>{price}</strong></p>
  </div>
</div>
<div class="pd">
  <div class="con">
    <div class="pd-layout">
      <main class="pm">{body_html}</main>
      {sidebar}
    </div>
  </div>
</div>
'''
    return wrap(title, page_body, pfx=pfx)

# ===== BCONS ASAHI =====
asahi_body = '''
<h2>BCONS ASAHI</h2>
<p><strong>Bcons Asahi</strong> la du an can ho dau tien duoi su hop tac giua Tap doan Bcons va doi tac Nhat Ban (Mecuria Investment). Nam toa lac tai mat tien duong Quoc lo 1K, phuong Dong Hoa, Thanh pho Ho Chi Minh, can ho chung cu Bcons Asahi (Green land Binh An) co quy mo xay dung 1 block, gom 496 can ho o ra thi truong.</p>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2025/09/tang1-bcons-asahi-scaled-1.jpg" alt="Mat bang tang 1" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2025/09/tang2-bcons-asahi-scaled-1.jpg" alt="Mat bang tang 2" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2025/09/tang-3-bcons-asahi-scaled-1.jpg" alt="Mat bang tang 3" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2025/09/tang-5-bcons-asahi-scaled-1.jpg" alt="Mat bang tang 5" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2025/09/thiet-ke-bcons-asahi-ql1k-1.jpg" alt="Thiet ke" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2025/09/thiet-ke-bcons-asahi-ql1k-6.jpg" alt="Thiet ke" loading="lazy"></a>
</div>
<h2>TONG QUAN DU AN</h2>
<table>
  <tr><th>Ten du an</th><td>Bcons Asahi (Green Land Binh An)</td></tr>
  <tr><th>Vi tri</th><td>QL1K, phuong Dong Hoa, TP. Ho Chi Minh</td></tr>
  <tr><th>Chu dau tu</th><td>Bcons &amp; Mecuria Investment (Quy dau tu Nhat Ban)</td></tr>
  <tr><th>Tong thau</th><td>Bcons Group</td></tr>
  <tr><th>Dien tich khu dat</th><td>3.233,64 m&#178;</td></tr>
  <tr><th>Quy mo</th><td>1 block cao 29 tang noi + 2 tang ham</td></tr>
  <tr><th>Tong so can</th><td>490 can ho o + 6 Shop House</td></tr>
  <tr><th>Tien ich</th><td>Ho boi vo cuc, vuon treo, shophouse, nha tre</td></tr>
  <tr><th>Du kien ban giao</th><td>Quy II/2027</td></tr>
  <tr><th>Gia ban</th><td>Tu 41 trieu/m&#178; &#8212; Can 1PN tu 1,5 ty dong</td></tr>
</table>
<h2>VI TRI DU AN</h2>
<p>Vi tri du an Bcons Asahi nam toa lac tren mat tien duong Quoc lo 1K (Hoang Cam), phuong Binh An, nay la phuong Dong Hoa, Thanh pho Ho Chi Minh.</p>
<ul>
  <li>Giao thong: ngay tren tuyen QL1K (Pham Van Dong noi dai), dai lo Vo Nguyen Giap, nha ga Suoi Tien Metro so 1</li>
  <li>Giao duc: sat DHQG TP.HCM, cac truong quoc te, Bschool lien cap mam non den dai hoc</li>
  <li>Tien ich: cho Dong Hoa, TTTM Bcons City, rap chieu phim, benh vien Hoan My, TTTM Go Di An</li>
  <li>Khong gian: huong loi tu mang xanh 600ha cua DHQG</li>
</ul>
<h2>CAC LOAI CAN HO</h2>
<ul>
  <li>Can 1 phong ngu: 35m&#178; va 39m&#178;</li>
  <li>Can 2 phong ngu: 48m&#178; &ndash; 52m&#178; &ndash; 54m&#178; &ndash; 60m&#178; &ndash; 69m&#178;</li>
  <li>Can 3 phong ngu: 74m&#178; va 76m&#178;</li>
</ul>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2025/09/thiet-ke-bcons-asahi-ql1k-2.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2025/09/thiet-ke-bcons-asahi-ql1k-3.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2025/09/thiet-ke-bcons-asahi-ql1k-4.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2025/09/thiet-ke-bcons-asahi-ql1k-5.jpg" alt="" loading="lazy"></a>
</div>
<h2>GIA BAN &amp; THANH TOAN</h2>
<p><strong>GIA BAN CHI TU 41 TRIEU/M&#178; &ndash; 1,5 TY/CAN HO</strong></p>
<ul>
  <li>Can 1PN: gia tu 1,5 ty/can</li>
  <li>Can 2PN: gia tu 1,99 ty/can</li>
</ul>
<h2>PHUONG THUC THANH TOAN</h2>
<ul>
  <li>Von tu co chi tu 15% khi KY HOP DONG MUA BAN</li>
  <li>Ho tro lai suat 0%/50% gia tri can ho den khi nhan ban giao</li>
  <li>Chiet khau khung/tong gia</li>
  <li>Ho tro vay toi 70&ndash;80% gia tri can ho</li>
</ul>
<h2>TIEN ICH</h2>
<ul>
  <li>Ho boi vo cuc</li>
  <li>Vuon tung Nhat</li>
  <li>Vuon hoa anh dao</li>
  <li>Khu vuc checkin theo mua</li>
  <li>Nha tre, trung tam thuong mai, shophouse, cong vien, vuon treo</li>
</ul>
<h2>PHAP LY</h2>
<ul>
  <li>Quyet dinh so 1059/QD-UBND ngay 10/05/2023 chap thuan chu truong dau tu</li>
  <li>Quyet dinh so 6694/QD-UBND ngay 30/10/2024 phe duyet quy hoach 1/500</li>
  <li>Giay chung nhan tham duyet PCCC so 1615/TD-PCCC ngay 13/06/2025</li>
  <li>Giay phep xay dung so 3707/GPXD ngay 27/06/2025</li>
</ul>
<h2>CO NEN MUA BCONS ASAHI KHONG?</h2>
<p><strong>Co</strong>, vi:</p>
<ul>
  <li>Nam tren mat tien QL1K, lien ke Metro, Lang Dai Hoc, KCN Cao &ndash; khai thac cho thue tot</li>
  <li>Phuong an thanh toan ban dau it, ho tro lai suat, ho tro vay 70%</li>
  <li>Muc gia ban de tiep can nhat khu vuc: 1,5 ty/can (41tr/m&#178;)</li>
  <li>Du an dau tien hop tac Nhat Ban, von nuoc ngoai, dam bao tien do</li>
  <li>Chu dau tu uy tin: 15 du an tai Di An, day du phap ly, xay dung dung tien do</li>
</ul>
<h2>FAQ</h2>
<p><strong>Gia ban bao nhieu?</strong> Don gia tu 41 trieu/m&#178;. Can 1PN tu 1,5 ty; Can 2PN tu 1,99 ty.</p>
<p><strong>Bao gio ban giao nha?</strong> Du kien Quy 2/2027.</p>
<p><strong>Vi tri o dau?</strong> Mat tien QL1K, ke ben DHQG va tuyen Metro so 1.</p>
'''

with open(f'{OUT}/du-an/bcons-asahi.html', 'w', encoding='utf-8') as f:
    f.write(proj_page('Bcons ASAHI', 'QL1K, Dong Hoa, TP.HCM', 'Tu 1,5 Ty/can - 41tr/m2', 'Dang mo ban', '#25a244', asahi_body))
print('OK bcons-asahi.html')

# ===== BCONS CENTRAL PARK =====
cp_body = '''
<h2>BCONS CENTRAL PARK</h2>
<img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1787554246410_1027907227192204778_g6752788579839982367_6ae57fb79727cca86e1c2a5d14aa0a36.jpg" alt="Bcons Central Park" style="width:100%;border-radius:10px;margin-bottom:18px" loading="lazy" onerror="this.style.display='none'">
<p><strong>BCONS CENTRAL PARK</strong> (Du an can ho cao tang Bcons Tam Hiep) la du an nha o tiep theo cua Tap doan Bcons Group tai phuong Tam Hiep, Thanh pho Dong Nai. Du an duoc quy hoach tren quy dat rong gan 3ha, ngay nut giao Phan Trung va Duong Tu Giang, trung tam TP Bien Hoa cu.</p>
<h2>TONG QUAN DU AN</h2>
<table>
  <tr><th>Ten du an</th><td>Bcons Central Park</td></tr>
  <tr><th>Ten phap ly</th><td>Khu Nha O Phuc Hop Cao Tang Phuong Tam Hiep</td></tr>
  <tr><th>Vi tri</th><td>236 duong Phan Trung, Phuong Tam Hiep, TP. Dong Nai</td></tr>
  <tr><th>Chu dau tu</th><td>Tap doan Bcons Group</td></tr>
  <tr><th>Don vi phan phoi</th><td>Cong Ty Co Phan BDS Bcons Homes</td></tr>
  <tr><th>Quy dat</th><td>2,7 ha</td></tr>
  <tr><th>Quy mo</th><td>5 block cao 22 tang + 2 tang ham</td></tr>
  <tr><th>Tong san pham</th><td>2.820 can ho + 113 can TMDV (Shop House)</td></tr>
  <tr><th>Tong von dau tu</th><td>4.500 ty dong</td></tr>
  <tr><th>Khoi cong</th><td>27/05/2026</td></tr>
  <tr><th>Du kien ban giao</th><td>Quy II/2029</td></tr>
  <tr><th>Gia ban</th><td>Tu 49,9 trieu/m&#178;</td></tr>
</table>
<h2>LOI THE VI TRI</h2>
<ul>
  <li><strong>Tam diem ket noi:</strong> Cach TP.HCM, san bay Tan Son Nhat, san bay Long Thanh chung 30&ndash;35 phut</li>
  <li><strong>Don bay tang gia tu Metro va Vanh dai 3:</strong> Nam sat cac truc giao thong huyet mach</li>
  <li><strong>Quy dat vang 2,6ha:</strong> Hiem hoi tai vung loi trung tam Bien Hoa</li>
  <li>Chi 2&ndash;5 phut: Vincom Plaza Bien Hoa, Benh vien Da khoa Dong Nai</li>
  <li>Chi 10&ndash;15 phut: Truong hoc, trung tam hanh chinh, khu vui choi</li>
</ul>
<h2>MAT BANG THIET KE</h2>
<p>Du an cung ung ra thi truong khoang 2.820 can ho voi co cau san pham:</p>
<ul>
  <li>Can ho Studio: 37&ndash;40m&#178;</li>
  <li>Can ho 1PN1WC: 43m&#178;</li>
  <li>Can ho 2PN1WC: 50&ndash;53m&#178;</li>
  <li>Can ho 2PN2WC: 60&ndash;73m&#178;</li>
  <li>Can ho 3PN2WC: 87&ndash;88m&#178;</li>
</ul>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/2-682x1024.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/3-682x1024.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/4-682x1024.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/5-682x1024.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/6-682x1024.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/7-682x1024.jpg" alt="" loading="lazy"></a>
</div>
<h2>TIEN ICH DANG CAP</h2>
<p>Bcons Central Park so huu he sinh thai khep kin voi <strong>60 hang muc tien ich</strong>:</p>
<ul>
  <li>To hop mat nuoc chuan 5 sao: ho boi resort, ho massage, ho boi tre em</li>
  <li>Quang truong anh sang, khu vuon canh quan xanh mat</li>
  <li>Khu chieu phim ngoai troi, khu BBQ</li>
  <li>Tuyen pho thuong mai sam uat</li>
  <li>Nha tre B.School, san choi nghe thuat</li>
  <li>Khu may tap ngoai troi, khu van dong da nang</li>
</ul>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/Tien-ich-Bcons-Central-Park.jpg" alt="Tien ich" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/25.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/24.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/23.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/22.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/21.jpg" alt="" loading="lazy"></a>
</div>
<h2>NHA MAU</h2>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/40.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/39.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/38.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/37.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/36.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/35.jpg" alt="" loading="lazy"></a>
</div>
<h2>PHUONG THUC THANH TOAN</h2>
<ul>
  <li><strong>PT1 &ndash; Tien do:</strong> Chiet khau 8,5%</li>
  <li><strong>PT2 &ndash; Vay NH:</strong> Von tu co 20%, ho tro 0% lai suat trong 24 thang</li>
  <li><strong>PT3 &ndash; Vay NH:</strong> Von tu co 10% ky HDMB, CDT cam ket lai suat 6,9% trong 4 nam</li>
</ul>
<div class="gal g2">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/PTTT-1.jpg" alt="Phuong thuc 1" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/PTTT-2.jpg" alt="Phuong thuc 2" loading="lazy"></a>
</div>
<h2>PHAP LY</h2>
<ul>
  <li>Bang cam ket ten du an</li>
  <li>Thong tin trien khai Khu nha o phuc hop cao tang phuong Tam Hiep</li>
  <li>Giay phep xay dung day du</li>
</ul>
'''
with open(f'{OUT}/du-an/bcons-central-park.html', 'w', encoding='utf-8') as f:
    f.write(proj_page('Bcons Central Park', '236 Phan Trung, Tam Hiep, Bien Hoa', 'Tu 49,9tr/m2', 'Dang mo ban', '#25a244', cp_body))
print('OK bcons-central-park.html')

# ===== BCONS ARIA =====
aria_body = '''
<h2>BCONS ARIA</h2>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/Phoi-canh-6-1-scaled.jpg" alt="Phoi canh" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/Phoi-canh-5-1-scaled.jpg" alt="Phoi canh" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/Phoi-canh-4-1-scaled.jpg" alt="Phoi canh" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/Phoi-canh-3-1-scaled.jpg" alt="Phoi canh" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/Phoi-canh-2-1-scaled.jpg" alt="Phoi canh" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/Phoi-canh-1-1-scaled.jpg" alt="Phoi canh" loading="lazy"></a>
</div>
<p><strong>Bcons Aria</strong> (Khu nha o cao tang Ngoi Sao Hoang Nam) la san pham can ho tiep theo cua Tap doan Bcons trien khai tren truc duong Ba Huyen Thanh Quan, Phuong Dong Hoa, Thanh Pho Ho Chi Minh. Duoc xay dung voi quy mo 2 block thap srung sung cao 37 tang, cung ung ra thi truong 1.274 san pham can ho hien dai.</p>
<h2>TONG QUAN DU AN</h2>
<table>
  <tr><th>Ten du an</th><td>Bcons Aria (Hoang Nam Ngoi Sao)</td></tr>
  <tr><th>Vi tri</th><td>Duong Ba Huyen Thanh Quan, phuong Dong Hoa, TP.HCM</td></tr>
  <tr><th>Chu dau tu</th><td>Tap doan Bcons</td></tr>
  <tr><th>Quy dat</th><td>7.877m&#178;</td></tr>
  <tr><th>Quy mo</th><td>1 Block thuong mai cao 37 tang + 1 tang ham</td></tr>
  <tr><th>San pham</th><td>1.274 can ho tieu chuan, can ho 2PN</td></tr>
  <tr><th>Tien ich</th><td>Ho boi, bai sac xe dien, nha tre, cong vien</td></tr>
  <tr><th>Du kien ban giao</th><td>Quy 4/2028</td></tr>
  <tr><th>Gia ban</th><td>Chi 46tr/m&#178;</td></tr>
  <tr><th>Phap ly</th><td>So hong so huu lau dai</td></tr>
</table>
<h2>VI TRI DU AN</h2>
<img src="https://bconsgroup.vn/wp-content/uploads/2026/08/Hoa-Do-Vi-Tri-1-scaled.jpg" alt="Vi tri Bcons Aria" loading="lazy" style="width:100%;border-radius:10px;margin-bottom:14px" onerror="this.style.display='none'">
<ul>
  <li>Trung tam TP.HCM: 25&ndash;35 phut qua Pham Van Dong, Vo Nguyen Giap, Vanh Dai 3, Metro so 1</li>
  <li>Khu do thi Bcons City: lien ke, huong tron tien ich</li>
  <li>Trung tam thuong mai: 5&ndash;10 phut den Bcons City Mall, sieu thi Go!, Vincom Plaza</li>
  <li>Lang dai hoc Quoc gia TP.HCM: gan ke</li>
</ul>
<h2>TIEN ICH 55 HANG MUC</h2>
<ul>
  <li>Ho boi vo cuc, ho boi tre em, khu ngam hoang hon</li>
  <li>Khu Anh Duong, phong Yoga, khu tap the duc ngoai troi</li>
  <li>San Billiards, bi lac, bong ban</li>
  <li>Nha tre B.School, san choi kham pha</li>
  <li>Vuon canh quan nhiet doi, Vuon tuong vi hoang gia, Vuon truc thanh tinh</li>
  <li>Sky Gardens, Family Gardens</li>
  <li>Pho thuong mai Infinity, khu BBQ ngoai troi</li>
  <li>Tram sac o to dien, xe may dien</li>
</ul>
<img src="https://bconsgroup.vn/wp-content/uploads/2026/08/Mat-bang-Tong-the-Tien-ich-scaled.jpg" alt="Mat bang tien ich" loading="lazy" style="width:100%;border-radius:10px;margin:14px 0" onerror="this.style.display='none'">
<h2>MAT BANG THIET KE</h2>
<p>Du an cung ung 1.274 san pham can ho 2PN voi da dang dien tich: <strong>52&ndash;67m&#178;</strong></p>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/MB-tang-04-1-scaled.jpg" alt="Mat bang tang 4" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/MB-tang-05-1-scaled.jpg" alt="Mat bang tang 5" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/MB-tang-06-14-1-scaled.jpg" alt="Mat bang tang 6-14" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/MB-tang-15-23-1-scaled.jpg" alt="Mat bang tang 15-23" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/MB-tang-24-30-1-scaled.jpg" alt="Mat bang tang 24-30" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/MB-tang-31-37-1-scaled.jpg" alt="Mat bang tang 31-37" loading="lazy"></a>
</div>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/260207_HopDenCanHoB-1.jpg" alt="Layout B" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/260207_HopDenCanHoC-1.jpg" alt="Layout C" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/260207_HopDenCanHoD-1.jpg" alt="Layout D" loading="lazy"></a>
</div>
<h2>NHA MAU BCONS ARIA</h2>
<p>Nha mau nam ngay tai TTTM Bcons City. Can ho ban giao hoan thien + noi that co ban:</p>
<ul>
  <li>Phong khach: cua thep chong chay khoa tu van tay, gach bong kinh 60x60, tran thach cao, den am tran</li>
  <li>Phong bep: tu bep tren va duoi, mat da, bon rua, may loc nuoc</li>
  <li>Phong ngu: san go cong nghiep, tran thach cao</li>
  <li>Phong tam: thiet bi day du kem buong tam kinh dung</li>
</ul>
<h2>PHUONG THUC THANH TOAN</h2>
<ul>
  <li>PT1: Theo tien do, uu dai 8,5%</li>
  <li>PT2: Vay NH, von tu co 20%, lai suat 0% trong 24 thang</li>
  <li>PT3: Von tu co 10%, CDT cam ket lai suat 6,9% trong 4 nam</li>
  <li>PT4: Von tu co 10%, ho tro 0% lai suat 24 thang, tra cham 1%/thang</li>
</ul>
<h2>PHAP LY</h2>
<ul>
  <li>Chap thuan chu truong dau tu du an Bcons Hoang Nam Ngoi Sao</li>
  <li>Quyet dinh cho phep chuyen doi muc dich su dung dat</li>
  <li>Phe duyet quy hoach 1/500</li>
</ul>
'''
with open(f'{OUT}/du-an/bcons-aria.html', 'w', encoding='utf-8') as f:
    f.write(proj_page('Bcons Aria', 'Ba Huyen Thanh Quan, Dong Hoa, TP.HCM', '46tr/m2', 'Dang booking', '#d4802a', aria_body))
print('OK bcons-aria.html')

# ===== GENERIC PROJECTS =====
generic = [
  ('bcons-center-city', 'Bcons Center City', 'TP. Di An, Binh Duong', '55tr/m2', 'Mo ban', '#25a244',
   'Khu do thi phuc hop, 5 block cao 29&ndash;36 tang, 1.800&ndash;1.940 can ho. Quy mo 3,2 ha. Ket hop can ho, thuong mai, dich vu. Phu hop ca an cu va dau tu.',
   []),
  ('bcons-city', 'Bcons City', 'TP. Di An, Binh Duong', '34&ndash;43tr/m2', 'Ban giao &amp; Mo ban', '#25a244',
   'Dai do thi quy mo lon, bao gom nhieu thap: Green Diamond, Green Sapphire, Green Topaz, Green Emerald. TTTM 3 tang, khach san 4 sao, truong hoc lien cap. Da ban giao nhieu thap, co so hong.',
   []),
  ('bcons-solary', 'Bcons Solary', 'Phuong Tan Dong Hiep, TP.HCM', '31tr/m2', 'Mo ban', '#25a244',
   'Can ho cao cap nam gan tuyen duong Vanh Dai 3, cach Metro so 1 khoang 350m, ngay cong Khu cong nghiep Tan Dong Hiep.',
   []),
  ('bcons-new-sky', 'Bcons New Sky', 'QL13, Lai Thieu, Thuan An, Binh Duong', '48,3tr/m2', 'Mo ban', '#25a244',
   'Can ho cao cap tai mat tien Quoc lo 13, phuong Lai Thieu, TP. Thuan An, Binh Duong. Vi tri chien luoc tren truc giao thong huyet mach ket noi TP.HCM va cac khu vuc trong diem.',
   []),
  ('bcons-city-life', 'Bcons City Life', 'TP. Tan Uyen, Binh Duong', '2,5&ndash;4 ty/can', 'Mo ban', '#25a244',
   'Du an nha pho thuong mai dau tien cua Tap doan Bcons. Toa lac tren duong To Huu (DH 412) &ndash; truc duong huyet mach ket noi cac khu cong nghiep lon. Quy mo 4,68 ha, 348 san pham da dang bao gom shophouse va dat nen.',
   []),
  ('bcons-avenue', 'Bcons Avenue', 'Xa lo Ha Noi, Binh Thang, Di An, Binh Duong', 'Lien he', 'Mo ban', '#25a244',
   'Can ho cao cap tai mat tien duong Xa lo Ha Noi, lien ke tuyen Metro Ben Thanh&ndash;Suoi Tien va Ben xe Mien Dong moi. Don dau xu huong T.O.D (phat trien do thi theo co so ha tang giao thong cong cong).',
   []),
  ('bcons-polaris', 'Bcons Polaris', 'Le Trong Tan, An Binh, Di An, Binh Duong', 'Lien he', 'Da ban giao', '#888',
   'Can ho cao cap tai mat tien duong Le Trong Tan, phuong An Binh, TP. Di An, lien ke truc duong Pham Van Dong, TP. Thu Duc. Da ban giao cho cu dan.',
   []),
  ('bcons-bee', 'Bcons Bee', 'Di An, Binh Duong', 'Lien he', 'Da ban giao &amp; So hong', '#888',
   'Du an da hoan thanh ban giao va cu dan da duoc cap so hong so huu lau dai. Nam trong he sinh thai bat dong san Bcons tai Di An.',
   []),
]

for slug, title, loc, price, status, badge, desc, imgs in generic:
    body = f'<h2>{title}</h2>\n<p>{desc}</p>\n'
    body += f'<h2>THONG TIN DU AN</h2>\n<table>\n'
    body += f'<tr><th>Ten du an</th><td>{title}</td></tr>\n'
    body += f'<tr><th>Vi tri</th><td>{loc}</td></tr>\n'
    body += f'<tr><th>Chu dau tu</th><td>Tap doan Bcons Group</td></tr>\n'
    body += f'<tr><th>Trang thai</th><td>{status}</td></tr>\n'
    body += f'<tr><th>Gia ban</th><td>{price}</td></tr>\n'
    body += f'</table>\n'
    body += f'<h2>LIEN HE DE BIET THEM CHI TIET</h2>\n'
    body += f'<p>De nhan thong tin chi tiet ve du an <strong>{title}</strong>, bang gia va chinh sach uu dai moi nhat, quy khach vui long lien he hotline <strong>0909 2222 54</strong> hoac dang ky tu van qua form ben phai.</p>\n'
    with open(f'{OUT}/du-an/{slug}.html', 'w', encoding='utf-8') as fh:
        fh.write(proj_page(title, loc, price, status, badge, body))
    print(f'OK {slug}.html')

# ===== DU AN INDEX =====
all_proj = [
  ('bcons-central-park','Bcons Central Park','Bien Hoa, Dong Nai','49,9tr/m2','Dang mo ban','https://bconsgroup.vn/wp-content/uploads/2026/08/1787554246410_1027907227192204778_g6752788579839982367_6ae57fb79727cca86e1c2a5d14aa0a36.jpg','Khu can ho bieu tuong tai Bien Hoa, 5 block 22 tang, 2.820 can ho.'),
  ('bcons-aria','Bcons Aria','Dong Hoa, TP.HCM','46tr/m2','Dang booking','https://bconsgroup.vn/wp-content/uploads/2026/08/Phoi-canh-6-1-scaled.jpg','Can ho 37 tang lien ke TP. Thu Duc, 1.274 can ho, gan Metro so 1.'),
  ('bcons-asahi','Bcons Asahi','Dong Hoa, TP.HCM','Tu 1,5 ty/can','Dang mo ban','','Can ho chuan Nhat, mat tien QL1K, 490 can ho, lien ke Metro &amp; DHQG.'),
  ('bcons-center-city','Bcons Center City','Di An, Binh Duong','55tr/m2','Mo ban','','Khu do thi phuc hop 5 block, 1.800&ndash;1.940 can ho, ket hop TM&amp;DV.'),
  ('bcons-city','Bcons City','Di An, Binh Duong','34&ndash;43tr/m2','Ban giao &amp; Mo ban','','Dai do thi quy mo lon, nhieu thap, da co so hong, TTTM, khach san 4 sao.'),
  ('bcons-solary','Bcons Solary','Tan Dong Hiep, TP.HCM','31tr/m2','Mo ban','','Nam gan Vanh Dai 3, cach Metro so 1 khoang 350m, ngay KCN Tan Dong Hiep.'),
  ('bcons-new-sky','Bcons New Sky','Thuan An, Binh Duong','48,3tr/m2','Mo ban','','Mat tien QL13, vi tri chien luoc ket noi TP.HCM.'),
  ('bcons-city-life','Bcons City Life','Tan Uyen, Binh Duong','2,5&ndash;4 ty/can','Mo ban','https://bconsgroup.vn/wp-content/uploads/2024/11/Phoi-canh-thuc-te-bcons-city-life.jpg','Nha pho thuong mai dau tien cua Bcons, quy mo 4,68 ha, 348 san pham.'),
  ('bcons-avenue','Bcons Avenue','Di An, Binh Duong','Lien he','Mo ban','','Mat tien Xa lo Ha Noi, lien ke Metro, don dau xu huong T.O.D.'),
  ('bcons-polaris','Bcons Polaris','Di An, Binh Duong','Lien he','Da ban giao','','Mat tien Le Trong Tan, lien ke Pham Van Dong. Da ban giao.'),
  ('bcons-bee','Bcons Bee','Di An, Binh Duong','Lien he','Da ban giao &amp; So hong','','Da hoan thanh ban giao, cu dan da co so hong so huu lau dai.'),
]
cards = ''.join(f'''
<div class="pc">
  <div class="pc-thumb">
    {'<img src="' + img + '" alt="' + t + '" loading="lazy" onerror="this.style.display=\'none\'">' if img else '<div class="pc-ph" style="background:linear-gradient(135deg,var(--navy),#1a4a7a)">&#127970;<br>' + t + '</div>'}
    <span class="pc-badge">{st}</span>
  </div>
  <div class="pc-body">
    <h3>{t}</h3>
    <p>{desc}</p>
    <div class="pc-meta"><span>&#128205; {loc}</span><span>&#128176; {price}</span></div>
    <a href="{slug}.html" class="pc-link">Xem Chi Tiet &rarr;</a>
  </div>
</div>''' for slug,t,loc,price,st,img,desc in all_proj)

du_an_idx = wrap('Tat Ca Du An', f'''
<div class="ph">
  <div class="con">
    <h1>TAT CA DU AN BCONS GROUP</h1>
    <p>Danh sach cac du an bat dong san dang va da trien khai</p>
  </div>
</div>
<section class="sec">
  <div class="con">
    <div class="pg">{cards}</div>
  </div>
</section>
''', pfx='../')
with open(f'{OUT}/du-an/index.html', 'w', encoding='utf-8') as f:
    f.write(du_an_idx)
print('OK du-an/index.html')
print('=== PROJECTS DONE ===')
