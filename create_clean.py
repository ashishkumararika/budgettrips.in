# -*- coding: utf-8 -*-
import re
import codecs

def read_html(path):
    with codecs.open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    # Fix the common ? / strange character encoding issues from pasting from word
    content = content.replace('', '')
    content = content.replace('â€¢', '•')
    content = content.replace('â€“', '-')
    content = content.replace('â€”', '—')
    content = content.replace('â€™', "'")
    content = content.replace('â€œ', '"')
    content = content.replace('â€', '"')
    content = content.replace('?', '')  # Clear stray question marks if they were replacement chars
    return content

html = read_html('c:/data/newc/about/index2.html')

# We'll extract only HEAD and create a clean modern layout.
head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', html, re.DOTALL)
head = head_match.group(1) if head_match else '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Ashoka Travels</title></head>'

new_css = """
  <!-- NEW AGE CSS -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  
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
      overflow-x: hidden;
    }
    h1, h2, h3, h4, h5, h6 {
      font-family: 'Playfair Display', serif;
    }
    a { text-decoration: none; }
    
    /* Top Bar */
    .top-bar-modern {
      background: var(--primary);
      color: #cbd5e1;
      font-size: 0.85rem;
      padding: 8px 0;
      letter-spacing: 0.5px;
    }
    .top-bar-modern a { color: #f8fafc; transition: 0.3s; }
    .top-bar-modern a:hover { color: var(--secondary); }

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
      padding: 1rem 0;
    }
    .navbar-brand h1 {
      font-family: 'Playfair Display', serif;
      font-weight: 800;
      margin: 0;
      font-size: 1.8rem;
      color: var(--primary);
    }
    .new-nav .nav-link {
      font-weight: 500;
      color: var(--text-main) !important;
      padding: 0.5rem 1.25rem !important;
      font-size: 0.95rem;
      position: relative;
    }
    .new-nav .nav-link::after {
      content: '';
      position: absolute;
      bottom: 0px; left: 1.25rem; right: 1.25rem;
      height: 2px;
      background: var(--secondary);
      transform: scaleX(0);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .new-nav .nav-link:hover::after { transform: scaleX(1); }
    .new-nav .nav-link:hover { color: var(--secondary) !important; }

    /* Cinematic Hero */
    .new-hero {
      position: relative;
      height: 90vh;
      min-height: 700px;
      background: url('img/wide%20golden%20temple%20view.jpg') center/cover no-repeat;
      display: flex;
      align-items: center;
      padding-top: 40px;
      border-radius: 0 0 50px 50px;
      overflow: hidden;
    }
    .new-hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, rgba(15,23,42,0.95) 0%, rgba(15,23,42,0.6) 100%);
    }
    .hero-content { position: relative; z-index: 2; color: white; }
    .hero-title {
      font-size: 4.5rem;
      line-height: 1.1;
      font-weight: 800;
      margin-bottom: 1.5rem;
      background: linear-gradient(to right, #ffffff, #94a3b8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-subtitle { font-size: 1.25rem; font-weight: 400; opacity: 0.9; margin-bottom: 2.5rem; max-width: 600px; line-height: 1.6; }
    
    /* Widget */
    .booking-widget {
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(24px);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      box-shadow: var(--shadow-glass);
      transform: translateY(20px);
      animation: floatUp 1s ease forwards;
    }
    @keyframes floatUp { to { transform: translateY(0); } }
    .widget-btn {
      width: 100%; padding: 1rem; border-radius: 12px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 10px; transition: all 0.3s;
    }
    .btn-call { background: var(--secondary); color: white; border: none; }
    .btn-call:hover { background: #2563eb; color: white; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(59,130,246,0.3); }
    .btn-wa { background: #25d366; color: white; border: none; }
    .btn-wa:hover { background: #1ebd57; color: white; transform: translateY(-2px); box-shadow: 0 10px 20px rgba(37,211,102,0.3); }

    /* Bento Grid Services */
    .bento-section { padding: 6rem 0; background: #fff; }
    .bento-grid { display: grid; grid-template-columns: repeat(4, 1fr); grid-auto-rows: 250px; gap: 1.5rem; }
    .bento-item {
      background: white; border-radius: var(--radius-lg); padding: 2.5rem; position: relative; overflow: hidden;
      box-shadow: var(--shadow-soft); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); display: flex; flex-direction: column; justify-content: space-between;
      border: 1px solid rgba(0,0,0,0.02);
    }
    .bento-item:hover { transform: translateY(-8px); box-shadow: 0 30px 60px -12px rgba(0,0,0,0.12); border-color: rgba(59, 130, 246, 0.1); }
    .bento-large { grid-column: span 2; grid-row: span 2; background: linear-gradient(135deg, #ffffff, #f8fafc); }
    .bento-wide { grid-column: span 2; grid-row: span 1; }
    .bento-icon { width: 64px; height: 64px; border-radius: 18px; display: flex; align-items: center; justify-content: center; font-size: 28px; margin-bottom: 2rem; transition: transform 0.3s; }
    .bento-item:hover .bento-icon { transform: scale(1.1); }
    .bento-item h3 { font-size: 1.5rem; font-family: 'Inter', sans-serif; font-weight: 700; color: var(--primary); margin-bottom: 0.75rem; }
    .bento-item p { color: var(--text-muted); font-size: 0.95rem; margin: 0; line-height: 1.6; }
    
    /* Tour Cards - Premium */
    .tour-section { padding: 6rem 0; background: var(--bg-light); border-radius: 40px; margin: 3rem 0; }
    .grid-tours { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
    .premium-tour-card {
      background: #fff; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-soft); border: 1px solid rgba(0,0,0,0.03); transition: all 0.4s ease;
      display: flex; flex-direction: column; height: 100%;
    }
    .premium-tour-card:hover { transform: translateY(-10px); box-shadow: 0 30px 50px rgba(0,0,0,0.1); }
    .tour-img-wrapper { position: relative; height: 220px; overflow: hidden; }
    .tour-img-wrapper img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }
    .premium-tour-card:hover .tour-img-wrapper img { transform: scale(1.08); }
    .tour-badge { position: absolute; top: 1rem; left: 1rem; background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); padding: 0.4rem 1rem; border-radius: 30px; font-weight: 600; font-size: 0.8rem; color: var(--primary); z-index: 10;}
    .tour-content { padding: 2rem; flex-grow: 1; display: flex; flex-direction: column; }
    .tour-title { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.4rem; color: var(--primary); margin-bottom: 1rem; }
    .tour-desc { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; flex-grow: 1; line-height: 1.5; }
    .tour-meta { display: flex; justify-content: space-between; align-items: center; padding-bottom: 1.5rem; border-bottom: 1px solid #f1f5f9; margin-bottom: 1.5rem; }
    .tour-meta span { color: var(--primary); font-weight: 600; font-size: 0.9rem; display: flex; align-items: center; gap: 0.5rem; }
    
    /* Modern Footer */
    .modern-footer { background: var(--primary); color: #94a3b8; padding: 5rem 0 2rem; margin-top: 4rem; border-radius: 50px 50px 0 0; }
    .modern-footer h4 { color: #fff; font-family: 'Inter', sans-serif; font-weight: 600; margin-bottom: 1.5rem; font-size: 1.2rem; }
    .modern-footer p { line-height: 1.7; }
    .footer-link { color: #94a3b8; display: block; margin-bottom: 0.75rem; transition: all 0.3s; }
    .footer-link:hover { color: var(--secondary); transform: translateX(5px); }
    .social-icon { width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,0.1); display: inline-flex; align-items: center; justify-content: center; color: #fff; margin-right: 0.5rem; transition: all 0.3s; }
    .social-icon:hover { background: var(--secondary); transform: translateY(-3px); }

    @media (max-width: 991px) {
      .hero-title { font-size: 3rem; }
      .bento-grid { grid-template-columns: repeat(2, 1fr); auto-rows: minmax(250px, auto); }
      .bento-large { grid-column: span 2; grid-row: span 1; }
    }
    @media (max-width: 768px) {
      .hero-title { font-size: 2.2rem; }
      .bento-grid { grid-template-columns: 1fr; }
      .bento-large, .bento-wide { grid-column: span 1; }
      .new-hero { padding-top: 80px; height: auto; padding-bottom: 60px; min-height: auto; }
      .navbar-collapse { background: var(--surface); padding: 1rem; border-radius: 1rem; margin-top: 1rem; box-shadow: var(--shadow-glass); }
    }
  </style>
</head>
"""

head = re.sub(r'<link href="css/bootstrap.*?\.css" rel="stylesheet">', '', head)
head = re.sub(r'<link href="css/style\.css".*?>', '', head)
head = head.replace('</head>', new_css)

modern_body = """
<body>

  <!-- Minimal Top Bar -->
  <div class="top-bar-modern d-none d-lg-block">
    <div class="container d-flex justify-content-between align-items-center">
      <div class="d-flex gap-4">
        <span><i class="fas fa-map-marker-alt text-warning me-2"></i> Amritsar, Punjab</span>
        <a href="mailto:info@budgettrips.in"><i class="fas fa-envelope text-warning me-2"></i> info@budgettrips.in</a>
      </div>
      <div class="d-flex gap-3">
        <a href="https://wa.me/919878120686"><i class="fab fa-whatsapp text-success me-1"></i> WhatsApp: 9878120686</a>
        <span>|</span>
        <a href="tel:9878120686"><i class="fas fa-phone-alt text-warning me-1"></i> Call: 9878120686</a>
      </div>
    </div>
  </div>

  <!-- Elegant Navbar -->
  <nav class="navbar navbar-expand-lg new-nav">
    <div class="container">
      <a class="navbar-brand d-flex align-items-center" href="index.html">
        <i class="fas fa-taxi text-warning fs-2 me-3"></i>
        <h1>Ashoka <span class="text-secondary" style="font-family: 'Inter', sans-serif; font-weight: 500; font-size: 1.2rem;">Travels</span></h1>
      </a>
      <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mx-auto mb-2 mb-lg-0">
          <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
          <li class="nav-item"><a class="nav-link" href="taxi-services.html">Services</a></li>
          <li class="nav-item"><a class="nav-link" href="carrental.html">Our Fleet</a></li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">
              Tours
            </a>
            <ul class="dropdown-menu border-0 shadow-sm" style="border-radius: 12px; overflow: hidden;">
              <li><a class="dropdown-item py-2" href="amritsar-heritage-tour.html">Amritsar Local</a></li>
              <li><a class="dropdown-item py-2" href="outstation-tours.html">Outstation Packages</a></li>
              <li><a class="dropdown-item py-2" href="golden-triangle-india.html">Golden Triangle</a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
        </ul>
        <a href="tel:9878120686" class="btn btn-primary rounded-pill px-4 fw-medium shadow-sm">
          Book Now
        </a>
      </div>
    </div>
  </nav>

  <!-- New Age Cinematic Hero -->
  <section class="new-hero">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-7 mb-5 mb-lg-0">
          <div class="hero-content">
            <span class="badge bg-warning text-dark px-4 py-2 rounded-pill mb-4 fw-bold shadow">
              <i class="fas fa-star text-dark me-2"></i>Amritsar's Premium Transport
            </span>
            <h1 class="hero-title">Discover Punjab<br>With Elegance.</h1>
            <p class="hero-subtitle">Experience first-class car rentals, guided heritage tours, and seamless outstation travel. Impeccable vehicles, verified drivers, and transparent pricing.</p>
            <div class="d-flex flex-wrap gap-4 mt-4">
              <div class="d-flex align-items-center gap-2">
                <div class="bg-success rounded-circle p-1 d-flex align-items-center justify-content-center" style="width: 24px; height: 24px;"><i class="fas fa-check text-white" style="font-size: 10px;"></i></div>
                <span class="fw-medium">24/7 Support</span>
              </div>
              <div class="d-flex align-items-center gap-2">
                <div class="bg-success rounded-circle p-1 d-flex align-items-center justify-content-center" style="width: 24px; height: 24px;"><i class="fas fa-check text-white" style="font-size: 10px;"></i></div>
                <span class="fw-medium">No Hidden Fees</span>
              </div>
              <div class="d-flex align-items-center gap-2">
                <div class="bg-success rounded-circle p-1 d-flex align-items-center justify-content-center" style="width: 24px; height: 24px;"><i class="fas fa-check text-white" style="font-size: 10px;"></i></div>
                <span class="fw-medium">Top-Rated Fleet</span>
              </div>
            </div>
          </div>
        </div>
        
        <div class="col-lg-5">
          <div class="booking-widget">
            <h3 class="mb-2 text-white" style="font-family: 'Inter', sans-serif; font-weight: 700;">Instant Booking</h3>
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
  <section class="bento-section">
    <div class="container">
      <div class="text-center mb-5 md-mb-0 pb-3">
        <h2 class="display-6 fw-bold text-dark mb-3">Exceptional Services</h2>
        <p class="text-muted fs-5">Tailored travel solutions for every journey type.</p>
      </div>
      
      <div class="bento-grid">
        <!-- Outstation -->
        <a href="outstation-tours.html" class="bento-item bento-large">
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
          <div class="mt-4 text-primary fw-bold">Explore Outstation Routes <i class="fas fa-arrow-right ms-2"></i></div>
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
              <div class="text-secondary fw-bold mt-3">View Local Cabs <i class="fas fa-arrow-right ms-2"></i></div>
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
          <div class="text-warning fw-bold mt-2">Book Transfer <i class="fas fa-arrow-right ms-2"></i></div>
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
          <div class="text-success fw-bold mt-2">View Tours <i class="fas fa-arrow-right ms-2"></i></div>
        </a>
      </div>
    </div>
  </section>

  <!-- Complete Redesigned Tour Packages Section -->
  <div class="container">
    <section class="tour-section">
      <div class="container px-4">
        <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-end mb-5">
          <div class="mb-4 mb-md-0">
            <h2 class="display-6 fw-bold text-dark mb-2">Our Premium Tours</h2>
            <p class="text-muted fs-5 mb-0">Handcrafted itineraries for unforgettable memories.</p>
          </div>
          <a href="amritsar-heritage-tour.html" class="btn btn-primary rounded-pill px-4 py-2 fw-medium shadow-sm">View All Packages</a>
        </div>
        
        <div class="grid-tours">
          <!-- Tour 1 -->
          <div class="premium-tour-card">
            <div class="tour-img-wrapper">
              <div class="tour-badge"><i class="fas fa-map-marker-alt text-danger me-1"></i> Local Amritsar</div>
              <img src="img/WhatsApp Image 2024-11-23 at 10.23.01 AM.jpeg" alt="Explore Amritsar">
            </div>
            <div class="tour-content">
              <h3 class="tour-title">Complete Amritsar Heritage</h3>
              <div class="tour-meta">
                <span><i class="far fa-clock"></i> 1 Day</span>
                <span><i class="fas fa-car-side"></i> Sedan / SUV</span>
              </div>
              <p class="tour-desc">Experience the soul of Punjab. Visit the divine Golden Temple, historic Jallianwala Bagh, Durgiana Temple, and witness the electrifying Wagah Border evening ceremony.</p>
              <a href="amritsar-heritage-tour.html" class="btn btn-outline-primary w-100 rounded-pill fw-medium">View Itinerary</a>
            </div>
          </div>
          
          <!-- Tour 2 -->
          <div class="premium-tour-card">
            <div class="tour-img-wrapper">
              <div class="tour-badge"><i class="fas fa-mountain text-success me-1"></i> Himachal</div>
              <img src="img/wide dalhousil.jpg" alt="Dalhousie Tour">
            </div>
            <div class="tour-content">
              <h3 class="tour-title">Dalhousie & Khajjiar Escape</h3>
              <div class="tour-meta">
                <span><i class="far fa-clock"></i> 3 Days / 2 Nights</span>
                <span><i class="fas fa-car-side"></i> Hill Expert Cab</span>
              </div>
              <p class="tour-desc">Escape to the 'Mini Switzerland of India'. Enjoy breathtaking views of the Dhauladhar range, pine traditions, and perfect weather away from the city heat.</p>
              <a href="amritsar-to-dharamshala.html" class="btn btn-outline-primary w-100 rounded-pill fw-medium">View Itinerary</a>
            </div>
          </div>
          
          <!-- Tour 3 -->
          <div class="premium-tour-card">
            <div class="tour-img-wrapper">
              <div class="tour-badge"><i class="fas fa-praying-hands text-warning me-1"></i> Devotional</div>
              <img src="img/devi.jpg" alt="Mata Vaishno Devi">
            </div>
            <div class="tour-content">
              <h3 class="tour-title">Mata Vaishno Devi Yatra</h3>
              <div class="tour-meta">
                <span><i class="far fa-clock"></i> 2 Days</span>
                <span><i class="fas fa-car-side"></i> Katra Drop/Return</span>
              </div>
              <p class="tour-desc">A comfortable and safe journey from Amritsar to Katra. Begin your spiritual pilgrimage with our dedicated travel service, ensuring peace of mind throughout.</p>
              <a href="vashino_devi.html" class="btn btn-outline-primary w-100 rounded-pill fw-medium">View Itinerary</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

  <!-- Modern Footer -->
  <footer class="modern-footer">
    <div class="container">
      <div class="row g-5 mb-5">
        <div class="col-lg-4 col-md-6">
          <a href="index.html" class="d-flex align-items-center mb-4 text-decoration-none">
            <i class="fas fa-taxi text-warning fs-3 me-2"></i>
            <h2 class="mb-0 text-white" style="font-family: 'Playfair Display', serif; font-weight: 800;">Ashoka <span class="text-secondary" style="font-family: 'Inter', sans-serif; font-weight: 500; font-size: 1.2rem;">Travels</span></h2>
          </a>
          <p class="pe-lg-4 mb-4">Amritsar's most trusted travel partner. Providing premium car rentals, outstation trips, and heritage tours with professional drivers and top-class vehicles.</p>
          <div class="d-flex">
            <a href="https://wa.me/919878120686" class="social-icon"><i class="fab fa-whatsapp"></i></a>
            <a href="#" class="social-icon"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social-icon"><i class="fab fa-instagram"></i></a>
          </div>
        </div>
        
        <div class="col-lg-2 col-md-6">
          <h4>Quick Links</h4>
          <a href="about.html" class="footer-link">About Us</a>
          <a href="carrental.html" class="footer-link">Our Fleet</a>
          <a href="taxi-services.html" class="footer-link">Taxi Services</a>
          <a href="outstation-tours.html" class="footer-link">Outstation Cabs</a>
          <a href="contact.html" class="footer-link">Contact Us</a>
        </div>
        
        <div class="col-lg-3 col-md-6">
          <h4>Popular Routes</h4>
          <a href="amritsar-to-dharamshala.html" class="footer-link">Amritsar to Dharamshala</a>
          <a href="amritsar-to-manali.html" class="footer-link">Amritsar to Manali</a>
          <a href="amritsar-to-shimla.html" class="footer-link">Amritsar to Shimla</a>
          <a href="vashino_devi.html" class="footer-link">Amritsar to Katra</a>
          <a href="amritsar-heritage-tour.html" class="footer-link">Local City Tour</a>
        </div>
        
        <div class="col-lg-3 col-md-6">
          <h4>Contact Info</h4>
          <div class="d-flex align-items-center mb-3">
            <i class="fas fa-map-marker-alt text-secondary me-3 fs-5"></i>
            <span>Opp. Railway Station, Amritsar, Punjab</span>
          </div>
          <div class="d-flex align-items-center mb-3">
            <i class="fas fa-phone-alt text-secondary me-3 fs-5"></i>
            <span>+91 98781 20686<br>+91 98781 20686</span>
          </div>
          <div class="d-flex align-items-center">
            <i class="fas fa-envelope text-secondary me-3 fs-5"></i>
            <span>info@budgettrips.in</span>
          </div>
        </div>
      </div>
      
      <div class="border-top border-secondary border-opacity-25 pt-4 text-center">
        <p class="mb-0 small">&copy; 2024 Ashoka Travels Amaritsar. All Rights Reserved. Designed with elegance.</p>
      </div>
    </div>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
"""

final_html = head + modern_body + "\\n</html>"

with codecs.open('c:/data/newc/about/index3.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated completely clean, modern index3.html without special char issues, with redesigned nav, tours and footer.")
