# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/data/bcons_v2')
from shared import *

def art_page(title, date, cat, body_html, pfx='../'):
    sidebar = SIDEBAR
    content = f'''
<div class="ph">
  <div class="con">
    <p class="bc"><a href="{pfx}index.html">Trang chu</a> &raquo; <a href="{pfx}tin-tuc.html">Tin Tuc</a> &raquo; {title}</p>
    <h1 class="art-title">{title}</h1>
    <div class="art-meta"><span>{cat}</span><span>{date}</span></div>
  </div>
</div>
<div class="pd">
  <div class="con">
    <div class="art-layout">
      <article class="art-body">{body_html}</article>
      {sidebar}
    </div>
  </div>
</div>
'''
    return wrap(title, content, pfx=pfx)

# ===== BAI 1: KHAI TRUONG NHA MAU =====
art1 = art_page(
    'Khai Truong Nha Mau Bcons Central Park Bien Hoa: Hut Khach Nho Khong Gian Toi Uu &amp; Gia Tu 49,9 Trieu/m2',
    '12/09/2026', 'Tin Tuc Du An',
    '''
<img src="https://bconsgroup.vn/wp-content/uploads/2026/09/40.jpg" alt="Nha mau Bcons Central Park" style="width:100%;border-radius:10px;margin-bottom:18px" loading="lazy">
<p>Ngay 06/09/2026, khu nha mau du an can ho cao tang Bcons Central Park chinh thuc mo cua tai Bcons City Center &mdash; trung tam mua sam, van hoa, giai tri hang dau tai Di An. Su kien thu hut hang ngan nguoi tham quan, nhan dien va trai nghiem truc tiep khong gian song noi troi cung cap boi Tap doan Bcons Group.</p>
<h2>BCONS CENTRAL PARK &mdash; DU AN CAN HO BAT DONG SAN MOI NHAT 2026 CUA BCONS</h2>
<p>Bcons Central Park la du an bat dong san moi nhat nam 2026 cua Tap doan Bcons Group. Du an noa lac tai 236 duong Phan Trung, Phuong Tam Hiep, Thanh pho Bien Hoa (Dong Nai). Du kien khi hoan thanh, du an se mang lai nguon cung can ho dat tieu chuan cao cho khu vuc, dong gop tich cuc vao su phat trien cua do thi Bien Hoa.</p>
<h3>Quy Mo Xay Dung</h3>
<ul>
  <li>Quy dat: gan 3 ha tai trung tam hanh chinh cu cua Bien Hoa</li>
  <li>5 block cao 22 tang + 2 tang ham</li>
  <li>2.820 can ho + 113 can TMDV (shophouse)</li>
  <li>Tong von dau tu: 4.500 ty dong</li>
  <li>Khoi cong: 27/05/2026 | Ban giao: Quy II/2029</li>
</ul>
<h3>Vi Tri Chien Luoc</h3>
<p>Ngay nut giao Phan Trung &amp; Duong Tu Giang, trung tam TP Bien Hoa cu. Ket noi TP.HCM, san bay Tan Son Nhat, san bay Long Thanh chi 30&ndash;35 phut.</p>
<h2>60 HANG MUC TIEN ICH</h2>
<ul>
  <li>To hop mat nuoc chuan 5 sao: ho boi resort, ho massage, ho boi tre em</li>
  <li>Quang truong anh sang, vuon canh quan xanh mat</li>
  <li>Khu chieu phim ngoai troi, khu BBQ</li>
  <li>Tuyen pho thuong mai sam uat</li>
  <li>Nha tre B.School, san choi nghe thuat</li>
  <li>Khu may tap ngoai troi, khu van dong da nang</li>
</ul>
<h2>GIA BAN &amp; CHINH SACH UU DAI</h2>
<p>Muc gia ban cua Bcons Central Park chi tu <strong>49,9 trieu/m&#178;</strong>:</p>
<ul>
  <li>Can Studio: 37&ndash;40m&#178;</li>
  <li>Can 1PN1WC: 43m&#178;</li>
  <li>Can 2PN1WC: 50&ndash;53m&#178;</li>
  <li>Can 2PN2WC: 60&ndash;73m&#178;</li>
  <li>Can 3PN2WC: 87&ndash;88m&#178;</li>
</ul>
<p><strong>3 phuong thuc thanh toan linh hoat:</strong></p>
<ul>
  <li>PT1: Tien do, chiet khau 8,5%</li>
  <li>PT2: Vay ngan hang, von tu co 20%, lai suat 0% trong 24 thang</li>
  <li>PT3: Von tu co chi 10%, CDT cam ket lai suat 6,9% trong 4 nam dau</li>
</ul>
<h2>NHA MAU &amp; HINH ANH THUC TE</h2>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/40.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/39.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/38.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/37.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/36.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/35.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/34.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/33.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/32.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/31.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/30.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/29.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/28.jpg" alt="" loading="lazy"></a>
</div>
<h2>PHAP LY RO RANG</h2>
<ul>
  <li>Bang cam ket ten du an</li>
  <li>Thong tin trien khai Khu nha o phuc hop cao tang phuong Tam Hiep</li>
  <li>Giay phep xay dung day du</li>
</ul>
<h2>LIEN HE TU VAN &amp; DAT CHO</h2>
<p>Hotline: <strong>0909 2222 54</strong> | Zalo: <a href="https://zalo.me/0909222254" target="_blank">zalo.me/0909222254</a><br>
Email: kinhdoanh@bcons.com.vn<br>
Dia chi: 176/1-176/3 Nguyen Van Thuong, Thanh My Tay, TP.HCM</p>
''')
with open(f'{OUT}/tin-tuc/khai-truong-nha-mau-bcons-central-park.html', 'w', encoding='utf-8') as f:
    f.write(art1)
print('OK bai 1')

# ===== BAI 2: COMPANY TRIP 2026 =====
art2 = art_page(
    'HANH TRINH COMPANY TRIP BCONS 2026 &ndash; ONE RHYTHMS BCONS, HOP LUC VUON XA',
    '03/08/2026', 'Su Kien',
    '''
<img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785560060167_5259956582289270614_g87504753891370911_5e3015fe585956490ad9c6677c861da3-1024x768.jpg" alt="Company Trip Bcons 2026" style="width:100%;border-radius:10px;margin-bottom:18px" loading="lazy">
<p>Tu ngay 29/7 den 01/8/2026, Tap doan Bcons da to chuc chuyen hanh trinh Company Trip 2026 voi chu de <strong>"ONE RHYTHMS BCONS &mdash; HOP LUC VUON XA"</strong>, dua hang nghin nhan su cua Bcons Group va Bcons Homes den voi co so dich vu phuc hop 5 sao tai Phu Quoc.</p>
<h2>YNH NGHIA VA MOT TIEU CUA CHUYEN DI</h2>
<p>Voi tieu chi "Bat dau tu Nhan Su, Phat trien Nhan Luc", Bcons Company Trip 2026 khong chi la mot chuyen du lich nghi duong thong thuong ma con la su kien gop phan xay dung tinh than doan ket, huong den tuong lai phat trien ben vung cua toan Bo may Bcons Group.</p>
<h2>HANH TRINH &amp; CAC HOAT DONG NOI BAT</h2>
<h3>Ngay 1: Cuoc Hanh Trinh Bat Dau (29/7)</h3>
<p>Toan bo nhan su Bcons xuat phat tu TP.HCM, dat chan den thien duong nghi duong Phu Quoc. Chiec may bay rieng dua theo toan bo nhan vien la mot trong nhung trai nghiem dac biet, the hien su quan tam cua lanh dao doi voi cuoc song va chat luong lao dong cua tung ca nhan.</p>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785555074207_1027907227192204778_g6399671543785879093_7c2d45a406b3b8b3ca3bc5fc0ef5b61f-1024x768.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785555074207_1027907227192204778_g6399671543785879093_7f1cf4f56d2ee74e6c30285a7a70e1ba-1024x768.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785555074207_1027907227192204778_g6399671543785879093_4b7697e67b2a5aa3b2b3600eebbb1284-1024x768.jpg" alt="" loading="lazy"></a>
</div>
<h3>Ngay 2: Hoi Nge Thuong Nien &amp; Gala Dinner (30/7)</h3>
<p>Hoi nghi Thuong nien 2026 la su kien trong tam trong chuyen Company Trip nam nay, noi toan the lanh dao va nhan su cung nhau ohn lai chang duong 2026 va dat muc tieu cho nam 2027. Phien Gala Dinner dang cap voi nhung man trinh dien am nhac, vu dao hoanh trang, trao giai thuong xuat sac va cac hoat dong giao luu bay to su doan ket, gan bo giua cac thanh vien trong gia dinh Bcons.</p>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785560060167_5259956582289270614_g87504753891370911_5e3015fe585956490ad9c6677c861da3-1024x768.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785560060167_5259956582289270614_g87504753891370911_699ab0e00aa7e2f9296bcce33a17b2bd-1024x768.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785560060167_5259956582289270614_g87504753891370911_72a4d8e52c6a3df01ca09b9a5a8e5c85-1024x768.jpg" alt="" loading="lazy"></a>
</div>
<h3>Ngay 3: Tham Quan &amp; Trai Nghiem (31/7)</h3>
<p>Mot ngay hoan toan thu gian, kham pha nhung diem den dep nhat cua Phu Quoc: bien Bai Truong, khu vui choi Vinwonders, trai nghiem am thuc &amp; mua sam. Buoi chieu, tat ca cung tham gia cac hoat dong teambuilding thon vi, tao nen nhung ky niem dep kho quen.</p>
<div class="gal">
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785560060167_5259956582289270614_g87504753891370911_f43e5afe77ce81db39d5a174c72be374-1024x768.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785560060167_5259956582289270614_g87504753891370911_2c7f44d75c27f71eec2fcc6c1dba0fb1-1024x768.jpg" alt="" loading="lazy"></a>
  <a href="#"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785560060167_5259956582289270614_g87504753891370911_25e8f4bf20afcfe37e69bef2cfe5e2c1-1024x768.jpg" alt="" loading="lazy"></a>
</div>
<h3>Ngay 4: Chao Tam Biet Phu Quoc (01/8)</h3>
<p>Khi chiec may bay dua toan bo nhan vien ve lai TP.HCM, moi nguoi mang theo nhung ky niem dep va nang luong moi de tiep tuc hanh trinh cung Bcons Group.</p>
<h2>Y NGHIA SAU SAC</h2>
<p>Company Trip 2026 la minh chung cho quan diem quan ly nhan su cua Bcons Group: <em>"Con nguoi la tai san quy gia nhat"</em>. Viec dau tu cho hanh phuc va su gan ket cua nhan vien la dong luc de toan bo bo may Bcons Group cung nhau vung buoc tren hanh trinh vuon tam cao hon, xa hon.</p>
''')
with open(f'{OUT}/tin-tuc/company-trip-bcons-2026.html', 'w', encoding='utf-8') as f:
    f.write(art2)
print('OK bai 2')

# ===== BAI 3: GIA CAN HO =====
art3 = art_page(
    'Gia Can Ho TPHCM Thap Hon Ha Noi 50%: Dong Tien Do Ve Nhu Cau O Thuc',
    '21/07/2026', 'Thi Truong',
    '''
<img src="https://bconsgroup.vn/wp-content/uploads/2026/06/Bcons-Center-Ket-Noi-Da-Cham-1024x751.jpg" alt="Gia can ho TPHCM" style="width:100%;border-radius:10px;margin-bottom:18px" loading="lazy">
<p>Trong khi Ha Noi chung kien muc gia can ho tang chong mat, thi truong bat dong san TP.HCM lai dang giu duoc muc gia on dinh hon, tham chi thap hon Ha Noi den 50%. Day dang la dieu kien thuan loi cho dong tien tu nhieu nguon do ve, huong den nhu cau o thuc su.</p>
<h2>THUC TRANG PHAN HOA GIA CAN HO HA NOI VA TPHCM</h2>
<p>Theo bao cao moi nhat tu cac don vi nghien cuu bat dong san uy tin, gia can ho tai Ha Noi dang cao gap 1,5&ndash;2 lan so voi TP.HCM trong cung phan khuc.</p>
<p>Muc gia trung binh can ho TP.HCM (2026): 55&ndash;65 trieu/m&#178;, trong khi muc gia trung binh can ho Ha Noi (2026): 80&ndash;120 trieu/m&#178;. Phan khuc binh dan tai TP.HCM (duoi 50 trieu/m&#178;) van con ton tai voi nhieu lua chon dan trai rong khap dia ban.</p>
<h2>NGUYEN NHAN TPHCM GIU GIA ON DINH HON</h2>
<ul>
  <li><strong>Nguon cung da dang:</strong> TP.HCM va cac tinh lap can (Binh Duong, Long An, Dong Nai) co nguon cung can ho doi dao hon</li>
  <li><strong>Lich su phat trien lau doi:</strong> thi truong BDS TP.HCM co lich su hon 30 nam, phat trien on dinh</li>
  <li><strong>Kiem soat dau co tot hon:</strong> cong cong thong tin minh bach, giao dich thong thoang</li>
  <li><strong>Cu dan huong toi o thuc:</strong> ty le mua de o thay vi dau co con cao</li>
</ul>
<h2>XU HUONG DONG TIEN DO VE TPHCM &amp; LAP CAN</h2>
<p>Nhieu nha dau tu tu mien Bac dang chuyen huong dong tien vao TP.HCM &amp; cac tinh vung ven do:</p>
<ul>
  <li>Muc gia hap dan hon, bien do tang gia con nhieu du dia</li>
  <li>Nhieu du an moi voi chinh sach thanh toan linh hoat, lai suat uu dai</li>
  <li>Ha tang giao thong (Metro, vanh dai 3, cao toc) dang trien khai dong bo</li>
  <li>Cac khu cong nghiep, trung tam giao duc, y te phat trien manh</li>
</ul>
<h2>BCONS GROUP &amp; CAC SAN PHAM PHU HOP NHU CAU O THUC</h2>
<p>Tap doan Bcons Group dang phat trien nhieu du an can ho tai TP.HCM va Dong Nai voi muc gia cuc ky canh tranh, phu hop cho nhu cau o thuc:</p>
<ul>
  <li><strong>Bcons Asahi:</strong> 41 trieu/m&#178; &mdash; mat tien QL1K, lien ke Metro, DHQG</li>
  <li><strong>Bcons Aria:</strong> 46 trieu/m&#178; &mdash; trung tam Di An, 37 tang hien dai</li>
  <li><strong>Bcons Central Park:</strong> 49,9 trieu/m&#178; &mdash; Bien Hoa, 5 block, san bay Long Thanh 30 phut</li>
</ul>
<h2>NHAN DINH CHUYEN GIA</h2>
<p>Cac chuyen gia bat dong san nhan dinh: <em>"Voi muc gia hien tai, can ho TP.HCM va vung ven dang o muc canh tranh cao, phu hop cho ca nguoi mua o thuc lan nha dau tu. Day la co hoi tot truoc khi gia di len khi ha tang moi di vao hoat dong."</em></p>
<p>Rieng Bcons Central Park tai Bien Hoa la lua chon dang chu y khi gia chi 49,9 trieu/m&#178; nhung vi tri khai thac tot, lien ket chac voi san bay Long Thanh &mdash; cong trinh se thay doi bo mat do thi Dong Nai trong thap ky toi.</p>
<h2>KET LUAN</h2>
<p>Muc gia can ho TPHCM dang o nguong hap dan, thap hon Ha Noi 50%, cung voi cac chinh sach ho tro lai suat, thanh toan linh hoat, day la thoi diem de hanh dong &mdash; du la mua o hay dau tu.</p>
''')
with open(f'{OUT}/tin-tuc/gia-can-ho-tphcm-thap-hon-ha-noi-50.html', 'w', encoding='utf-8') as f:
    f.write(art3)
print('OK bai 3')

# ===== BAI 4: TAI TRO GIAI CHAY HTV =====
art4 = art_page(
    'Tap Doan Bcons Tai Tro Giai Chay Y Chi Con Dao HTV 2026',
    '07/07/2026', 'Su Kien',
    '''
<img src="https://bconsgroup.vn/wp-content/uploads/2026/07/Bcons-HTV-1.jpg" alt="Bcons tai tro giai chay Con Dao HTV 2026" style="width:100%;border-radius:10px;margin-bottom:18px" loading="lazy">
<p>Tap doan Bcons Group vinh du la don vi <strong>Tai tro Vang</strong> cho <strong>Giai Chay Y Chi Con Dao HTV 2026</strong> &mdash; giai chay bo quoc te duoc to chuc tai Con Dao, Ba Ria &ndash; Vung Tau. Day la mot trong nhung giai chay lon va uy tin nhat Viet Nam, thu hut hang nghin van dong vien trong va ngoai nuoc tham du.</p>
<h2>VE GIAI CHAY Y CHI CON DAO HTV 2026</h2>
<p>Giai Chay Y Chi Con Dao la giai marathon quoc te duoc to chuc hang nam tai Con Dao, Ba Ria &ndash; Vung Tau. Giai chay qua nhung con duong ven bien va rung nui tuyet dep cua Con Dao, thu hut nhieu van dong vien chuyen nghiep va phong trao tu khap noi the gioi.</p>
<p>Nam 2026, giai thu hut hon <strong>5.000 van dong vien</strong> den tu 30 quoc gia va vung lanh tho, gom cac cu ly: 5km, 10km, 21km (ban marathon) va 42km (marathon day du).</p>
<h2>TAP DOAN BCONS &mdash; DOI TAC TIN CAY CUA CONG DONG</h2>
<p>Viec Tap doan Bcons tai tro cho giai chay Con Dao the hien cam ket cua doanh nghiep doi voi:</p>
<ul>
  <li><strong>Suc khoe cong dong:</strong> khuyen khich van dong, the thao, loi song lanh manh</li>
  <li><strong>Phat trien du lich:</strong> gop phan quang ba hinh anh Con Dao den ban be quoc te</li>
  <li><strong>Trach nhiem xa hoi:</strong> la mot phan trong chien luoc CSR cua Bcons Group</li>
  <li><strong>Xay dung thuong hieu:</strong> gia tang nhan dien thuong hieu Bcons tren thi truong</li>
</ul>
<h2>TINH THAN "Y CHI" VA GIA TRI BCONS</h2>
<p>"Y Chi" &mdash; hai tu ngan gon nhung chua dung toan bo ban linh cua mot van dong vien marathon. Chinh tinh than vuot kho, khong bo cuoc truoc nhung kho khan ay cung la gia tri ma Tap doan Bcons xay dung trong hon 13 nam hoat dong:</p>
<blockquote style="border-left:4px solid var(--gold);padding-left:18px;margin:18px 0;font-style:italic;color:#555">
"Moi can ho Bcons ban giao la mot hanh trinh tu y tuong den hien thuc, can y chi, ban linh va su tap trung. Chung toi tai tro cho giai chay nay vi chung toi hieu the nao la phai to ve dich."
</blockquote>
<h2>CAC HOAT DONG CONG DONG CUA BCONS</h2>
<ul>
  <li>2023: Tai tro Giai marathon TP. Di An lan thu nhat</li>
  <li>2024: Dong hanh cung Quy hoc bong cho sinh vien ngheo vuot kho</li>
  <li>2025: To chuc Giai chay Bcons Run for Community tai TP.HCM</li>
  <li>2026: Tai tro Vang Giai Chay Y Chi Con Dao HTV 2026</li>
</ul>
<h2>KET LUAN</h2>
<p>Viec Tap doan Bcons tro thanh Nha tai tro Vang cho Giai Chay Y Chi Con Dao HTV 2026 mot lan nua khang dinh vi the va trach nhiem cua doanh nghiep doi voi cong dong. Day la buoc di phu hop voi tam nhin phat trien ben vung, huong den con nguoi va xa hoi cua Bcons Group.</p>
''')
with open(f'{OUT}/tin-tuc/tap-doan-bcons-tai-tro-giai-chay-con-dao-htv-2026.html', 'w', encoding='utf-8') as f:
    f.write(art4)
print('OK bai 4')

# ===== TIN TUC LISTING =====
news_listing = wrap('Tin Tuc', '''
<div class="ph">
  <div class="con">
    <h1>TIN TUC BCONS GROUP</h1>
    <p>Cap nhat tin tuc moi nhat tu Tap doan Bcons Group</p>
  </div>
</div>
<section class="sec">
<div class="con">
  <div class="nf">
    <button class="nf-btn active" onclick="filterNews(this,\'all\')">Tat Ca</button>
    <button class="nf-btn" onclick="filterNews(this,\'du-an\')">Tin Tuc Du An</button>
    <button class="nf-btn" onclick="filterNews(this,\'su-kien\')">Su Kien</button>
    <button class="nf-btn" onclick="filterNews(this,\'thi-truong\')">Thi Truong</button>
  </div>
  <div class="ng" id="news-grid">
    <div class="nc" data-cat="du-an">
      <div class="nc-thumb"><img src="https://bconsgroup.vn/wp-content/uploads/2026/09/40.jpg" alt="" loading="lazy" onerror="this.parentNode.style.background=\'linear-gradient(135deg,#0d2137,#1a4a7a)\'"></div>
      <div class="nc-body">
        <div class="nc-cat">Tin Tuc Du An</div>
        <h3><a href="tin-tuc/khai-truong-nha-mau-bcons-central-park.html">Khai Truong Nha Mau Bcons Central Park Bien Hoa: Hut Khach Nho Khong Gian Toi Uu &amp; Gia Tu 49,9 Trieu/m2</a></h3>
        <div class="nc-foot"><span class="nc-date">12/09/2026</span><a href="tin-tuc/khai-truong-nha-mau-bcons-central-park.html" class="nc-more">Doc tiep &rarr;</a></div>
      </div>
    </div>
    <div class="nc" data-cat="su-kien">
      <div class="nc-thumb"><img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785560060167_5259956582289270614_g87504753891370911_5e3015fe585956490ad9c6677c861da3-1024x768.jpg" alt="" loading="lazy" onerror="this.parentNode.style.background=\'linear-gradient(135deg,#1a4a7a,#0d2137)\'"></div>
      <div class="nc-body">
        <div class="nc-cat">Su Kien</div>
        <h3><a href="tin-tuc/company-trip-bcons-2026.html">HANH TRINH COMPANY TRIP BCONS 2026 &ndash; ONE RHYTHMS BCONS, HOP LUC VUON XA</a></h3>
        <div class="nc-foot"><span class="nc-date">03/08/2026</span><a href="tin-tuc/company-trip-bcons-2026.html" class="nc-more">Doc tiep &rarr;</a></div>
      </div>
    </div>
    <div class="nc" data-cat="thi-truong">
      <div class="nc-thumb"><img src="https://bconsgroup.vn/wp-content/uploads/2026/06/Bcons-Center-Ket-Noi-Da-Cham-1024x751.jpg" alt="" loading="lazy" onerror="this.parentNode.style.background=\'linear-gradient(135deg,#2a4a1a,#1a3a0d)\'"></div>
      <div class="nc-body">
        <div class="nc-cat">Thi Truong</div>
        <h3><a href="tin-tuc/gia-can-ho-tphcm-thap-hon-ha-noi-50.html">Gia Can Ho TPHCM Thap Hon Ha Noi 50%: Dong Tien Do Ve Nhu Cau O Thuc</a></h3>
        <div class="nc-foot"><span class="nc-date">21/07/2026</span><a href="tin-tuc/gia-can-ho-tphcm-thap-hon-ha-noi-50.html" class="nc-more">Doc tiep &rarr;</a></div>
      </div>
    </div>
    <div class="nc" data-cat="su-kien">
      <div class="nc-thumb"><img src="https://bconsgroup.vn/wp-content/uploads/2026/07/Bcons-HTV-1.jpg" alt="" loading="lazy" onerror="this.parentNode.style.background=\'linear-gradient(135deg,#4a0d0d,#7a1a1a)\'"></div>
      <div class="nc-body">
        <div class="nc-cat">Su Kien</div>
        <h3><a href="tin-tuc/tap-doan-bcons-tai-tro-giai-chay-con-dao-htv-2026.html">Tap Doan Bcons Tai Tro Giai Chay Y Chi Con Dao HTV 2026</a></h3>
        <div class="nc-foot"><span class="nc-date">07/07/2026</span><a href="tin-tuc/tap-doan-bcons-tai-tro-giai-chay-con-dao-htv-2026.html" class="nc-more">Doc tiep &rarr;</a></div>
      </div>
    </div>
  </div>
</div>
</section>
''')
with open(f'{OUT}/tin-tuc.html', 'w', encoding='utf-8') as f:
    f.write(news_listing)
print('OK tin-tuc.html')
print('=== NEWS DONE ===')
