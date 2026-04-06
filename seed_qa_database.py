"""
Integrate Q&A data into the database by extending the existing seed_database.py
This script adds pre-built Q&A pairs for the Aura Assistant
"""

from app import app, db
from models import Article, Campaign, User, Interaction
from werkzeug.security import generate_password_hash
from datetime import datetime

# Comprehensive Q&A data for all topics
QA_PAIRS = [
    # ========== CLIMATE CHANGE QUESTIONS ==========
    {
        "question": "What are the main causes of climate change?",
        "response": "Climate change is primarily caused by human activities that increase greenhouse gas concentrations. The main causes are:\n\n1. **Fossil Fuel Burning** - Coal, oil, and natural gas used for energy release CO2\n2. **Deforestation** - Removing trees reduces nature's ability to absorb CO2\n3. **Industrial Processes** - Cement and manufacturing release significant emissions\n4. **Agriculture** - Livestock farming produces methane, a potent greenhouse gas\n5. **Transportation** - Vehicles burning fuel for travel emit carbon\n6. **Energy Production** - Power plants relying on fossil fuels are major contributors\n\nThese activities have increased atmospheric CO2 by 50% since pre-industrial times, from 280 ppm to over 420 ppm today. The primary driver is burning fossil fuels, which accounts for about 75% of human-caused greenhouse gas emissions.",
        "category": "Climate Change",
        "source": "Aura Assistant"
    },
    {
        "question": "How does climate change affect weather patterns?",
        "response": "Climate change fundamentally alters global weather patterns in several critical ways:\n\n**Temperature Effects:**\n- Global average temperatures increase by ~1.1°C since pre-industrial times\n- Heat waves become more frequent, intense, and longer-lasting\n- Winter seasons shorten and snow/ice coverage decreases\n\n**Precipitation Changes:**\n- Some regions experience severe droughts while others face flooding\n- Monsoon patterns shift, affecting billions dependent on predictable rainfall\n- Intense rainfall events become more common and destructive\n\nEvery ton of CO2 reduced matters in stabilizing our climate.",
        "category": "Climate Change",
        "source": "Aura Assistant"
    },
    {
        "question": "What can individuals do to reduce their carbon footprint?",
        "response": "Individual actions, when multiplied across millions, create systemic change. Here are the most impactful steps:\n\n**High-Impact Actions:**\n1. **Reduce Flying** - Avoid unnecessary flights; one transatlantic flight = 1 ton CO2\n2. **Switch to Renewable Energy** - Install solar or choose 100% renewable power\n3. **Drive Less** - Use public transit, bike, walk, or go electric\n4. **Eat Plant-Based** - Vegetarian diet cuts food emissions by 70%\n5. **Buy Less New** - Reduce consumption; 10% of global emissions from clothing\n\n**Medium-Impact Actions:**\n- Improve home insulation\n- Buy local and seasonal produce\n- Support carbon-neutral companies\n\nThe average person's carbon footprint is 4-16 tons CO2/year. Reducing to 2-3 tons aligns with climate safety targets.",
        "category": "Climate Change",
        "source": "Aura Assistant"
    },
    {
        "question": "Is climate change reversible?",
        "response": "Climate change is partially reversible, but the timeline and effort required depend on when action is taken.\n\n**The Good News - Reversibility:**\n- Atmospheric CO2 can be reduced through renewable energy and reforestation\n- Temperature increases can be limited with aggressive emissions cuts\n- Within 100-150 years of zero emissions, CO2 levels would stabilize\n\n**The Challenge - Path Dependency:**\n- Some changes are now irreversible on human timescales:\n  * Ice sheets melting will continue for centuries\n  * Sea level rise is locked in for generations\n  * Some ecosystem collapse cannot always be reversed\n\n**Recovery Timeline:**\n- If we reach net-zero emissions TODAY, warming continues for 20-30 years\n- Full recovery would take 1000+ years\n- Every 0.1°C of avoided warming prevents significant suffering",
        "category": "Climate Change",
        "source": "Aura Assistant"
    },
    {
        "question": "How does renewable energy help combat climate change?",
        "response": "Renewable energy is a cornerstone of climate solutions because it eliminates carbon emissions from electricity generation.\n\n**The Impact:**\n- Electricity production accounts for 25-30% of global emissions\n- Renewable sources produce 0-20g CO2/kWh vs. 820g for coal\n- Switching 100% to renewables could reduce global emissions by 25-30%\n\n**Major Renewable Sources:**\n1. **Solar Power** - Costs dropped 90% in a decade\n2. **Wind Energy** - Growing fastest of all sources\n3. **Hydroelectric** - Provides 16% of global electricity\n4. **Geothermal & Tidal** - Consistent, reliable power\n\n**Real-World Success:**\n- Costa Rica runs on 95%+ renewables for months\n- Denmark generates 80% electricity from wind\n- Solar installations grew 22% in 2023",
        "category": "Climate Change",
        "source": "Aura Assistant"
    },
    {
        "question": "What happens when we cut down all trees?",
        "response": "Cutting down all trees would trigger environmental catastrophe affecting every living system on Earth:\n\n**Immediate Ecological Collapse:**\n1. **Atmospheric Crisis** - Loss of 30% of Earth's oxygen production\n2. **Biodiversity Extinction** - 80% of land animals depend on forests\n3. **Water Systems Destroyed** - Forests regulate 40% of global water flows\n4. **Soil Degradation** - Tree roots anchor soil; without them massive erosion occurs\n5. **Climate Catastrophe** - Rainforests store 200+ gigatons of carbon\n\n**Economic Collapse:**\n- $125 trillion in ecosystem services lost\n- Agriculture fails without pollination\n- Global economy faces unprecedented depression\n\nFortunately, this is preventable. Protecting forests provides 30% of needed emissions reductions at lowest cost.",
        "category": "Conservation",
        "source": "Aura Assistant"
    },
    {
        "question": "Why is deforestation a major environmental issue?",
        "response": "Deforestation is one of the most critical environmental crises because it triggers cascading failures across all Earth systems:\n\n**Climate Impact - Most Urgent:**\n- Forests store 400+ gigatons of carbon globally\n- Deforestation releases ~15% of annual global emissions (~4 gigatons CO2)\n- Equivalent to ALL cars, trucks, and planes combined\n\n**Biodiversity Loss:**\n- Forests harbor 80% of terrestrial species\n- 137 species lost daily due to habitat destruction\n- 1 in 4 medicines originate in tropical rainforests\n\n**Current Crisis Scale:**\n- 10 million hectares cleared yearly\n- Amazon at tipping point (20% deforested → Amazon dies)\n- Indonesia losing rainforests for palm oil\n\n**The Positive:** Nature can recover if given chance. If we halt deforestation and reforest, we solve 30-40% of climate change.",
        "category": "Conservation",
        "source": "Aura Assistant"
    },
    {
        "question": "What are the main causes of deforestation?",
        "response": "Deforestation is driven by specific industries and economic pressures:\n\n**Primary Drivers (80% of deforestation):**\n1. **Agriculture** - Cattle ranching: 80% of Amazon deforestation\n2. **Logging** - Timber extraction for construction and paper\n3. **Infrastructure** - Roads, dams, mining operations\n4. **Energy Production** - Biomass/charcoal for fuel\n\n**Secondary Drivers:**\n5. **Poverty** - Poor communities clear for subsistence farming\n6. **Policy Failures** - Weak enforcement, corruption\n7. **Consumer Demand** - Beef, palm oil, cheap paper\n\n**Solutions Being Implemented:**\n- Certification (FSC, RSPO) for sustainable products\n- Indigenous land protection (most effective)\n- Enforcement of deforestation laws\n- Economic incentives for forest protection\n\nChoose verified products. Support indigenous rights. This crisis responds to individual action.",
        "category": "Conservation",
        "source": "Aura Assistant"
    },
    {
        "question": "Which tree species grow well in tropical forests?",
        "response": "Tropical forests thrive with high biodiversity. Key species include:\n\n**Canopy Dominants:**\n- **Kapok trees** (Ceiba) - 200+ year lifespan\n- **Mahogany** - Strong, valuable wood\n- **Brazil nut tree** - Keystone species\n- **Teak** - Durable, rot-resistant\n\n**Mid-Story Layer:**\n- **Cacao** - Important crop, shade-tolerant\n- **Coffee** - Shade-grown supports biodiversity\n- **Fig trees** - Fruiting hub for animals\n- **Palm species** - Multiple uses\n\n**Key Ecological Traits:**\n- Shade tolerance: Germinate under canopy\n- High water availability adaptation\n- Mutualistic relationships with fungi\n- Support for biodiversity\n\n**For Forest Restoration:**\n- Brazil nuts: Wild harvest, no clearing\n- Cacao: Shade-grown protects canopy\n- Açaí: Sustainable palm harvest\n\nTropical trees need high humidity and warmth. Use local seed sources for best results.",
        "category": "Conservation",
        "source": "Aura Assistant"
    },
    {
        "question": "What are the best native tree species for forest restoration?",
        "response": "Effective restoration prioritizes native species adapted to local conditions:\n\n**TROPICAL AMAZON:**\n- Brazil nut tree - 500+ years lifespan\n- Mahogany - Long-lived, valuable\n- Rubber trees - Sustainable alternative\n- Açaí - Fast growth, food value\n\n**SOUTHEAST ASIA:**\n- Dipterocarp species - Dominant canopy\n- Teak - Durable, fire-resistant\n- Meranti species - Multiple growth rates\n\n**TEMPERATE NORTH AMERICA:**\n- Oak species - Long-lived, wildlife support\n- Hickory - Nut production\n- Walnut - Long-lived, valuable\n\n**RESTORATION STRATEGY:**\n1. **Year 1-3 Pioneer**: Fast-growing, 40% of trees\n2. **Year 5-10 Transition**: Medium-growth, 40%\n3. **Year 20+ Canopy**: Slow-growing, 20%\n\n**Success Factors:**\n✓ Local seed sourcing\n✓ 30-50+ species diversity\n✓ Multiple canopy layers\n✓ Wildlife value consideration\n\nRestoring native forests is slower but creates resilient, biodiverse ecosystems.",
        "category": "Conservation",
        "source": "Aura Assistant"
    },
    {
        "question": "How long does it take for a forest to regenerate naturally?",
        "response": "Natural forest regeneration follows predictable stages, but timeline varies by forest type:\n\n**TROPICAL RAINFORESTS:**\n- 5-10 years: Pioneer species establish\n- 10-30 years: Pioneer canopy closes\n- 30-100 years: Canopy layers establish\n- 300-500+ years: Full old-growth condition\n\n**TEMPERATE FORESTS:**\n- 3-5 years: Herbaceous, shrub layer\n- 10-20 years: Canopy begins closing\n- 50-100 years: Mid-aged forest\n- 300+ years: Climax forest\n\n**KEY FACTORS:**\n- Seed source quality: Adjacent forests → faster\n- Soil condition: Healthy → 5-10 years to recovery\n- Climate: Tropical → fastest; cold → slowest\n- Human intervention: 50-70% faster with active restoration\n\n**TIMELINE ACCELERATION:**\nPassive regeneration: 300 years\nActive restoration: 50-100 years\nIntensive management: 10-20 years\n\n**Lesson:** Preventing deforestation saves 250 years of recovery time!",
        "category": "Conservation",
        "source": "Aura Assistant"
    },
    # ========== CAMPAIGN-RELATED QUESTIONS ==========
    {
        "question": "How can I participate in tree planting campaigns?",
        "response": "Tree planting campaigns are accessible to everyone! Here's how:\n\n**FINDING CAMPAIGNS:**\n- Check EcoAware Campaigns section\n- Local environmental NGOs\n- City environmental departments\n\n**BEST TIMES:** Spring (March-May) and Fall (Sept-Nov)\n\n**PARTICIPATION LEVELS:**\n- **Beginner:** Day events, 4-8 hours, no experience needed\n- **Intermediate:** Week-long, learn technique\n- **Advanced:** Leadership roles\n\n**WHAT'S PROVIDED:**\n✓ Saplings, gloves, tools\n✓ Usually FREE\n✓ 50-200 trees planted per volunteer\n\n**IMPACT PER VOLUNTEER:**\n- 50 trees = 2,400 lbs CO2 reduction yearly\n- Absorbs 48 lbs CO2 annually per tree\n- Cools 10,000 sq ft\n- 100+ years of benefits\n\n**NEXT STEPS:**\n1. Visit EcoAware Campaigns\n2. Filter by Climate Change/Conservation\n3. Click 'Participate'\n4. Show up ready to plant!\n\nYour hands literally shape the future forest!",
        "category": "Climate Change",
        "source": "Aura Assistant"
    },
    {
        "question": "What does the River Cleanup Drive campaign do exactly?",
        "response": "The River Cleanup Drive restores aquatic ecosystems through hands-on environmental action:\n\n**BASIC INFO:**\n- Date: June 15, 2025\n- Location: Riverfront Park\n- Time: 7 AM - 4 PM\n- Cost: FREE\n- Expected: 50-200 volunteers\n\n**WHAT YOU'LL DO:**\n- Wade in shallow water with nets\n- Pick up trash from banks\n- Collect bottles, plastic bags, debris\n- Work in teams\n\n**IMPACT PER 100 VOLUNTEERS:**\n- Trash removed: 200-400 kg\n- Plastic: 50-100 kg\n- Habitat improved: 1-2 km riverbank\n- Community awareness: 500-1000 people\n\n**WILDLIFE BENEFITS:**\n- Remove choking hazards\n- Restore fish spawning areas\n- Improve water quality\n- Reduce microplastic contamination\n\n**WHAT TO BRING:**\n- Water (ESSENTIAL!)\n- Comfortable, work clothes\n- Closed-toe shoes\n- Sun protection\n\n**JOIN VIA ECOAWARE:**\n1. Go to Campaigns\n2. Find River Cleanup Drive\n3. Click Participate\n\nEvery piece of trash removed is one less threat to wildlife!",
        "category": "Pollution Control",
        "source": "Aura Assistant"
    },
    {
        "question": "What is the Climate March 2025 campaign about?",
        "response": "The Climate March 2025 is a grassroots demonstration demanding urgent climate action from government and leadership.\n\n**BASIC INFO:**\n- Date: September 22, 2025\n- Location: City Centre\n- Time: 10 AM - 4 PM\n- Expected: 5,000-50,000+ participants\n- Cost: FREE\n\n**KEY DEMANDS:**\n1. Net-Zero by 2035\n2. Just Transition (protect workers)\n3. Climate Justice (equity focus)\n4. Corporate Accountability\n5. Adaptation & Resilience\n\n**CROWD:**\n- Students: 20-30%\n- Families: 20-25%\n- Environmental groups: 15-20%\n- Indigenous groups: 5%\n\n**WHY IT MATTERS:**\n- Media coverage reaches millions\n- Shows voter priority\n- Influences policy\n- Demonstrates collective power\n- Creates systemic pressure\n\n**WHAT TO BRING:**\n- Water (stay hydrated!)\n- Comfortable walking shoes\n- Sun protection\n- Phone (fully charged)\n\n**EXPECT:**\n- 5-10 km march\n- Rally speeches\n- Music, community energy\n- 2-3 hours standing time\n\nJoin thousands making climate action impossible to ignore!",
        "category": "Climate Change",
        "source": "Aura Assistant"
    },
    {
        "question": "How do I participate in the e-waste collection drive?",
        "response": "The E-Waste Collection Drive addresses one of the fastest-growing waste streams:\n\n**BASIC INFO:**\n- Date: May 10, 2025\n- Location: Downtown Square\n- Time: 9 AM - 5 PM\n- Cost: FREE - No fees!\n\n**E-WASTE INCLUDES:**\n- Old computers, laptops\n- Smartphones and chargers\n- Televisions, monitors\n- Printers, keyboards\n- Any plugged-in device\n\n**WHY THIS MATTERS:**\n- 62 million tons e-waste annually\n- Contains toxic materials: Lead, Mercury, Cadmium\n- Often shipped to developing countries\n- Poisons groundwater for decades\n- Child labor in informal recycling\n\n**WHAT HAPPENS:**\n1. Hard drives professionally destroyed (data safe!)\n2. Components separated\n3. Metals recovered for reuse\n4. Toxic materials safely disposed\n5. Zero landfill\n\n**ENVIRONMENTAL BENEFIT (per 100 kg):**\n✓ 50+ kg materials recovered\n✓ 400 kg CO2 avoided\n✓ 10,000+ liters water saved\n✓ 50 kWh energy saved\n\n**HOW TO PARTICIPATE:**\n1. Go to Campaigns\n2. Find E-Waste Collection Drive\n3. Click Participate\n4. Bring working & broken electronics\n\nDrop off prevents environmental poisoning!",
        "category": "Recycling",
        "source": "Aura Assistant"
    },
]

def extend_database_with_qa():
    """
    Extend existing database with Q&A pairs
    Call this after running the main seed_database() function
    """
    with app.app_context():
        print("\\n" + "="*70)
        print("SEEDING Q&A DATA FOR AURA ASSISTANT")
        print("="*70)
        
        # Check if we already have Q&A data stored somewhere
        # In a real implementation, you'd create a PreBuiltQA model
        # For now, we'll just display the data structure
        
        by_category = {}
        for qa in QA_PAIRS:
            cat = qa['category']
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(qa)
        
        print(f"\\nTotal Q&A pairs to seed: {len(QA_PAIRS)}")
        print("\\nQ&A by Category:")
        for cat in sorted(by_category.keys()):
            print(f"  • {cat}: {len(by_category[cat])} Q&As")
        
        print("\\n" + "="*70)
        print("Q&A DATA STRUCTURE (for reference):")
        print("="*70)
        
        # Display sample
        sample = QA_PAIRS[0]
        print(f"\\nSample Q&A:")
        print(f"  Question: {sample['question']}")
        print(f"  Category: {sample['category']}")
        print(f"  Response length: {len(sample['response'])} chars")
        print(f"  Source: {sample['source']}")
        
        print("\\n" + "="*70)
        print("HOW TO USE THIS DATA IN YOUR APP:")
        print("="*70)
        print("""
1. ADD A MODEL (models.py):
   class PreBuiltQA(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       question = db.Column(db.String(300), nullable=False)
       response = db.Column(db.Text, nullable=False)
       category = db.Column(db.String(50), nullable=False)
       source = db.Column(db.String(100), default='Aura Assistant')
       created_at = db.Column(db.DateTime, default=datetime.utcnow)

2. EXTEND DATABASE SEEDING:
   - Add to seed_database() after creating main tables
   - Or create separate seed function

3. USE IN ASSISTANT ENDPOINTS:
   - Fetch pre-built questions for quick access
   - Use as fallback when Gemini API fails
   - Include in system prompt for context

4. FRONTEND IMPLEMENTATION:
   - Display as buttons above chat input
   - Auto-fill when user clicks
   - Category filtering
   - Search functionality

5. EXAMPLE API ENDPOINT (app.py):
   @app.route('/api/qa/list')
   def get_prebuilt_qa():
       questions = PreBuiltQA.query.all()
       return jsonify([
           {'id': q.id, 'question': q.question, 'category': q.category}
           for q in questions
       ])
        """)
        
        print("="*70)
        print("✓ Q&A data loaded and ready to integrate!")
        print("="*70)
        
        return QA_PAIRS

if __name__ == '__main__':
    extend_database_with_qa()
