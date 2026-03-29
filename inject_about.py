import sys
import re

def rewrite_about(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The block we are replacing is everything between <!-- Hero Section --> and <!-- Footer Start -->
    start_tag = '<!-- Hero Section -->'
    end_tag = '<!-- Footer Start -->'
    
    if start_tag not in content or end_tag not in content:
        print("Could not find start/end tags in about.html")
        return

    new_html = '''<!-- Hero Section -->
<style>
/* Luxury About Page Styles */
.about-luxury-hero {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
    padding: 180px 0 100px 0;
    position: relative;
    overflow: hidden;
    color: #fff;
    border-bottom: 1px solid rgba(212, 175, 55, 0.2);
}
.about-luxury-hero::after {
    content: '';
    position: absolute;
    top: -50%; left: -50%; width: 200%; height: 200%;
    background: radial-gradient(circle at 50% 50%, rgba(212, 175, 55, 0.05) 0%, transparent 50%);
    animation: goldPulse 15s ease-in-out infinite alternate;
    z-index: 0;
}
@keyframes goldPulse {
    0% { transform: scale(0.95); opacity: 0.8; }
    100% { transform: scale(1.05); opacity: 1; }
}
.hero-content {
    position: relative;
    z-index: 2;
}
.luxury-quote-box {
    margin-bottom: 30px;
    display: inline-block;
    background: rgba(212, 175, 55, 0.05);
    padding: 10px 25px;
    border-radius: 50px;
    border: 1px solid rgba(212, 175, 55, 0.2);
}
.luxury-quote-text {
    font-family: 'Georgia', serif;
    font-style: italic;
    color: #d4af37;
    font-size: 1rem;
    letter-spacing: 1px;
}
.about-title {
    font-size: 3.5rem;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 25px;
    background: linear-gradient(45deg, #fff, #a0a0a0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.about-title span {
    background: linear-gradient(45deg, #f9d423, #d4af37, #ff4e50);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.about-subtitle {
    font-size: 1.25rem;
    color: #a0a0a0;
    line-height: 1.8;
    max-width: 700px;
}

/* Philosophy Section */
.philosophy-section {
    background: #000;
    padding: 100px 0;
    position: relative;
}
.glass-box {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(16px);
    border-radius: 20px;
    padding: 50px;
    height: 100%;
    transition: transform 0.4s ease, border-color 0.4s ease;
}
.glass-box:hover {
    transform: translateY(-10px);
    border-color: rgba(212, 175, 55, 0.4);
    box-shadow: 0 20px 40px rgba(0,0,0,0.8);
}
.glass-icon {
    font-size: 2.5rem;
    color: #d4af37;
    margin-bottom: 25px;
}
.glass-title {
    color: #fff;
    font-size: 1.5rem;
    margin-bottom: 15px;
    font-weight: 700;
}
.glass-text {
    color: #a0a0a0;
    line-height: 1.7;
    font-size: 1rem;
}

/* Elite Stats */
.elite-stats {
    background: linear-gradient(180deg, #000 0%, #0a0a0a 100%);
    padding: 80px 0;
    border-top: 1px solid rgba(212, 175, 55, 0.1);
    border-bottom: 1px solid rgba(212, 175, 55, 0.1);
}
.stat-item {
    text-align: center;
    padding: 30px;
}
.stat-number {
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(45deg, #d4af37, #f9d423);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.stat-label {
    color: #a0a0a0;
    font-size: 1.1rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Luxury Testimonials */
.reviews-section {
    background: #050505;
    padding: 100px 0;
}
.review-card {
    background: rgba(20, 20, 20, 0.8);
    border: 1px solid rgba(212, 175, 55, 0.1);
    border-radius: 15px;
    padding: 40px;
    margin-bottom: 30px;
    position: relative;
}
.review-card::before {
    content: '\\f10d';
    font-family: 'Font Awesome 5 Free';
    font-weight: 900;
    position: absolute;
    top: 30px;
    right: 30px;
    font-size: 3rem;
    color: rgba(212, 175, 55, 0.1);
}
.review-text {
    color: #dfdfdf;
    font-size: 1.1rem;
    font-style: italic;
    line-height: 1.8;
    margin-bottom: 25px;
}
.review-author {
    color: #fff;
    font-weight: 700;
    font-size: 1.1rem;
}
.review-location {
    color: #d4af37;
    font-size: 0.85rem;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.review-stars {
    color: #d4af37;
    font-size: 0.9rem;
    margin-top: 10px;
}
</style>

<section class="about-luxury-hero">
    <div class="container hero-content">
        <div class="row align-items-center">
            <div class="col-lg-8">
                <div class="luxury-quote-box">
                    <i class="fa fa-quote-left" style="color: #d4af37; margin-right: 10px;"></i>
                    <span class="luxury-quote-text">"A journey of a thousand miles begins with a single step, guided by elegance."</span>
                </div>
                <h1 class="about-title">The Standard of<br><span>Premium Mobility.</span></h1>
                <p class="about-subtitle">BudgetTrips was founded with a singular vision: to elevate travel across North India from a mere commute into a masterclass in comfort, reliability, and luxury. We are not just a transport company; we are curators of impeccable journeys.</p>
                <div class="mt-5">
                    <a href="mailto:info@budgettrips.in" class="btn rounded-pill px-5 py-3 shadow" style="background: #d4af37; color: #000; font-weight: 700; letter-spacing: 1px;"><i class="fas fa-envelope me-2"></i> Contact Concierge</a>
                </div>
            </div>
            <div class="col-lg-4 d-none d-lg-block text-end">
                <div style="position: relative; display: inline-block;">
                    <div style="position: absolute; top: -20px; right: -20px; width: 100%; height: 100%; border: 2px solid #d4af37; border-radius: 20px; z-index: 1;"></div>
                    <img src="img/about-2.png" alt="Premium Fleet" class="img-fluid rounded shadow-lg" style="position: relative; z-index: 2; border-radius: 20px;">
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Elite Philosophy -->
<section class="philosophy-section">
    <div class="container">
        <div class="text-center mb-5 pb-4">
            <h6 class="text-uppercase" style="color: #d4af37; letter-spacing: 3px; font-weight: 700;">Our Philosophy</h6>
            <h2 class="text-white" style="font-size: 2.5rem; font-weight: 300;">Why Elites Choose Us</h2>
        </div>
        <div class="row g-4">
            <div class="col-lg-4 col-md-6">
                <div class="glass-box">
                    <i class="fas fa-gem glass-icon"></i>
                    <h3 class="glass-title">Uncompromising Quality</h3>
                    <p class="glass-text">Every vehicle in our fleet is meticulously maintained. From pristine interiors to rigorous mechanical checks, we ensure your environment is spotless.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="glass-box">
                    <i class="fas fa-user-tie glass-icon"></i>
                    <h3 class="glass-title">Expert Chauffeurs</h3>
                    <p class="glass-text">Our drivers are seasoned professionals. Vetted, courteous, and deeply knowledgeable about the nuances of navigating North Indian terrain.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="glass-box">
                    <i class="fas fa-clock glass-icon"></i>
                    <h3 class="glass-title">24/7 Precision Support</h3>
                    <p class="glass-text">Travel doesn't sleep, and neither do we. Our dedicated support team monitors every journey to guarantee a seamless, zero-friction experience.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Elite Stats -->
<section class="elite-stats">
    <div class="container">
        <div class="row g-4">
            <div class="col-md-3 col-6 stat-item">
                <div class="stat-number">10<span style="font-size: 2rem;">+</span></div>
                <div class="stat-label">Years Heritage</div>
            </div>
            <div class="col-md-3 col-6 stat-item">
                <div class="stat-number">12<span style="font-size: 2rem;">k+</span></div>
                <div class="stat-label">Elite Clients</div>
            </div>
            <div class="col-md-3 col-6 stat-item">
                <div class="stat-number">85<span style="font-size: 2rem;">+</span></div>
                <div class="stat-label">Destinations</div>
            </div>
            <div class="col-md-3 col-6 stat-item">
                <div class="stat-number">4.9<span style="font-size: 2rem;">/5</span></div>
                <div class="stat-label">Global Rating</div>
            </div>
        </div>
    </div>
</section>

<!-- Luxury Reviews -->
<section class="reviews-section">
    <div class="container">
        <div class="text-center mb-5">
            <h6 class="text-uppercase" style="color: #d4af37; letter-spacing: 3px; font-weight: 700;">Testimonials</h6>
            <h2 class="text-white" style="font-size: 2.5rem; font-weight: 300;">Words from our Guests</h2>
        </div>
        <div class="row g-4">
            <div class="col-lg-4 col-md-6">
                <div class="review-card">
                    <p class="review-text">"A masterclass in chauffeured service. Our family trip to Himachal was handled with impeccable professionalism from start to finish."</p>
                    <div class="review-author">Anjali Verma</div>
                    <div class="review-location">Mumbai, India</div>
                    <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="review-card">
                    <p class="review-text">"I regularly book with them for my corporate VIPs arriving in Amritsar. The Innova fleet is flawless, and the drivers are incredibly polished."</p>
                    <div class="review-author">Rahul Mehta</div>
                    <div class="review-location">New Delhi, India</div>
                    <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="review-card">
                    <p class="review-text">"The only way to explore Punjab. They managed our entire heritage tour. Absolute luxury and complete peace of mind."</p>
                    <div class="review-author">Simran Kaur</div>
                    <div class="review-location">Chandigarh, India</div>
                    <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Footer Start -->
'''
    
    start_index = content.find(start_tag)
    end_index = content.find(end_tag) + len(end_tag)
    
    new_content = content[:start_index] + new_html + content[end_index - len(end_tag):]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully overhauled about.html")

rewrite_about('about.html')
