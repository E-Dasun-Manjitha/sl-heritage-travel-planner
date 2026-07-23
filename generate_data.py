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
- Cultural Respect: Never pose for photos touching or climbing sacred monuments or Buddha statues. Avoid wearing clothes with religious symbols."""
    }
    
    for filename, content in docs.items():
        filepath = os.path.join(data_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created {filepath}")
        
if __name__ == "__main__":
    generate_documents()
