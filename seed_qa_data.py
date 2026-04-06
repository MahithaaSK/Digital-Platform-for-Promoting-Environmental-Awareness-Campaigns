"""
Seed dummy Q&A data for pre-built questions and AI responses about:
- Climate change
- Trees and deforestation
- Tree species for forests
- Questions related to existing campaigns
"""

qa_data = [
    # ========== CLIMATE CHANGE QUESTIONS ==========
    {
        "question": "What are the main causes of climate change?",
        "response": """Climate change is primarily caused by human activities that increase greenhouse gas concentrations. The main causes are:

1. **Fossil Fuel Burning** - Coal, oil, and natural gas used for energy release CO2
2. **Deforestation** - Removing trees reduces nature's ability to absorb CO2
3. **Industrial Processes** - Cement and manufacturing release significant emissions
4. **Agriculture** - Livestock farming produces methane, a potent greenhouse gas
5. **Transportation** - Vehicles burning fuel for travel emit carbon
6. **Energy Production** - Power plants relying on fossil fuels are major contributors

These activities have increased atmospheric CO2 by 50% since pre-industrial times, from 280 ppm to over 420 ppm today. The primary driver is burning fossil fuels, which accounts for about 75% of human-caused greenhouse gas emissions.

The solution lies in transitioning to renewable energy, protecting forests, and adopting sustainable practices across all sectors.""",
        "category": "Climate Change"
    },
    {
        "question": "How does climate change affect weather patterns?",
        "response": """Climate change fundamentally alters global weather patterns in several critical ways:

**Temperature Effects:**
- Global average temperatures increase by ~1.1°C since pre-industrial times
- Heat waves become more frequent, intense, and longer-lasting
- Winter seasons shorten and snow/ice coverage decreases

**Precipitation Changes:**
- Some regions experience severe droughts while others face flooding
- Monsoon patterns shift, affecting billions dependent on predictable rainfall
- Intense rainfall events become more common and destructive

**Storm Intensification:**
- Warmer oceans fuel more powerful hurricanes and typhoons
- Extreme weather events are 5-10 times more likely now than in 1900
- Atmospheric instability increases tornado and severe thunderstorm frequency

**Sea Level Rise:**
- Melting ice sheets and thermal expansion raise sea levels
- Coastal communities face increased flooding and saltwater intrusion
- Island nations face existential threats

**Regional Impacts:**
- Arctic warms 3-4 times faster than global average
- Jet streams destabilize, causing prolonged hot/cold spells
- Tropical systems shift poleward

The key insight: These aren't random changes—they follow predictable physics. A warmer atmosphere holds more moisture and has more energy, explaining the severity and frequency of extreme weather we observe.""",
        "category": "Climate Change"
    },
    {
        "question": "What can individuals do to reduce their carbon footprint?",
        "response": """Individual actions, when multiplied across millions, create systemic change. Here are the most impactful steps:

**High-Impact Actions (Biggest emissions reduction):**
1. **Reduce Flying** - Avoid unnecessary flights; one transatlantic flight = 1 ton CO2 (~1 month of driving
2. **Switch to Renewable Energy** - Install solar or choose 100% renewable power
3. **Drive Less** - Use public transit, bike, walk, or go electric
4. **Eat Plant-Based** - Meat production is resource-intensive; vegetarian diet cuts food emissions by 70%
5. **Buy Less New** - Reduce consumption and fast fashion; 10% of global emissions come from clothing

**Medium-Impact Actions:**
- Improve home insulation and heating efficiency
- Buy local and seasonal produce
- Reduce meat consumption (even partially helps)
- Support carbon-neutral companies
- Use public transportation regularly

**Smaller but Important Actions:**
- Switch to LED bulbs (75% less energy than incandescent)
- Compost organic waste
- Reduce water usage
- Recycle properly
- Choose sustainable products

**Advocacy (Often overlooked but critical):**
- Vote for climate-conscious policies
- Support carbon pricing and renewable energy subsidies
- Raise awareness in your community
- Push workplaces for sustainable practices
- Support environmental organizations

**Key Insight:** The average person's carbon footprint is 4-16 tons CO2/year depending on country. Reducing to 2-3 tons aligns with climate safety targets. Every ton avoided matters.""",
        "category": "Climate Change"
    },
    {
        "question": "Is climate change reversible?",
        "response": """Climate change is partially reversible, but the timeline and effort required depend on when action is taken. Here's the reality:

**The Good News - Reversibility:**
- Atmospheric CO2 can be reduced through renewable energy and reforestation
- Temperature increases can be limited with aggressive emissions cuts
- Within 100-150 years of zero emissions, CO2 levels would stabilize somewhat

**The Challenge - Path Dependency:**
- Some changes are now irreversible on human timescales:
  * Ice sheets melting will continue for centuries
  * Sea level rise is locked in for generations
  * Ecosystem collapse cannot always be reversed
  
**Critical Temperature Thresholds:**
- 1.5°C: Tipping points activate (Amazon dieback, permafrost thaw)
- 2°C: Severe impacts become dominant; many ecosystems collapse
- 3-4°C: Civilization faces major disruptions

**Recovery Timeline:**
- If we reach net-zero emissions TODAY, warming continues for 20-30 years
- Full recovery would take 1000+ years
- Every 0.1°C of avoided warming prevents significant suffering

**The Urgent Message:**
While some reversal is possible, preventing additional warming is far easier than reversing it. This is why limiting warming to 1.5°C is so critical—each degree of additional warming locks in permanent damage.

The time to act is NOW. Every year of delay makes the problem exponentially harder to solve.""",
        "category": "Climate Change"
    },
    {
        "question": "How does renewable energy help combat climate change?",
        "response": """Renewable energy is a cornerstone of climate solutions because it eliminates the carbon emissions from electricity generation. Here's how it works:

**The Impact:**
- Electricity production accounts for 25-30% of global emissions
- Renewable sources (solar, wind, hydro) produce 0-20g CO2/kWh vs. 820g for coal
- Switching 100% to renewables could reduce global emissions by 25-30%

**Major Renewable Sources:**

1. **Solar Power**
   - Costs have dropped 90% in a decade
   - Installation time: months vs. years for coal plants
   - Produces clean electricity for 25-30 years
   - Scales from rooftops to utility-scale farms

2. **Wind Energy**
   - Growing fastest of all sources
   - Offshore wind is more consistent than onshore
   - One turbine powers 600+ homes
   - Minimal environmental impact compared to fossil fuels

3. **Hydroelectric**
   - Provides 16% of global electricity
   - Extremely reliable baseload power
   - Multi-use (dams provide water management, recreation)

4. **Geothermal & Tidal**
   - Consistent, reliable power sources
   - Lower environmental impact
   - Still developing but promising

**Real-World Success:**
- Countries like Costa Rica run on 95%+ renewables for months
- Denmark generates 80% electricity from wind
- Solar installations grew 22% in 2023 alone

**Grid Challenges Being Solved:**
- Battery storage improving rapidly (Tesla Megapacks, etc.)
- Smart grids balance variable supply
- Interconnected systems share excess power

**Economic Win:**
- Renewable jobs now outnumber fossil fuel jobs
- Solar and wind are cheapest energy sources in most markets
- Reduces energy independence vulnerability

By switching to renewables, we eliminate emissions while creating jobs and energy security.""",
        "category": "Climate Change"
    },

    # ========== DEFORESTATION/CUTTING TREES QUESTIONS ==========
    {
        "question": "What happens when we cut down all trees?",
        "response": """Cutting down all trees would trigger environmental catastrophe affecting every living system on Earth:

**Immediate Ecological Collapse:**

1. **Atmospheric Crisis**
   - Loss of 30% of Earth's oxygen production (from photosynthesis)
   - Uncontrolled CO2 accumulation—no trees to absorb it
   - Atmospheric CO2 could reach 800+ ppm within decades
   - Temperature spike of 5-8°C within a century

2. **Biodiversity Extinction**
   - 80% of land animals depend on forests
   - Loss of 137 species/day would become 137,000/day
   - Irreversible ecological collapse
   - Medicinal plants (25% of drugs) would vanish

3. **Water Systems Destroyed**
   - Forests regulate water cycles (40% of global water flows from forested areas)
   - Aquifers would degrade
   - Rivers would dry up
   - Floods and droughts become catastrophic without forest regulation

4. **Soil Degradation**
   - Tree roots anchor soil
   - Without them: massive erosion, mudslides, desertification
   - Agricultural land becomes barren
   - Dust storms would dominate landscape

5. **Climate Catastrophe**
   - Rainforests alone store 200+ gigatons of carbon
   - Release would be equivalent to 1000 years of fossil fuel emissions
   - Trigger runaway climate change feedback loops
   - Permafrost thaw releases methane—exponential warming

**Economic Collapse:**
- $125 trillion in ecosystem services lost
- Agriculture fails without pollination and water
- Fisheries collapse (forests regulate ocean nutrients)
- Global economy faces unprecedented depression

**What Would Happen Within 10 Years:**
1. Oxygen levels drop noticeably
2. Extreme weather becomes constant
3. Agricultural collapse causes global famine
4. Mass migration creates conflicts
5. Civilization as we know it becomes unsustainable

**Fortunately:** This is preventable. Protecting and restoring forests is among the most cost-effective climate solutions—providing 30% of needed emissions reductions at lowest cost.""",
        "category": "Conservation"
    },
    {
        "question": "Why is deforestation a major environmental issue?",
        "response": """Deforestation—the clearing of forests at unsustainable rates—is one of the most critical environmental crises because it triggers cascading failures across all Earth systems:

**Climate Impact - Most Urgent:**
- Forests store 400+ gigatons of carbon globally
- Deforestation releases ~15% of annual global greenhouse gas emissions (~4 gigatons CO2)
- Equivalent to ALL cars, trucks, and planes combined
- Destroys nature's biggest carbon capture tool

**Biodiversity Loss:**
- Forests harbor 80% of terrestrial species
- 137 species lost daily due to habitat destruction
- Tropical rainforests alone: 1 in 4 medicines originate here
- Indigenous knowledge and genetic diversity vanish forever

**Water Cycle Disruption:**
- Trees regulate water: absorb, filter, release gradually
- Deforestation causes:
  * Extreme flooding (no absorption)
  * Severe droughts (no moisture release)
  * Aquifer depletion
  * Saltwater intrusion in coastal areas

**Soil and Erosion:**
- Tree roots stabilize soil
- Without them: 24 billion tons of fertile soil lost annually
- Leads to mudslides, landslides, loss of arable land
- Creates dust bowls and desertification

**Socioeconomic Consequences:**
- 1.6 billion people depend on forest products
- Indigenous communities lose homes and livelihoods
- Increased poverty and inequality
- Conflicts over remaining forest resources

**Current Crisis Scale:**
- 10 million hectares (38,600 sq miles) cleared yearly
- Amazon at tipping point (20% deforested → Amazon dies)
- Indonesia losing rainforests for palm oil
- Africa's forests shrinking rapidly

**The Positive:** Nature can recover if given chance. Protected forests grow back; if we halt deforestation TODAY and reforest, we solve 30-40% of climate change within decades.""",
        "category": "Conservation"
    },
    {
        "question": "What are the main causes of deforestation?",
        "response": """Deforestation isn't random—it's driven by specific industries and economic pressures. Understanding causes is key to solutions:

**Primary Drivers (80% of deforestation):**

1. **Agriculture** - 80% of Amazon deforestation
   - Cattle ranching: 80% of Amazon deforestation
   - Soy farming: expanding into forest for animal feed
   - Palm oil plantations in Southeast Asia
   - Sugar, coffee, cocoa farming

2. **Logging**
   - Timber extraction for construction and paper
   - Often illegal logging in protected areas
   - Selective logging degrades ecosystem integrity
   - Provides only ~2% of global employment but drives massive forest loss

3. **Infrastructure Development**
   - Roads open access to pristine forests
   - Dams flood vast forest areas
   - Mining operations (gold, oil, minerals)
   - Urban expansion consuming forests

4. **Energy Production**
   - Biomass/charcoal for fuel
   - Oil/gas exploration requires clearing
   - Hydroelectric dams

**Secondary Drivers:**

5. **Poverty and Policy Failures**
   - Poor communities clear forests for subsistence farming
   - Weak enforcement of environmental laws
   - Corruption: Officials allow illegal logging
   - Indigenous land rights not recognized

6. **Consumer Demand**
   - Your burger (beef) → Amazon deforestation
   - Palm oil (50% of processed foods)
   - Cheap paper and cardboard
   - Furniture and wood products

**Geographic Hotspots:**
- Amazon (Brazilian cattle and soy)
- Southeast Asia (palm oil in Malaysia, Indonesia)
- Central Africa (unsustainable logging)
- Boreal forests (timber extraction)

**Economic Structure Problem:**
- Forests worth more dead (timber, land) than alive
- Carbon sequestration, biodiversity value not priced in
- Corporations profit while communities and climate pay cost

**Solutions Being Implemented:**
- Certification (FSC, RSPO) for sustainable products
- Indigenous land protection (most effective conservation)
- Enforcement of deforestation laws
- Economic incentives for forest protection
- Consumer pressure on companies
- Restoration and reforestation programs

Choose products verified to not drive deforestation. Support indigenous land rights. This is one crisis where individual AND systemic action create measurable change.""",
        "category": "Conservation"
    },

    # ========== TREE SPECIES FOR FORESTS QUESTIONS ==========
    {
        "question": "Which tree species grow well in tropical forests?",
        "response": """Tropical forests thrive with high biodiversity, but certain species are particularly well-adapted and important for ecosystem health:

**Canopy Dominants (Tallest Trees):**

1. **Emergent Layer (50-80m):**
   - Kapok trees (*Ceiba pentandra*) - Massive, 200+ year lifespan
   - Mahogany (*Swietenia macrophylla*) - Strong, valuable wood
   - Brazil nut tree (*Bertholletia excelsa*) - Keystone species
   - Teak (*Tectona grandis*) - Durable, rot-resistant wood

2. **Upper Canopy (35-50m):**
   - Rubber trees (*Hevea brasiliensis*) - Commercially important
   - Bamboo variants - Fast-growing, versatile
   - Rosewood species - High value but endangered

**Mid-Story Layer (10-35m):**
   - Cacao (*Theobroma cacao*) - Important crop, shade-tolerant
   - Coffee (*Coffea* species) - Shade-grown variety supports biodiversity
   - Fig trees (*Ficus* species) - Fruiting hub, animal food source
   - Palm species (*Elaeis*, *Mauritius*) - Multiple uses

**Understory & Regeneration:**
   - Açaí palm (*Euterpe oleracea*) - Nutritious berries, sustainable harvest
   - Guarana (*Paullinia cupana*) - Used traditionally
   - Guaranã palm - Attracts wildlife
   - Heliconias - Shade-tolerant flowering plants
   - Medicinal plants (1000s of species)

**Key Ecological Traits - Why These Thrive:**
- **Shade tolerance:** Germinate under canopy cover
- **High water availability:** Adapted to wet conditions
- **Rapid decomposition:** Break down in humid climate
- **Mutualistic relationships:** Partner with fungi, animals
- **Biodiversity:** Support wildlife, insects, fungi

**Best Species for Forest Restoration:**
1. **Pioneer Species** (First to grow in cleared areas):
   - Balsa (*Ochroma pyramidale*)
   - Various heliconias
   - Guaraná

2. **Establishing Canopy:**
   - Brazil nut tree (slow but essential)
   - Mahogany (valuable, long-lived)
   - Mixed native species

**Sustainable Harvesting Options:**
- Brazil nuts: Wild harvest, no forest clearing needed
- Cacao: Shade-grown (protects canopy)
- Açaí: Sustainable palm harvest
- Rubber: Should use already-domesticated trees, not wild

**Restoration Best Practice:**
- Mix fast-growing pioneers with slow-growing canopy species
- Restore multiple layers simultaneously
- Use local seed sources for genetic adaptation
- Support indigenous cultivation knowledge

**Practical Info for Planting:**
- Tropical trees need high humidity, warmth year-round
- Dappled shade during establishment helps survival
- Native trees outperform non-natives
- Diverse plantings support more wildlife

The most biodiverse forests have maximum species diversity—aim for 50+ native tree species per hectare in restoration projects.""",
        "category": "Conservation"
    },
    {
        "question": "What are the best native tree species for forest restoration?",
        "response": """Effective forest restoration prioritizes native species adapted to local conditions. Here's a region-by-region guide:

**TROPICAL REGIONS:**

*Amazon Basin:*
- Brazil nut tree (*Bertholletia excelsa*) - Slow growing, 500+ years lifespan
- Mahogany (*Swietenia*) - Valuable, long-lived
- Rubber trees (*Hevea brasiliensis*) - Sustainable alternative to clearing
- Açaí (*Euterpe*) - Fast growth, food value
- Cupuaçu (*Theobroma grandiflorum*) - Nitrogen-fixing, productive
- Various pioneer acacias - Quick establishment

*Southeast Asia:*
- Dipterocarp species - Dominant canopy, slow-growing
- Ramin (*Gonystylus*) - Valuable, slow regeneration
- Meranti species - Multiple growth rates
- Teak (*Tectona grandis*) - Durable, fire-resistant
- Dryobalanops (camphor) - Aromatic, long-lived

*Central Africa:*
- Iroko (*Milicia excelsa*) - Hardwood, 350+ year lifespan
- Sapele (*Entandrophragma cylindricum*) - Medium-duration, valuable
- African walnut (*Lovoa trichilioides*) - Quality wood
- Various acacias - Nitrogen fixation, pioneer role
- Bamboos native to region - Fast establishment

**TEMPERATE REGIONS:**

*North America:*
- Oak species (*Quercus*) - Long-lived, wildlife support
- Hickory (*Carya*) - Nut production, wildlife food
- Walnut (*Juglans nigra*) - Long-lived, valuable
- Ash (*Fraxinus*) - Fast-growing, shade provider
- Maple species (*Acer*) - Beautiful, wildlife support

*Europe:*
- Beech (*Fagus sylvatica*) - Shade-producing, slow-growing
- Oak species (*Quercus robur*, *Q. petraea*) - Long-lived (500+ years)
- Spruce (*Picea*) - Evergreen structure
- Pine species (*Pinus*) - Pioneer role, quick establishment
- Birch (*Betula*) - Fast pioneer, nitrogen fixation

*Asia-Pacific:*
- Hinoki cypress - Long-lived, fire-resistant
- Various eucalypts - Native to region, fast-growing
- Kauri (*Agathis*) - Ancient, long-lived
- Camphor, cinnamon species - Aromatic benefits

**RESTORATION STRATEGY - Layered Approach:**

1. **Year 1-3: Pioneer Phase**
   - Fast-growing species (5-10 year rotation)
   - Create shade, stabilize soil
   - Examples: Acacias, Balsa, Alders
   - Percentage: 40% of planted trees

2. **Year 5-10: Transition Phase**
   - Medium-growth species (20-50 years)
   - Fill canopy gaps, begin structure
   - Examples: Mahogany, Meranti, Ash
   - Percentage: 40% of planted trees

3. **Year 20+: Canopy Phase**
   - Slow-growing, long-lived species (100-500 years)
   - Permanent structure, climax forest
   - Examples: Brazil nut, Oak, Dipterocarp
   - Percentage: 20% of planted trees

**CRITICAL SUCCESS FACTORS:**

✓ **Local Sourcing:** Use seed from nearby populations
✓ **Diversity:** Plant 30-50+ species minimum
✓ **Canopy Layers:** Mix understory, mid-story, canopy species
✓ **Wildlife Value:** Include trees fruiting at different seasons
✓ **Soil Preparation:** Add nitrogen-fixing species
✓ **Water Management:** Match species to soil moisture
✓ **Management:** Initial weeding/tending for 3-5 years
✓ **Scale:** 1000+ trees per hectare needed for forest function

**Recommended Species Mix (Example - Temperate):**
- 40% Oak (long-lived, wildlife)
- 20% Ash (fast-growing filler)
- 15% Hickory/Walnut (mast crops for wildlife)
- 15% Birch/Alder (pioneer nitrogen-fixers)
- 10% Specialist species (flowering, medicinal)

**Planting Timeline:**
- Best time: Early spring or fall
- Spacing: 2-4 meters apart depending on species
- Initial height: 30-60cm (smaller = cheaper, better survival)
- Survival rates: 70-90% with proper care

**Long-term Investment:**
- 5 years to establish self-sufficiency
- 30 years to significant biomass
- 100+ years to old-growth function
- 300-500 years to true forest recovery

Restoring native forests is slower but vastly superior to monoculture plantations. The result is resilient, biodiverse ecosystem.""",
        "category": "Conservation"
    },
    {
        "question": "How long does it take for a forest to regenerate naturally?",
        "response": """Natural forest regeneration follows predictable stages, but timeline varies dramatically by conditions and forest type:

**REGENERATION TIMELINE BY FOREST TYPE:**

**Tropical Rainforests (Most Complex):**
- *5-10 years:* Pioneer species establish (Balsa, heliconias)
- *10-30 years:* Pioneer canopy closes, mid-story develops
- *30-100 years:* Canopy layers establish, biodiversity increases
- *100-300 years:* Old-growth characteristics appear
- *300-500+ years:* Full old-growth condition (if ever reached)

**Temperate Forests (Moderate Timeline):**
- *3-5 years:* Herbaceous and shrub layer
- *10-20 years:* Canopy begins closing
- *50-100 years:* Mid-aged forest conditions
- *150-300 years:* Old-growth characteristics
- *300+ years:* Climax forest with ancient trees

**Boreal/Coniferous (Slowest):**
- *5-10 years:* Pioneer shrubs, light-demanding species
- *20-50 years:* Dense young forest
- *100-200 years:* Mature forest
- *200-400 years:* Old-growth conditions

**KEY FACTORS AFFECTING REGENERATION SPEED:**

1. **Seed Source Quality**
   - Adjacent intact forests → faster (seeds blown in)
   - Isolated clearings → much slower (few seeds)
   - Restoration plantings → controlled, predictable

2. **Soil Condition**
   - Healthy soil: recovers in 5-10 years
   - Severely degraded: may take 20-30 years
   - Erosion: slows recovery dramatically

3. **Climate**
   - Tropical wet → fastest (constant growing season)
   - Temperate → moderate speed
   - Dry regions → very slow or require intervention
   - Cold regions → slowest

4. **Initial Disturbance Severity**
   - Selective logging: 10-30 years to recovery
   - Complete clearing: 30-100+ years
   - Fire: 20-80 years depending on intensity
   - Mining: 100+ years (soil severely degraded)

5. **Human Intervention**
   - No intervention: slow but steady
   - Active restoration: 50-70% faster
   - Intensive management: can achieve results in 10-20 years

**REGENERATION STAGES:**

*Stage 1: Pioneer Community (Years 0-10)*
- Fast-growing, light-demanding species
- Low biodiversity (10-20 species)
- Builds soil, stabilizes land
- Examples: Grasses, fast trees (Balsa, Acacia)

*Stage 2: Early Successional Forest (Years 10-30)*
- Canopy closing over
- Shade-tolerant species establish
- Biodiversity increasing (50-100 species)
- Soil building continues

*Stage 3: Mid-Successional Forest (Years 30-100)*
- Multiple canopy layers
- Old pioneers dying, replaced by longer-lived species
- Biodiversity high (200-500 species)
- Complex structure, increasing stability

*Stage 4: Late-Successional Forest (100-300 years)*
- Long-lived climax species dominant
- Maximum biodiversity (in tropical: 1000+ species)
- Complex canopy structure with gaps
- Thick soil, complex nutrient cycling

*Stage 5: Old-Growth Forest (300+ years)*
- Ancient trees (100-500+ years old)
- Complex understory
- Full ecosystem services (full CO2, water, biodiversity function)
- Maximum resilience

**BIODIVERSITY RECOVERY TIMELINE:**
- Year 5: 5-10% of pre-disturbance species present
- Year 20: 30-50% of species
- Year 50: 60-75% of species
- Year 100: 85-95% of species
- Year 200+: Near 100% recovery (or new equilibrium)

*Note: Some species may never return if local extinctions occur*

**CARBON RECOVERY:**
- Year 5: 5% of pre-disturbance carbon stored
- Year 20: 20-30% recovered
- Year 50: 50-70% recovered
- Year 100: 80-90% recovered
- Year 200+: Full recovery or new maximum

**FOREST FUNCTION RECOVERY:**
- Water filtration: 10-15 years to partial function
- Erosion prevention: 5-10 years
- Wildlife habitat: 20-50 years (depends on species needs)
- Climate regulation: 100+ years for full function
- Microclimate/humidity: 30-50 years

**ACCELERATION THROUGH PLANTING:**

Passive (No planting): Tropical forest might take 300 years to reach full productivity

Active Restoration: Can reduce timeline 50-70%
- Plant pioneer + canopy mix
- Timeline: 50-100 years to mature forest
- Investment: $1000-5000 per hectare
- Payback: Long-term ecosystem services worth millions

**PRACTICAL LESSON:**
- Preventing deforestation saves centuries of recovery time
- Restoring is faster but expensive
- Best approach: Protect existing forests + restore degraded areas
- Forest recovery is possible but requires patience and investment

The golden rule: A forest that took 300 years to grow cannot be replaced in 50 years, but smart restoration can create functioning forests in 30-50 years.""",
        "category": "Conservation"
    },

    # ========== CAMPAIGN-RELATED QUESTIONS ==========
    {
        "question": "How can I participate in tree planting campaigns?",
        "response": """Tree planting campaigns are accessible to everyone! Here's how to get involved:

**FINDING CAMPAIGNS:**

1. **Online Platforms**
   - EcoAware platform (check Campaigns section)
   - Local environmental NGOs websites
   - City/government environmental departments
   - Search: "[your city] tree planting volunteer"

2. **Timing**
   - Best seasons: Spring (March-May) and Fall (Sept-Nov)
   - Some regions: Year-round in tropical areas
   - Check specific campaign dates

**PARTICIPATION LEVELS:**

*Beginner-Friendly:*
- Day events: Bring gloves, shovel optional
- No experience needed
- 4-8 hour commitment
- Plant 50-200 trees per person typically

*Intermediate:*
- Week-long events
- Learn proper technique
- Help with follow-up care
- Deeper connection to land

*Advanced:*
- Leadership roles
- Coordinate volunteers
- Site planning
- Ongoing maintenance

**WHAT TO EXPECT:**

✓ What's provided: Usually saplings, gloves, tools
✓ What to bring: Water, sun protection, comfortable clothes
✓ Physical demands: Moderate (lots of digging/standing)
✓ Group size: 10-500+ volunteers
✓ Cost: Usually FREE, sometimes small donation requested

**CAMPAIGN DETAILS (From EcoAware Platform):**

1. **Tree Planting Marathon**
   - Date: July 1, 2025
   - Location: City Outskirts
   - Goal: Plant 1000 trees in one day
   - Join via: Dashboard or Campaigns page
   - Expected: 100-200 volunteers
   - Organizer: Alice Green

2. **Local River Cleanup + Tree Planting**
   - Often combined events
   - Clean area first
   - Plant native species after
   - Better success rates

3. **Community Garden with Trees**
   - May 25, 2025
   - Community bonding
   - Long-term benefit
   - Ongoing maintenance involvement

**BEFORE YOU GO:**

✓ Register online (most campaigns require this)
✓ Wear comfortable, work-appropriate clothes
✓ Bring water (essential!)
✓ Wear sunscreen
✓ Know the location, arrival time
✓ Ask about parking/transportation
✓ Bring a friend (more fun!)

**DURING PARTICIPATION:**

✓ Follow volunteer coordinator instructions
✓ Use proper digging technique (prevents injury)
✓ Pace yourself (stay hydrated!)
✓ Ask questions about native species being planted
✓ Take photos for memories
✓ Network with other volunteersEnvironmentalists

**AFTER THE EVENT:**

✓ Some campaigns organize follow-ups (watering schedules)
✓ Track "your" trees' growth
✓ Share on social media
✓ Thank organizers
✓ Consider ongoing involvement

**ADDITIONAL WAYS TO SUPPORT:**

- **Donate:** Sponsor 5-10 trees ($5-20 each typically)
- **Share:** Tell friends about campaigns
- **Vote:** Support tree-friendly policies
- **Plant at home:** Start backyard biodiversity
- **Maintain:** Help water/care for saplings

**IMPACT OF YOUR EFFORT:**

- Single tree: Absorbs 48 lbs CO2 annually, cools 10,000 sq ft
- 50 trees (one volunteer): 2,400 lbs CO2 reduction yearly
- 1,000 trees (full event): 48 tons CO2 reduction yearly
- Long-term: Trees provide 100+ years of benefits

**COMPANY PARTICIPATION:**

- Team building via corporate volunteering
- Companies measure impact
- Great for employee morale
- Builds community goodwill

**LOCAL CAMPAIGN TIPS:**

- Start small: Join one event first
- Find your motivation: Climate, biodiversity, community?
- Connect with organizers: More benefits from ongoing involvement
- Bring expertise: Arborists, landscapers especially valued
- Think long-term: Maintenance jobs often needed

**NEXT STEPS:**
1. Visit the EcoAware Campaigns page
2. Filter by "Climate Change" or "Conservation"
3. Click Tree Planting Marathon or other events
4. Hit "Participate" to join
5. Show up with enthusiasm!

Join thousands making tangible climate impact. Your hands literally shape the future forest!""",
        "category": "Climate Change"
    },
    {
        "question": "What does the River Cleanup Drive campaign do exactly?",
        "response": """The River Cleanup Drive is a hands-on environmental campaign focused on restoring aquatic ecosystems. Here's exactly what it involves:

**CAMPAIGN OVERVIEW:**

- **Title:** River Cleanup Drive
- **Date:** June 15, 2025
- **Time:** Usually 7 AM - 4 PM (full day)
- **Location:** Riverfront Park
- **Organizer:** Admin Team
- **Expected Participants:** 50-200 volunteers
- **Cost:** FREE

**MISSION:**
Remove trash and pollution from river banks and shallow waters, restore habitat for aquatic wildlife, and raise community awareness about water pollution.

**WHAT YOU'LL DO:**

*Morning Session (Organization):*
- Check-in and safety briefing (30 min)
- Divide into teams
- Assign river sections
- Distribute equipment

*Main Cleanup (5-6 hours):*
- Wade into shallow water with nets
- Pick up trash from banks
- Collect debris, bottles, plastic bags
- Document what you find (for data)
- Work in coordinated teams

*Afternoon Session (Completion):*
- Sort and weigh collected waste
- Recycle appropriate materials
- Proper disposal of contaminated items
- Group photo and celebration

**EQUIPMENT PROVIDED:**

✓ Heavy-duty gloves
✓ Grab tools (10-foot litter grabbers)
✓ Nets for water collection
✓ Bins for sorting waste
✓ Safety vests for visibility
✓ First aid kit

**WHAT YOU SHOULD BRING:**

- Water and hydration salts (ESSENTIAL)
- Snacks (provided, but bring extra)
- Sun protection (sunscreen, hat)
- Closed-toe shoes (waterproof)
- Change of clothes
- Towel
- Camera (optional, for documentation)

**PHYSICAL DEMANDS:**

- Moderate to Challenging
- 3-4 hours of active work
- Wading in up to knee-depth water
- Bending, stretching, lifting
- NOT recommended if: Injured, pregnant, weak swimmers

**SAFETY PROTOCOLS:**

✓ Water depth: Max 1.5 meters, monitored
✓ Buddy system: Never work alone
✓ First aiders: 3-5 trained volunteers present
✓ Clear water first: Check for hazards
✓ No sharp waste pickup: Use grabbers, not bare hands
✓ Tetanus protection: Recommended before event

**TYPICAL FINDINGS:**

- Plastic bottles: 60-80% of collected trash
- Fishing line and nets
- Metal cans and containers
- Shopping bags and clothing
- Tires and car parts (occasionally)
- Glass bottles (dangerous!)
- Food waste and packaging

**IMPACT OF YOUR WORK:**

Per 100 volunteers, typically:
- **Trash removed:** 200-400 kg
- **Plastic reduced:** 50-100 kg
- **Habitat improved:** 1-2 km of riverbank
- **Staff time reduced:** 2-3 months worth of work
- **Community awareness:** Reaches 500-1000 through media

**WHAT HAPPENS TO COLLECTED WASTE:**

- Recyclables (plastic, metal, cardboard): Recycling centers
- Organic matter: Compost facilities
- Hazardous waste: Proper disposal facilities
- Data: Logged for pollution hotspot reports
- Findings: Shared with city environmental office

**POST-CLEANUP ACTIVITIES:**

✓ Informal gathering (lunch/snacks)
✓ Discussion about water quality
✓ Volunteer appreciation
✓ Group photos
✓ Certificate of participation offered
✓ Talk about follow-up campaigns

**WHY THIS MATTERS:**

**Ecosystem Impact:**
- Removes choking hazards for wildlife
- Restores fish spawning areas
- Improves water quality
- Reduces microplastic contamination

**Community Benefits:**
- Beautiful river access restored
- Mental health from nature connection
- Community bonding
- Visible positive change

**Long-term Effect:**
- Awareness prevents future littering
- Inspires policy changes
- Documents pollution patterns
- Builds momentum for conservation

**BEFORE SIGNING UP:**

✓ Confirm you can commit full day
✓ Check if swimming ability required (usually not)
✓ Prepare physically (light exercise beforehand helps)
✓ Arrange transportation
✓ Tell someone where you'll be

**WHAT MAKES IT DIFFERENT FROM BEACH CLEANUP:**

- River-specific: Different trash patterns
- More social: Smaller, tighter-knit teams
- Ongoing ecosystem: Same river studied over years
- Local impact: Directly affects your community's water
- Biodiversity focus: Restores animal habitats

**JOIN VIA ECOAWARE:**

1. Go to Campaigns dashboard
2. Find "River Cleanup Drive"
3. Click "Participate"
4. Fill basic info
5. Show up ready to help!

**VOLUNTEER STORIES:**

"I found a turtle tangled in fishing line. Cutting it free was the most meaningful thing I've done." - Maria

"Seeing how much plastic was in OUR river made me change my shopping habits immediately." - James

"Best Saturday ever. New friends, causes purpose, real impact." - Petra

The River Cleanup Drive transforms your Saturday into meaningful environmental action while making your river safer and cleaner. Every piece of trash removed is one less threat to wildlife.""",
        "category": "Pollution Control"
    },
    {
        "question": "What is the Climate March 2025 campaign about?",
        "response": """The Climate March 2025 is a powerful grassroots demonstration demanding urgent climate action from government and leadership. Here's the full picture:

**CAMPAIGN OVERVIEW:**

- **Title:** Climate March 2025
- **Date:** September 22, 2025
- **Time:** 10 AM - 4 PM
- **Location:** City Centre
- **Organizer:** Clara Bloom
- **Expected Participants:** 5,000-50,000+ (global simultaneous marches)
- **Cost:** FREE (donations accepted)
- **Permits:** Official city authorization

**MISSION:**
Unite voices demanding climate-friendly policies, hold governments accountable, pressure corporations for emissions cuts, and inspire global climate action.

**WHAT YOU'LL DO:**

*Before March:*
- Make a protest sign/banner
- Learn chants and talking points
- Connect with march coordinators
- Invite friends

*During March:*
- Meet at assembly point (City Centre)
- March with thousands through main streets
- Chant slogans: "Climate Action Now", "1.5 to Survive"
- Rally speeches (2-3 hours total)
- Music, community energy
- Media coverage

*After March:*
- Network with activists
- Attend post-march workshops
- Volunteer for follow-up campaigns
- Meet elected officials (sometimes)

**MARCH ROUTE:**
(Typical City Centre march):
1. Assemble: City Centre Plaza (9 AM)
2. March: Main Avenue (45 min walk)
3. Rally: Gov. Building steps (2+ hours)
4. Media: Interviews, photography
5. Disbanding: Evening

**KEY MESSAGES:**

The march centers these demands:

1. **Net-Zero by 2035**
   - Rapid transition to renewable energy
   - Phase out fossil fuels
   - Industrial emissions cuts

2. **Just Transition**
   - Protect workers losing fossil fuel jobs
   - Invest in green job training
   - Support affected communities

3. **Climate Justice**
   - Address impact on low-income, indigenous communities
   - Compensate climate-affected nations
   - Equity in green transition

4. **Corporate Accountability**
   - Hold multinationals responsible for emissions
   - Tax carbon pollution
   - Support climate leaders

5. **Adaptation & Resilience**
   - Fund disaster preparedness
   - Restore ecosystems
   - Support vulnerable populations

**TYPICAL MARCH CROWD:**

- Students: 20-30% (school strikes)
- Families: 20-25% (kids, strollers welcome)
- Environmental groups: 15-20% (organized delegations)
- Workers unions: 5-10% (green jobs advocates)
- Indigenous groups: 5% (land defenders)
- General public: 20-25% (concerned citizens)

**VISUAL ELEMENTS:**

✓ Signs and banners (make creative ones!)
✓ Artistic floats and installations
✓ Face paint (climate-themed)
✓ Costumes (polar bears, dinosaurs, etc.)
✓ Musical instruments (drums, horns)
✓ Flags and symbols
✓ Children's art projects

**WHAT TO BRING:**

- Comfortable walking shoes (ESSENTIAL - 5-10 km walk)
- Water (Stay hydrated!)
- Snacks
- Sun protection (hat, sunscreen)
- Phone charged (for emergencies, photos)
- ID (for security)
- Umbrella (check forecast!)
- First aid supplies
- Sign-making materials if making your own

**SAFETY CONSIDERATIONS:**

✓ Police presence: Generally supportive but monitoring
✓ Crowd control: Marshals maintain order
✓ Medical support: Red Cross, paramedics on-site
✓ Buddy system: Stay with group
✓ Emergency exits: Know routes if needed
✓ Hydration stations: Throughout march route

**WHAT MAKES IT POWERFUL:**

**Media Impact:**
- International news coverage
- Amplifies climate message to millions
- Shows government voter concern
- Influences policy discussions

**Direct Political Pressure:**
- Elected officials paying attention
- Demonstrates voter priority
- Influences election platforms
- Shows constituency support

**Community Building:**
- Sense of collective power
- Networking with like-minded people
- Inspiration for ongoing action
- Solidarity across causes

**Psychological Impact:**
- Individual empowerment: Fighting back against despair
- Hope from community
- Belief in possibility of change
- Motivation for personal action

**HISTORICAL CONTEXT:**

- 2019 Global Climate Strikes: 4 million people, 163 countries
- Australian protests influenced renewable energy policy
- EU climate ambitions influenced by street pressure
- Corporate commitments increased after public marches

**DURING MARCH - TIPS:**

✓ Stay with your group
✓ Take breaks in shade
✓ Drink water regularly (don't wait until thirsty)
✓ Wear comfortable, breathable clothes
✓ Consider going partway if energy low
✓ Take photos for memory/social media
✓ Be respectful of diverse views (broad coalition)
✓ Help others (give water, assist fallen)

**COMMON MARCH ACTIVITIES:**

- Synchronized chants (powerful, motivating)
- Call-and-response with speakers
- Singing (climate songs often used)
- Silent moments (respect/memory)
- Speeches from leaders (5-10 min each)
- Live music (bands sometimes invited)
- Volunteer coordination talks

**WHAT HAPPENS WITH MARCH DATA:**

- Participant counts reported globally
- Media coverage influences narrative
- Political calculations change with turnout
- NGOs use momentum for campaigns
- Social media amplifies message
- Inspection reports follow-up

**JOIN VIA ECOAWARE:**

1. Go to Campaigns dashboard
2. Find "Climate March 2025"
3. Click "Participate"
4. Fill details
5. Get march updates via email

**POST-MARCH NEXT STEPS:**

- Join ongoing campaign groups
- Contact elected representatives
- Volunteer for political campaigns supporting climate action
- Attend strategy sessions
- Organize community events
- Educate others

**REALISTIC EXPECTATIONS:**

✓ Doesn't guarantee policy change immediately (but creates conditions)
✓ Marches are part of larger strategy (emails, voting, pressure also needed)
✓ One march isn't sufficient (sustained campaigns maintain momentum)
✓ You'll meet thousands sharing your values
✓ Participation is powerful, even if outcome feels uncertain

**WHY THIS MARCH MATTERS NOW (2025):**

- Critical climate tipping points approaching
- Policy windows closing for 1.5°C limit
- Global negotiations happening
- Young people voting for first time
- Corporate commitments need enforcing

**FINAL THOUGHT:**

The Climate March 2025 transforms individual climate concern into collective power. Walking with thousands sends a message: We demand change NOW. Your presence literally counts—reported in attendance figures, seen on cameras, felt by decision-makers.

History shows marches work. Join thousands making climate action impossible to ignore.""",
        "category": "Climate Change"
    },
    {
        "question": "How do I participate in the e-waste collection drive?",
        "response": """The E-Waste Collection Drive is an essential campaign addressing one of the fastest-growing waste streams. Here's how to participate and what makes it important:

**CAMPAIGN OVERVIEW:**

- **Title:** E-Waste Collection Drive
- **Date:** May 10, 2025
- **Time:** 9 AM - 5 PM
- **Location:** Downtown Square
- **Organizer:** Test User Team
- **Cost:** FREE - No drop-off fees!
- **What's accepted:** All electronics

**WHAT IS E-WASTE?**

E-waste (electronic waste) includes:
- Old computers, laptops, tablets
- Smartphones and chargers
- Printers, scanners, peripherals
- Televisions and monitors
- Refrigerators and appliances
- Audio equipment, speakers
- Gaming consoles
- Broken electronics of all types

**WHY E-WASTE MATTERS:**

⚠️ **The Crisis:**
- 62 million tons generated annually worldwide
- 82% ends up in landfills (should be 0%)
- Contains toxic materials:
  * Lead (causes brain damage)
  * Mercury (neurological harm)
  * Cadmium (cancer risk)
  * Arsenic (toxin)
  * Uranium (radioactive)

**Environmental Impact:**
- These toxins leach into groundwater
- Poison drinking water supplies
- Contaminate agricultural land
- Bioaccumulate in food chain
- Persistent for decades/centuries

**Social Impact:**
- Often shipped to developing countries
- Informal recyclers exposed to toxins
- Child labor in disassembly (35+ countries)
- Communities poisoned for rich nations' waste

**Resource Waste:**
- Gold, silver, copper extracted via toxic methods
- 95% more energy than mining new materials
- Recoverable materials: $57 billion annually
- Mostly lost to landfills

**HOW THE DRIVE WORKS:**

*Drop-Off Process:*
1. Drive to Downtown Square parking
2. Look for E-Waste Collection tent (yellow/green)
3. Park and approach collection volunteers
4. Describe items you're dropping
5. Volunteers categorize devices
6. Fill out brief form (privacy data destruction)
7. Done! Receipt provided for tax purposes

*What Gets Recorded:*
- Item type and weight
- Condition (working/broken)
- Privacy destruction confirmation
- Your volunteer status (optional)

**WHAT ITEMS TO BRING:**

✓ Bring:
- Desktop computers (towers)
- Laptops and notebooks
- Tablets, e-readers
- Smartphones (even broken)
- Phone chargers, cables
- Monitors (old and new)
- Printers (inkjet or laser)
- Scanners and fax machines
- Keyboards, mice
- External hard drives
- Routers, modems
- Gaming consoles
- Televisions (any size)
- Microwaves
- Coffee makers, toasters
- Electric kettles
- Exhaust fans
- Power tools
- Small appliances
- Audio equipment
- Headphones, earbuds
- Digital cameras
- Electronic toys
- Any plugged-in device

✗ Don't bring:
- Lightbulbs (separate recycling)
- Batteries (separate program)
- Cords and wires (sometimes accepted separately)
- Broken glass (safety hazard)

**PRIVACY PROTECTION:**

IMPORTANT: Personal data destroyed!

✓ All hard drives professionally wiped
✓ Data destruction certified
✓ Certificate provided
✓ No data recovery possible
✓ Your digital privacy protected

*Process:*
- Hard drives removed
- Crushed/degaussed (magnetic field erased)
- Incinerated at end of day
- Certified destruction documentation

**WHAT HAPPENS TO YOUR ELECTRONICS:**

*Step 1: Initial Assessment*
- Sorted by type (computers, appliances, etc.)
- Tested for working condition
- Hard drives identified for destruction

*Step 2: Component Separation*
- Working devices donated (non-profit refurbishment)
- Recyclable devices: Manual disassembly
- Toxic materials: Isolated for safe disposal
- Metals extracted: Gold, copper, silver, aluminum

*Step 3: Material Recovery*
- Screens: Glass recycling
- Metals: Smelters (recovered, reused)
- Plastics: Industrial reuse
- Precious metals: Refineries (used in new electronics)

*Step 4: Safe Disposal*
- Toxic materials: Hazmat facilities
- Incineration at proper temperatures
- Ash disposal: Secure containment
- Zero landfill goal

**ENVIRONMENTAL BENEFITS (Per 100 kg e-waste):**

✓ 50+ kg materials recovered for reuse
✓ CO2: 400 kg emissions avoided
✓ Water: 10,000+ liters saved (vs new mining)
✓ Energy: 50 kWh saved
✓ Landfill waste prevented: 100%
✓ Toxic groundwater contamination: Prevented

**HOW TO HELP BEYOND DROPPING OFF:**

1. **Volunteer at Collection Site**
   - Check items received
   - Organize materials
   - Help with logistics
   - 4-8 hour shifts available

2. **Become a Collection Site**
   - Register your business/organization
   - Become permanent drop-off location
   - Free training provided
   - Brings customers

3. **Education**
   - Tell friends about program
   - Share on social media
   - Educate about e-waste dangers
   - Promote responsible consumption

4. **Advocacy**
   - Push for local e-waste laws
   - Support producer responsibility
   - Demand manufacturer take-back programs
   - Vote for environmental candidates

**TAX DEDUCTION:**

✓ Donations often tax-deductible
✓ Receipt provided listing items
✓ Consult with accountant
✓ Usually deductible as charitable donation

**JOIN VIA ECOAWARE:**

1. Go to Campaigns dashboard
2. Find "E-Waste Collection Drive"
3. Click "Participate"
4. Get location details/updates
5. Show up with your electronics!

**BEFORE YOU COME:**

✓ Gather old electronics
✓ Don't steal data removal (we handle it)
✓ Bring working and broken items
✓ Come early (spots can fill afternoon)
✓ Bring receipt for large items (optional)
✓ Allow 10-15 min per visit

**DURING DROP-OFF:**

✓ Be honest about item condition
✓ Ask questions (they're experts!)
✓ Don't remove hard drive yourself
✓ Optional: Volunteer afterwards
✓ Take receipt
✓ Feel good!

**E-WASTE FACTS:**

- Average person generates: 30 lbs e-waste/year
- Typical household throws away: 300+ pounds over lifetime
- Working electronics donated: 30-50% of received items
- Precious metals recovered: $57 billion potential annually
- Only 20% currently recycled (target: 100%)

**ALTERNATIVE OPTIONS:**

If downtown square inconvenient:
- Check for ongoing collection sites
- Mail-back programs (some retailers)
- Manufacturer take-back programs
- Local repair shops (often accept)
- E-waste collection events (seasonal)

**IMPACT OF YOUR EFFORT:**

Your dropped e-waste prevents:
- Toxic groundwater contamination (your drinking water!)
- Child labor in informal recycling (3-5 devices)
- Unnecessary mining (recovers ~50 kg materials)
- Landfill toxins (100+ years persistence)
- Environmental justice violation (waste imperialism halted)

**LET'S DO SOME MATH:**

Your participation + 500 people drop-off:
- 50,000+ kg electronic waste diverted from landfills
- 2,000+ kg precious metals recovered
- 10+ tons materials reused in manufacturing
- 200,000+ kg CO2 emissions avoided
- Toxic groundwater contamination prevented

**CALL TO ACTION:**

Don't let electronics become toxic waste. Gather what you've got, bring it to Downtown Square on May 10, and join hundreds making responsible disposal happen. Your old tech gets a second life—or responsible recycling—and none of it poisons the environment.

See you at the collection drive!""",
        "category": "Recycling"
    },
]

if __name__ == '__main__':
    print("=" * 70)
    print("DUMMY Q&A DATA FOR ECOAWARE ASSISTANT")
    print("=" * 70)
    print(f"\nTotal Q&A pairs generated: {len(qa_data)}\n")
    
    for i, qa in enumerate(qa_data, 1):
        print(f"\n{i}. Question: {qa['question']}")
        print(f"   Category: {qa['category']}")
        print(f"   Response Preview: {qa['response'][:100]}...")
        print(f"   Response Length: {len(qa['response'])} characters")
    
    print("\n" + "=" * 70)
    print("HOW TO USE THIS DATA:")
    print("=" * 70)
    print("""
1. INTEGRATE INTO DATABASE:
   - Modify models.py to add a Question model
   - Create a Pre-built Q&A table
   - Run seed script to populate database

2. USE IN FRONTEND:
   - Display pre-built questions in Assistant page
   - Show as quick-access buttons
   - Auto-fill user questions for faster responses

3. AI CONTEXT:
   - Include in Gemini system prompt for better answers
   - Use as fallback responses if API fails
   - Improve AI consistency with provided templates

4. FOR TESTING:
   - Test chatbot with diverse questions
   - Verify response quality
   - Check UI implementation

CATEGORIES COVERED:
- Climate Change (5 Q&As)
- Conservation (5 Q&As)
- Campaign-Related Questions (4 Q&As)

TOTAL TOPICS INCLUDED:
✓ Climate change causes & solutions
✓ Deforestation impacts & causes
✓ Tree species for restoration
✓ Forest regeneration timeline
✓ Tree planting campaigns
✓ River cleanup campaigns
✓ Climate marches
✓ E-waste recycling campaigns
    """)
    
    print("\n" + "=" * 70)
    print("EXPORT TO JSON (For frontend use):")
    print("=" * 70)
    
    import json
    json_data = json.dumps(qa_data, indent=2)
    print(f"\nJSON export ready. Length: {len(json_data)} characters")
    
    # Save to file
    with open('dummy_qa_data.json', 'w') as f:
        json.dump(qa_data, f, indent=2)
    print("✓ Saved to: dummy_qa_data.json")
    
    # Summary statistics
    categories = {}
    for qa in qa_data:
        cat = qa['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\n" + "=" * 70)
    print("STATISTICS:")
    print("=" * 70)
    for cat, count in sorted(categories.items()):
        print(f"  • {cat}: {count} Q&As")
    
    avg_response_length = sum(len(qa['response']) for qa in qa_data) / len(qa_data)
    print(f"\n  Average response length: {avg_response_length:,.0f} characters")
    print("=" * 70)
