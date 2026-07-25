import os

def generate_documents():
    data_dir = "./data"
    os.makedirs(data_dir, exist_ok=True)
    
    docs = {
        "doc_01_sigiriya.txt": """Sigiriya Rock Fortress
Sigiriya, also known as the Lion Rock, is a stunning ancient fortress built by King Kashyapa in the 5th century. It is a UNESCO World Heritage site and one of Sri Lanka's most iconic attractions.
Location: Central Province, near Dambulla.
Entrance Ticket Cost: The entrance fee for foreign tourists is $35 USD per person (which is approximately 11,300 LKR).
Dress Code: Dress comfortably for a hike. There is no strict religious dress code for climbing the rock, but modest attire is appreciated. Good hiking shoes are highly recommended as there are 1,200 steep metal steps.
Rules: Climbing during mid-day is extremely hot; start early (around 7:00 AM) or late afternoon. Do not touch or photograph the frescoes with flash. Watch out for wasps; keep quiet in designated wasp zones.
Transport: Easily reachable by tuk-tuk or bus from Dambulla (about 30-40 minutes). Private taxis and rented scooters are also popular.
Key Features: Mirror Wall, Sigiriya Frescoes, Lion's Paw, and the summit ruins with panoramic views.""",

        "doc_02_dambulla.txt": """Dambulla Cave Temple
The Dambulla Cave Temple (also known as the Golden Temple of Dambulla) is the largest and best-preserved cave temple complex in Sri Lanka, dating back to the 1st century BC.
Location: Dambulla, Central Province.
Entrance Ticket Cost: Foreign visitor tickets cost 2,000 LKR (approximately $6 USD) per person. Tickets must be purchased at the counter at the bottom of the hill before climbing up.
Dress Code: Strict temple rules apply. Shoulders and knees must be fully covered. Wraps/sarongs are available for rent at the entrance. Hats and shoes must be removed before entering the cave chambers.
Rules: No photography of people posing with Buddha statues (your back must not face the Buddha). Do not touch the ancient murals. Keep food items sealed to avoid attracting wild monkeys.
Transport: Accessible by public bus from Kandy, Sigiriya, or Colombo. The temple lies along the main highway, making tuk-tuks a convenient transport choice.
Key Features: Five main cave chambers containing 153 Buddha statues, murals depicting the life of Lord Buddha, and a giant Golden Buddha statue at the base.""",

        "doc_03_polonnaruwa.txt": """Polonnaruwa Ancient City
Polonnaruwa was the second capital of Sri Lanka, flourishing from the 11th to the 13th century. Today, it is a UNESCO World Heritage site showcasing monumental ruins of palaces, temples, and reservoirs.
Location: North Central Province.
Entrance Ticket Cost: The entrance fee for foreign visitors is $30 USD (around 9,700 LKR) per person.
Dress Code: As there are active sacred sites within the ruins (such as the Vatadage and Gal Vihara), modest clothing covering shoulders and knees is mandatory. Shoes and hats must be removed when stepping onto the stone platforms of temples.
Rules: Bicycles are the best way to explore the archaeological park. Beware of hot stone surfaces when walking barefoot at sacred sites (wearing socks is allowed).
Transport: Rented bicycles are available at the entrance for 500-1000 LKR per day. Tuk-tuks can be hired for a guided tour of the ruins for about 3,000-4,000 LKR.
Key Features: Gal Vihara (four massive rock-cut Buddha statues), the Royal Palace ruins, Vatadage, Lankatilaka, and Parakrama Samudra (massive man-made reservoir).""",

        "doc_04_anuradhapura.txt": """Anuradhapura Sacred City
Anuradhapura is one of the ancient capitals of Sri Lanka, famous for its well-preserved ruins of ancient Sri Lankan civilization. It was a major center of Theravada Buddhism for centuries.
Location: North Central Province.
Entrance Ticket Cost: The archaeological site ticket costs $30 USD (approximately 9,700 LKR) for foreign visitors. Some individual temples inside may have small separate donations.
Dress Code: Strict religious dress code. White clothing is preferred but any modest clothing covering shoulders and knees is acceptable. You must walk barefoot on sandy and stone paths within temple bounds.
Rules: Do not turn your back directly to Buddha statues for photos. Silence must be maintained near meditating pilgrims.
Transport: Best explored by hiring a tuk-tuk for the day (around 4,000-5,000 LKR) or renting a bicycle. Taxis are available for comfortable travel between distant stupas.
Key Features: Sri Maha Bodhi (the oldest documented sacred tree in the world), Ruwanwelisaya Stupa, Jetavanaramaya Stupa, and the twin ponds (Kuttam Pokuna).""",

        "doc_05_kandy_temple.txt": """Temple of the Sacred Tooth Relic (Sri Dalada Maligawa)
The Temple of the Sacred Tooth Relic is a highly revered Buddhist temple housing the relic of the tooth of the Buddha. It is located in the royal palace complex of the former Kingdom of Kandy.
Location: Kandy city center, Central Province.
Entrance Ticket Cost: The entrance fee is 2,000 LKR (approx $6 USD) for SAARC tourists and 2,500 LKR (approx $8 USD) for other foreign nationals.
Dress Code: Very strict dress code. Shoulders and knees must be covered. Wearing white or light-colored clothing is highly respected. Footwear and hats must be deposited at the shoe storage counter before entry.
Rules: Photography is allowed, but photographing the inner sanctum containing the casket is prohibited. Maintain silence and respect worshipers during the ritual (Thewawa) times: dawn, midday, and evening.
Transport: Conveniently located in Kandy town, easily reachable by walking, local tuk-tuk, or bus.
Key Features: Paththirippuwa (octagonal tower), Golden Canopy, Royal Palace complex, and the daily cultural dance performance nearby (1,500-2,000 LKR).""",

        "doc_06_galle_fort.txt": """Galle Dutch Fort
Galle Fort is a historical, archaeological, and architectural heritage monument built by the Portuguese in 1588, then extensively fortified by the Dutch in the 17th century. It is a living heritage site with a blend of history and modern boutique shops.
Location: Galle, Southern Province.
Entrance Ticket Cost: Free entry. Walking around the public streets, ramparts, and fort walls has no cost. However, specific museums (like the National Maritime Museum) charge small fees of 500-1,000 LKR.
Dress Code: Casual and relaxed. Swimwear is not allowed on the streets inside the Fort, but regular shorts and t-shirts are perfectly fine. Modest clothing is only required if visiting the temple or mosque inside.
Rules: Respect the local residents living inside the fort. Watch your step when walking along the high fort walls.
Transport: Galle is connected to Colombo by the Southern Expressway (bus/taxi) and the coastal railway line. Inside the fort, walking is the best option.
Key Features: Galle Lighthouse, Dutch Reformed Church, Maritime Museum, the Pedlar Street boutique shops, and watching the sunset from the Flag Rock Bastion.""",

        "doc_07_yala_national_park.txt": """Yala National Park Safari
Yala National Park is the most famous wildlife sanctuary in Sri Lanka, boasting one of the highest leopard densities in the world.
Location: Southeastern region, main gateway is Tissamaharama.
Entrance Ticket Cost: Park entry permit plus service charges cost around $30-$40 USD per person. A private safari jeep rental costs between 12,000 and 18,000 LKR ($40-$60 USD) depending on half-day or full-day tours. Total combined cost for 2 people is typically 30,000-35,000 LKR.
Dress Code: Earth-toned, neutral-colored clothing (khaki, green, brown) is recommended. Avoid bright clothes. Bring sunglasses, hats, and a dust scarf.
Rules: Do not feed or tease the animals. Never get out of the safari jeep under any circumstances unless at the designated beach resting spot. Littering is strictly forbidden.
Transport: Reach Tissamaharama by bus or private taxi. The safari company will pick you up directly from your hotel in a 4x4 open-top jeep.
Key Features: Leopard sightings, wild elephants, sloth bears, crocodiles, and diverse bird species.""",

        "doc_08_sinharaja.txt": """Sinharaja Rainforest
Sinharaja Forest Reserve is a national park and a biodiversity hotspot in Sri Lanka. It is of international significance and has been designated a Biosphere Reserve and World Heritage Site by UNESCO.
Location: Southwest lowland wet zone.
Entrance Ticket Cost: The entrance fee for foreign visitors is 2,000 LKR ($6 USD). A mandatory local guide fee is about 2,000 to 3,000 LKR per trek.
Dress Code: Long trousers, high socks, and hiking shoes. Leech socks are highly recommended as the rainforest is heavily populated with leeches. Bring rain gear.
Rules: Keep to the designated walking trails. Do not disturb the fauna and flora. Take all plastic waste back with you.
Transport: Access points are Kudawa (near Kalawana) or Deniyaya. Can be reached via hired taxi or local buses, followed by a short tuk-tuk ride to the entrance.
Key Features: Tropical rainforest canopy, endemic bird species (blue magpie), purple-faced langur monkeys, and beautiful forest waterfalls.""",

        "doc_09_train_kandy_ella.txt": """Kandy to Ella Scenic Train Train Journey
The train trip between Kandy and Ella is widely considered one of the most scenic train rides in the world. It passes through lush green tea plantations, mountain passes, and waterfalls.
Location: Central Highlands connecting Kandy, Nanu Oya (Nuwara Eliya), Demodara, and Ella.
Ticket Costs: 
- 1st Class Reserved: 3,000 - 5,000 LKR (must book 30 days in advance).
- 2nd Class Reserved: 2,000 - 3,000 LKR.
- 3rd Class Unreserved: 500 LKR (bought on the day, very crowded).
Dress Code: Comfortable clothing. Hill country can get cool and misty, so carrying a light jacket or sweater is advised.
Rules: Do not hang precariously out of the open doors or windows, as there are narrow tunnels and close-cut rocks along the track.
Transport: The train departs from Kandy Railway Station. It is recommended to check timetables beforehand. The journey takes approximately 6 to 7 hours.
Key Features: Tea estate vistas, Great Western Station, Pattipola (highest railway station in Sri Lanka), and the Demodara Loop.""",

        "doc_10_ella_attractions.txt": """Ella Mountain Town Attractions
Ella is a charming, laid-back hillside town popular for hiking, breathtaking views, and tea-country scenery.
Location: Badulla District, Uva Province.
Costs: 
- Nine Arch Bridge: Free entrance.
- Little Adam's Peak: Free entrance.
- Ella Rock: Free (local guides might request 2,000 LKR, but can be hiked independently).
- Ravana Falls: Free to view from the roadside.
Dress Code: Sporty hiking wear. Carry a rain jacket, as weather changes rapidly in the hills. Wear insect repellent.
Rules: Do not walk on the active railway tracks at the Nine Arch Bridge when a train is approaching. Stay on marked paths on Ella Rock to avoid falling off cliffs.
Transport: Easily navigable on foot or via cheap local tuk-tuks (500-1,000 LKR for short trips).
Key Features: Walking along the railway lines, panoramic views from Little Adam's Peak, and Ravana Pool Club.""",

        "doc_11_mirissa_beach.txt": """Mirissa Beach & Whale Watching
Mirissa is a popular coastal town famous for its sandy beaches, surfing spots, vibrant nightlife, and whale watching excursions.
Location: Matara District, Southern Province.
Costs: 
- Whale Watching Boat Tour: $40-$50 USD (12,000-15,000 LKR) per person (includes breakfast).
- Coconut Tree Hill: Free entry.
- Surfboard rental: 500-1,000 LKR per hour.
Dress Code: Beachwear, shorts, swimwear, and flip-flops. Bring sunscreen, sunglasses, and hats.
Rules: Ensure you book whale watching with conservation-approved operators who do not chase the whales.
Transport: Mirissa is situated along the main coastal highway, easily reached by bus, train (to Weligama station), or express taxi from Colombo.
Key Features: Coconut Tree Hill sunset, Parrot Rock, whale watching (blue whales, dolphins), and beachside seafood restaurants.""",

        "doc_12_hikkaduwa_coral.txt": """Hikkaduwa Coral Sanctuary & Beach
Hikkaduwa is renowned for its marine sanctuary, vibrant coral reefs, surfing breaks, and sandy beaches. It is a top spot for snorkeling and diving.
Location: Galle District, Southern Province.
Costs: 
- Snorkeling gear rental: 500-1,000 LKR per day.
- Glass-bottom boat ride: 3,000-5,000 LKR per group.
- Scuba diving: $40-$60 USD per dive.
Dress Code: Swimwear, rash guards, beach attire.
Rules: Never step on, touch, or break the coral reefs. Do not feed the sea turtles that swim close to the shore. Use reef-safe sunscreen.
Transport: Highly accessible via the coastal railway line (Hikkaduwa Station) or main coastal road buses.
Key Features: Hikkaduwa Marine National Park, snorkeling with giant green turtles, and beach bars.""",

        "doc_13_temple_dress_code.txt": """Sacred Temple Etiquette and Dress Codes
When visiting any Buddhist temple, Hindu Kovil, or religious site in Sri Lanka, strict cultural rules must be observed to show respect.
General Rules:
- Dress Modestly: Both men and women must cover their shoulders and knees. Sleeveless tops, tank tops, short skirts, and shorts are strictly forbidden.
- Light Colors: Wearing white or light-colored clothing is highly appreciated and shows respect in Buddhist culture.
- Remove Shoes and Hats: All footwear (shoes, sandals, socks) and headwear (hats, caps, headbands) must be removed before entering the sacred temple enclosure. Shoe counters are available at the entrance for a small tip (50-100 LKR).
- No Buddha Tattoos: Displaying tattoos of Lord Buddha is considered highly offensive and can lead to questioning. Cover any such tattoos.
- Behavior: Never pose with your back turned towards a Buddha statue. Avoid public displays of affection within temple grounds.""",

        "doc_14_colombo_tour.txt": """Colombo City Tour & Attractions
Colombo is the commercial capital and largest city of Sri Lanka, offering a blend of colonial architecture, modern skyscrapers, and diverse cultural sites.
Location: Western Province.
Costs:
- Gangaramaya Temple: 400 LKR entrance fee.
- National Museum: 1,000 LKR entrance fee for foreigners.
- Lotus Tower: $20 USD (approx 6,400 LKR) for observation deck ticket.
- Galle Face Green: Free public park.
Dress Code: Casual attire for city walks. If visiting Gangaramaya Temple, cover shoulders and knees.
Rules: Be careful when crossing roads. Tuk-tuk drivers must use a meter; ensure you ask "Meter please" before boarding.
Transport: Easily get around using ride-hailing apps like PickMe or Uber (highly recommended to avoid overcharging).
Key Features: Colombo Fort colonial buildings, Red Mosque (Jami Ul-Alfar), Pettah Market, and lake-side Gangaramaya Temple.""",

        "doc_15_travel_budgeting.txt": """Travel Budgeting & Currency Guide
A guide to managing money, budgeting, and typical expenses when traveling in Sri Lanka.
Currency: Sri Lankan Rupee (LKR). $1 USD is approximately 310-330 LKR (variable).
Typical Daily Budgets:
- Budget Traveler: 8,000 - 15,000 LKR per day (public transport, local guesthouses, local rice and curry).
- Mid-Range Traveler: 25,000 - 60,000 LKR per day (private tuk-tuks/taxis, mid-tier hotels, mix of local and Western dining).
- Luxury Traveler: 80,000 LKR+ per day (private chauffeur, boutique luxury villas, high-end dining).
Payment Methods: Cash is king in rural areas, local shops, and tuk-tuks. Carry small denominations (100, 500, 1000 LKR notes). Credit cards (Visa, Mastercard) are accepted in major supermarkets, hotels, and upscale restaurants.
Tipping: A 10% service charge is often added to restaurant bills. Otherwise, a tip of 100-500 LKR for drivers, guides, and hotel staff is highly appreciated.""",

        "doc_16_sri_lanka_weather.txt": """Sri Lanka Weather & Monsoons
Sri Lanka has a tropical climate with two distinct monsoon seasons that affect different parts of the island at different times.
Monsoon Seasons:
- Yala Monsoon (May to September): Brings rain to the South and West coasts and the Hill Country. Best to visit the East Coast (Arugam Bay, Trincomalee) during this time.
- Maha Monsoon (October to January): Brings rain to the North and East. Best to visit the South and West coasts (Mirissa, Galle, Hikkaduwa, Colombo) and Hill Country.
Inter-monsoon periods (February to April): Generally dry and sunny across the entire island, making this the peak tourist season.
Packing Tips: Light, breathable cotton clothing is best. Bring a raincoat/umbrella, sunscreen, and warm clothing if visiting the chilly Hill Country (Nuwara Eliya).""",

        "doc_17_local_transport.txt": """Local Transport Options in Sri Lanka
Getting around Sri Lanka is an adventure, with options ranging from cheap public transport to private convenience.
Transport Choices:
1. Tuk-Tuks: Iconic three-wheelers. Great for short distances. Always negotiate the price beforehand or use a metered tuk-tuk. In Colombo, use PickMe/Uber. Expect 100-150 LKR per kilometer.
2. Public Buses: Very cheap (50-200 LKR for long distances). They can be crowded, noisy, and fast. Excellent for budget travelers.
3. Trains: Affordable and scenic. Standard classes (2nd/3rd class) are cheap. Advanced reservation is necessary for 1st class.
4. Private Taxi/Chauffeur: Rented car with a driver. Most comfortable option for families or multi-city trips. Costs around $50-$80 USD (16,000-25,000 LKR) per day including fuel and driver accommodation.""",

        "doc_18_sri_lankan_food.txt": """Sri Lankan Cuisine Overview
Sri Lankan food is rich in spices, coconut milk, and unique flavors. It is a highlight of any trip to the island.
Must-Try Foods:
- Rice and Curry: The staple meal. A mount of rice served with various curries (dhal, chicken, fish, jackfruit, beetroot) and sambols. Cost: 400-800 LKR at local eateries; 1,500-3,000 LKR at tourist restaurants.
- Hoppers (Appa): Bowl-shaped savory pancakes made from fermented rice batter and coconut milk. Best eaten with an egg in the middle (Egg Hopper) and lunu miris (spicy onion sambol). Cost: 50-100 LKR per hopper.
- Kottu Roti: Street food made from chopped parotta flatbread, vegetables, eggs, meat, and spices. Highly energetic and noisy preparation. Cost: 600-1,200 LKR.
- Ceylon Tea: World-famous black tea grown in the high country. Try it plain or as milk tea. Cost: 100-300 LKR.""",

        "doc_19_national_parks_safari.txt": """Guide to National Parks Safaris
Sri Lanka is a premier wildlife destination. Beyond Yala, several other national parks offer outstanding safari experiences.
Key Parks:
1. Udawalawe National Park: Famous for wild elephants. Best elephant viewing guaranteed. Combined cost (entry + jeep) is about 25,000-30,000 LKR for two people.
2. Minneriya National Park: Famous for 'The Gathering' of hundreds of Asian elephants near the reservoir (typically between July and October). Total cost is around 28,000-33,000 LKR for two people.
3. Wilpattu National Park: Largest park, known for leopards and sloth bears, with a quieter, less crowded feel than Yala. Total cost is around 32,000-38,000 LKR.
Booking Tip: Safaris are typically run in the early morning (6 AM - 9 AM) or late afternoon (3 PM - 6 PM).""",

        "doc_20_horton_plains.txt": """Horton Plains National Park & World's End
Horton Plains is a protected national park in the central highlands covered by montane grassland and cloud forest.
Location: Near Nuwara Eliya, Central Province.
Entrance Ticket Cost: Foreign visitor entrance permit costs around 10,000 LKR (approx $30 USD) including service charges and vehicle entry.
Dress Code: Wear layers. It is very cold and windy at 5:00 AM, but gets warm and sunny by 9:00 AM. Wear sturdy walking shoes.
Rules: Strictly zero plastic allowed. All plastic wrappers, labels, and water bottles will have their labels removed at the checkpoint. No littering. Stick to the 9km circular trail.
Transport: Hire a private van or tuk-tuk from Nuwara Eliya (about 1.5 hours drive, costs 3,000-5,000 LKR) starting at 5:00 AM to reach before the mist covers the view.
Key Features: World's End (a sheer cliff drop of 880 meters), Baker's Falls, and endemic wildlife.""",

        "doc_21_adam_peak.txt": """Adam's Peak (Sri Pada) Hike
Adam's Peak is a 2,243-meter tall holy mountain, revered as a sacred pilgrimage site by Buddhists, Hindus, Christians, and Muslims.
Location: Nallathanniya (Dalhousie), Central Province.
Costs: Free entry. Voluntary donations are accepted at the temples along the way.
Dress Code: Comfortable, warm athletic wear. The climb is cold at night but you will sweat. Modesty is required at the summit shrine (cover shoulders and knees, remove shoes).
Rules: Respect the pilgrims. Climbing season is from December to May (peak season). The path is lit and lined with shops during the season. Off-season climbing requires headlamps and has no shops.
Transport: Reach Hatton by train or bus, then take a local bus or tuk-tuk to Nallathanniya.
Key Features: Climbing 5,500 stone steps at night to witness a spectacular sunrise and the triangular shadow of the mountain cast on the surrounding clouds.""",

        "doc_22_pinnewala.txt": """Pinnawala Elephant Orphanage
Pinnawala is an orphanage, nursery, and captive breeding ground for wild Asian elephants.
Location: Pinnawala village, near Kegalle.
Entrance Ticket Cost: Foreign visitor ticket costs 3,000 LKR (approx $9 USD) per adult.
Schedules:
- Bottle feeding baby elephants: 9:15 AM and 1:15 PM.
- Elephant bath in the Maha Oya river: 10:00 AM - 12:00 PM and 2:00 PM - 4:00 PM.
Rules: Visitors must stay behind safety barriers. Do not feed elephants outside authorized food feeding stalls.
Transport: Located off the main Colombo-Kandy road. Can be reached by taking a train to Rambukkana station and a short tuk-tuk ride, or hiring a taxi.
Key Features: Watching the herd of elephants walk down the village streets to bathe in the river.""",

        "doc_23_sri_lankan_food_costs.txt": """Detailed Food Costs & Dining Budget
Understanding food prices helps in planning daily expenses accurately across Sri Lanka.
Food Cost Breakdowns:
1. Local Eateries (Kade):
   - Local Breakfast (hoppers/roti + tea): 200 - 400 LKR ($0.75 - $1.25 USD)
   - Rice & Curry Lunch (Veg/Chicken): 400 - 800 LKR ($1.30 - $2.50 USD)
   - Kottu Roti Dinner: 600 - 1,200 LKR ($2.00 - $4.00 USD)
2. Tourist-Oriented Cafes & Restaurants:
   - Western Breakfast (avocado toast, coffee): 1,500 - 2,500 LKR ($5.00 - $8.00 USD)
   - Seafood Dinner (whole grilled fish/prawns): 3,000 - 6,000 LKR ($10.00 - $20.00 USD)
   - Fruit Juice / King Coconut: 200 - 500 LKR
3. Supermarkets (Cargills Food City, Keells):
   - 1.5L Mineral Water: 120 LKR
   - Local fruits (bananas, mangoes): 200 - 500 LKR per kg.""",

        "doc_24_tea_estates.txt": """Tea Estates & Nuwara Eliya Tea Tours
Nuwara Eliya, often called 'Little England', is the heart of Sri Lanka's tea production industry.
Location: Nuwara Eliya District, Central Province.
Costs:
- Tea Factory Tour: Often free or a small fee of 500-1,000 LKR ($1.50 - $3.00 USD) which includes a tea tasting session.
- Plucking tea leaves experience: 1,000 - 2,000 LKR.
- High Tea at Grand Hotel: 3,500 - 5,000 LKR per person (famous colonial experience).
Dress Code: Hill country is cold (10-18 degrees Celsius). Warm jackets, long pants, and closed shoes are recommended.
Rules: Follow guidelines when walking inside active factory machinery rooms.
Transport: Rent a tuk-tuk for a tea country tour (approx 3,000 LKR per half-day) or hire a private vehicle.
Key Features: Damro Labookellie Tea Center, Pedro Tea Estate, and beautiful waterfalls like Devon Falls and St. Clair's Falls.""",

        "doc_25_bentota.txt": """Bentota Beach & Water Sports
Bentota is a coastal town famous for its golden beaches, water sports activities, and the scenic Bentota River.
Location: Galle District, Southern Province.
Costs:
- Jet ski rental: 4,000 - 6,000 LKR for 15 minutes.
- Banana boat ride: 2,500 - 4,000 LKR per person.
- Madu River Safari (balapitiya): 4,000 - 6,000 LKR per private boat (1-2 hours tour).
Dress Code: Swimwear and beach casuals.
Rules: Always wear a life jacket when participating in water sports or river safaris.
Transport: Located about 2 hours south of Colombo along the main coastal highway. Easy to reach via express bus, train, or private taxi.
Key Features: Bentota beach, Madu Ganga river mangroves, cinnamon island, and local turtle hatcheries.""",

        "doc_26_jaffna_heritage.txt": """Jaffna Cultural Heritage & Travel
Jaffna, situated at the northernmost tip of Sri Lanka, offers a distinct Tamil cultural experience, colorful Hindu temples, and unique cuisine.
Location: Northern Province.
Costs:
- Nallur Kandaswamy Kovil: Free entry.
- Jaffna Fort: Free entry.
- Ferry to Delft Island: 100 LKR (government ferry) or 1,500 LKR (private boat).
Dress Code: Strict temple rules apply. At Nallur Kovil, women must cover shoulders and knees. Men must remove their shirts and enter bare-chested. Shoes must be left outside.
Rules: Photography is strictly prohibited inside the Nallur Kovil temple sanctum.
Transport: The Yal Devi express train runs from Colombo directly to Jaffna (journey takes 6-7 hours). Inside Jaffna, tuk-tuks and rental scooters are best.
Key Features: Nallur Kovil, Jaffna Fort ruins, Delft Island wild ponies, and Jaffna crab curry.""",

        "doc_27_trincomalee.txt": """Trincomalee Beaches & Pigeon Island
Trincomalee is a port city on the northeast coast, famous for its natural harbor, whale watching, and Pigeon Island marine sanctuary.
Location: Eastern Province.
Costs:
- Pigeon Island National Park Permit + Boat: 10,000 - 15,000 LKR per group of 2-4 people (includes snorkeling gears).
- Koneswaram Temple: Free entry.
Dress Code: Modest clothing for Koneswaram Temple. Swimwear is appropriate for Nilaveli and Uppuveli beaches.
Rules: Standing on the coral reef at Pigeon Island is strictly banned. Keep distance from marine life (turtles, blacktip reef sharks).
Transport: Trincomalee is accessible via overnight trains or daily buses from Colombo.
Key Features: Snorkeling at Pigeon Island, Koneswaram Temple perched on Swami Rock, and whale watching (May to October).""",

        "doc_28_arugam_bay.txt": """Arugam Bay Surf & Vibe Guide
Arugam Bay is a world-class surfing destination, known for its relaxed surf-town atmosphere, point breaks, and nightlife.
Location: Ampara District, Eastern Province.
Costs:
- Surfboard rental: 1,000 - 1,500 LKR per day.
- Surf lesson with instructor: 3,000 - 5,000 LKR per hour.
- Kudumbigala Monastery: Free entry.
Dress Code: Beachwear, bikinis, boardshorts. Modest clothing is only needed if visiting nearby historic monasteries.
Rules: Respect local line-ups in the surf point breaks. Surf season is from May to September.
Transport: Located on the southeast coast. Reachable via private taxi from Colombo/Ella, or long-distance buses.
Key Features: Main Point surf break, Elephant Rock sunset, and Kumana National Park safari nearby.""",

        "doc_29_udawalawe.txt": """Udawalawe National Park & Elephant Transit Home
Udawalawe is a key sanctuary for wild elephants and a major ecotourism destination in Sri Lanka.
Location: Border of Sabaragamuwa and Uva Provinces.
Costs:
- Park Entrance Ticket: ~$25 USD per foreign adult.
- Safari Jeep Hire: 10,000 - 14,000 LKR.
- Elephant Transit Home: 1,000 LKR entry fee.
Schedules:
- Elephant Transit Home feeding times: 9:00 AM, 12:00 PM, 3:00 PM, and 6:00 PM daily.
Rules: Do not approach the elephant calves at the transit home. Safaris are restricted to designated tracks.
Transport: Reached via bus or taxi from Ella, Mirissa, or Colombo.
Key Features: Watching orphaned baby elephants being fed milk, and herds of wild elephants roaming the grasslands.""",

        "doc_30_travel_safety.txt": """General Travel Safety & Tips
Essential safety, health, and emergency guidelines for tourists traveling in Sri Lanka.
Tips:
- Emergency Numbers: Tourist Police: 1912, General Police: 119, Ambulance (Suwa Seriya): 1990.
- Health: Drink only bottled or filtered water. Ensure street food is hot and freshly prepared. Carry mosquito repellent to protect against Dengue fever.
- Scams: Avoid unofficial beach boys or tour guides. Always check prices before ordering food or boarding tuk-tuks. Use metered transport.
- Connectivity: Buy a tourist SIM card (Dialog or Mobitel) at Colombo Airport. 20-30 GB data costs around 2,000 - 3,000 LKR ($7-$10 USD).
- Cultural Respect: Never pose for photos touching or climbing sacred monuments or Buddha statues. Avoid wearing clothes with religious symbols.""",

        "doc_100_sri_lanka_railways_headquarters.txt": """Authority: Sri Lanka Railways (SLR)
Headquarters: Olcott Mawatha, Colombo Fort | Hotline: 1971 | Station Office: +94 11 243 4215
Online Booking Portal: seatreservation.railway.gov.lk
Service: Information on 30-day seat reservations, special luxury observation cars (Viceroy Special, Ella Odyssey), and train delay status.""",

        "doc_31_budget_hostels_colombo_kandy.txt": """Category: Budget Accommodation (Hostels & Backpacker Lodges)
Locations: Colombo & Kandy
Price Range: LKR 2,500 - LKR 6,000 per bed/night
Popular Options: Clock Inn Colombo, Hosterville Kandy, Backpacker's Nest Kandy.
Amenities: Shared dorms, free Wi-Fi, air conditioning, communal kitchen, locker storage. Ideal for solo travelers and low-budget itineraries.""",

        "doc_32_budget_guesthouses_ella_nuwaraeliya.txt": """Category: Budget Accommodation (Family Homestays)
Locations: Ella & Nuwara Eliya
Price Range: LKR 4,000 - LKR 8,000 per room/night
Popular Options: Ella Eco Lodges, Mount Wave Homestay Nuwara Eliya.
Amenities: Includes traditional home-cooked Sri Lankan breakfast. Hosts assist with tuk-tuk arrangements for hikes to Little Adam's Peak and Ella Rock.""",

        "doc_33_budget_beach_cabanas_south.txt": """Category: Budget Beach Cabanas & Surf Hostels
Locations: Mirissa, Weligama, Arugam Bay
Price Range: LKR 3,500 - LKR 7,500 per night
Popular Spots: Hangtime Hostel Weligama, Sea Turtle Cabanas Mirissa.
Amenities: Beachfront access, surf board rentals (LKR 1,000/hr), open-air dining, and social atmosphere for backpackers.""",

        "doc_34_heritage_villas_galle_fort.txt": """Category: Mid-Range Heritage Villas
Location: Galle Dutch Fort
Price Range: LKR 20,000 - LKR 35,000 per room/night
Popular Options: Taru Villas Rampart Street, Fort Bazaar, Prince of Galle.
Details: Restored Dutch colonial merchant houses within the UNESCO ramparts. Includes air conditioning, courtyard gardens, and full breakfast.""",

        "doc_35_tea_bungalows_hill_country.txt": """Category: Plantation Bungalows & Tea Estate Lodges
Locations: Hatton, Nuwara Eliya, Bandarawela
Price Range: LKR 25,000 - LKR 45,000 per night
Popular Options: Stafford Bungalow Nuwara Eliya, Camellia Hills Hatton.
Details: Historic British tea planter bungalows surrounded by tea estates. Features fireplace lounges, high tea, and guided tea walks.""",

        "doc_36_midrange_resorts_cultural_triangle.txt": """Category: Mid-Range Eco Resorts
Locations: Sigiriya & Dambulla
Price Range: LKR 15,000 - LKR 30,000 per night
Popular Options: Sigiriya Village Hotel, Aliya Resort & Spa.
Details: Eco-friendly chalets with direct views of Sigiriya Rock Fortress. Includes swimming pools, buffet breakfasts, and bicycle rentals.""",

        "doc_37_eco_lodges_knuckles_kitulgala.txt": """Category: Rainforest Eco-Lodges & Nature Retreats
Locations: Knuckles Mountain Range & Kitulgala
Price Range: LKR 12,000 - LKR 22,000 per night
Popular Options: Rukgala Retreat, Kitulgala Adventure Camp.
Details: Secluded nature lodges near rivers and forests. Designed for trekking, yoga, and whitewater rafting participants.""",

        "doc_38_beach_resorts_bentota_tangalle.txt": """Category: Beachfront Resorts & Villas
Locations: Bentota & Tangalle
Price Range: LKR 18,000 - LKR 35,000 per night
Popular Options: Cinnamon Bey Beruwala, Maya Tangalle Villa.
Details: Direct ocean access, infinity pools, Ayurvedic spa centers, and seafood dining on the beach.""",

        "doc_39_luxury_tea_trails.txt": """Category: Luxury Tea Plantation Estates
Location: Ceylon Tea Trails (Hatton)
Price Range: USD 600 - USD 1,100 per night (All-Inclusive)
Details: Relais & Châteaux property featuring restored tea planter bungalows. Includes private butler service, gourmet dining, and guided estate walks.""",

        "doc_40_luxury_safari_camps_yala.txt": """Category: Luxury Tented Safari Camps
Location: Yala National Park Border
Price Range: USD 450 - USD 900 per night (All-Inclusive)
Popular Options: Wild Coast Tented Lodge, Leopard Safaris.
Details: Air-conditioned luxury canvas domes, private 4x4 game drives with naturalist guides, and outdoor fine dining.""",

        "doc_41_luxury_clifftop_resorts_weligama.txt": """Category: Luxury Oceanfront Resorts
Locations: Weligama & Tangalle
Price Range: USD 400 - USD 850 per night
Popular Options: Cape Weligama, Anantara Peace Haven Tangalle.
Details: Clifftop ocean views, private plunge pools, dedicated wellness spas, and private cove beaches.""",

        "doc_42_luxury_wellness_santani.txt": """Category: Luxury Mountain Wellness Retreat
Location: Santani Wellness Resort (Kandy)
Price Range: USD 350 - USD 700 per night
Details: Minimalist eco-villas overlooking the Knuckles Range. Focuses on Ayurvedic detox, yoga, custom wellness cuisine, and hydrotherapy.""",

        "doc_43_luxury_heritance_kandalama.txt": """Category: Iconic Architectural Eco-Hotel
Location: Heritance Kandalama (Dambulla)
Price Range: LKR 55,000 - LKR 95,000 per night
Details: Designed by architect Geoffrey Bawa. Built into a cliff face overlooking Kandalama Lake. Features infinity pools and lake eco-tours.""",

        "doc_44_colombo_luxury_five_star.txt": """Category: City Luxury Hotels
Location: Colombo Coastal Promenade
Price Range: LKR 45,000 - LKR 85,000 per night
Popular Options: Shangri-La Colombo, Cinnamon Life, Kingsbury.
Details: High-rise luxury, rooftop bars, international buffets, casino access, and adjacent shopping malls.""",

        "doc_45_boutique_villas_ella_98acres.txt": """Category: Hill Country Eco Resort
Location: 98 Acres Resort & Spa (Ella)
Price Range: USD 250 - USD 450 per night
Details: Standalone chalets on a tea estate overlooking Ella Gap. Located next to Little Adam's Peak and Flying Ravana Zipline.""",

        "doc_46_flying_ravana_zipline_ella.txt": """Activity: Flying Ravana Mega Zipline
Location: Mini Adam's Peak, Ella
Rates: USD 30 - USD 45 per person
Details: Dual-wire zipline over half a kilometer long, reaching speeds up to 80 km/h over tea estates. Certified by European Rope Course Association.""",

        "doc_47_kitulgala_whitewater_rafting.txt": """Activity: Kitulgala White Water Rafting & Canyoning
Location: Kelani River, Kitulgala
Package Cost: USD 35 - USD 65 per person (approx LKR 10,000 - 18,000)
Details: Covers 5 km of Grade 2 & 3 rapids, waterfall abseiling, cliff jumping, safety gear, and local lunch.""",

        "doc_48_hiking_adam_peak.txt": """Activity: Adam's Peak (Sri Pada) Night Hike
Location: Nallathanniya (Dalhousie)
Cost: Free entry
Details: 5,200 stone steps climb starting at 2:00 AM to reach the summit for sunrise. Season runs from December to May.""",

        "doc_49_hiking_knuckles_range.txt": """Activity: Knuckles Mountain Range Trekking & Camping
Location: Matale / Kandy District
Guided Day Hike Cost: USD 40 - USD 70 per person (Includes mandatory local guide permit & packed lunch).
2-Day Camping Package: USD 150 - USD 250 (Includes tents, campfire dinner, and mountain guides).""",

        "doc_50_hot_air_ballooning_dambulla.txt": """Activity: Hot Air Balloon Safari
Location: Dambulla / Kandalama
Cost: USD 220 - USD 260 per adult
Details: 1-hour flight over Sigiriya Rock, lakes, and jungle canopy. Season runs from November to April. Includes champagne breakfast upon landing.""",

        "doc_51_scuba_diving_snorkeling.txt": """Activity: Scuba Diving & Snorkeling
Locations: Hikkaduwa, Trincomalee (Nilaveli), Pigeon Island
Beginner Scuba Dive: USD 70 - USD 90.
Pigeon Island Snorkeling Tour: LKR 9,000 - LKR 12,000 including boat transfer and marine national park permit.""",

        "doc_52_surfing_packages.txt": """Activity: Surf Lessons & Board Rentals
Locations: Weligama Bay (Nov-April) & Arugam Bay (May-Oct)
1-Hour Beginner Lesson: LKR 3,500 - LKR 5,000 (Includes instructor and board).
5-Day Surf Camp Package: USD 250 - USD 400 (Includes accommodation and daily coaching).""",

        "doc_53_hiking_ella_rock.txt": """Activity: Hiking Little Adam's Peak & Ella Rock
Location: Ella
Little Adam's Peak: Free entry, easy 1.5-hour round-trip hike.
Ella Rock Guided Hike: LKR 3,000 - LKR 5,000 for a local guide (recommended due to unmapped tea estate paths).""",

        "doc_54_sinharaja_rainforest_trek.txt": """Activity: Deep Jungle Trek & Bird Watching
Location: Sinharaja Rainforest Reserve
Guided Package Fee: LKR 6,000 - LKR 10,000 (Includes mandatory Forest Department ranger guide and leech socks rental).""",

        "doc_55_cooking_class_tours.txt": """Activity: Traditional Sri Lankan Culinary Class
Locations: Kandy, Ella, Galle Fort
Price per Person: LKR 4,000 - LKR 8,000
Includes: Local vegetable market tour, clay-pot cooking of 5 local curries over a coconut-wood fire, and a buffet meal.""",

        "doc_56_tourist_police_hotlines.txt": """Facility: Tourist Police Division Headquarters & Regional Units
Tourist Police Hotline: 1912 (24/7 Toll-Free)
Police Emergency: 119 / 118
Regional Offices: Colombo (+94 11 242 1052), Kandy (+94 81 222 2222), Galle/Hikkaduwa (+94 91 227 5545), Sigiriya (+94 66 493 0327).
Role: Assisting tourists with theft reports, passport losses, scam complaints, and safety disputes.""",

        "doc_57_national_ambulance_suwa_seriya.txt": """Service: 1990 Suwa Seriya Free National Ambulance
Hotline: 1990 (Toll-Free 24/7)
Coverage: Available island-wide across all 25 districts.
Details: Equipped with trained paramedics and life-support technology for traffic accidents, medical emergencies, and mountain rescues.""",

        "doc_58_disaster_management_weather.txt": """Facility: Disaster Management Centre & Department of Meteorology
Disaster Call Centre Hotline: 117
Emergency DMC Landline: +94 11 213 6222
Use Case: Essential for landslide alerts, flood warnings, or weather updates before embarking on high-altitude hikes.""",

        "doc_59_national_hospital_colombo.txt": """Facility: National Hospital of Sri Lanka (Colombo)
Type: Public Tertiary General Hospital & National Trauma Center
Emergency Hotline: 1959 | Landline: +94 11 269 1111
Details: 24/7 emergency accident service and intensive care units.""",

        "doc_60_kandy_galle_hospitals.txt": """Facility: Major Regional Teaching Hospitals
National Hospital Kandy: +94 81 222 2261 (Serves Kandy, Sigiriya, Dambulla, and Knuckles Range).
Karapitiya Teaching Hospital Galle: +94 91 223 2261 (Serves Hikkaduwa, Galle, Mirissa, and Southern Coast).""",

        "doc_61_nuwara_eliya_badulla_hospitals.txt": """Facility: Hill Country District Hospitals
Nuwara Eliya District General Hospital: +94 52 222 2261
Badulla Provincial General Hospital (Near Ella): +94 55 222 2261
Details: Medical care for hiking injuries, altitude issues, or leech bite infections near Ella and Nuwara Eliya.""",

        "doc_62_private_hospitals.txt": """Facility: Private Hospital Networks (Lanka Hospitals, Asiri Health, Nawaloka)
Lanka Hospitals Colombo: +94 11 553 0000 | Emergency: 1566
Asiri Central Hospital Colombo: +94 11 452 4400
Asiri Hospital Kandy: +94 81 452 8800
Details: Multi-specialty care accepting international travel insurance policies.""",

        "doc_63_pickme_uber_coverage.txt": """App Availability: PickMe & Uber App Coverage
Active Coverage Zones: Colombo Metro, Negombo, Kandy City, Galle, Matara, and Kurunegala.
Supported Classes: Metered Tuk-Tuks, Flex Cars, Sedans, and Vans.
Note: Limited or unavailable in remote areas (Ella, Sigiriya, Arugam Bay, Yala), where local tuk-tuks or private drivers are required.""",

        "doc_64_expressway_terminals.txt": """Facility: Highway Express Bus Terminals
Makumbura Multimodal Transport Center (Kottawa): Terminal for luxury expressway buses to Galle, Matara, Hambantota, and Katunayake Airport.
Kandy Central Bus Stand: Hub for long-distance buses to Nuwara Eliya, Dambulla, Trincomalee, and Jaffna.""",

        "doc_65_driving_permits_aac.txt": """Topic: Self-Drive Rentals & AAC Driving Permits
Requirement: An International Driving Permit (IDP) must be endorsed by the Automobile Association of Ceylon (AAC) in Colombo (Cost: ~USD 25 / LKR 7,500).
AAC Colombo Office: No. 40, Sir Mohamed Macan Markar Mawatha, Colombo 03 | Tel: +94 11 242 1528.""",

        "doc_66_hela_bojun_outlets.txt": """Concept: Hela Bojun Hala (Ministry of Agriculture Enterprise)
Mission: Empowers female agricultural entrepreneurs while serving traditional, preservative-free Sri Lankan vegetarian food.
Price Range: LKR 50 - LKR 300 per item.
Key Locations: Peradeniya (Gannoruwa Rd), Kandy Town, Dambulla Main Rd, Anuradhapura, Battaramulla (Diyatha Uyana), Matara Beach Rd.
Popular Menu: Finger millet (Kurakkan) pittu, polos cutlets, herbal porridge (Konda Karawala), mung bean patties, fresh fruit juices.""",

        "doc_67_botanical_gardens.txt": """Attractions: Royal Botanical Gardens Peradeniya & Hakgala Gardens
Peradeniya (Kandy): Fee LKR 3,000 foreign adult. Features Orchid House, Giant Bamboo lawn, and Royal Palm Avenue.
Hakgala (Nuwara Eliya): Fee LKR 3,540 foreign adult. High-altitude rose gardens and alpine fernery.
Henarathgoda (Gampaha): Fee LKR 3,540 foreign adult. Home to Sri Lanka's first planted rubber tree.""",

        "doc_68_pinnawala_and_udawalawe_elephants.txt": """Attractions: Elephant Sanctuaries
Pinnawala Elephant Orphanage (Kegalle): USD 15 / LKR 4,500. Milk feeding at 9:15 AM & 1:15 PM; river bathing at 10:00 AM & 2:00 PM.
Udawalawe Elephant Transit Home (DWC): LKR 1,500 entrance. Ethical rehabilitation of wild orphan calves. Public feeding viewing at 9:00 AM, 12:00 PM, 3:00 PM, 6:00 PM.""",

        "doc_69_forest_dept_and_dwc_permits.txt": """Authority: Forest Conservation Dept & Dept of Wildlife Conservation (DWC)
Forest Dept Tel: +94 11 286 6631 | DWC Tel: +94 11 288 8585
Permit Rules: Camping or off-trail trekking in Forest Reserves (Knuckles, Sinharaja) REQUIRES prior written approval from the Forest Dept. DWC circuit bungalows and campsites (Yala, Wilpattu, Horton Plains) must be reserved via `dwc.lankagate.gov.lk`.""",

        "doc_70_sltda_and_drone_permits.txt": """Authority: Sri Lanka Tourism Development Authority (SLTDA) & Civil Aviation Authority (CAASL)
SLTDA Hotline: 1912 (24/7 Tourist Assistance)
CAASL Tel: +94 11 235 8800
Drone Rule: Flying recreational or commercial drones REQUIRES prior online approval from CAASL, Ministry of Defence security clearance, and Archaeology Dept approval for heritage sites.""",

        "doc_71_tourist_police_colombo_headquarters.txt": """Facility: Tourist Police Division Headquarters & Hotlines
Location: No. 80, Galle Road, Colombo 03
Landline: +94 11 242 1052 | Tourist Police Hotline: 1912 (24/7 Service)
Police Emergency Hotline: 119 / 118
Role: Handles tourist complaints, theft reports, lost passports, and scam investigations across Sri Lanka.""",

        "doc_72_tourist_police_kandy_nuwaraeliya.txt": """Facility: Hill Country Tourist Police Units
Kandy Tourist Police Unit: Kandy Police Station premises | Tel: +94 81 222 2222
Nuwara Eliya Tourist Police Unit: Central Bus Stand Premises | Tel: +94 52 222 2222
Role: Assists travelers in Kandy, Ella, and Nuwara Eliya with local safety, guide verification, and mountain emergency response.""",

        "doc_73_tourist_police_galle_hikkaduwa.txt": """Facility: Southern Coast Tourist Police Units
Galle / Hikkaduwa Unit: Narigama, Hikkaduwa | Tel: +94 91 227 5545
Bentota / Moragalla Unit: Galle Road, Beruwala | Tel: +94 34 227 6049
Role: Coastline safety monitoring, beach harassment prevention, surf safety guidance, and water activity disputes.""",

        "doc_74_tourist_police_sigiriya_dambulla.txt": """Facility: Cultural Triangle Tourist Police Units
Sigiriya Unit: Near Rock Entrance Junction | Tel: +94 66 493 0327
Dambulla Unit: New Bus Stand Premises | Tel: +94 66 567 7966
Anuradhapura Unit: Lion's Post Junction | Tel: +94 11 313 3686
Role: Protection of heritage sites, ticket scam prevention, and crowd control.""",

        "doc_75_tourist_police_arugambay_negombo.txt": """Facility: East Coast & Airport Region Tourist Police
Arugam Bay / Pottuvil Unit: Panama Road, Arugam Bay | Tel: +94 11 308 1044
Negombo / Eththukala Unit: Poruthota Road, Eththukala | Tel: +94 31 227 5555
Airport Tourist Police (BIA): Katunayake | Tel: +94 11 225 1475""",

        "doc_76_disaster_management_117.txt": """Facility: Disaster Management Centre & Department of Meteorology
Disaster Call Centre: 117 (Disaster alerts, floods, landslides, extreme weather warnings)
Emergency DMC Landline: +94 11 213 6222
Department of Meteorology Weather Inquiries: +94 11 268 6686
Use Case: Essential for verifying mountain trail safety or monsoon landslide warnings before high-altitude hikes.""",

        "doc_77_national_hospital_colombo.txt": """Facility: National Hospital of Sri Lanka (Colombo)
Type: Public Tertiary General Hospital & National Trauma Center
Emergency Hotline: 1959 | General Landline: +94 11 269 1111
Accident Service: Open 24/7 with specialized trauma teams and intensive care units.""",

        "doc_78_kandy_teaching_hospital.txt": """Facility: National Hospital Kandy (Teaching Hospital)
Type: Major Public Hospital in Central Province
Landline: +94 81 222 2261
Details: Primary trauma center for emergencies occurring in Kandy, Sigiriya, Dambulla, Matale, and Knuckles Mountain Range.""",

        "doc_79_karapitiya_galle_hospital.txt": """Facility: Karapitiya Teaching Hospital (Galle)
Type: Main Government Tertiary Hospital in Southern Province
Landline: +94 91 223 2261
Details: Serves emergency cases across Hikkaduwa, Galle, Unawatuna, Mirissa, and Matara coastal zones.""",

        "doc_80_nuwaraeliya_badulla_hospitals.txt": """Facility: Hill Country District General Hospitals
Nuwara Eliya District General Hospital: +94 52 222 2261
Badulla Provincial General Hospital (Near Ella): +94 55 222 2261
Details: Essential medical reference points for hiking injuries, altitude issues, or leech bite infections near Ella and Nuwara Eliya.""",

        "doc_81_private_hospitals_lanka_asiri.txt": """Facility: Private Hospital Networks (Lanka Hospitals, Asiri Health, Nawaloka)
Lanka Hospitals Colombo: +94 11 553 0000 | Emergency: 1566
Asiri Central Hospital Colombo: +94 11 452 4400
Asiri Hospital Kandy: +94 81 452 8800
Details: Multi-specialty private care accepting international travel insurance policies.""",

        "doc_82_pickme_intercity_fares.txt": """Service: PickMe Intercity Outstation Rides
Sample Fares: Colombo Airport to Kandy (~LKR 12,000 - 16,000); Colombo to Galle Fort via Highway (~LKR 10,000 - 14,000).
Advantage: Upfront fixed digital pricing avoiding street driver fare negotiations.""",

        "doc_83_expressway_bus_terminals.txt": """Facility: Major Highway Bus Terminals
Makumbura Multimodal Transport Center (Kottawa): Primary terminal for luxury expressway buses to Galle, Matara, Hambantota, and Katunayake Airport.
Kandy Central Bus Stand: Hub for buses to Nuwara Eliya, Dambulla, Trincomalee, and Jaffna.""",

        "doc_84_aac_driving_permits_colombo.txt": """Topic: Self-Drive Rentals & AAC Temporary Driving Permits
Rule: An International Driving Permit (IDP) alone is NOT sufficient in Sri Lanka.
Permit Requirement: Foreign drivers must get their IDP endorsed by the Automobile Association of Ceylon (AAC) in Colombo (Cost: ~USD 25 / LKR 7,500).
AAC Colombo Office: No. 40, Sir Mohamed Macan Markar Mawatha, Colombo 03 | Tel: +94 11 242 1528.""",

        "doc_85_hela_bojun_kandy_peradeniya.txt": """Locations: Hela Bojun Outlets in Kandy & Peradeniya
1. Peradeniya Outlet: Near Royal Botanical Gardens Entrance, Gannoruwa Road.
2. Kandy Town Outlet: Near Kandy Lake / Market Complex.
Hours: 6:30 AM to 6:30 PM daily.
Price Range: LKR 50 - LKR 300 per food item.""",

        "doc_86_hela_bojun_dambulla_anuradhapura.txt": """Locations: Hela Bojun Outlets in Dambulla, Anuradhapura, Matara
1. Dambulla Outlet: Opposite Agriculture Complex, Main Road Dambulla.
2. Anuradhapura Outlet: Near New Town Railway Station.
3. Matara Outlet: Beach Road, Matara.
Hours: 6:30 AM to 7:00 PM daily.""",

        "doc_87_hela_bojun_battaramulla_colombo.txt": """Locations: Hela Bojun Outlets in Western Province
Battaramulla Outlet: Near Diyatha Uyana / Ministry of Agriculture Complex, Battaramulla.
Details: High-footfall outlet offering traditional herbal drinks (Ranawara, Iramusu, Beli Flower) and steamed millet rotis.""",

        "doc_88_henarathgoda_gampaha_gardens.txt": """Attraction: Henarathgoda Botanical Garden
Location: Gampaha (30 km from Colombo)
Entrance Fee (Foreign Adult): LKR 3,540
Highlights: Site where the first rubber tree in the British Empire was planted in 1876. Features ancient tropical trees and boat rides on the lake.""",

        "doc_89_seetawaka_wet_zone_gardens.txt": """Attraction: Seetawaka Wet Zone Botanical Garden
Location: Avissawella (60 km from Colombo)
Entrance Fee (Foreign Adult): LKR 3,540
Highlights: Sri Lanka's newest botanical garden dedicated to wet-zone flora conservation. Features golf-cart tours and paddle boating.""",

        "doc_90_pinnawala_elephant_orphanage_official.txt": """Attraction: Pinnawala Elephant Orphanage (Department of National Zoological Gardens)
Location: Rambukkana (Kegalle District)
Entrance Fee (Foreign Adult): USD 15 / LKR 4,500
Daily Schedule: Milk feeding at 9:15 AM & 1:15 PM; River bathing procession at 10:00 AM & 2:00 PM at Ma Oya River.""",

        "doc_91_millennium_elephant_foundation.txt": """Attraction: Millennium Elephant Foundation (MEF)
Location: Karandupona, Rambukkana (Adjacent to Pinnawala)
Entry / Walk Package: LKR 6,000 - LKR 12,000 per person
Ethical Focus: Non-riding sanctuary. Offers elephant walk experience, elephant washing in the river, and medical care volunteering.""",

        "doc_92_ridiyagama_safari_park.txt": """Attraction: Ridiyagama Open Safari Park
Location: Ambalantota (Hambantota District)
Entrance Fee (Foreign Adult): USD 20 / LKR 6,000 (Includes air-conditioned safari bus tour)
Highlights: 500-acre open safari drive featuring African lions, Bengal tigers, herbivores, and Asian elephants.""",

        "doc_93_forest_department_camping_permits.txt": """Authority: Department of Forest Conservation Sri Lanka
Headquarters: Sampathpaya, Battaramulla, Colombo | Tel: +94 11 286 6631
Permit Requirement: Camping in Forest Reserves (e.g., Knuckles, Sinharaja, Kanneliya) REQUIRES prior written approval and permit issuance from the Forest Dept.
Prohibited Actions: Open campfires without designated fire rings, single-use plastic bottles, and unguided off-trail trekking.""",

        "doc_94_department_of_wildlife_conservation_dwc.txt": """Authority: Department of Wildlife Conservation (DWC)
Headquarters: No. 811A, Jayanthipura Road, Battaramulla | Tel: +94 11 288 8585
eService Portal: dwc.lankagate.gov.lk
Permit Service: Mandatory online or head-office booking for DWC Wildlife Circuit Bungalows and designated campsite pitches inside Yala, Wilpattu, Horton Plains, and Udawalawe.""",

        "doc_95_horton_plains_world_end_permits.txt": """Attraction: Horton Plains National Park & World's End
Managing Body: Department of Wildlife Conservation
Entrance Fee (Foreign Adult): USD 25 + Vehicle Permit + VAT (Approx LKR 9,500 total per person)
Opening Hours: 6:00 AM to 4:00 PM (Best to enter before 9:00 AM to avoid mist obscuring World's End cliff).
Strict Prohibition: Plastic bags, single-use water wrappers, and disposable plastic bottles are confiscated at the entrance gate.""",

        "doc_96_adam_peak_sanctuary_regulations.txt": """Attraction: Peak Wilderness Sanctuary (Adam's Peak / Sri Pada)
Managing Body: Department of Wildlife Conservation & Divisional Secretariat Nallathanniya
Permit Rule: Public hiking via Hatton/Nallathanniya trail is free during peak season (Dec to May). Off-season trekking (June to Nov) requires informing the Nallathanniya Police Station before ascending.""",

        "doc_97_archaeology_department_site_permits.txt": """Authority: Department of Archaeology Sri Lanka
Headquarters: Sir Marcus Fernando Mawatha, Colombo 07 | Tel: +94 11 269 2840
Permit Rule: Special commercial photography, filming, or scientific research at non-ticketed archaeological ruins (e.g., Ritigala, Pidurangala, Nalanda Gedige) requires advance written approval.""",

        "doc_98_srilanka_tourism_development_authority.txt": """Authority: Sri Lanka Tourism Development Authority (SLTDA)
Head Office: No. 80, Galle Road, Colombo 03 | Tel: +94 11 242 6900
Hotline: 1912 (24/7 Tourist Assistance)
Role: Formal registration verification for hotels, tour drivers, travel agencies, and official tourist guides.""",

        "doc_99_immigration_and_emigration_department.txt": """Authority: Department of Immigration and Emigration Sri Lanka
Headquarters: Suhurupaya, Battaramulla, Sri Jayawardenepura Kotte | Tel: +94 11 210 1500
Official ETA Portal: eta.gov.lk
Services: 30-day ETA tourist visa extensions (up to 6 months), visa status queries, and passport loss documentation."""
    }
    
    for filename, content in docs.items():
        filepath = os.path.join(data_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created {filepath}")
        
if __name__ == "__main__":
    generate_documents()
