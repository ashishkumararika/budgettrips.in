import sys
import re

def add_faq():
    with open('index3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start of the footer
    footer_start = content.find('<!-- Ultra Premium Footer -->')
    if footer_start == -1: 
        print("Couldn't find footer, aborting.")
        return
        
    faq_html = '''
    <!-- Elite FAQ Section -->
    <section class="elite-faq-section py-5 wow fadeInUp" data-wow-delay="0.1s" style="background: linear-gradient(180deg, #f8f9fa 0%, #ffffff 100%);">
      <div class="container">
        <div class="text-center">
          <h6 class="section-title text-center text-primary text-uppercase" style="letter-spacing: 5px;">Common Queries</h6>
          <h2 class="mb-5" style="font-weight: 800; font-size: 2.5rem; text-transform: uppercase; background: linear-gradient(135deg, #2c3e50, #000000); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Frequently Asked <span class="text-primary" style="-webkit-text-fill-color: #FEA116;">Questions</span></h2>
        </div>
        
        <div class="row justify-content-center">
          <div class="col-lg-10">
            <div class="accordion custom-accordion" id="faqAccordion">
              
              <!-- FAQ Item 1 -->
              <div class="accordion-item mb-4" style="border: none; border-radius: 12px; box-shadow: 0 5px 25px rgba(0,0,0,0.06); overflow: hidden;">
                <h2 class="accordion-header" id="headingOne">
                  <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne" style="font-weight: 600; font-size: 1.15rem; padding: 22px 25px; background: white; color: #1a1a1a;">
                    How do I book a premium taxi or outstation tour with Budget Trips?
                  </button>
                </h2>
                <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#faqAccordion">
                  <div class="accordion-body" style="padding: 20px 25px; background: #fafafa; color: #444; line-height: 1.8; font-size: 1.05rem;">
                    You can effortlessly book your journey directly on our website, drop us an email, or contact our 24/7 dedicated travel experts via WhatsApp or phone. We provide instant confirmations and detailed itineraries customized simply for you.
                  </div>
                </div>
              </div>
              
              <!-- FAQ Item 2 -->
              <div class="accordion-item mb-4" style="border: none; border-radius: 12px; box-shadow: 0 5px 25px rgba(0,0,0,0.06); overflow: hidden;">
                <h2 class="accordion-header" id="headingTwo">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo" style="font-weight: 600; font-size: 1.15rem; padding: 22px 25px; background: white; color: #1a1a1a;">
                    What is the average fare for trips like Amritsar to Wagah Border?
                  </button>
                </h2>
                <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#faqAccordion">
                  <div class="accordion-body" style="padding: 20px 25px; background: #fafafa; color: #444; line-height: 1.8; font-size: 1.05rem;">
                    Our premium fares are highly competitive while keeping luxury standards intact. A standard elite sedan (Swift Dzire) to Wagah Border starts around &#8377;800-1200, whereas our Elite SUVs (Innova/Crysta) cost around &#8377;1200-1500 depending on exact timeline and requirements.
                  </div>
                </div>
              </div>
              
              <!-- FAQ Item 3 -->
              <div class="accordion-item mb-4" style="border: none; border-radius: 12px; box-shadow: 0 5px 25px rgba(0,0,0,0.06); overflow: hidden;">
                <h2 class="accordion-header" id="headingThree">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree" style="font-weight: 600; font-size: 1.15rem; padding: 22px 25px; background: white; color: #1a1a1a;">
                    Can I customize my Golden Triangle or Himachal Tour Package?
                  </button>
                </h2>
                <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#faqAccordion">
                  <div class="accordion-body" style="padding: 20px 25px; background: #fafafa; color: #444; line-height: 1.8; font-size: 1.05rem;">
                    Absolutely. Budget Trips specializes in tailor-made itineraries. Whether you need an extended stay in Manali, specific luxury hotel bookings, or an exclusive Maharaja Tempo Traveller for a large group, we will completely craft everything to perfection based on your input.
                  </div>
                </div>
              </div>
              
              <!-- FAQ Item 4 -->
              <div class="accordion-item mb-4" style="border: none; border-radius: 12px; box-shadow: 0 5px 25px rgba(0,0,0,0.06); overflow: hidden;">
                <h2 class="accordion-header" id="headingFour">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour" style="font-weight: 600; font-size: 1.15rem; padding: 22px 25px; background: white; color: #1a1a1a;">
                    Are your drivers experienced with outstation hill routes?
                  </button>
                </h2>
                <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour" data-bs-parent="#faqAccordion">
                  <div class="accordion-body" style="padding: 20px 25px; background: #fafafa; color: #444; line-height: 1.8; font-size: 1.05rem;">
                    Yes, all our chauffeurs go through rigorous training. We deploy specialized Hill Experts for high-altitude destinations like Shimla, Manali, and Dalhousie. They are incredibly well-versed in mountain driving, local terrain, and multiple languages for your safety and ultimate traveling comfort.
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </section>
    '''

    style_html = '''
    <style>
      .custom-accordion .accordion-button:not(.collapsed) {
        background-color: #FEA116;
        color: #fff !important;
        box-shadow: none;
      }
      .custom-accordion .accordion-button:focus {
        box-shadow: none;
        border-color: rgba(0,0,0,0.1);
      }
      .custom-accordion .accordion-button::after {
        filter: brightness(0);
        margin-left: auto;
      }
      .custom-accordion .accordion-button:not(.collapsed)::after {
        filter: brightness(0) invert(1);
      }
    </style>
    '''

    if 'Elite FAQ Section' in content:
        print('FAQ already added!')
        return

    new_content = content[:footer_start] + faq_html + '\n\n' + content[footer_start:]
    
    # inject styles in head before </head>
    head_end = new_content.find('</head>')
    if head_end != -1:
        new_content = new_content[:head_end] + style_html + new_content[head_end:]

    with open('index3.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('FAQ Section added successfully!')

if __name__ == '__main__':
    add_faq()
