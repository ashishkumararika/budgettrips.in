import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Colors
text = text.replace('--bg-light: #f8fafc;', '--bg-light: #050505;')
text = text.replace('--text-main: #1e293b;', '--text-main: #f8fafc;')
text = text.replace('--surface: #ffffff;', '--surface: #0a0a0a;')
text = text.replace('--surface-glass: rgba(255, 255, 255, 0.7);', '--surface-glass: rgba(10, 10, 10, 0.85);')

# 2. Hero Overhaul
text = text.replace('Outstation Cabs<br><span>from Amritsar</span>', '<span style="background: linear-gradient(45deg, #fff, #d4af37); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Punjab to Himachal</span><br><span>Premium Cabs</span>')
text = text.replace('Experience North India with unparalleled luxury, reliability, and local expertise. Book your premium ride today.', 'Your trusted itinerary partner for outstation cabs from Amritsar to Dalhousie, Dharamshala, Manali & Shimla. Book your Innova or Maharaja Tempo today.')

# 3. Swap Book Buttons (Form -> WhatsApp)
start_buttons = text.find('<div class="d-flex flex-wrap gap-3 mt-4">')
end_buttons = text.find('</div>', start_buttons) + 6
if start_buttons != -1:
    new_buttons = '''<div class="d-flex flex-wrap gap-3 mt-4">
    <a href="https://wa.me/919878120686?text=Hi!%20I%20want%20to%20book%20a%20cab%20from%20Amritsar%20to%20Himachal." target="_blank" class="btn rounded-pill px-4 py-3 shadow" style="background: #25D366; color: #fff; font-weight: 700; font-size: 1.1rem; border: 2px solid #25D366;">
        <i class="fab fa-whatsapp me-2" style="font-size: 1.3rem;"></i> WhatsApp to Book
    </a>
    <a href="tel:+919878120686" class="btn rounded-pill px-4 py-3 shadow" style="background: rgba(0,0,0,0.4); color: #d4af37; border: 2px solid #d4af37; font-weight: 700; font-size: 1.1rem; backdrop-filter: blur(5px);">
        <i class="fas fa-phone-alt me-2"></i> Call Concierge
    </a>
</div>'''
    text = text[:start_buttons] + new_buttons + text[end_buttons:]

# 4. Replace Bento section with Dark Luxury route cards
start_bento = text.find('<!-- World-Class Bento Services -->')
end_bento = text.find('<!-- Elite Fleet Presentation -->')

if start_bento != -1 and end_bento != -1:
    new_bento_html = '''<!-- Top Route Focus (Dark Luxury Theme) -->
  <section class="bento-section" style="padding: 6rem 0; background: #000; border-top: 1px solid rgba(212, 175, 55, 0.1);">
    <div class="container">
      <div class="text-center mb-5 pb-3 wow fadeInUp" data-wow-delay="0.1s">
        <span class="badge px-4 py-2 rounded-pill mb-3 fw-bold shadow-lg" style="background: rgba(212, 175, 55, 0.1); color: #d4af37; border: 1px solid rgba(212,175,55,0.3); letter-spacing: 2px;">HIMALAYAN EXPERTS</span>
        <h2 class="display-4 fw-bold mb-3" style="color: #fff; letter-spacing: -1px;">Amritsar to <span style="color: #d4af37;">Hill Stations</span></h2>
        <p class="fs-5 mx-auto" style="color: #a0a0a0; max-width: 750px;">Most of our clients travel from the heart of Punjab straight to the serene Himalayas. We provide exclusive, well-maintained cabs for your scenic outstation journeys.</p>     
      </div>

      <div class="row g-4 justify-content-center wow fadeInUp" data-wow-delay="0.2s">
        <div class="col-lg-4 col-md-6">
            <div style="background: linear-gradient(145deg, rgba(20,20,20,0.9), rgba(10,10,10,0.8)); border: 1px solid rgba(212, 175, 55, 0.15); border-radius: 20px; padding: 40px; height: 100%; position: relative; overflow: hidden;">
                <i class="fas fa-mountain mb-4" style="font-size: 2.5rem; color: #d4af37;"></i>
                <h3 style="color: #fff; font-size: 1.5rem; font-weight: 700; margin-bottom: 15px;">Manali & Rohtang</h3>
                <p style="color: #a0a0a0; margin-bottom: 25px;">A magnificent 400km drive through the valleys. Best experienced in our premium Innova Crysta.</p>
                <div class="d-flex justify-content-between align-items-center">
                    <a href="amritsar-to-manali.html" style="color: #d4af37; text-decoration: none; font-weight: 600; text-transform: uppercase;">View Route <i class="fas fa-arrow-right ms-1"></i></a>
                    <a href="https://wa.me/919878120686?text=I'm%20interested%20in%20a%20cab%20from%20Amritsar%20to%20Manali." target="_blank" style="color: #25D366; font-size: 1.5rem; text-decoration: none;"><i class="fab fa-whatsapp"></i></a>
                </div>
            </div>
        </div>
        <div class="col-lg-4 col-md-6">
            <div style="background: linear-gradient(145deg, rgba(20,20,20,0.9), rgba(10,10,10,0.8)); border: 1px solid rgba(212, 175, 55, 0.15); border-radius: 20px; padding: 40px; height: 100%; position: relative; overflow: hidden;">
                <i class="fas fa-vihara mb-4" style="font-size: 2.5rem; color: #d4af37;"></i>
                <h3 style="color: #fff; font-size: 1.5rem; font-weight: 700; margin-bottom: 15px;">Dharamshala</h3>
                <p style="color: #a0a0a0; margin-bottom: 25px;">The spiritual and scenic escape. Smooth rides to the home of the Dalai Lama with expert hill-station chauffeurs.</p>
                <div class="d-flex justify-content-between align-items-center">
                    <a href="amritsar-to-dharamshala.html" style="color: #d4af37; text-decoration: none; font-weight: 600; text-transform: uppercase;">View Route <i class="fas fa-arrow-right ms-1"></i></a>
                    <a href="https://wa.me/919878120686?text=I'm%20interested%20in%20a%20cab%20from%20Amritsar%20to%20Dharamshala." target="_blank" style="color: #25D366; font-size: 1.5rem; text-decoration: none;"><i class="fab fa-whatsapp"></i></a>
                </div>
            </div>
        </div>
        <div class="col-lg-4 col-md-6">
            <div style="background: linear-gradient(145deg, rgba(20,20,20,0.9), rgba(10,10,10,0.8)); border: 1px solid rgba(212, 175, 55, 0.15); border-radius: 20px; padding: 40px; height: 100%; position: relative; overflow: hidden;">
                <i class="fas fa-gopuram mb-4" style="font-size: 2.5rem; color: #d4af37;"></i>
                <h3 style="color: #fff; font-size: 1.5rem; font-weight: 700; margin-bottom: 15px;">Amritsar & Border</h3>
                <p style="color: #a0a0a0; margin-bottom: 25px;">Before heading to the hills, explore the Golden Temple, Jallianwala Bagh, and the thrilling Wagah Border retreat.</p>
                <div class="d-flex justify-content-between align-items-center">
                    <a href="amritsar-heritage-tour.html" style="color: #d4af37; text-decoration: none; font-weight: 600; text-transform: uppercase;">View Route <i class="fas fa-arrow-right ms-1"></i></a>
                    <a href="https://wa.me/919878120686?text=I'm%20interested%20in%20Amritsar%20Local." target="_blank" style="color: #25D366; font-size: 1.5rem; text-decoration: none;"><i class="fab fa-whatsapp"></i></a>
                </div>
            </div>
        </div>
      </div>
    </div>
  </section>
  
  <!-- Elite Fleet Presentation -->'''

    text = text[:start_bento] + new_bento_html + text[end_bento + len('<!-- Elite Fleet Presentation -->'):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done script")
