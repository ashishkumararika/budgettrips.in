import re
import codecs

def upgrade_nav():
    file_path = r'c:\data\newc\about\index3.html'
    
    with codecs.open(file_path, 'r', 'utf-8') as f:
        content = f.read()

    # Look for the container-fluid nav-bar p-0 and everything inside it until the end of the nav
    nav_pattern = re.compile(
        r'<!-- Sticky Navbar & Hero Start -->\s*<div class="container-fluid nav-bar[^>]*>.*?</nav>\s*</div>', 
        re.DOTALL
    )
    
    # We will also try a broader pattern if the first one fails
    nav_pattern_alt = re.compile(
        r'<nav[^>]*>.*?</nav>', 
        re.DOTALL
    )

    ultra_nav_html = """
<!-- Ultra Modern Floating Navbar Start -->
  <style>
    /* Ultra Modern Glassmorphism Navbar CSS */
    .ultra-nav-wrapper {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 1200px;
        z-index: 9999;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .ultra-nav {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 100px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255,255,255,0.8);
        padding: 10px 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .ultra-brand {
        font-weight: 800;
        font-size: 1.5rem;
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
        gap: 32px;
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
        font-weight: 500;
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
    
    /* Mega Menu */
    .mega-menu {
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%) translateY(15px);
        background: #ffffff;
        border-radius: 20px;
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
        background: #f8fafc;
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
        .ultra-links, .ultra-cta {
            display: none;
        }
        .ultra-mobile-toggle {
            display: block;
        }
        .ultra-nav-wrapper {
            top: 10px;
            width: 95%;
        }
        .ultra-nav {
            padding: 10px 20px;
        }
    }
    /* Simple mobile nav backdrop */
    .mobile-overlay {
        position: fixed;
        inset: 0;
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(10px);
        z-index: 9998;
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
            <a href="service.html" class="mega-item">
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
      </ul>

      <a href="contact.html" class="ultra-cta">Contact Us</a>

      <button class="ultra-mobile-toggle" onclick="document.getElementById('mobile-overlay').classList.toggle('active')">
        <i class="bi bi-list"></i>
      </button>
    </nav>
  </div>

  <div id="mobile-overlay" class="mobile-overlay">
    <button style="position:absolute; top:20px; right:20px; background:none; border:none; font-size:2rem; cursor:pointer;" onclick="document.getElementById('mobile-overlay').classList.remove('active')"><i class="bi bi-x-lg"></i></button>
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="service.html">Services</a>
    <a href="taxi-services.html">Tours</a>
    <a href="contact.html" class="ultra-cta" style="display:inline-block; margin-top:20px;">Contact Us</a>
  </div>
<!-- Ultra Modern Floating Navbar End -->
"""

    if "container-fluid nav-bar" in content:
        new_content = re.sub(
            r'<!-- Sticky Navbar & Hero Start -->\s*<div class="container-fluid nav-bar[^>]*>.*?</nav>\s*</div>', 
            "<!-- Sticky Navbar & Hero Start -->\n" + ultra_nav_html, 
            content, 
            flags=re.DOTALL
        )
        if new_content == content:
            print("Substitution didn't change anything? Falling back to broad <nav> replacement.")
            new_content = re.sub(
                r'<nav\b[^>]*>.*?</nav>',
                ultra_nav_html,
                content,
                count=1,
                flags=re.DOTALL
            )
            
    else:
        new_content = re.sub(
            r'<nav\b[^>]*>.*?</nav>',
            ultra_nav_html,
            content,
            count=1,
            flags=re.DOTALL
        )

    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(new_content)
    
    print("Done applying ultra-modern menu to index3.html.")

if __name__ == '__main__':
    upgrade_nav()
