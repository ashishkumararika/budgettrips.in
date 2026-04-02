import sys

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<!-- Modern Fleet Integration -->'

trust_html = '''
  <!-- Mountain & Family Safety Feature -->
  <section class="py-5" style="background: #080808; border-top: 1px solid rgba(212,175,55,0.1);">
    <div class="container">
      <div class="row align-items-center g-5">
        <div class="col-lg-6 wow fadeInLeft" data-wow-delay="0.1s">
            <h6 class="text-uppercase mb-3" style="color: #25D366; font-weight: 700; letter-spacing: 2px;"><i class="fas fa-shield-alt me-2"></i> Your Safety is Our Priority</h6>
            <h2 class="display-6 fw-bold mb-4" style="color: #fff;">Why Families & Solo Travelers Trust Us</h2>
            <p class="mb-4" style="color: #a0a0a0; font-size: 1.1rem;">Traveling across state lines to the Himalayas requires more than just a car. It requires absolute reliability. We have designed our service around total peace of mind.</p>
            
            <div class="d-flex align-items-start mb-4">
                <div class="flex-shrink-0" style="width: 50px; height: 50px; background: rgba(212,175,55,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(212,175,55,0.3);">
                    <i class="fas fa-steering-wheel" style="font-size: 1.5rem; color: #d4af37;"></i>
                </div>
                <div class="ms-4">
                    <h5 style="color: #fff; font-weight: 600;">Mountain-Trained Chauffeurs</h5>
                    <p style="color: #a0a0a0; margin: 0;">Driving in Himachal Pradesh is challenging. Our drivers have 5+ years of exclusive hill-station driving experience.</p>
                </div>
            </div>

            <div class="d-flex align-items-start mb-4">
                <div class="flex-shrink-0" style="width: 50px; height: 50px; background: rgba(37,211,102,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(37,211,102,0.3);">
                    <i class="fas fa-female" style="font-size: 1.5rem; color: #25D366;"></i>
                </div>
                <div class="ms-4">
                    <h5 style="color: #fff; font-weight: 600;">Female & Family Safe</h5>
                    <p style="color: #a0a0a0; margin: 0;">Strict code of conduct. Live GPS sharing enabled. Our drivers are trained to be respectful, polite, and completely professional.</p>
                </div>
            </div>

            <div class="d-flex align-items-start mb-4">
                <div class="flex-shrink-0" style="width: 50px; height: 50px; background: rgba(212,175,55,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(212,175,55,0.3);">
                    <i class="fas fa-car-crash" style="font-size: 1.5rem; color: #d4af37;"></i>
                </div>
                <div class="ms-4">
                    <h5 style="color: #fff; font-weight: 600;">Zero-Breakdown Policy</h5>
                    <p style="color: #a0a0a0; margin: 0;">All vehicles are heavily serviced before outstation trips. In the rare event of an issue, we dispatch a replacement cab immediately.</p>
                </div>
            </div>

            <a href="https://wa.me/919878120686?text=I%20have%20a%20query%20regarding%20outstation%20safety%20and%20booking." target="_blank" class="btn px-4 py-3 mt-2 fw-bold" style="background: transparent; border: 2px solid #25D366; color: #25D366; border-radius: 50px;">
                <i class="fab fa-whatsapp me-2"></i>Chat with our Safety Team
            </a>
        </div>
        
        <!-- Social Proof / Testimonial Stack -->
        <div class="col-lg-6 wow fadeInRight" data-wow-delay="0.3s">
            <div style="background: linear-gradient(145deg, #111, #050505); border: 1px solid rgba(212,175,55,0.2); border-radius: 20px; padding: 40px; position: relative;">
                <i class="fas fa-quote-left mb-4" style="font-size: 3rem; color: rgba(212,175,55,0.2); position: absolute; top: 30px; right: 40px;"></i>
                <h4 style="color: #d4af37; margin-bottom: 30px;">What our passengers say</h4>
                
                <div style="border-left: 3px solid #25D366; padding-left: 20px; margin-bottom: 30px;">
                    <p style="color: #e0e0e0; font-style: italic; font-size: 1.1rem; line-height: 1.6;">"Traveled from Amritsar to Dalhousie with my wife and two young daughters. The driver was incredibly polite, never sped on the dangerous curves, and made us feel 100% secure the entire 4 days."</p>
                    <h6 style="color: #fff; margin: 0;">Rahul Sharma</h6>
                    <small style="color: #a0a0a0;">Family Trip to Himachal</small>
                </div>

                <div style="border-left: 3px solid #d4af37; padding-left: 20px;">
                    <p style="color: #e0e0e0; font-style: italic; font-size: 1.1rem; line-height: 1.6;">"As a solo female traveler visiting the Golden Temple and Wagah Border, I was nervous. My cab driver acted like a local guardian. Extremely respectful and safe!"</p>
                    <h6 style="color: #fff; margin: 0;">Priya Desai</h6>
                    <small style="color: #a0a0a0;">Solo Traveler, Mumbai</small>
                </div>
            </div>
        </div>
      </div>
    </div>
  </section>

'''

if target in text and 'Why Families & Solo Travelers Trust Us' not in text:
    text = text.replace(target, trust_html + target)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Trust section added successfully.")
else:
    print("Target not found or already added.")
