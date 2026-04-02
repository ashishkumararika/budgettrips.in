import sys

with open('taxi-services.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<!-- Header Start -->'
end_marker = '<!-- Footer Start -->'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    fleet_html = '''<!-- Header Start -->
<div class="container-fluid bg-breadcrumb" style="background: linear-gradient(rgba(5, 5, 5, 0.85), rgba(5, 5, 5, 0.85)), url('img/wide%20golden%20temple%20view.jpg') center center no-repeat; background-size: cover; border-bottom: 1px solid rgba(212,175,55,0.2);">
  <div class="container text-center py-5" style="max-width: 900px">
    <h1 class="text-white display-4 mb-3 wow fadeInDown" data-wow-delay="0.1s" style="letter-spacing: -1px; font-weight: 700;">
      Our <span style="color: #d4af37;">Premium Fleet</span>
    </h1>
    <ol class="breadcrumb justify-content-center mb-0 wow fadeInDown" data-wow-delay="0.3s">
      <li class="breadcrumb-item"><a href="index.html" style="color: #a0a0a0;">Home</a></li>
      <li class="breadcrumb-item active" style="color: #d4af37;">Our Fleet</li>
    </ol>
  </div>
</div>
<!-- Header End -->

<!-- Fleet Main Section -->
<div class="container-fluid py-5" style="background: #050505; color: #fff;">
  <div class="container py-5">
    <div class="text-center mb-5 wow fadeInUp" data-wow-delay="0.1s">
        <h6 class="text-uppercase" style="color: #25D366; font-weight: 700; letter-spacing: 2px;">Hill-Station Ready Vehicles</h6>
        <h2 class="display-5 mb-3" style="color: #fff;">Travel in Absolute <span style="color: #d4af37;">Comfort & Safety</span></h2>
        <p style="color: #a0a0a0; max-width: 700px; margin: 0 auto; font-size: 1.1rem;">Whether you're exploring the bustling streets of Amritsar or embarking on a thrilling journey to the Himalayas, our meticulously maintained and spacious cabs ensure a flawless ride.</p>
    </div>

    <!-- Vehicles Grid -->
    <div class="row g-5">
        
        <!-- Innova Crysta -->
        <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.3s">
            <div style="background: linear-gradient(145deg, #111, #0a0a0a); border: 1px solid rgba(212,175,55,0.2); border-radius: 20px; overflow: hidden; height: 100%;">
                <div style="padding: 40px; border-bottom: 1px solid rgba(255,255,255,0.05); background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%); text-align: center;">
                    <i class="fas fa-car-side" style="font-size: 5rem; color: #d4af37; opacity: 0.8; filter: drop-shadow(0 0 10px rgba(212,175,55,0.3));"></i>
                </div>
                <div style="padding: 40px;">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h3 style="color: #fff; margin:0; font-weight: 700;">Innova Crysta / Hycross</h3>
                        <span style="background: rgba(212,175,55,0.1); color: #d4af37; padding: 5px 15px; border-radius: 50px; font-size: 0.9rem; font-weight:bold;">Most Demanded</span>
                    </div>
                    <p style="color: #a0a0a0;">The ultimate executive SUV. Famous for unmatchable comfort on the steep mountain roads of Himachal. Plenty of room to stretch your legs.</p>
                    
                    <ul class="list-unstyled mb-4" style="color: #e0e0e0;">
                        <li class="mb-2"><i class="fas fa-users me-2" style="color: #25D366; width:20px;"></i> <strong>Seating:</strong> 6 to 7 Passengers</li>
                        <li class="mb-2"><i class="fas fa-suitcase me-2" style="color: #25D366; width:20px;"></i> <strong>Luggage:</strong> 3-4 Large Bags (Carrier equipped)</li>
                        <li class="mb-2"><i class="fas fa-snowflake me-2" style="color: #25D366; width:20px;"></i> <strong>Features:</strong> Dual AC, Plush Captain Seats</li>
                        <li class="mb-2"><i class="fas fa-mountain me-2" style="color: #25D366; width:20px;"></i> <strong>Best For:</strong> Manali, Shimla, Premium Family Tours</li>
                    </ul>

                    <div class="d-flex gap-3">
                        <a href="https://wa.me/919878120686?text=I%20want%20to%20book%20an%20Innova%20Crysta" target="_blank" class="btn flex-grow-1 py-3" style="background: #25D366; color: #fff; font-weight: 600; border-radius: 10px;"><i class="fab fa-whatsapp me-2"></i> Book Innova</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Maruti Ertiga -->
        <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.4s">
            <div style="background: linear-gradient(145deg, #111, #0a0a0a); border: 1px solid rgba(212,175,55,0.2); border-radius: 20px; overflow: hidden; height: 100%;">
                <div style="padding: 40px; border-bottom: 1px solid rgba(255,255,255,0.05); background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%); text-align: center;">
                    <i class="fas fa-car-rear" style="font-size: 5rem; color: #d4af37; opacity: 0.8;"></i>
                </div>
                <div style="padding: 40px;">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h3 style="color: #fff; margin:0; font-weight: 700;">Maruti Ertiga / Carens</h3>
                        <span style="background: rgba(212,175,55,0.1); color: #d4af37; padding: 5px 15px; border-radius: 50px; font-size: 0.9rem; font-weight:bold;">Family Favorite</span>
                    </div>
                    <p style="color: #a0a0a0;">The perfect budget-friendly MUV for medium families. Efficient, smooth, and easily navigates winding Himalayan terrain.</p>
                    
                    <ul class="list-unstyled mb-4" style="color: #e0e0e0;">
                        <li class="mb-2"><i class="fas fa-users me-2" style="color: #25D366; width:20px;"></i> <strong>Seating:</strong> 5 to 6 Passengers</li>
                        <li class="mb-2"><i class="fas fa-suitcase me-2" style="color: #25D366; width:20px;"></i> <strong>Luggage:</strong> 2-3 Medium Bags</li>
                        <li class="mb-2"><i class="fas fa-snowflake me-2" style="color: #25D366; width:20px;"></i> <strong>Features:</strong> AC, Smooth Suspension</li>
                        <li class="mb-2"><i class="fas fa-mountain me-2" style="color: #25D366; width:20px;"></i> <strong>Best For:</strong> Dalhousie, Dharamshala, Budget Tours</li>
                    </ul>

                    <div class="d-flex gap-3">
                        <a href="https://wa.me/919878120686?text=I%20want%20to%20book%20a%20Maruti%20Ertiga" target="_blank" class="btn flex-grow-1 py-3" style="background: transparent; border: 2px solid #25D366; color: #25D366; font-weight: 600; border-radius: 10px;"><i class="fab fa-whatsapp me-2"></i> Book Ertiga</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Premium Sedan -->
        <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.5s">
            <div style="background: linear-gradient(145deg, #111, #0a0a0a); border: 1px solid rgba(212,175,55,0.2); border-radius: 20px; overflow: hidden; height: 100%;">
                <div style="padding: 40px; border-bottom: 1px solid rgba(255,255,255,0.05); background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%); text-align: center;">
                    <i class="fas fa-car" style="font-size: 5rem; color: #d4af37; opacity: 0.8;"></i>
                </div>
                <div style="padding: 40px;">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h3 style="color: #fff; margin:0; font-weight: 700;">Sedan (Dzire / Amaze)</h3>
                        <span style="background: rgba(212,175,55,0.1); color: #d4af37; padding: 5px 15px; border-radius: 50px; font-size: 0.9rem; font-weight:bold;">Couples & Solo</span>
                    </div>
                    <p style="color: #a0a0a0;">A smart choice for couples, solo travelers, or small groups. Extremely comfortable for city tours and highway cruising.</p>
                    
                    <ul class="list-unstyled mb-4" style="color: #e0e0e0;">
                        <li class="mb-2"><i class="fas fa-users me-2" style="color: #25D366; width:20px;"></i> <strong>Seating:</strong> 3 to 4 Passengers</li>
                        <li class="mb-2"><i class="fas fa-suitcase me-2" style="color: #25D366; width:20px;"></i> <strong>Luggage:</strong> 2 Large Bags (Spacious boot)</li>
                        <li class="mb-2"><i class="fas fa-snowflake me-2" style="color: #25D366; width:20px;"></i> <strong>Features:</strong> Fast AC, Sedate Ride</li>
                        <li class="mb-2"><i class="fas fa-city me-2" style="color: #25D366; width:20px;"></i> <strong>Best For:</strong> Amritsar Local, Interstate Drops</li>
                    </ul>

                    <div class="d-flex gap-3">
                        <a href="https://wa.me/919878120686?text=I%20want%20to%20book%20a%20Sedan" target="_blank" class="btn flex-grow-1 py-3" style="background: transparent; border: 2px solid #25D366; color: #25D366; font-weight: 600; border-radius: 10px;"><i class="fab fa-whatsapp me-2"></i> Book Sedan</a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tempo Traveller -->
        <div class="col-lg-6 wow fadeInUp" data-wow-delay="0.6s">
            <div style="background: linear-gradient(145deg, #111, #0a0a0a); border: 1px solid rgba(212,175,55,0.2); border-radius: 20px; overflow: hidden; height: 100%;">
                <div style="padding: 40px; border-bottom: 1px solid rgba(255,255,255,0.05); background: radial-gradient(circle at center, #1a1a1a 0%, #050505 100%); text-align: center;">
                    <i class="fas fa-bus" style="font-size: 5rem; color: #d4af37; opacity: 0.8;"></i>
                </div>
                <div style="padding: 40px;">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h3 style="color: #fff; margin:0; font-weight: 700;">Luxury Tempo Traveller</h3>
                        <span style="background: rgba(212,175,55,0.1); color: #d4af37; padding: 5px 15px; border-radius: 50px; font-size: 0.9rem; font-weight:bold;">Large Groups</span>
                    </div>
                    <p style="color: #a0a0a0;">Pushback seats, ample headroom, and massive luggage capacity. Bring the whole extended family for an epic Himalayan adventure.</p>
                    
                    <ul class="list-unstyled mb-4" style="color: #e0e0e0;">
                        <li class="mb-2"><i class="fas fa-users me-2" style="color: #25D366; width:20px;"></i> <strong>Seating:</strong> 9 to 16 Passengers</li>
                        <li class="mb-2"><i class="fas fa-suitcase me-2" style="color: #25D366; width:20px;"></i> <strong>Luggage:</strong> 10+ Bags (Dedicated carrier)</li>
                        <li class="mb-2"><i class="fas fa-music me-2" style="color: #25D366; width:20px;"></i> <strong>Features:</strong> Pushback seats, Custom AV system</li>
                        <li class="mb-2"><i class="fas fa-mountain me-2" style="color: #25D366; width:20px;"></i> <strong>Best For:</strong> Group Tours, Extended Family Trips</li>
                    </ul>

                    <div class="d-flex gap-3">
                        <a href="https://wa.me/919878120686?text=I%20want%20to%20book%20a%20Tempo%20Traveller" target="_blank" class="btn flex-grow-1 py-3" style="background: transparent; border: 2px solid #25D366; color: #25D366; font-weight: 600; border-radius: 10px;"><i class="fab fa-whatsapp me-2"></i> Custom Quote</a>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <!-- Assurance Banner -->
    <div class="mt-5 p-5 text-center wow fadeInUp" data-wow-delay="0.7s" style="background: radial-gradient(circle at center, #151515 0%, #050505 100%); border: 1px solid rgba(212,175,55,0.3); border-radius: 20px;">
        <h4 style="color: #d4af37; margin-bottom: 20px; font-weight: 700;">All Vehicles are Mountain-Ready</h4>
        <p style="color: #a0a0a0; font-size: 1.1rem; max-width: 800px; margin: 0 auto 30px;">Every car in our fleet undergoes a rigorous 20-point mechanical check before dispatch on any outstation journey. Heavy tread tires, optimal brake fluids, and pristine AC mapping mean you have zero breakdown worries on steep terrain.</p>
        <a href="tel:919878120686" class="btn px-4 py-3" style="background: #25D366; color: #fff; font-weight: bold; border-radius: 50px;"><i class="fas fa-phone-alt me-2"></i> Speak to our Transport Manager</a>
    </div>

  </div>
</div>
<!-- Fleet Main Section End -->
'''
    new_text = text[:start_idx] + fleet_html + text[end_idx:]
    with open('taxi-services.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fleet replaced successfully.")
else:
    print("Markers not found.")
