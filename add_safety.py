import sys

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<!-- Top Route Focus (Dark Luxury Theme) -->'

safety_html = '''<!-- Safety & Security Trust Strip -->
  <div class="container-fluid py-4" style="background: linear-gradient(90deg, #111 0%, #0a0a0a 100%); border-top: 1px solid rgba(212,175,55,0.2); border-bottom: 1px solid rgba(212,175,55,0.2);">
    <div class="container">
      <div class="row g-4 text-center">
        <div class="col-md-3 col-6 wow fadeIn" data-wow-delay="0.1s">
            <i class="fas fa-shield-check mb-2" style="font-size: 2rem; color: #25D366;"></i>
            <h5 style="color: #fff; font-size: 1rem; font-weight: 600;">Verified Drivers</h5>
            <p style="color: #a0a0a0; font-size: 0.85rem; margin:0;">Background-checked locals</p>
        </div>
        <div class="col-md-3 col-6 wow fadeIn" data-wow-delay="0.2s">
            <i class="fas fa-map-marker-alt mb-2" style="font-size: 2rem; color: #d4af37;"></i>
            <h5 style="color: #fff; font-size: 1rem; font-weight: 600;">GPS Tracking</h5>
            <p style="color: #a0a0a0; font-size: 0.85rem; margin:0;">Fitted in all premium cabs</p>
        </div>
        <div class="col-md-3 col-6 wow fadeIn" data-wow-delay="0.3s">
            <i class="fas fa-user-shield mb-2" style="font-size: 2rem; color: #25D366;"></i>
            <h5 style="color: #fff; font-size: 1rem; font-weight: 600;">Family Safe</h5>
            <p style="color: #a0a0a0; font-size: 0.85rem; margin:0;">Strictly professional & polite</p>
        </div>
        <div class="col-md-3 col-6 wow fadeIn" data-wow-delay="0.4s">
            <i class="fas fa-headset mb-2" style="font-size: 2rem; color: #d4af37;"></i>
            <h5 style="color: #fff; font-size: 1rem; font-weight: 600;">24/7 Support</h5>
            <p style="color: #a0a0a0; font-size: 0.85rem; margin:0;">Direct WhatsApp assistance</p>
        </div>
      </div>
    </div>
  </div>

  '''

if target in text and '<!-- Safety & Security Trust Strip -->' not in text:
    text = text.replace(target, safety_html + target)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Safety strip added successfully.")
else:
    print("Target not found or already added.")
