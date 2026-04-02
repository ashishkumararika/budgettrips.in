import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the entire background dark instead of white/gray
html = re.sub(r'--bg-light:\s*#[a-fA-F0-9]+;', '--bg-light: #050505;', html)
html = re.sub(r'--text-main:\s*#[a-fA-F0-9]+;', '--text-main: #f8fafc;', html)
html = re.sub(r'--surface:\s*#[a-fA-F0-9]+;', '--surface: #0a0a0a;', html)

# Let's adjust the Hero text and buttons for the user Journey
# Old title: 'Outstation Cabs from Amritsar'
html = re.sub(r'<h1 class="hero-title">.*?</h1>', '<h1 class="hero-title" style="background: linear-gradient(45deg, #fff, #d4af37); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Punjab to Himachal<br><span>Premium Cabs</span></h1>', html, flags=re.DOTALL)
html = re.sub(r'<p class="hero-subtitle">.*?</p>', '<p class="hero-subtitle" style="color: #dfdfdf;">Your trusted travel partner for Outstation Taxis from Amritsar to Dalhousie, Dharamshala, Manali, Shimla, and beyond. Book an Innova, Swift, or Maharaja Tempo today.</p>', html, flags=re.DOTALL)

# Change hero CTAs to focus on WhatsApp and Call
book_buttons = '''
<div class="d-flex flex-wrap gap-3 mt-4">
    <a href="https://wa.me/919878120686?text=Hi!%20I%20want%20to%20book%20a%20cab%20from%20Amritsar%20to%20Himachal." target="_blank" class="btn rounded-pill px-5 py-3 shadow" style="background: #25D366; color: #fff; font-weight: 700; letter-spacing: 1px; font-size: 1.1rem; border: 2px solid #25D366; transition: 0.3s;">
        <i class="fab fa-whatsapp me-2" style="font-size: 1.3rem;"></i> WhatsApp to Book
    </a>
    <a href="tel:+919878120686" class="btn rounded-pill px-5 py-3 shadow" style="background: transparent; color: #d4af37; border: 2px solid #d4af37; font-weight: 700; letter-spacing: 1px; font-size: 1.1rem; transition: 0.3s;">
        <i class="fas fa-phone-alt me-2"></i> Call Concierge
    </a>
</div>
'''
html = re.sub(r'<div class="d-flex flex-wrap gap-3 mt-4">.*?</div>', book_buttons, html, flags=re.DOTALL, count=1)

# Now Let's fix the Bento section (Gray/White) to match the dark theme and highlight the routes!
bento_pattern = re.compile(r'<!-- World-Class Bento Services -->(.*?)<!-- Elite Fleet Presentation -->', re.DOTALL)

new_bento = '''<!-- Route Focus & Services (Dark Luxury Theme) -->
  <section class="bento-section" style="padding: 6rem 0; background: #000; border-top: 1px solid rgba(212, 175, 55, 0.1);">
    <div class="container">
      <div class="text-center mb-5 pb-3 wow fadeInUp" data-wow-delay="0.1s">
        <span class="badge px-4 py-2 rounded-pill mb-3 fw-bold shadow-lg" style="background: rgba(212, 175, 55, 0.1); color: #d4af37; letter-spacing: 2px; font-size: 0.85rem; border: 1px solid rgba(212,175,55,0.3);">TOP ROUTES & SERVICES</span>
        <h2 class="display-4 fw-bold mb-3" style="color: #fff; letter-spacing: -1px;">Amritsar to <span style="color: #d4af37;">Hill Stations</span></h2>
        <p class="fs-5 mx-auto" style="color: #a0a0a0; max-width: 750px;">Most of our clients travel from the heart of Punjab straight to the serene Himalayas. We provide exclusive, hygienic, and well-maintained cabs for your scenic outstation journeys.</p>     
      </div>

      <div class="row g-4 justify-content-center wow fadeInUp" data-wow-delay="0.2s">
        <!-- Route 1 -->
        <div class="col-lg-4 col-md-6">
            <div style="background: linear-gradient(145deg, #0a0a0a, #111); border: 1px solid rgba(212, 175, 55, 0.1); border-radius: 20px; padding: 40px; height: 100%; transition: 0.3s; position: relative; overflow: hidden;" onmouseover="this.style.borderColor='rgba(212, 175, 55, 0.5)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.borderColor='rgba(212, 175, 55, 0.1)'; this.style.transform='none';">
                <i class="fas fa-mountain mb-4" style="font-size: 2.5rem; color: #d4af37;"></i>
                <h3 style="color: #fff; font-size: 1.5rem; font-weight: 700; margin-bottom: 15px;">Manali & Rohtang</h3>
                <p style="color: #a0a0a0; margin-bottom: 25px;">A magnificent 400km drive through the valleys. Best experienced in our premium Innova Crysta for comfort through the winding roads.</p>
                <a href="amritsar-to-manali.html" style="color: #d4af37; text-decoration: none; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem;">View Route <i class="fas fa-arrow-right ms-2"></i></a>
            </div>
        </div>
        <!-- Route 2 -->
        <div class="col-lg-4 col-md-6">
            <div style="background: linear-gradient(145deg, #0a0a0a, #111); border: 1px solid rgba(212, 175, 55, 0.1); border-radius: 20px; padding: 40px; height: 100%; transition: 0.3s; position: relative; overflow: hidden;" onmouseover="this.style.borderColor='rgba(212, 175, 55, 0.5)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.borderColor='rgba(212, 175, 55, 0.1)'; this.style.transform='none';">
                <i class="fas fa-vihara mb-4" style="font-size: 2.5rem; color: #d4af37;"></i>
                <h3 style="color: #fff; font-size: 1.5rem; font-weight: 700; margin-bottom: 15px;">Dharamshala & Dalhousie</h3>
                <p style="color: #a0a0a0; margin-bottom: 25px;">The spiritual and scenic escape. Smooth rides to the home of the Dalai Lama, complete with expert hill-station chauffeurs.</p>
                <a href="amritsar-to-dharamshala.html" style="color: #d4af37; text-decoration: none; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem;">View Route <i class="fas fa-arrow-right ms-2"></i></a>
            </div>
        </div>
        <!-- Route 3 -->
        <div class="col-lg-4 col-md-6">
            <div style="background: linear-gradient(145deg, #0a0a0a, #111); border: 1px solid rgba(212, 175, 55, 0.1); border-radius: 20px; padding: 40px; height: 100%; transition: 0.3s; position: relative; overflow: hidden;" onmouseover="this.style.borderColor='rgba(212, 175, 55, 0.5)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.borderColor='rgba(212, 175, 55, 0.1)'; this.style.transform='none';">
                <i class="fas fa-gopuram mb-4" style="font-size: 2.5rem; color: #d4af37;"></i>
                <h3 style="color: #fff; font-size: 1.5rem; font-weight: 700; margin-bottom: 15px;">Amritsar Local & Border</h3>
                <p style="color: #a0a0a0; margin-bottom: 25px;">Before heading to the hills, explore the Golden Temple, Jallianwala Bagh, and the thrilling Wagah Border retreat ceremony.</p>
                <a href="amritsar-heritage-tour.html" style="color: #d4af37; text-decoration: none; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem;">View Route <i class="fas fa-arrow-right ms-2"></i></a>
            </div>
        </div>
      </div>

    </div>
  </section>
  
  <!-- Elite Fleet Presentation -->'''

if bento_pattern.search(html):
    html = bento_pattern.sub(new_bento, html)
else:
    print("Could not find Bento block boundaries using regex properly.")

# Fix Features Quick Bar color
html = re.sub(r'bg-white rounded-circle shadow-sm', 'bg-dark border border-secondary rounded-circle shadow-sm', html)
html = re.sub(r'text-dark fw-bold mb-1', 'text-white fw-bold mb-1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done")
