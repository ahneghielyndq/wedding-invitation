from flask import Flask, render_template_string
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#MarryCrisGotHerDonDon</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, rgba(232, 238, 243, 0.3) 0%, rgba(240, 244, 248, 0.3) 50%, rgba(229, 235, 240, 0.3) 100%), url('/static/couple.jpg');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            min-height: 100vh;
            color: #333;
            overflow-x: hidden;
        }

        .hero {
            text-align: center;
            padding: 60px 20px;
            background: transparent;
            animation: fadeIn 1.5s ease-in;
        }

        .names {
            font-size: clamp(2.5rem, 8vw, 5rem);
            color: #7d9aad;
            margin-bottom: 20px;
            font-weight: 300;
            letter-spacing: 2px;
            animation: slideDown 1s ease-out;
        }

        .ampersand {
            font-size: clamp(2rem, 6vw, 4rem);
            color: #6b7280;
            font-style: italic;
            margin: 0 15px;
        }

        .tagline {
            font-size: clamp(1rem, 3vw, 1.5rem);
            color: #666;
            font-style: italic;
            margin-bottom: 30px;
            animation: fadeIn 2s ease-in;
        }

        .divider {
            width: 100px;
            height: 2px;
            background: linear-gradient(90deg, transparent, #7d9aad, transparent);
            margin: 30px auto;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }

        .section {
            background: rgba(255, 255, 255, 0.75);
            border-radius: 20px;
            padding: 40px 30px;
            margin: 30px 0;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            animation: slideUp 0.8s ease-out;
            backdrop-filter: blur(10px);
        }

        .section-title {
            font-size: clamp(1.8rem, 4vw, 2.5rem);
            color: #7d9aad;
            text-align: center;
            margin-bottom: 25px;
            font-weight: 400;
        }

        .date-info {
            text-align: center;
            font-size: clamp(1.2rem, 3vw, 1.8rem);
            color: #555;
            line-height: 1.8;
        }

        .date-large {
            font-size: clamp(2rem, 5vw, 3rem);
            color: #7d9aad;
            font-weight: bold;
            display: block;
            margin: 20px 0;
        }

        .location-card {
            background: linear-gradient(135deg, #f0f5f9 0%, #f5f8fa 100%);
            padding: 25px;
            border-radius: 15px;
            margin: 20px 0;
            border-left: 4px solid #7d9aad;
        }

        .location-title {
            font-size: 1.3rem;
            color: #7d9aad;
            margin-bottom: 10px;
            font-weight: 600;
        }

        .location-details {
            color: #666;
            line-height: 1.8;
            font-size: 1.1rem;
        }

        .schedule {
            display: grid;
            gap: 20px;
            margin-top: 20px;
        }

        .schedule-item {
            background: linear-gradient(135deg, #fff 0%, #fafafa 100%);
            padding: 20px;
            border-radius: 12px;
            border-left: 3px solid #6b7280;
            transition: transform 0.3s ease;
        }

        .schedule-item:hover {
            transform: translateX(5px);
        }

        .schedule-time {
            font-weight: bold;
            color: #7d9aad;
            font-size: 1.2rem;
        }

        .schedule-event {
            color: #555;
            margin-top: 5px;
            font-size: 1.1rem;
        }

        .rsvp-button {
            display: inline-block;
            background: linear-gradient(135deg, #7d9aad 0%, #96afc0 100%);
            color: white;
            padding: 18px 50px;
            border-radius: 50px;
            text-decoration: none;
            font-size: 1.3rem;
            margin: 20px 0;
            transition: all 0.3s ease;
            box-shadow: 0 5px 20px rgba(125, 154, 173, 0.3);
            border: none;
            cursor: pointer;
        }

        .rsvp-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 30px rgba(125, 154, 173, 0.4);
        }

        .dress-code {
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #f0f4f8 0%, #f5f7fa 100%);
            border-radius: 15px;
            margin: 20px 0;
        }

        .dress-code-title {
            color: #6b7280;
            font-size: 1.3rem;
            margin-bottom: 10px;
            font-weight: 600;
        }

        .dress-code-text {
            color: #666;
            font-size: 1.1rem;
        }

        .footer {
            text-align: center;
            padding: 40px 20px;
            color: #888;
            font-style: italic;
        }

        .hearts {
            font-size: 1.5rem;
            color: #9db4c4;
            margin: 20px 0;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        @keyframes slideDown {
            from {
                transform: translateY(-30px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }

        @keyframes slideUp {
            from {
                transform: translateY(30px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }

        @media (max-width: 600px) {
            .section {
                padding: 30px 20px;
                margin: 20px 10px;
            }
            
            .hero {
                padding: 40px 15px;
            }
        }
    </style>
</head>
<body>
    <div class="hero">
        <div class="names">
            Maricris <span class="ampersand">&</span> Dondon
        </div>
        <div class="tagline">Together with our families, We invite you to celebrate our wedding</div>
        <div style="font-size: 1.2rem; color: #7d9aad; margin-bottom: 20px;">#MarryCrisGotHerDonDon.</div>
        <div class="hearts">♥ ♥ ♥</div>
    </div>

    <div class="container">
        <div class="section">
            <h2 class="section-title">Save The Date</h2>
            <div class="divider"></div>
            <div class="date-info">
                <span class="date-large">January 24, 2026</span>
                Saturday at 9:30 AM
            </div>
        </div>

        <div class="section">
            <h2 class="section-title">Ceremony & Reception</h2>
            <div class="divider"></div>
            
            <div class="location-card" style="text-align: center; border-left: none;">
                <div class="location-title">CEREMONY</div>
                <div class="location-details">
                    Our Lady of the Rosary Parish<br>
                    Rosario, Batangas<br>
                </div>
            </div>

            <div class="location-card" style="text-align: center; border-left: none;">
                <div class="location-title" style="color: #7d9aad;">RECEPTION</div>
                <div class="location-details">
                    Brgy. Mavalor<br>
                    Rosario, Batangas<br>
                </div>
            </div>
        </div>

        <div class="section">
            <h2 class="section-title">De Quina - Dimaano Nuptials</h2>
            <div class="divider"></div>
            
            <div style="text-align: center; margin: 30px 0;">
                <h3 style="color: #7d9aad; font-size: 1.3rem; margin-bottom: 15px; font-weight: 600;">Groom</h3>
                <p style="color: #555; font-size: 1.1rem; margin-bottom: 5px;">Dondon De Quina</p>
                
                <h3 style="color: #7d9aad; font-size: 1.3rem; margin-top: 20px; margin-bottom: 15px; font-weight: 600;">Bride</h3>
                <p style="color: #555; font-size: 1.1rem; margin-bottom: 5px;">Maricris Dimaano</p>
                
                <h3 style="color: #7d9aad; font-size: 1.3rem; margin-top: 20px; margin-bottom: 15px; font-weight: 600;">Groom's Parents</h3>
                <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mr. Lorenzo Lasat De Quina</p>
                <p style="color: #555; font-size: 1.1rem; margin-bottom: 5px;">Mrs. Pelilia Carrido De Quina</p>
                
                <h3 style="color: #7d9aad; font-size: 1.3rem; margin-top: 20px; margin-bottom: 15px; font-weight: 600;">Bride's Parents</h3>
                <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mr. Tito Illagan Dimaano</p>
                <p style="color: #555; font-size: 1.1rem; margin-bottom: 5px;">Mrs. Antipas Balbaira Dimaano</p>
                
                <h3 style="color: #7d9aad; font-size: 1.3rem; margin-top: 20px; margin-bottom: 15px; font-weight: 600;">Principal Sponsors</h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px;">
                    <div>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mr. Ben Ilagan</p>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mr. Christian Raza</p>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mr. Fred Capili</p>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mr. Leonardo Briguela</p>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mr. Sixto Puetes</p>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mr. Victorino Perez</p>
                        <p style="color: #555; font-size: 1.1rem;">Mr. Christian Pasia</p>
                    </div>
                    <div>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mrs. Marilyn Ilagan</p>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mrs. Nora Raza</p>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mrs. Liza Capili</p>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mrs. Neneth Briguela</p>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mrs. Buena Inocentess</p>
                        <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Mrs. Estela Perez</p>
                        <p style="color: #555; font-size: 1.1rem;">Mrs. Editha Pasia</p>
                    </div>
                </div>
                
                <h3 style="color: #7d9aad; font-size: 1.3rem; margin-top: 20px; margin-bottom: 15px; font-weight: 600;">Best Man</h3>
                <p style="color: #555; font-size: 1.1rem; margin-bottom: 20px;">Darwin De Quina</p>
                
                <h3 style="color: #7d9aad; font-size: 1.3rem; margin-bottom: 15px; font-weight: 600;">Maid of Honor</h3>
                <p style="color: #555; font-size: 1.1rem; margin-bottom: 30px;">Analyn Dimaano</p>
                
                <h3 style="color: #7d9aad; font-size: 1.3rem; margin-bottom: 15px; font-weight: 600;">Secondary Sponsors</h3>
                
                <div style="margin-bottom: 25px;">
                    <p style="color: #7d9aad; font-style: italic; font-size: 1.1rem; margin-bottom: 5px;">Candle - to light our path</p>
                    <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">James Carlo Dimaano</p>
                    <p style="color: #555; font-size: 1.1rem;">Angel Grace De Quina</p>
                </div>
                
                <div style="margin-bottom: 25px;">
                    <p style="color: #7d9aad; font-style: italic; font-size: 1.1rem; margin-bottom: 5px;">Veil - to cloth us as one</p>
                    <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Angelo De Quina</p>
                    <p style="color: #555; font-size: 1.1rem;">Alhea Marie Puetes</p>
                </div>
                
                <div style="margin-bottom: 25px;">
                    <p style="color: #7d9aad; font-style: italic; font-size: 1.1rem; margin-bottom: 5px;">Cord - to bind us together</p>
                    <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Kim Jayvee Lacerna</p>
                    <p style="color: #555; font-size: 1.1rem;">Shaina Krischel Puetes</p>
                </div>
                
                <h3 style="color: #7d9aad; font-size: 1.3rem; margin-top: 20px; margin-bottom: 15px; font-weight: 600;">To guide us on our way</h3>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 25px;">
                    <div>
                        <p style="color: #7d9aad; font-style: italic; font-size: 1.1rem; margin-bottom: 8px;">Groomsmen</p>
                        <p style="color: #555; font-size: 1.1rem;">Jhon Aaron Lacerna</p>
                    </div>
                    <div>
                        <p style="color: #7d9aad; font-style: italic; font-size: 1.1rem; margin-bottom: 8px;">Bridesmaid</p>
                        <p style="color: #555; font-size: 1.1rem;">Ahngelie De Quina</p>
                    </div>
                </div>
                
                <div style="margin-bottom: 25px;">
                    <p style="color: #7d9aad; font-style: italic; font-size: 1.1rem; margin-bottom: 5px;">Bible Bearer - to carry our symbol of faith</p>
                    <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Macrenzoel Abraham Medrano</p>
                    <p style="color: #555; font-size: 1.1rem;">Charles Kiervin Dimaano</p>
                </div>
                
                <div style="margin-bottom: 25px;">
                    <p style="color: #7d9aad; font-style: italic; font-size: 1.1rem; margin-bottom: 5px;">Ring Bearer - to carry our symbol of love</p>
                    <p style="color: #555; font-size: 1.1rem;">Cyron Dimaano</p>
                </div>
                
                <div style="margin-bottom: 25px;">
                    <p style="color: #7d9aad; font-style: italic; font-size: 1.1rem; margin-bottom: 8px;">Flower Girls - to shower our path with flowers</p>
                    <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Agatha Arellano</p>
                    <p style="color: #555; font-size: 1.1rem; margin-bottom: 3px;">Alexa Dimaano</p>
                    <p style="color: #555; font-size: 1.1rem;">Messhly Sabit</p>
                </div>
                
                <div>
                    <p style="color: #7d9aad; font-style: italic; font-size: 1.1rem; margin-bottom: 5px;">Coin Bearer - to carry our symbol of treasure</p>
                    <p style="color: #555; font-size: 1.1rem;">Cyron Dimaano</p>
                </div>
            </div>
        </div>

        <div class="footer">
            <div class="hearts">♥</div>
            <p>We can't wait to celebrate with you!</p>
        </div>

    <script>
        function handleRSVP() {
            alert('Thank you for your interest! Please contact us at wedding@example.com to RSVP.');
        }

        const sections = document.querySelectorAll('.section');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, { threshold: 0.1 });

        sections.forEach(section => {
            observer.observe(section);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)