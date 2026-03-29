import sys
import re

def rewrite_contact(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    start_tag = '<!-- Header Start -->'
    end_tag = '<!-- Contact End -->'
    
    if start_tag not in content or end_tag not in content:
        print("Could not find start/end tags in contact.html")
        return

    new_html = '''<!-- Header Start -->
<style>
/* Luxury Contact Page Styles */
.contact-hero {
    background: linear-gradient(135deg, #050505 0%, #1a1a1a 100%);
    padding: 180px 0 80px 0;
    position: relative;
    overflow: hidden;
    color: #fff;
    border-bottom: 1px solid rgba(212, 175, 55, 0.2);
}
.contact-hero::after {
    content: '';
    position: absolute;
    top: -50%; left: -50%; width: 200%; height: 200%;
    background: radial-gradient(circle at 50% 50%, rgba(212, 175, 55, 0.05) 0%, transparent 40%);
    animation: goldPulse 15s ease-in-out infinite alternate;
    z-index: 0;
}
.hero-content { position: relative; z-index: 2; }
.contact-title {
    font-size: 3.5rem;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 25px;
    background: linear-gradient(45deg, #fff, #a0a0a0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.contact-title span {
    background: linear-gradient(45deg, #f9d423, #d4af37, #ff4e50);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Contact Main Section */
.contact-section {
    background: #000;
    padding: 100px 0;
}
.glass-contact-box {
    background: rgba(20, 20, 20, 0.9);
    border: 1px solid rgba(212, 175, 55, 0.15);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 40px;
    height: 100%;
    transition: transform 0.4s ease, border-color 0.4s ease;
}
.glass-contact-box:hover {
    transform: translateY(-5px);
    border-color: rgba(212, 175, 55, 0.4);
    box-shadow: 0 15px 30px rgba(0,0,0,0.6);
}
.contact-icon-wrapper {
    width: 70px;
    height: 70px;
    background: rgba(212, 175, 55, 0.1);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 25px;
}
.contact-icon-wrapper i {
    font-size: 1.8rem;
    color: #d4af37;
}
.contact-detail-title {
    color: #fff;
    font-size: 1.3rem;
    margin-bottom: 10px;
    font-weight: 700;
}
.contact-detail-text, .contact-detail-text a {
    color: #a0a0a0;
    line-height: 1.7;
    font-size: 1rem;
    text-decoration: none;
    transition: color 0.3s ease;
}
.contact-detail-text a:hover {
    color: #d4af37;
}

/* Luxury Form */
.luxury-form-container {
    background: rgba(10, 10, 10, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 50px;
}
.luxury-form-control {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #fff;
    border-radius: 10px;
    padding: 15px 20px;
    transition: all 0.3s ease;
}
.luxury-form-control:focus {
    background: rgba(255, 255, 255, 0.05);
    border-color: #d4af37;
    box-shadow: 0 0 15px rgba(212, 175, 55, 0.1);
    color: #fff;
}
.luxury-btn {
    background: linear-gradient(45deg, #d4af37, #f9d423);
    color: #000;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 15px 30px;
    border: none;
    border-radius: 10px;
    transition: all 0.3s ease;
    text-transform: uppercase;
}
.luxury-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(212, 175, 55, 0.3);
}

/* Social links */
.social-circle {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.05);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    margin-right: 15px;
    font-size: 1.2rem;
    transition: all 0.3s ease;
}
.social-circle:hover {
    background: #d4af37;
    color: #000;
    transform: translateY(-3px);
}
</style>

<section class="contact-hero text-center">
    <div class="container hero-content">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="luxury-quote-box mb-4" style="display: inline-block; background: rgba(212, 175, 55, 0.05); padding: 10px 25px; border-radius: 50px; border: 1px solid rgba(212, 175, 55, 0.2);">
                    <i class="fa fa-quote-left" style="color: #d4af37; margin-right: 10px;"></i>
                    <span style="font-family: 'Georgia', serif; font-style: italic; color: #d4af37; font-size: 1rem; letter-spacing: 1px;">"Connectivity is the essence of flawless travel."</span>
                </div>
                <h1 class="contact-title wow fadeInUp" data-wow-delay="0.1s">Get in <span>Touch</span></h1>
                <p class="text-white-50 fs-5 wow fadeInUp" data-wow-delay="0.2s">Our concierge team is at your disposal 24/7. Reach out to arrange your bespoke itinerary, request a custom quote, or inquire about our premium fleet.</p>
            </div>
        </div>
    </div>
</section>
<!-- Header End -->

<!-- Contact Start -->
<div class="contact-section">
    <div class="container">
        <div class="row g-5">
            <!-- Contact Details -->
            <div class="col-lg-5 wow fadeInLeft" data-wow-delay="0.1s">
                <div class="glass-contact-box mb-4">
                    <div class="contact-icon-wrapper">
                        <i class="fas fa-map-marked-alt"></i>
                    </div>
                    <h3 class="contact-detail-title">Corporate Office</h3>
                    <p class="contact-detail-text">Shop No.9, First Floor, Ram Talai Chownk, New Golden Avenue, Opp. Hotel Dewdrop Shankh, Amritsar, Punjab 143001</p>
                </div>
                
                <div class="row g-4 mb-4">
                    <div class="col-md-6">
                        <div class="glass-contact-box" style="padding: 30px;">
                            <div class="contact-icon-wrapper" style="width: 50px; height: 50px; margin-bottom: 15px;">
                                <i class="fas fa-phone" style="font-size: 1.2rem;"></i>
                            </div>
                            <h3 class="contact-detail-title" style="font-size: 1.1rem;">Call Us</h3>
                            <p class="contact-detail-text"><a href="tel:+919878120686">+91 9878120686</a></p>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="glass-contact-box" style="padding: 30px;">
                            <div class="contact-icon-wrapper" style="width: 50px; height: 50px; margin-bottom: 15px;">
                                <i class="fas fa-envelope" style="font-size: 1.2rem;"></i>
                            </div>
                            <h3 class="contact-detail-title" style="font-size: 1.1rem;">Email Us</h3>
                            <p class="contact-detail-text"><a href="mailto:info@budgettrips.in">info@budgettrips.in</a></p>
                        </div>
                    </div>
                </div>

                <div class="glass-contact-box">
                    <h3 class="contact-detail-title mb-4">Connect With Us</h3>
                    <a href="https://www.facebook.com/people/Budget-Trips/61577447729088/" class="social-circle" target="_blank"><i class="fab fa-facebook-f"></i></a>
                    <a href="https://www.instagram.com/budgettrips59/" class="social-circle" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="https://www.youtube.com/@Budgettrips_in" class="social-circle" target="_blank"><i class="fab fa-youtube"></i></a>
                </div>
            </div>

            <!-- Form -->
            <div class="col-lg-7 wow fadeInRight" data-wow-delay="0.3s">
                <div class="luxury-form-container">
                    <h3 class="text-white mb-4" style="font-size: 2rem; font-weight: 300;">Send a <span style="color: #d4af37; font-weight: 700;">Message</span></h3>
                    <form action="https://formsubmit.co/info@budgettrips.in" method="POST">
                        <input type="hidden" name="_next" value="https://budgettrips.in/thank-you.html">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="text" name="_honey" style="display:none">

                        <div class="row g-4">
                            <div class="col-md-6">
                                <input type="text" class="form-control luxury-form-control" id="name" name="Name" placeholder="Your Name" required>
                            </div>
                            <div class="col-md-6">
                                <input type="email" class="form-control luxury-form-control" id="email" name="Email" placeholder="Your Email" required>
                            </div>
                            <div class="col-md-6">
                                <input type="tel" class="form-control luxury-form-control" id="phone" name="Phone" placeholder="Phone Number" required>
                            </div>
                            <div class="col-md-6">
                                <input type="text" class="form-control luxury-form-control" id="service" name="Service" placeholder="Service Interested In (e.g. Innova)">
                            </div>
                            <div class="col-12">
                                <textarea class="form-control luxury-form-control" placeholder="Tell us about your travel plans..." id="message" name="Message" style="height: 150px" required></textarea>
                            </div>
                            <div class="col-12">
                                <button type="submit" class="w-100 luxury-btn">Submit Request</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>

        <!-- Luxury Map Interface -->
        <div class="row mt-5 pt-5 wow fadeInUp" data-wow-delay="0.5s">
            <div class="col-12">
                <div style="border: 2px solid rgba(212, 175, 55, 0.2); border-radius: 20px; overflow: hidden; padding: 10px; background: rgba(20,20,20,0.8);">
                    <iframe class="w-100 rounded" 
                    style="height: 450px; filter: grayscale(80%) contrast(1.2) brightness(0.9) invert(10%); opacity: 0.9;"
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3426.082760846671!2d74.8623476756391!3d31.634308044282566!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x391964b9c82a05fd%3A0x770577af2cfb1a77!2sRam%20Talai%20Chowk%2C%20New%20Golden%20Avenue%2C%20Amritsar%2C%20Punjab%20143001!5e0!3m2!1sen!2sin!4v1712728845671!5m2!1sen!2sin"
                    loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- Contact End -->'''
    
    start_index = content.find(start_tag)
    end_index = content.find(end_tag) + len(end_tag)
    
    new_content = content[:start_index] + new_html + content[end_index:]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully overhauled contact.html")

rewrite_contact('contact.html')
