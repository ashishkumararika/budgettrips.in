import re
import codecs

def replace_nav():
    with codecs.open(r'c:\data\newc\about\index3.html', 'r', 'utf-8') as f:
        html = f.read()

    ultra_nav = """<!-- Ultra Modern Floating Navbar Start -->
  <style>
    /* Ultra Modern Glassmorphism Navbar CSS */
    .ultra-nav-wrapper {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 85%;
        max-width: 1100px;
        z-index: 9999;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .ultra-nav {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 100px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255,255,255,0.8);
        padding: 8px 16px 8px 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .ultra-brand {
        font-weight: 800;
        font-size: 1.4rem;
        color: #0f172a;
        text-decoration: none;
        letter-spacing: -0.5px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .ultra-brand i {
        color: #2563eb;
    }
    .ultra-links {
        display: flex;
        gap: 28px;
        align-items: center;
        margin: 0;
        padding: 0;
        list-style: none;
    }
    .ultra-link-item {
        position: relative;
    }
    .ultra-link {
        color: #475569;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.95rem;
        transition: color 0.2s;
        padding: 8px 0;
        display: inline-flex;
        align-items: center;
        gap: 4px;
    }
    .ultra-link:hover, .ultra-link.active {
        color: #0f172a;
    }
    
    .ultra-actions {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .ultra-cta {
        background: #0f172a;
        color: #ffffff !important;
        padding: 10px 24px;
        border-radius: 100px;
        font-weight: 600;
        font-size: 0.95rem;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.2);
    }
    .ultra-cta:hover {
        background: #2563eb;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.3);
    }
    
    .ultra-call-icon {
        width: 42px;
        height: 42px;
        background: #22c55e;
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 14px rgba(34, 197, 94, 0.3);
    }
    .ultra-call-icon:hover {
        background: #16a34a;
        transform: scale(1.05);
    }

    /* Mega Menu */
    .mega-menu {
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%) translateY(15px);
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(16px);
        border-radius: 24px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1), 0 0 0 1px rgba(0,0,0,0.05);
        padding: 24px;
        width: max-content;
        min-width: 400px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        pointer-events: none;
    }
    .ultra-link-item:hover .mega-menu {
        opacity: 1;
        visibility: visible;
        transform: translateX(-50%) translateY(5px);
        pointer-events: auto;
    }
    .mega-item {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        text-decoration: none;
        color: #0f172a;
        padding: 12px;
        border-radius: 12px;
        transition: background 0.2s;
    }
    .mega-item:hover {
        background: #f1f5f9;
    }
    .mega-icon {
        background: #eff6ff;
        color: #2563eb;
        width: 40px;
        height: 40px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        flex-shrink: 0;
    }
    .mega-text h4 {
        margin: 0 0 4px;
        font-size: 0.95rem;
        font-weight: 600;
    }
    .mega-text p {
        margin: 0;
        font-size: 0.8rem;
        color: #64748b;
        line-height: 1.4;
    }

    /* Mobile handling */
    .ultra-mobile-toggle {
        display: none;
        background: none;
        border: none;
        font-size: 1.5rem;
        color: #0f172a;
        cursor: pointer;
    }
    @media (max-width: 991px) {
        .ultra-links, .ultra-actions {
            display: none !important;
        }
        .ultra-mobile-toggle {
            display: block;
        }
        .ultra-nav-wrapper {
            top: 15px;
            width: 92%;
        }
        .ultra-nav {
            padding: 10px 20px;
        }
    }
    /* Simple mobile nav backdrop */
    .mobile-overlay {
        position: fixed;
        inset: 0;
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(10px);
        z-index: 10000;
        display: none;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 24px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .mobile-overlay.active {
        display: flex;
        opacity: 1;
    }
    .mobile-overlay a {
        font-size: 1.5rem;
        font-weight: 600;
        color: #0f172a;
        text-decoration: none;
    }
  </style>

  <div class="ultra-nav-wrapper">
    <nav class="ultra-nav">
      <a href="index.html" class="ultra-brand">
        <i class="bi bi-geo-alt-fill"></i> BudgetTrips
      </a>
      
      <ul class="ultra-links">
        <li class="ultra-link-item"><a href="index.html" class="ultra-link active">Home</a></li>
        <li class="ultra-link-item"><a href="about.html" class="ultra-link">About</a></li>
        
        <!-- Services Dropdown -->
        <li class="ultra-link-item">
          <a href="service.html" class="ultra-link" style="cursor: default;">
            Services <i class="bi bi-chevron-down" style="font-size: 0.7rem; margin-top:2px;"></i>
          </a>
          <div class="mega-menu">
            <a href="taxi-services.html" class="mega-item">
              <div class="mega-icon"><i class="fas fa-taxi"></i></div>
              <div class="mega-text">
                <h4>Taxi Services</h4>
                <p>Premium airport & local cabs</p>
              </div>
            </a>
            <a href="hotel-booking.html" class="mega-item">
              <div class="mega-icon"><i class="fas fa-hotel"></i></div>
              <div class="mega-text">
                <h4>Hotel Booking</h4>
                <p>Best stays at budget prices</p>
              </div>
            </a>
            <a href="bus-tour-booking.html" class="mega-item">
              <div class="mega-icon"><i class="fas fa-bus"></i></div>
              <div class="mega-text">
                <h4>Bus Tours</h4>
                <p>Group travel across Punjab</p>
              </div>
            </a>
            <a href="outstation-tours.html" class="mega-item">
              <div class="mega-icon"><i class="fas fa-route"></i></div>
              <div class="mega-text">
                <h4>Outstation</h4>
                <p>Long distance trips handled</p>
              </div>
            </a>
          </div>
        </li>

        <!-- Tours Dropdown -->
        <li class="ultra-link-item">
          <a href="#" class="ultra-link" style="cursor: default;">
            Tours <i class="bi bi-chevron-down" style="font-size: 0.7rem; margin-top:2px;"></i>
          </a>
          <div class="mega-menu" style="min-width: 500px; grid-template-columns: 1fr 1fr 1fr;">
            <a href="amritsar-to-manali.html" class="mega-item">
              <div class="mega-icon"><i class="fas fa-mountain"></i></div>
              <div class="mega-text"><h4>Manali</h4></div>
            </a>
            <a href="amritsar-to-shimla.html" class="mega-item">
              <div class="mega-icon"><i class="fas fa-snowflake"></i></div>
              <div class="mega-text"><h4>Shimla</h4></div>
            </a>
            <a href="golden-triangle-india.html" class="mega-item">
              <div class="mega-icon"><i class="fas fa-map-marked-alt"></i></div>
              <div class="mega-text"><h4>Golden Triangle</h4></div>
            </a>
            <a href="amritsar-to-dharamshala.html" class="mega-item">
              <div class="mega-icon"><i class="fas fa-vihara"></i></div>
              <div class="mega-text"><h4>Dharamshala</h4></div>
            </a>
            <a href="amritsar-to-mussoorie.html" class="mega-item">
              <div class="mega-icon"><i class="fas fa-tree"></i></div>
              <div class="mega-text"><h4>Mussoorie</h4></div>
            </a>
            <a href="amritsar-to-auli.html" class="mega-item">
              <div class="mega-icon"><i class="fas fa-skiing"></i></div>
              <div class="mega-text"><h4>Auli</h4></div>
            </a>
          </div>
        </li>

        <li class="ultra-link-item"><a href="contact.html" class="ultra-link">Contact</a></li>
      </ul>

      <div class="ultra-actions">
        <a href="tel:9878120686" class="ultra-call-icon" title="Call Now">
            <i class="bi bi-telephone-fill"></i>
        </a>
        <a href="contact.html" class="ultra-cta">Get A Quote</a>
      </div>

      <button class="ultra-mobile-toggle" onclick="document.getElementById('mobile-overlay').classList.toggle('active')">
        <i class="bi bi-list"></i>
      </button>
    </nav>
  </div>

  <div id="mobile-overlay" class="mobile-overlay">
    <button style="position:absolute; top:25px; right:25px; background:none; border:none; font-size:2rem; cursor:pointer;" onclick="document.getElementById('mobile-overlay').classList.remove('active')"><i class="bi bi-x-lg"></i></button>
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="service.html">Services</a>
    <a href="amritsar-to-manali.html">Tours</a>
    <a href="contact.html" class="ultra-cta" style="display:inline-block; margin-top:20px;">Contact Us</a>
  </div>
<!-- Ultra Modern Floating Navbar End -->

  <!-- New Age Cinematic Hero -->"""

    # We will slice out everything between <!-- Sticky Navbar & Hero Start --> and <!-- New Age Cinematic Hero -->
    pattern = re.compile(r'<!-- Sticky Navbar & Hero Start -->.*?<!-- New Age Cinematic Hero -->', re.DOTALL)
    
    if pattern.search(html):
        new_html = pattern.sub(ultra_nav, html)
        with codecs.open(r'c:\data\newc\about\index3.html', 'w', 'utf-8') as f:
            f.write(new_html)
        print("Success! Executed replacement.")
    else:
        print("Failed to find pattern.")

if __name__ == '__main__':
    replace_nav()
