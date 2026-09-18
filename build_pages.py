# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/data/bcons_v2')
from shared import *

# ==================== HOMEPAGE ====================
home = wrap('Trang Chu', '''
<section class="hero">
  <div class="hero-bg" style="background-image:url('https://bconsgroup.vn/wp-content/uploads/2026/08/Phoi-canh-6-1-scaled.jpg')"></div>
  <div class="con">
    <div class="hero-body">
      <span class="hero-tag">Bcons Group &#8212; Khac biet o chu Tin</span>
      <h1>BCONS GROUP<br>Tien phong kien tao<br>khong gian song ly tuong</h1>
      <p>Tap doan bat dong san hang dau tai Binh Duong va TP.HCM voi hon 15 du an thanh cong</p>
      <div class="hero-btns">
        <a href="du-an/index.html" class="btn-gold">Xem Du An</a>
        <a href="lien-he.html" class="btn-wh">Lien He Ngay</a>
      </div>
    </div>
  </div>
</section>

<section class="sec">
<div class="con">
  <div class="ab-grid">
    <div class="ab-img">
      <img src="https://bconsgroup.vn/wp-content/uploads/2024/11/logo-bcons-group.png" alt="Bcons Group">
    </div>
    <div class="ab-txt">
      <p class="lbl" style="display:inline-block;background:#ddeeff;color:var(--blue);padding:4px 14px;border-radius:16px;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">Gioi Thieu</p>
      <h2>BCONS GROUP</h2>
      <p><strong>Cong ty Co phan Dau tu Xay dung BCONS</strong> la doanh nghiep hoat dong trong cac linh vuc: <strong>Bat dong san, Kinh doanh dich vu, Giao duc va Logistic.</strong></p>
      <p>BCONS GROUP ung dung cong nghe B.I.M vao tat ca qua trinh quan ly du an, thiet ke, thi cong xay dung nham chuan hoa theo tieu chuan quoc te.</p>
      <div class="stats">
        <div class="stat"><div class="n">15+</div><div class="t">Du an trien khai</div></div>
        <div class="stat"><div class="n">10+</div><div class="t">Nam kinh nghiem</div></div>
        <div class="stat"><div class="n">10.000+</div><div class="t">Can ho ban giao</div></div>
        <div class="stat"><div class="n">90%</div><div class="t">Ty le hap thu</div></div>
      </div>
      <a href="gioi-thieu.html" class="btn-gold" style="display:inline-block">Xem Them</a>
    </div>
  </div>
</div>
</section>

<section class="sec sec-alt">
<div class="con">
  <div class="sh">
    <span class="lbl">Bcons Group</span>
    <h2>CAC CHUNG CU BCONS NOI BAT</h2>
    <p>Tien phong mang den trai nghiem song ly tuong giua long do thi</p>
    <div class="divider"></div>
  </div>
  <div class="pg">
    <div class="pc">
      <div class="pc-thumb">
        <img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1787554246410_1027907227192204778_g6752788579839982367_6ae57fb79727cca86e1c2a5d14aa0a36.jpg" alt="Bcons Central Park" loading="lazy" onerror="this.style.display=\'none\'">
        <span class="pc-badge">Dang mo ban</span>
      </div>
      <div class="pc-body">
        <h3>Bcons Central Park</h3>
        <p>Khu can ho bieu tuong tai trung tam Phuong Tam Hiep, Bien Hoa. 5 block cao 22 tang, 2.820 can ho. Ket noi thuan tien den TP.HCM, san bay Long Thanh.</p>
        <div class="pc-meta"><span>&#128205; Bien Hoa, Dong Nai</span><span>&#128176; 49,9tr/m2</span></div>
        <a href="du-an/bcons-central-park.html" class="pc-link">Kham pha du an &rarr;</a>
      </div>
    </div>
    <div class="pc">
      <div class="pc-thumb">
        <img src="https://bconsgroup.vn/wp-content/uploads/2026/08/Phoi-canh-6-1-scaled.jpg" alt="Bcons Aria" loading="lazy" onerror="this.style.display=\'none\'">
        <span class="pc-badge">Dang booking</span>
      </div>
      <div class="pc-body">
        <h3>Bcons Aria</h3>
        <p>Can ho hien dai tai trung tam Di An, Binh Duong. 1 block 37 tang, 1.274 can ho. Lien ke TP. Thu Duc, gan Metro so 1.</p>
        <div class="pc-meta"><span>&#128205; Dong Hoa, TP.HCM</span><span>&#128176; 46tr/m2</span></div>
        <a href="du-an/bcons-aria.html" class="pc-link">Kham pha du an &rarr;</a>
      </div>
    </div>
    <div class="pc">
      <div class="pc-thumb">
        <div class="pc-ph" style="background:linear-gradient(135deg,#0d3a6b,#1a6fb5)">&#127970;<br>BCONS ASAHI</div>
        <span class="pc-badge">Dang mo ban</span>
      </div>
      <div class="pc-body">
        <h3>Bcons Asahi</h3>
        <p>Can ho chuan Nhat giua long Dong Hoa, TP.HCM. 1 block 29 tang, 490 can ho. Mat tien QL1K, lien ke Metro so 1 va DHQG.</p>
        <div class="pc-meta"><span>&#128205; Dong Hoa, TP.HCM</span><span>&#128176; Tu 1,5 ty/can</span></div>
        <a href="du-an/bcons-asahi.html" class="pc-link">Kham pha du an &rarr;</a>
      </div>
    </div>
    <div class="pc">
      <div class="pc-thumb">
        <div class="pc-ph" style="background:linear-gradient(135deg,#1a4a3a,#2a7a5a)">&#127961;&#65039;<br>CENTER CITY</div>
        <span class="pc-badge">Mo ban</span>
      </div>
      <div class="pc-body">
        <h3>Bcons Center City</h3>
        <p>Khu do thi phuc hop, 5 block cao 29-36 tang, 1.800-1.940 can ho. Ket hop can ho, thuong mai, dich vu.</p>
        <div class="pc-meta"><span>&#128205; Di An, Binh Duong</span><span>&#128176; 55tr/m2</span></div>
        <a href="du-an/bcons-center-city.html" class="pc-link">Kham pha du an &rarr;</a>
      </div>
    </div>
    <div class="pc">
      <div class="pc-thumb">
        <img src="https://bconsgroup.vn/wp-content/uploads/2024/11/Phoi-canh-thuc-te-bcons-city-life.jpg" alt="Bcons City Life" loading="lazy" onerror="this.parentNode.style.background=\'linear-gradient(135deg,#4a2a0d,#8a5a1a)\'">
        <span class="pc-badge">Mo ban</span>
      </div>
      <div class="pc-body">
        <h3>Bcons City Life</h3>
        <p>Nha pho thuong mai dau tien cua Bcons. Toa lac tai TP. Tan Uyen, Binh Duong. Quy mo 4,68 ha, 348 san pham da dang.</p>
        <div class="pc-meta"><span>&#128205; Tan Uyen, Binh Duong</span><span>&#128176; 2,5-4 ty/can</span></div>
        <a href="du-an/bcons-city-life.html" class="pc-link">Kham pha du an &rarr;</a>
      </div>
    </div>
    <div class="pc">
      <div class="pc-thumb">
        <div class="pc-ph" style="background:linear-gradient(135deg,#1a2a4a,#2a4a7a)">&#127962;<br>BCONS CITY</div>
        <span class="pc-badge">Ban giao &amp; Mo ban</span>
      </div>
      <div class="pc-body">
        <h3>Bcons City</h3>
        <p>Dai do thi quy mo lon, nhieu thap: Green Diamond, Sapphire, Topaz, Emerald. TTTM 3 tang, khach san 4 sao, truong hoc lien cap.</p>
        <div class="pc-meta"><span>&#128205; Di An, Binh Duong</span><span>&#128176; 34-43tr/m2</span></div>
        <a href="du-an/bcons-city.html" class="pc-link">Kham pha du an &rarr;</a>
      </div>
    </div>
  </div>
  <div style="text-align:center;margin-top:40px">
    <a href="du-an/index.html" class="btn-gold">Xem Tat Ca Du An</a>
  </div>
</div>
</section>

<section class="sec">
<div class="con">
  <div class="sh">
    <span class="lbl">Cap nhat moi nhat</span>
    <h2>BANG TIN BCONS GROUP</h2>
    <div class="divider"></div>
  </div>
  <div class="ng">
    <div class="nc">
      <div class="nc-thumb">
        <img src="https://bconsgroup.vn/wp-content/uploads/2026/09/40.jpg" alt="" loading="lazy" onerror="this.parentNode.style.background=\'linear-gradient(135deg,#0d2137,#1a4a7a)\'">
      </div>
      <div class="nc-body">
        <div class="nc-cat">Tin Tuc Du An</div>
        <h3><a href="tin-tuc/khai-truong-nha-mau-bcons-central-park.html">Khai Truong Nha Mau Bcons Central Park Bien Hoa: Hut Khach Nho Khong Gian Toi Uu &amp; Gia Tu 49,9 Trieu/m2</a></h3>
        <div class="nc-foot"><span class="nc-date">12/09/2026</span><a href="tin-tuc/khai-truong-nha-mau-bcons-central-park.html" class="nc-more">Doc tiep &rarr;</a></div>
      </div>
    </div>
    <div class="nc">
      <div class="nc-thumb">
        <img src="https://bconsgroup.vn/wp-content/uploads/2026/08/1785560060167_5259956582289270614_g87504753891370911_5e3015fe585956490ad9c6677c861da3-1024x768.jpg" alt="" loading="lazy" onerror="this.parentNode.style.background=\'linear-gradient(135deg,#1a4a7a,#0d2137)\'">
      </div>
      <div class="nc-body">
        <div class="nc-cat">Su Kien</div>
        <h3><a href="tin-tuc/company-trip-bcons-2026.html">HANH TRINH COMPANY TRIP BCONS 2026 &ndash; ONE RHYTHMS BCONS, HOP LUC VUON XA</a></h3>
        <div class="nc-foot"><span class="nc-date">03/08/2026</span><a href="tin-tuc/company-trip-bcons-2026.html" class="nc-more">Doc tiep &rarr;</a></div>
      </div>
    </div>
    <div class="nc">
      <div class="nc-thumb">
        <img src="https://bconsgroup.vn/wp-content/uploads/2026/06/Bcons-Center-Ket-Noi-Da-Cham-1024x751.jpg" alt="" loading="lazy" onerror="this.parentNode.style.background=\'linear-gradient(135deg,#2a4a1a,#1a3a0d)\'">
      </div>
      <div class="nc-body">
        <div class="nc-cat">Thi Truong</div>
        <h3><a href="tin-tuc/gia-can-ho-tphcm-thap-hon-ha-noi-50.html">Gia Can Ho TPHCM Thap Hon Ha Noi 50%: Dong Tien Do Ve Nhu Cau O Thuc</a></h3>
        <div class="nc-foot"><span class="nc-date">21/07/2026</span><a href="tin-tuc/gia-can-ho-tphcm-thap-hon-ha-noi-50.html" class="nc-more">Doc tiep &rarr;</a></div>
      </div>
    </div>
    <div class="nc">
      <div class="nc-thumb">
        <img src="https://bconsgroup.vn/wp-content/uploads/2026/07/Bcons-HTV-1.jpg" alt="" loading="lazy" onerror="this.parentNode.style.background=\'linear-gradient(135deg,#4a0d0d,#7a1a1a)\'">
      </div>
      <div class="nc-body">
        <div class="nc-cat">Su Kien</div>
        <h3><a href="tin-tuc/tap-doan-bcons-tai-tro-giai-chay-con-dao-htv-2026.html">Tap Doan Bcons Tai Tro Giai Chay Y Chi Con Dao HTV 2026</a></h3>
        <div class="nc-foot"><span class="nc-date">07/07/2026</span><a href="tin-tuc/tap-doan-bcons-tai-tro-giai-chay-con-dao-htv-2026.html" class="nc-more">Doc tiep &rarr;</a></div>
      </div>
    </div>
  </div>
  <div style="text-align:center;margin-top:40px">
    <a href="tin-tuc.html" class="btn-gold">Xem Tat Ca Tin Tuc</a>
  </div>
</div>
</section>

<section class="sec sec-alt">
<div class="con">
  <div class="sh">
    <span class="lbl">Hop tac</span>
    <h2>DOI TAC BCONS GROUP</h2>
    <div class="divider"></div>
  </div>
  <div class="part-grid">
''' + ''.join([
    f'<div class="part-item"><img src="https://bconsgroup.vn/wp-content/uploads/2024/11/{fn}" alt="{nm}" loading="lazy" onerror="this.style.display=\'none\'"></div>'
    for nm, fn in [
        ('MB','MB.jpg'),('TP Bank','tpbank-1.jpg'),('Vinaconex','zsdgs-1536x1118-1-1024x745.jpg'),
        ('BDIF','bdif.jpg'),('Binh Ha','binh-ha.jpg'),('CC1 Mekong','CC1-Mekong.jpg'),
        ('Cong Thanh','cong-thanh.jpg'),('DKM','dkm-1.jpg'),('Fecon','fecon.jpg'),
        ('Fico','fico.jpg'),('Fujitech','fujitech-1.jpg'),('GRHM','grhm.jpg'),
        ('Japan Window','japan-windown.jpg'),('Kim Phong','Kim-phong.jpg'),('MEP','mep.jpg'),
        ('Nam Visai','Nam-visai.jpg'),('Navicons','navicons.jpg'),('The Wall','The-waall.jpg'),
        ('Untitled','Untitled-1.jpg'),('Veda','Veda-1.jpg'),('Viet Nhat','viet-nhat-1.jpg'),
    ]
]) + '''
  </div>
</div>
</section>
''')

with open(f'{OUT}/index.html', 'w', encoding='utf-8') as f:
    f.write(home)
print('OK index.html')

# ==================== GIOI THIEU ====================
gt = wrap('Gioi Thieu', '''
<div class="ph">
  <div class="con">
    <h1>GIOI THIEU BCONS GROUP</h1>
    <p>Tap doan bat dong san hang dau mien Nam Viet Nam</p>
  </div>
</div>
<section class="sec">
<div class="con">
  <div class="ab-grid">
    <div class="ab-img">
      <img src="https://bconsgroup.vn/wp-content/uploads/2024/11/logo-bcons-group.png" alt="Bcons Group">
    </div>
    <div class="ab-txt">
      <h2>CONG TY CO PHAN DAU TU XAY DUNG BCONS</h2>
      <p><strong>Bcons Group</strong>, thanh lap vao thang 3 nam 2013, la mot tap doan da nganh hoat dong trong cac linh vuc: <strong>Bat dong san, Kinh doanh dich vu, Giao duc va Logistic.</strong></p>
      <p>Mot trong nhung diem noi bat la viec ung dung cong nghe <strong>B.I.M (Building Information Modeling)</strong> vao toan bo qua trinh quan ly du an, thiet ke va thi cong xay dung.</p>
      <p><strong>Tru so chinh:</strong> Bcons Tower I, 176/1-176/3 Duong Nguyen Van Thuong, Phuong 25, Quan Binh Thanh, TP. Ho Chi Minh.</p>
      <div class="stats">
        <div class="stat"><div class="n">15+</div><div class="t">Du an bat dong san</div></div>
        <div class="stat"><div class="n">12</div><div class="t">Cong ty thanh vien</div></div>
        <div class="stat"><div class="n">2013</div><div class="t">Nam thanh lap</div></div>
        <div class="stat"><div class="n">1B USD</div><div class="t">Muc tieu DT 2026</div></div>
      </div>
    </div>
  </div>
</div>
</section>
<section class="sec sec-alt">
<div class="con">
  <div class="sh">
    <span class="lbl">Lo trinh</span>
    <h2>TAM NHIN PHAT TRIEN</h2>
    <div class="divider"></div>
  </div>
  <div class="tl">
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div style="flex:1"></div>
      <div class="tl-box" style="flex:2">
        <div class="yr">2013 - 2018</div>
        <h4>Hinh Thanh &amp; Phat Trien</h4>
        <p>Hinh thanh va phat trien thuong hieu tren thi truong bat dong san Binh Duong va TP.HCM.</p>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-box" style="flex:2">
        <div class="yr">2019 - 2022</div>
        <h4>Dao Tao &amp; Phat Trien Nhan Luc</h4>
        <p>Dao tao va phat trien nguon nhan luc chat luong cao, xay dung doi ngu ke thua.</p>
      </div>
      <div style="flex:1"></div>
    </div>
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div style="flex:1"></div>
      <div class="tl-box" style="flex:2">
        <div class="yr">Tu 2023</div>
        <h4>Tap Doan Da Nganh</h4>
        <p>Cong ty me voi 12 cong ty thanh vien dat doanh thu tren 0,3 ty USD. Muc tieu 1 ty USD vao 2026.</p>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-box" style="flex:2">
        <div class="yr">Sau 2030</div>
        <h4>Tap Doan Da Nganh Tam Co</h4>
        <p>Tro thanh tap doan da nganh voi doanh thu tren 5 ty USD, vuon tam quoc te.</p>
      </div>
      <div style="flex:1"></div>
    </div>
  </div>
</div>
</section>
<section class="sec">
<div class="con">
  <div class="sh">
    <span class="lbl">Van hoa</span>
    <h2>GIA TRI COT LOI</h2>
    <div class="divider"></div>
  </div>
  <div class="vals">
    <div class="val-card"><div class="ic">&#129309;</div><h4>Van Hoa Chu Tin</h4><p>Tin voi chinh minh, tin voi khach hang va doi tac. Chu Tin la nen tang cua moi hoat dong.</p></div>
    <div class="val-card"><div class="ic">&#11088;</div><h4>Van Hoa Neu Guong</h4><p>Cap tren guong mau, khoi nguon sang tao, tao moi truong lam viec cau tien.</p></div>
    <div class="val-card"><div class="ic">&#9889;</div><h4>Van Hoa Ky Luat</h4><p>Dao tao va ren luyen con nguoi ky luat, suy nghi ky luat va hanh dong ky luat.</p></div>
    <div class="val-card"><div class="ic">&#128218;</div><h4>Van Hoa Hoc Tap</h4><p>Dao tao doi ngu ke thua lien tuc va gin giu van hoa cua tap doan qua cac the he.</p></div>
  </div>
</div>
</section>
''')
with open(f'{OUT}/gioi-thieu.html', 'w', encoding='utf-8') as f:
    f.write(gt)
print('OK gioi-thieu.html')

# ==================== LIEN HE ====================
lh = wrap('Lien He', '''
<div class="ph">
  <div class="con">
    <h1>LIEN HE BCONS GROUP</h1>
    <p>Chung toi luon san sang ho tro ban 24/7</p>
  </div>
</div>
<section class="sec">
<div class="con">
  <div class="cg">
    <div class="ci">
      <h3>THONG TIN LIEN HE</h3>
      <div class="citem"><span class="ic">&#128205;</span><p><strong>Dia chi tru so:</strong><br>Bcons Tower I, 176/1-176/3 Duong Nguyen Van Thuong, Phuong 25, Quan Binh Thanh, TP. Ho Chi Minh</p></div>
      <div class="citem"><span class="ic">&#128222;</span><p><strong>Hotline:</strong><br><a href="tel:0909222254" style="color:var(--blue);font-size:1.4rem;font-weight:900">0909 2222 54</a></p></div>
      <div class="citem"><span class="ic">&#9993;</span><p><strong>Email:</strong><br>kinhdoanh@bcons.com.vn</p></div>
      <div class="citem"><span class="ic">&#128172;</span><p><strong>Zalo:</strong><br><a href="https://zalo.me/0909222254" target="_blank" style="color:var(--blue)">zalo.me/0909222254</a></p></div>
      <div class="citem"><span class="ic">&#9200;</span><p><strong>Gio lam viec:</strong><br>Thu Hai - Thu Sau: 8:00 - 17:30<br>Thu Bay: 8:00 - 12:00</p></div>
      <div style="margin-top:24px;background:#e8f0fb;border-radius:10px;padding:20px">
        <strong>PHONG KINH DOANH:</strong><br>
        &#128222; 0347 494 061 (Quang Bcons)<br>
        &#128172; <a href="https://zalo.me/0347494061" target="_blank" style="color:var(--blue)">Chat Zalo</a>
      </div>
    </div>
    <div>
      <div class="cf-box">
        <h3>GUI THONG TIN TU VAN</h3>
        <div class="fg"><label>Ho va ten *</label><input type="text" placeholder="Nguyen Van A"></div>
        <div class="fg"><label>So dien thoai *</label><input type="tel" placeholder="0909 xxx xxx"></div>
        <div class="fg"><label>Email</label><input type="email" placeholder="email@example.com"></div>
        <div class="fg"><label>Du an quan tam</label>
          <select>
            <option>-- Chon du an --</option>
            <option>Bcons Central Park</option>
            <option>Bcons Aria</option>
            <option>Bcons Asahi</option>
            <option>Bcons Center City</option>
            <option>Bcons City</option>
          </select>
        </div>
        <div class="fg"><label>Noi dung</label><textarea placeholder="Nhu cau cua ban..."></textarea></div>
        <button class="sbm">Gui Thong Tin</button>
      </div>
    </div>
  </div>
</div>
</section>
''')
with open(f'{OUT}/lien-he.html', 'w', encoding='utf-8') as f:
    f.write(lh)
print('OK lien-he.html')

print('=== PAGES DONE ===')
