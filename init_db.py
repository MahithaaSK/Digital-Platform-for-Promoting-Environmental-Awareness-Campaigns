from app import app, db
from models import Article, Campaign, User
from werkzeug.security import generate_password_hash

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        users_data = [
            ("Admin", "admin@ecoaware.com", "admin123", "admin", "#2F855A"),
            ("Test User", "user@test.com", "password", "user", "#48BB78"),
            ("Alice Green", "alice@test.com", "password", "user", "#3182CE"),
            ("Bob Earth", "bob@test.com", "password", "user", "#D69E2E"),
            ("Clara Bloom", "clara@test.com", "password", "user", "#805AD5"),
            ("David River", "david@test.com", "password", "user", "#DD6B20"),
            ("Emma Sky", "emma@test.com", "password", "user", "#E53E3E"),
            ("Frank Woods", "frank@test.com", "password", "user", "#2B6CB0"),
            ("Grace Sun", "grace@test.com", "password", "user", "#276749"),
            ("Henry Soil", "henry@test.com", "password", "user", "#744210"),
        ]
        
        created_users = []
        for name, email, pw, role, color in users_data:
            photo = f"https://ui-avatars.com/api/?name={name.replace(' ', '+')}&background={color[1:]}&color=fff&size=128"
            u = User(name=name, email=email, password_hash=generate_password_hash(pw), role=role, profile_photo=photo)
            db.session.add(u)
            created_users.append(u)
        
        db.session.commit()
        
        # Get references by email
        def u(email): return User.query.filter_by(email=email).first()
        
        admin = u("admin@ecoaware.com")
        user1 = u("user@test.com")
        alice = u("alice@test.com")
        bob = u("bob@test.com")
        clara = u("clara@test.com")
        david = u("david@test.com")
        emma = u("emma@test.com")
        frank = u("frank@test.com")
        grace = u("grace@test.com")
        henry = u("henry@test.com")
        
        # Build a rich follow network
        user1.follow(alice); user1.follow(bob); user1.follow(clara); user1.follow(grace)
        alice.follow(user1); alice.follow(emma); alice.follow(david)
        bob.follow(user1); bob.follow(frank); bob.follow(henry)
        clara.follow(alice); clara.follow(grace); clara.follow(emma)
        david.follow(user1); david.follow(bob); david.follow(frank)
        emma.follow(alice); emma.follow(clara); emma.follow(grace)
        frank.follow(bob); frank.follow(david); frank.follow(henry)
        grace.follow(user1); grace.follow(emma); grace.follow(clara)
        henry.follow(frank); henry.follow(david); henry.follow(bob)
        
        db.session.commit()
        
        articles_data = [
            ("The Urgency of Climate Action",
             "Global temperatures are rising at an unprecedented rate. It is crucial to reduce greenhouse gas emissions by transitioning to renewable energy, driving less, and eating more plant-based foods. Every small action contributes to the global effort against catastrophic warming.",
             "Climate Change", admin.id),
            ("How to Start Composting at Home",
             "Composting at home is an easy way to reduce landfill waste. You simply need a bin, some green waste like vegetable peels, and brown waste like dry leaves or cardboard. Within months, you'll have rich organic fertilizer for your garden and reduce your household waste significantly.",
             "Recycling", alice.id),
            ("Solar Power Explained for Beginners",
             "Solar energy is becoming cheaper and more accessible every year. Photovoltaic cells convert sunlight directly into electricity. Installing panels on your roof can drastically reduce your electricity bills and carbon footprint over a 25-year lifespan.",
             "Renewable Energy", bob.id),
            ("Oceans Without Plastic: What You Can Do",
             "Marine life is severely threatened by microplastics and large plastic debris. Turtles and birds often mistake plastic bags for jellyfish. Reducing single-use plastics like straws, bags, and bottles is the first step towards clean oceans.",
             "Pollution Control", clara.id),
            ("Protecting Endangered Species Today",
             "Habitat loss is the main driver of extinction today. Human expansion, deforestation, and agriculture wipe out the homes of countless species. Conservation starts with protecting wilderness areas and supporting sustainable products.",
             "Conservation", emma.id),
            ("The Future of Wind Energy",
             "Wind turbines are scaling up and offshore wind is booming globally. Wind energy provides a clean, infinite source of power that doesn't produce greenhouse gases during operation. Many countries now rely heavily on wind for over 30% of their electricity.",
             "Renewable Energy", bob.id),
            ("Understanding Your Carbon Footprint",
             "Your carbon footprint is the total amount of greenhouse gases generated by your actions. Flying less, using public transport, and buying local goods are the three most effective individual actions you can take to reduce your personal climate impact.",
             "Climate Change", user1.id),
            ("Recycling Myths Debunked",
             "Not everything with a recycling symbol is actually recyclable. The chasing arrows often just indicate the type of plastic. Always check with your local recycling facility to see what they accept to avoid wishcycling.",
             "Recycling", alice.id),
            ("Air Quality in Urban Areas",
             "Vehicle emissions and industrial output cause severe respiratory issues in cities. Planting urban forests, expanding green spaces, and transitioning to electric public transit are proven effective solutions for improving air quality.",
             "Pollution Control", david.id),
            ("The Vital Role of Bees",
             "Pollinators are vital for our food supply and ecosystem health. Without bees, many of the fruits and vegetables we eat simply wouldn't exist. Planting native wildflowers and avoiding pesticides can dramatically support local bee populations.",
             "Conservation", grace.id),
            ("Electric Vehicles: The Road Ahead",
             "Transitioning from internal combustion engines to electric motors is one of the biggest wins in the fight against global warming. When paired with renewable grid energy, the net emission reduction of EVs is over 70% compared to petrol cars.",
             "Climate Change", user1.id),
            ("Water Conservation Starts at Home",
             "Fix leaky faucets, take shorter showers, and water your lawn only during the coolest parts of the day to prevent evaporation. A household can save over 10,000 litres annually through simple behavioural changes.",
             "Conservation", henry.id),
            ("Mangroves: Nature's Coastal Shields",
             "Mangrove forests protect coastlines from storm surges, store more carbon per hectare than rainforests, and serve as nurseries for fish. Restoring mangroves is one of the most cost-effective climate solutions available.",
             "Conservation", grace.id),
            ("Making Sense of Green Energy Labels",
             "When buying energy, look for verified renewable certificates. Greenwashing is rampant in the energy sector. Understanding what RECS, GO certificates and PPAs mean will help you make genuinely green energy choices.",
             "Renewable Energy", frank.id),
            ("Citizen Science for the Environment",
             "Apps like iNaturalist and eBird let everyday citizens contribute critical biodiversity data. Participating in citizen science projects helps researchers track ecosystem changes and direct conservation efforts more effectively.",
             "Conservation", emma.id),
        ]
        
        for title, content, cat, author_id in articles_data:
            a = Article(title=title, content=content, category=cat, author_id=author_id)
            db.session.add(a)
            
        campaigns_data = [
            ("River Cleanup Drive", "Join us to clean the local river banks. We will provide gloves and bags. All waste is responsibly disposed of.", "Pollution Control", "2025-06-15", "Riverfront Park", admin.id),
            ("Tree Planting Marathon", "We aim to plant 1000 trees in one day. Bring a shovel and energy! Saplings and refreshments provided.", "Climate Change", "2025-07-01", "City Outskirts", alice.id),
            ("Solar Panel Workshop", "Learn how to install basic solar setups for small electronics. Great intro to renewable energy for beginners.", "Renewable Energy", "2025-05-20", "Community Centre", bob.id),
            ("E-Waste Collection Drive", "Drop off your old electronics safely. We ensure they are properly recycled and toxic materials are safely handled.", "Recycling", "2025-05-10", "Downtown Square", user1.id),
            ("Wildlife Rescue Training", "Basic training for helping injured urban wildlife until professionals arrive. No experience needed.", "Conservation", "2025-08-12", "Nature Reserve", admin.id),
            ("Zero Plastic Week Challenge", "A challenge to live without single-use plastics for an entire week. Join global participants online.", "Pollution Control", "2025-06-01", "Online / Global", bob.id),
            ("Community Garden Setup", "Help build a shared garden for the neighbourhood to promote local, sustainable produce and community bonds.", "Conservation", "2025-05-25", "Block 42", alice.id),
            ("Wind Farm Educational Tour", "Educational tour of the new offshore wind farm. Great for students, families, and eco-enthusiasts!", "Renewable Energy", "2025-09-10", "Harbor Dock", frank.id),
            ("Compost Bin Distribution", "Giving away free compost bins to residents to encourage home composting and reduce landfill waste.", "Recycling", "2025-07-20", "Town Hall", user1.id),
            ("Climate March 2025", "March together to demand stronger climate policies from local and national government. Make your voice heard!", "Climate Change", "2025-09-22", "City Centre", clara.id),
            ("Mangrove Restoration Day", "Hands-on mangrove planting along the coastal reserve. Contributes directly to carbon sequestration and coastal protection.", "Conservation", "2025-10-05", "Coastal Reserve", grace.id),
            ("Air Quality Monitoring Hackathon", "Build DIY air quality sensors and contribute data to city-wide pollution maps. Tech skills welcome but not required!", "Pollution Control", "2025-08-30", "Innovation Hub", david.id),
        ]
        
        for title, desc, cat, date, loc, author_id in campaigns_data:
            c = Campaign(title=title, description=desc, category=cat, date=date, location=loc, author_id=author_id)
            db.session.add(c)
            
        db.session.commit()
        print("✅ Database seeded: 10 users, 15 articles, 12 campaigns, and follow network created.")

if __name__ == '__main__':
    seed_database()
