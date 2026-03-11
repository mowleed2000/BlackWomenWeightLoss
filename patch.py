import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Fix the broken pound sign replace
html = html.replace('£', '$')
html = html.replace('', '')

# Add 7th product
if 'Ultimate Value Bundle' not in html:
    product_7_html = '''                <!-- Product 7 -->
                <div class="product-card shadow-lg"
                    style="background: var(--bg-card); border-radius: 8px; overflow: hidden; display: flex; flex-direction: column; grid-column: 1 / -1; border: 2px solid var(--clr-pink);">
                    <div
                        style="height: 200px; background: linear-gradient(135deg, rgba(82,10,147,0.8), rgba(236,72,153,0.8)), url('assets/before2.png'); background-size: cover; background-position: center top; padding: 1.5rem; display: flex; align-items:flex-start;">
                        <span class="badge bg-pink">ULTIMATE VALUE BUNDLE</span>
                    </div>
                    <div
                        style="padding: 2rem; flex-grow: 1; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 2rem;">
                        <div style="flex: 1; min-width: 300px;">
                            <h3 class="mb-1 text-white" style="font-size: 2rem;">The Complete Ecosystem Bundle</h3>
                            <p class="text-muted mb-3" style="font-size: 1.1rem;">Get instant lifetime access to ALL 6 digital products above. The 30-Day Kickstart, Home Workout Guide, Recipe Vault, 21-Day Challenge, Progress Tracker, and Starter Guide.</p>
                        </div>
                        <div style="text-align: right; min-width: 200px;">
                            <p class="text-white font-bold mb-2" style="font-size: 2.5rem;">$60</p>
                            <a href="#" target="_blank" class="btn btn-primary w-100"
                                style="padding: 1rem; font-size: 1.2rem;"><i class="fas fa-unlock"></i> Unlock Everything</a>
                        </div>
                    </div>
                </div>'''
    
    product_6_end_str = '''                            <p class="text-purple font-bold text-lg mb-2">$15</p>
                            <a href="app-starter-guide.html" target="_blank" class="btn btn-outline w-100"
                                style="padding: 0.75rem;"><i class="fas fa-desktop"></i> Open App OS</a>
                        </div>
                    </div>
                </div>'''
                
    if product_6_end_str in html:
        html = html.replace(product_6_end_str, product_6_end_str + '\n\n' + product_7_html)

# Replace IG feed placeholders
ig_html = '''            <div class="ig-feed grid-4">
                <div class="ig-post shadow-sm"
                    style="background-image: url('assets/workout1.png'); background-position: top; background-size: cover;">
                    <div class="ig-overlay"><i class="fab fa-instagram"></i></div>
                </div>
                <div class="ig-post shadow-sm"
                    style="background-image: url('assets/before2.png'); background-position: top; background-size: cover;">
                    <div class="ig-overlay"><i class="fab fa-instagram"></i></div>
                </div>
                <div class="ig-post shadow-sm"
                    style="background-image: url('assets/workout2.png'); background-position: top; background-size: cover;">
                    <div class="ig-overlay"><i class="fab fa-instagram"></i></div>
                </div>
                <div class="ig-post shadow-sm"
                    style="background-image: url('assets/tiana.png'); background-position: top; background-size: cover;">
                    <div class="ig-overlay"><i class="fab fa-instagram"></i></div>
                </div>
            </div>'''
html = re.sub(r'<div class="ig-feed grid-4">.*?</div>\s*</div>\s*</section>', ig_html + '\n        </div>\n    </section>', html, flags=re.DOTALL)

# Add Modals and CSS
modals_html = '''
    <!-- Modals -->
    <style>
        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 9999; justify-content: center; align-items: center; padding: 1rem; }
        .modal-content { background: var(--clr-darker); border-radius: 12px; border-left: 4px solid var(--clr-pink); max-width: 600px; width: 100%; padding: 2.5rem; color: #fff; position: relative; }
        .close-modal { position: absolute; top: 15px; right: 20px; color: #fff; font-size: 1.5rem; cursor: pointer; transition: 0.2s; }
        .close-modal:hover { color: var(--clr-pink); }
    </style>
    
    <div id="modal-faith" class="modal">
        <div class="modal-content">
            <i class="fas fa-times close-modal" onclick="this.closest('.modal').style.display='none'"></i>
            <h2 class="mb-2" style="font-family:'Oswald', sans-serif; font-size: 2rem;">Faith's Transformation</h2>
            <p style="font-size: 1.1rem; color: #fff;"><strong>"BWWL Changed my life by making weight loss inevitable."</strong></p>
            <p class="text-muted mt-2" style="line-height: 1.7;">I was trying a new fad diet every single month. Nothing stuck. Then I joined BWWL and grabbed the Ultimate Bundle. The biggest game changer was the meal planner and the Logbook OS. Having everything connected in one digital space meant I didn't have to guess anymore. I dropped 45lbs, but more importantly, I found the confidence I had lost.</p>
        </div>
    </div>
    
    <div id="modal-tiana" class="modal">
        <div class="modal-content">
            <i class="fas fa-times close-modal" onclick="this.closest('.modal').style.display='none'"></i>
            <h2 class="mb-2" style="font-family:'Oswald', sans-serif; font-size: 2rem;">Tiana's Transformation</h2>
            <p style="font-size: 1.1rem; color: #fff;"><strong>"The trackers kept me accountable when I wanted to quit."</strong></p>
            <p class="text-muted mt-2" style="line-height: 1.7;">The 21-Day Gamified Challenge honestly rewired my brain. Before BWWL, if I had one bad meal, I would give up for a week. The challenges and the Progress Tracker made consistency kind of addictive? I dropped 6 dress sizes and completely reshaped my waist.</p>
        </div>
    </div>
    
    <div id="modal-ariana" class="modal">
        <div class="modal-content">
            <i class="fas fa-times close-modal" onclick="this.closest('.modal').style.display='none'"></i>
            <h2 class="mb-2" style="font-family:'Oswald', sans-serif; font-size: 2rem;">Ariana's Transformation</h2>
            <p style="font-size: 1.1rem; color: #fff;"><strong>"Zero guesswork left."</strong></p>
            <p class="text-muted mt-2" style="line-height: 1.7;">I hated the gym. I felt intimidated and didn't know what machines to use. The BWWL Home Workout Guide let me build my body in my living room. Combined with the 30-Day Kickstart, the fat just started dropping. This ecosystem gave me my life back.</p>
        </div>
    </div>
'''
if '<!-- Modals -->' not in html:
    html = html.replace('</body>', modals_html + '\n</body>')

# Replace Footer IG link
html = html.replace('<a href="#"><i class="fab fa-instagram text-pink"></i> Instagram</a>', '<a href="https://www.instagram.com/blackwomenweightloss/" target="_blank"><i class="fab fa-instagram text-pink"></i> Instagram</a>')

# Insert Image in Get Featured Section
get_featured_info_str = '''                <div class="featured-info">'''
get_featured_replacement = '''                <div class="featured-info">
                    <img src="assets/submit_photo.png" alt="Submit Photo Inspiration" class="w-100 shadow-lg mb-4" style="border-radius:12px; object-fit: cover; max-height: 380px;">'''
if 'assets/submit_photo.png' not in html:
    html = html.replace(get_featured_info_str, get_featured_replacement, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
