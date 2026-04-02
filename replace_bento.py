import sys

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_bento = text.find('<!-- World-Class Bento Services -->')
end_bento = text.find('<!-- Modern Fleet Integration -->')

if start_bento != -1 and end_bento != -1:
    new_bento_html = '''<!-- Top Route Focus (Dark Luxury Theme) -->
  <section class="bento-section" style="padding: 6rem 0; background: #000; border-top: 1px solid rgba(212, 175, 55, 0.1);">
    <div class="container">
      <div class="text-center mb-5 pb-3 wow fadeInUp" data-wow-delay="0.1s">
        <span class="badge px-4 py-2 rounded-pill mb-3 fw-bold shadow-lg" style="background: rgba(212, 175, 55, 0.1); color: #d4af37; border: 1px solid rgba(212,175,55,0.3); letter-spacing: 2px;">HIMALAYAN EXPERTS</span>
        <h2 class="display-4 fw-bold mb-3" style="color: #fff; letter-spacing: -1px;">Amritsar to <span style="color: #d4af37;">Hill Stations</span></h2>
        <p class="fs-5 mx-auto" style="color: #a0a0a0; max-width: 750px;">Most of our clients travel from the heart of Punjab straight to the serene Himalayas. We provide exclusive, well-maintained cabs for your scenic outstation journeys. Call or WhatsApp us to get instant pricing.</p>     
      </div>

      <div class="row g-4 justify-content-center wow fadeInUp" data-wow-delay="0.2s">
        <div class="col-lg-4 col-md-6">
            <div style="background: linear-gradient(145deg, rgba(20,20,20,0.9), rgba(10,10,10,0.8)); border: 1px solid rgba(212, 175, 55, 0.15); border-radius: 20px; padding: 40px; height: 100%; position: relative; overflow: hidden; transition: transform 0.3s; transform-origin: center;" onmouseover="this.style.transform='scale(1.03)';" onmouseout="this.style.transform='scale(1)';">
                <i class="fas fa-mountain mb-4" style="font-size: 2.5rem; color: #d4af37;"></i>
                <h3 style="color: #fff; font-size: 1.5rem; font-weight: 700; margin-bottom: 15px;">Manali & Rohtang</h3>
                <p style="color: #a0a0a0; margin-bottom: 25px;">A magnificent 400km drive through the valleys. Best experienced in our premium Innova Crysta.</p>
                <div class="d-flex justify-content-between align-items-center mt-auto">
                    <a href="amritsar-to-manali.html" style="color: #d4af37; text-decoration: none; font-weight: 600; text-transform: uppercase; font-size: 0.9rem;">View Route <i class="fas fa-arrow-right ms-1"></i></a>
                    <a href="https://wa.me/919878120686?text=I'm%20interested%20in%20a%20cab%20from%20Amritsar%20to%20Manali." target="_blank" style="background: #25D366; color: #fff; padding: 10px 15px; border-radius: 50px; text-decoration: none; font-weight:bold; font-size:14px;"><i class="fab fa-whatsapp me-1"></i> Book</a>
                </div>
            </div>
        </div>
        <div class="col-lg-4 col-md-6">
            <div style="background: linear-gradient(145deg, rgba(20,20,20,0.9), rgba(10,10,10,0.8)); border: 1px solid rgba(212, 175, 55, 0.15); border-radius: 20px; padding: 40px; height: 100%; position: relative; overflow: hidden; transition: transform 0.3s; transform-origin: center;" onmouseover="this.style.transform='scale(1.03)';" onmouseout="this.style.transform='scale(1)';">
                <i class="fas fa-vihara mb-4" style="font-size: 2.5rem; color: #d4af37;"></i>
                <h3 style="color: #fff; font-size: 1.5rem; font-weight: 700; margin-bottom: 15px;">Dharamshala</h3>
                <p style="color: #a0a0a0; margin-bottom: 25px;">The spiritual and scenic escape. Smooth rides to the home of the Dalai Lama with expert hill-station chauffeurs.</p>
                <div class="d-flex justify-content-between align-items-center mt-auto">
                    <a href="amritsar-to-dharamshala.html" style="color: #d4af37; text-decoration: none; font-weight: 600; text-transform: uppercase; font-size: 0.9rem;">View Route <i class="fas fa-arrow-right ms-1"></i></a>
                    <a href="https://wa.me/919878120686?text=I'm%20interested%20in%20a%20cab%20from%20Amritsar%20to%20Dharamshala." target="_blank" style="background: #25D366; color: #fff; padding: 10px 15px; border-radius: 50px; text-decoration: none; font-weight:bold; font-size:14px;"><i class="fab fa-whatsapp me-1"></i> Book</a>
                </div>
            </div>
        </div>
        <div class="col-lg-4 col-md-6">
            <div style="background: linear-gradient(145deg, rgba(20,20,20,0.9), rgba(10,10,10,0.8)); border: 1px solid rgba(212, 175, 55, 0.15); border-radius: 20px; padding: 40px; height: 100%; position: relative; overflow: hidden; transition: transform 0.3s; transform-origin: center;" onmouseover="this.style.transform='scale(1.03)';" onmouseout="this.style.transform='scale(1)';">
                <i class="fas fa-gopuram mb-4" style="font-size: 2.5rem; color: #d4af37;"></i>
                <h3 style="color: #fff; font-size: 1.5rem; font-weight: 700; margin-bottom: 15px;">Amritsar & Border</h3>
                <p style="color: #a0a0a0; margin-bottom: 25px;">Before heading to the hills, explore the Golden Temple, Jallianwala Bagh, and the thrilling Wagah Border retreat.</p>
                <div class="d-flex justify-content-between align-items-center mt-auto">
                    <a href="amritsar-heritage-tour.html" style="color: #d4af37; text-decoration: none; font-weight: 600; text-transform: uppercase; font-size: 0.9rem;">View Route <i class="fas fa-arrow-right ms-1"></i></a>
                    <a href="https://wa.me/919878120686?text=I'm%20interested%20in%20Amritsar%20Local." target="_blank" style="background: #25D366; color: #fff; padding: 10px 15px; border-radius: 50px; text-decoration: none; font-weight:bold; font-size:14px;"><i class="fab fa-whatsapp me-1"></i> Book</a>
                </div>
            </div>
        </div>
      </div>
    </div>
  </section>

  '''

    text = text[:start_bento] + new_bento_html + text[end_bento:]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replaced Bento with dark route cards successfully.")
else:
    print("Tags not found.")
