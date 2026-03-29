# -*- coding: utf-8 -*-
import re

html = open('c:/data/newc/about/index2.html', encoding='utf-8').read()

head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', html, re.DOTALL)
head = head_match.group(1) if head_match else ''

new_css = """
  <!-- NEW AGE CSS -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #0f172a;
      --secondary: #3b82f6;
      --accent: #f59e0b;
      --surface: #ffffff;
      --surface-glass: rgba(255, 255, 255, 0.7);
      --bg-light: #f8fafc;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --radius-lg: 24px;
      --radius-xl: 32px;
      --shadow-soft: 0 20px 40px -10px rgba(0,0,0,0.05);
      --shadow-glass: 0 8px 32px rgba(31, 38, 135, 0.07);
    }
    body {
      font-family: 'Inter', sans-serif;
      color: var(--text-main);
      background-color: var(--bg-light);
      -webkit-font-smoothing: antialiased;
    }
    h1, h2, h3, h4, h5, h6 {
      font-family: 'Playfair Display', serif;
    }
    
    /* Elegant Nav */
    .new-nav {
      background: var(--surface-glass);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(255,255,255,0.3);
      position: sticky;
      top: 0;
      z-index: 1000;
      transition: all 0.3s ease;
    }
    .new-nav .nav-link {
      font-weight: 500;
      color: var(--primary) !important;
      padding: 1rem 1.5rem !important;
      position: relative;
    }
    .new-nav .nav-link::after {
      content: '';
      position: absolute;
      bottom: 8px; left: 1.5rem; right: 1.5rem;
      height: 2px;
      background: var(--secondary);
      transform: scaleX(0);
      transition: transform 0.3s ease;
    }
    .new-nav .nav-link:hover::after {
      transform: scaleX(1);
    }

    /* Cinematic Hero */
    .new-hero {
      position: relative;
      height: 90vh;
      min-height: 700px;
      background: url('img/wide%20golden%20temple%20view.jpg') center/cover no-repeat;
      display: flex;
      align-items: center;
      padding-top: 80px;
      border-radius: 0 0 40px 40px;
      overflow: hidden;
    }
    .new-hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, rgba(15,23,42,0.95) 0%, rgba(15,23,42,0.6) 100%);
    }
    .hero-content {
      position: relative;
      z-index: 2;
      color: white;
    }
    .hero-title {
      font-size: 5rem;
      line-height: 1.1;
      font-weight: 800;
      margin-bottom: 1.5rem;
      background: linear-gradient(to right, #ffffff, #94a3b8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
      font-size: 1.25rem;
      font-weight: 400;
      opacity: 0.9;
      margin-bottom: 2.5rem;
      max-width: 600px;
    }
    
    /* Glassmorphism Booking Widget */
    .booking-widget {
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(24px);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      box-shadow: var(--shadow-glass);
      color: white;
      transform: translateY(20px);
      animation: floatUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes floatUp {
      to { transform: translateY(0); }
    }
    
    .widget-btn {
      width: 100%;
      padding: 1rem;
      border-radius: 12px;
      font-weight: 600;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      transition: all 0.3s ease;
      text-decoration: none;
    }
    .btn-call { background: var(--secondary); color: white; border: none; }
    .btn-call:hover { background: #2563eb; color: white; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(59,130,246,0.3); }
    .btn-wa { background: #25d366; color: white; border: none; }
    .btn-wa:hover { background: #1ebd57; color: white; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(37,211,102,0.3); }

    /* Bento Grid Services */
    .bento-section {
      padding: 6rem 0;
    }
    .bento-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-auto-rows: 250px;
      gap: 1.5rem;
    }
    .bento-item {
      background: white;
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-soft);
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      text-decoration: none;
      border: 1px solid rgba(0,0,0,0.02);
    }
    .bento-item:hover {
      transform: translateY(-8px);
      box-shadow: 0 30px 60px -12px rgba(0,0,0,0.12);
      border-color: rgba(59, 130, 246, 0.1);
    }
    .bento-large { grid-column: span 2; grid-row: span 2; background: linear-gradient(135deg, white, #f8fafc); }
    .bento-wide { grid-column: span 2; grid-row: span 1; }
    
    .bento-icon {
      width: 64px; height: 64px;
      border-radius: 18px;
      display: flex; align-items: center; justify-content: center;
      font-size: 28px;
      margin-bottom: 2rem;
      transition: transform 0.3s;
    }
    .bento-item:hover .bento-icon { transform: scale(1.1); }
    
    .bento-item h3 { font-size: 1.6rem; font-family: 'Inter', sans-serif; font-weight: 700; color: var(--primary); margin-bottom: 0.75rem; }
    .bento-item p { color: var(--text-muted); font-size: 1rem; margin: 0; line-height: 1.6; }
    .bento-link { font-weight: 600; display: inline-flex; align-items: center; transition: gap 0.3s; }
    .bento-item:hover .bento-link { gap: 10px; }
    .bento-item .bento-link i { transition: transform 0.3s; }
    .bento-item:hover .bento-link i { transform: translateX(5px); }

    /* Fleet Cards */
    .fleet-section { background: var(--bg-light); padding: 5rem 0; border-radius: 40px; margin: 2rem 0; }
    .fleet-card {
      background: white;
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      box-shadow: var(--shadow-soft);
      border: 1px solid rgba(0,0,0,0.03);
      transition: all 0.3s;
    }
    .fleet-card:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.08); }
    .fleet-img-wrap {
      height: 200px;
      border-radius: 16px;
      overflow: hidden;
      margin-bottom: 1.5rem;
      background: #f1f5f9;
    }
    .fleet-img-wrap img {
      width: 100%; height: 100%; object-fit: contain; padding: 1rem; transition: transform 0.5s;
    }
    .fleet-card:hover .fleet-img-wrap img { transform: scale(1.08); }

    @media (max-width: 991px) {
      .hero-title { font-size: 3.5rem; }
      .bento-grid { grid-template-columns: repeat(2, 1fr); auto-rows: minmax(250px, auto); }
      .bento-large { grid-column: span 2; grid-row: span 1; }
    }
    @media (max-width: 768px) {
      .hero-title { font-size: 2.5rem; }
      .bento-grid { grid-template-columns: 1fr; }
      .bento-large, .bento-wide { grid-column: span 1; }
      .new-hero { padding-top: 100px; height: auto; padding-bottom: 60px; min-height: auto; }
    }
  </style>
</head>
"""

head = head.replace('</head>', new_css)

navbar_match = re.search(r'(<!-- Sticky Navbar & Hero Start -->.*?</nav>\s*</div>)', html, re.DOTALL)
navbar = navbar_match.group(1) if navbar_match else ''
navbar = navbar.replace('navbar-light bg-white', 'new-nav').replace('sticky-top shadow-sm', '')

tours_match = re.search(r'(<!-- Tour Packages Start -->.*?<!-- Tour Packages End -->)', html, re.DOTALL)
tours = tours_match.group(1) if tours_match else ''

footer_match = re.search(r'(<!-- Footer Start -->.*)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

body_content = f"""<body>
{navbar}

  <!-- New Age Cinematic Hero -->
  <section class="new-hero">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-7 mb-5 mb-lg-0 wow fadeInUp">
          <div class="hero-content">
            <span class="badge bg-warning text-dark px-4 py-2 rounded-pill mb-4 fw-bold shadow">
              <i class="fas fa-star text-dark me-2"></i>Amritsar's Premium Transport
            </span>
            <h1 class="hero-title">Discover Punjab<br>With Elegance.</h1>
            <p class="hero-subtitle">Experience first-class car rentals, guided heritage tours, and seamless outstation travel. Impeccable vehicles, verified drivers, and transparent pricing.</p>
            <div class="d-flex flex-wrap gap-4 mt-4">
              <div class="d-flex align-items-center gap-2">
                <div class="bg-success rounded-circle p-1"><i class="fas fa-check text-white small"></i></div>
                <span class="fw-medium">24/7 Support</span>
              </div>
              <div class="d-flex align-items-center gap-2">
                <div class="bg-success rounded-circle p-1"><i class="fas fa-check text-white small"></i></div>
                <span class="fw-medium">No Hidden Fees</span>
              </div>
              <div class="d-flex align-items-center gap-2">
                <div class="bg-success rounded-circle p-1"><i class="fas fa-check text-white small"></i></div>
                <span class="fw-medium">Top-Rated Fleet</span>
              </div>
            </div>
          </div>
        </div>
        
        <div class="col-lg-5 wow fadeInRight" data-wow-delay="0.2s">
          <div class="booking-widget">
            <h3 class="mb-2 text-white">Instant Booking</h3>
            <p class="mb-4 text-white-50">Skip the hassle. Secure your ride instantly.</p>
            
            <a href="tel:9878120686" class="widget-btn btn-call mb-3">
              <i class="fas fa-phone-alt fa-lg"></i>
              <span class="fs-5">Call +91 9878120686</span>
            </a>
            
            <a href="https://wa.me/919878120686?text=Hi%2C%20I%20want%20to%20book%20a%20taxi" target="_blank" class="widget-btn btn-wa">
              <i class="fab fa-whatsapp fa-lg"></i>
              <span class="fs-5">WhatsApp Us</span>
            </a>
            
            <p class="text-center mt-4 mb-0 text-white-50 small">
              <i class="fas fa-bolt text-warning me-1"></i> Responses typically under 2 mins
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Modern Bento Services -->
  <section class="bento-section bg-white">
    <div class="container">
      <div class="text-center mb-5 md-mb-0 pb-3">
        <h2 class="display-5 fw-bold text-dark mb-3">Exceptional Services</h2>
        <p class="text-muted fs-5">Tailored travel solutions for every journey type.</p>
      </div>
      
      <div class="bento-grid">
        <!-- Outstation -->
        <a href="outstation-tours.html" class="bento-item bento-large group">
          <div>
            <div class="bento-icon bg-primary bg-opacity-10 text-primary">
              <i class="fas fa-route"></i>
            </div>
            <h3>Outstation Journeys</h3>
            <p class="mb-4">Travel to Dalhousie, Manali, Shimla, Katra, or Delhi in complete comfort. Our hill-station experts ensure a safe, scenic, and smooth ride across North India.</p>
            <div class="row g-3 mt-4 text-muted">
              <div class="col-6"><i class="fas fa-check-circle text-primary me-2"></i>One-way Drops</div>
              <div class="col-6"><i class="fas fa-check-circle text-primary me-2"></i>Round Trips</div>
              <div class="col-6"><i class="fas fa-check-circle text-primary me-2"></i>Multi-day Tours</div>
              <div class="col-6"><i class="fas fa-check-circle text-primary me-2"></i>Hill Experts</div>
            </div>
          </div>
          <div class="mt-4 text-primary bento-link">Explore Outstation Routes <i class="fas fa-arrow-right ms-2"></i></div>
        </a>
        
        <!-- Local -->
        <a href="taxi-services.html" class="bento-item bento-wide">
          <div class="d-flex gap-4 align-items-center h-100">
            <div class="bento-icon bg-secondary bg-opacity-10 text-secondary mb-0 flex-shrink-0" style="width: 80px; height: 80px;">
              <i class="fas fa-city fs-2"></i>
            </div>
            <div>
              <h3>Local City Exploration</h3>
              <p>8Hr/80Km flat packages. Visit Golden Temple, Jallianwala Bagh, and local markets effortlessly.</p>
              <div class="text-secondary bento-link mt-3">View Local Cabs <i class="fas fa-arrow-right ms-2"></i></div>
            </div>
          </div>
        </a>
        
        <!-- Airport -->
        <a href="taxi-services.html" class="bento-item">
          <div>
            <div class="bento-icon bg-warning bg-opacity-10 text-warning">
              <i class="fas fa-plane-arrival"></i>
            </div>
            <h3>Airport Transfer</h3>
            <p>Punctual pick-ups and drops at SGRDJI Airport Amritsar.</p>
          </div>
          <div class="text-warning bento-link mt-2">Book Transfer <i class="fas fa-arrow-right ms-2"></i></div>
        </a>
        
        <!-- Heritage -->
        <a href="amritsar-heritage-tour.html" class="bento-item">
          <div>
            <div class="bento-icon bg-success bg-opacity-10 text-success">
              <i class="fas fa-gopuram"></i>
            </div>
            <h3>Heritage Tours</h3>
            <p>Guided spiritual and historical sightseeing across the city.</p>
          </div>
          <div class="text-success bento-link mt-2">View Tours <i class="fas fa-arrow-right ms-2"></i></div>
        </a>
      </div>
    </div>
  </section>

  <!-- Modern Fleet Integration -->
  <div class="container">
    <section class="fleet-section">
      <div class="container px-4 px-md-5">
        <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-end mb-5">
          <div class="mb-4 mb-md-0">
            <h2 class="display-6 fw-bold text-dark mb-2">Our Premium Fleet</h2>
            <p class="text-muted fs-5 mb-0">Immaculate vehicles for every group size.</p>
          </div>
          <a href="carrental.html" class="btn btn-primary rounded-pill px-4 py-2 fw-medium shadow-sm">View Complete Fleet</a>
        </div>
        
        <div class="row g-4">
          <div class="col-md-6 col-lg-3">
            <div class="fleet-card h-100">
              <div class="fleet-img-wrap">
                <img src="img/sadan.jpg" alt="Sedan">
              </div>
              <h4 class="fw-bold mb-1 fs-5">Sedan Class</h4>
              <p class="text-muted small mb-3">Dzire, Etios • 4 Seats • AC</p>
              <div class="d-flex justify-content-between align-items-center pt-2 border-top">
                <span class="fs-6 fw-bold text-primary">?10/km</span>
                <a href="tel:9878120686" class="btn btn-sm btn-outline-primary rounded-pill px-3">Book</a>
              </div>
            </div>
          </div>
          
          <div class="col-md-6 col-lg-3">
            <div class="fleet-card h-100">
              <div class="fleet-img-wrap">
                <img src="img/ertiga.jpg" alt="SUV">
              </div>
              <h4 class="fw-bold mb-1 fs-5">SUV Compact</h4>
              <p class="text-muted small mb-3">Ertiga, Carens • 6 Seats • AC</p>
              <div class="d-flex justify-content-between align-items-center pt-2 border-top">
                <span class="fs-6 fw-bold text-primary">?14/km</span>
                <a href="tel:9878120686" class="btn btn-sm btn-outline-primary rounded-pill px-3">Book</a>
              </div>
            </div>
          </div>
          
          <div class="col-md-6 col-lg-3">
            <div class="fleet-card h-100">
              <div class="fleet-img-wrap">
                <img src="img/inova.jpeg" alt="Innova">
              </div>
              <h4 class="fw-bold mb-1 fs-5">Premium SUV</h4>
              <p class="text-muted small mb-3">Innova Crysta • 7 Seats • AC</p>
              <div class="d-flex justify-content-between align-items-center pt-2 border-top">
                <span class="fs-6 fw-bold text-primary">?18/km</span>
                <a href="tel:9878120686" class="btn btn-sm btn-outline-primary rounded-pill px-3">Book</a>
              </div>
            </div>
          </div>
          
          <div class="col-md-6 col-lg-3">
            <div class="fleet-card h-100">
              <div class="fleet-img-wrap">
                <img src="img/maharaja.jpg" alt="Tempo">
              </div>
              <h4 class="fw-bold mb-1 fs-5">Luxury Tempo</h4>
              <p class="text-muted small mb-3">Maharaja • 12-17 Seats</p>
              <div class="d-flex justify-content-between align-items-center pt-2 border-top">
                <span class="fs-6 fw-bold text-primary">?22/km</span>
                <a href="tel:9878120686" class="btn btn-sm btn-outline-primary rounded-pill px-3">Book</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
"""

out = head + body_content + tours + footer
open('c:/data/newc/about/index3.html', 'w', encoding='utf-8').write(out)
print("Complete!")
