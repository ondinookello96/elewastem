"""
ElewaSTEM Vector Science Diagram Generator
Provides lightweight, responsive SVG diagrams and flowcharts for African STEM learners with offline caching.
"""

from typing import Dict, Any, Optional

DIAGRAMS = {
    "photosynthesis": {
        "title_sw": "Mchoro wa Usanisinuru (Photosynthesis Process)",
        "title_en": "Photosynthesis Flowchart Diagram",
        "topic_id": "photosynthesis",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 380" class="w-full h-auto rounded-2xl shadow-inner bg-gradient-to-b from-sky-100 via-emerald-50 to-amber-50 font-sans">
  <!-- Sun & Solar Radiation -->
  <circle cx="90" cy="80" r="45" fill="#FBBF24" stroke="#F59E0B" stroke-width="4"/>
  <path d="M90 20 L90 5 M90 140 L90 155 M30 80 L15 80 M150 80 L165 80 M45 35 L35 25 M135 125 L145 135 M45 125 L35 135 M135 35 L145 25" stroke="#F59E0B" stroke-width="4" stroke-linecap="round"/>
  <text x="90" y="85" font-size="12" font-weight="bold" fill="#78350F" text-anchor="middle">☀️ Mwangaza</text>
  <text x="90" y="100" font-size="10" fill="#92400E" text-anchor="middle">wa Jua (Light)</text>

  <!-- Sun Rays Arrow -->
  <path d="M140 100 Q 220 120 280 160" fill="none" stroke="#F59E0B" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arrow-sun)"/>
  
  <!-- Plant Stem & Main Leaf -->
  <path d="M320 380 C 320 280 340 240 360 200" fill="none" stroke="#047857" stroke-width="12" stroke-linecap="round"/>
  <!-- Big Beautiful Leaf -->
  <path d="M350 210 C 220 120 180 220 350 270 C 500 240 480 130 350 210 Z" fill="#10B981" stroke="#047857" stroke-width="4"/>
  <!-- Leaf Veins -->
  <path d="M250 190 C 300 210 350 220 430 200" fill="none" stroke="#065F46" stroke-width="3"/>
  <path d="M300 200 L 290 170 M 340 210 L 340 160 M 380 215 L 390 175 M 320 215 L 310 245 M 360 215 L 370 250" fill="none" stroke="#065F46" stroke-width="2"/>
  <text x="350" y="195" font-size="13" font-weight="900" fill="#064E3B" text-anchor="middle">KLOROFILI (Chlorophyll)</text>

  <!-- Input 1: CO2 from Air -->
  <rect x="30" y="210" width="130" height="42" rx="8" fill="#E0E7FF" stroke="#6366F1" stroke-width="2"/>
  <text x="95" y="228" font-size="11" font-weight="bold" fill="#312E81" text-anchor="middle">Gesi ya Kaboni (CO₂)</text>
  <text x="95" y="243" font-size="9" fill="#4338CA" text-anchor="middle">Inaingia kupitia Stomata ➔</text>
  <path d="M165 230 L 220 230" fill="none" stroke="#6366F1" stroke-width="3" marker-end="url(#arrow-blue)"/>

  <!-- Input 2: Water (H2O) from Roots -->
  <rect x="250" y="325" width="140" height="42" rx="8" fill="#DBEAFE" stroke="#3B82F6" stroke-width="2"/>
  <text x="320" y="343" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle">Maji (H₂O) & Madini</text>
  <text x="320" y="357" font-size="9" fill="#1D4ED8" text-anchor="middle">Kutoka Mizizini ⬆️</text>

  <!-- Output 1: Oxygen (O2) Released -->
  <rect x="470" y="120" width="145" height="45" rx="8" fill="#D1FAE5" stroke="#10B981" stroke-width="2"/>
  <text x="542" y="138" font-size="11" font-weight="bold" fill="#064E3B" text-anchor="middle">💨 Oksijeni Safi (O₂)</text>
  <text x="542" y="153" font-size="9" fill="#047857" text-anchor="middle">Inatoka nje kwa viumbe</text>
  <path d="M420 160 L 465 145" fill="none" stroke="#10B981" stroke-width="3" marker-end="url(#arrow-green)"/>

  <!-- Output 2: Glucose / Food -->
  <rect x="470" y="240" width="145" height="45" rx="8" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
  <text x="542" y="258" font-size="11" font-weight="bold" fill="#78350F" text-anchor="middle">🍬 Sukari / Glukosi</text>
  <text x="542" y="273" font-size="9" fill="#92400E" text-anchor="middle">Chakula cha kukuza mmea</text>
  <path d="M420 240 L 465 255" fill="none" stroke="#F59E0B" stroke-width="3" marker-end="url(#arrow-yellow)"/>

  <!-- Equation Banner -->
  <rect x="120" y="15" width="400" height="30" rx="15" fill="#065F46" opacity="0.9"/>
  <text x="320" y="35" font-size="11" font-weight="bold" fill="#ECFDF5" text-anchor="middle">6CO₂ (Hewa) + 6H₂O (Maji) + Jua ➔ Glukosi + 6O₂ (Oksijeni)</text>
</svg>"""
    },
    "aquatic_biology_kisumu": {
        "title_sw": "Mchoro wa Yavuyavu za Samaki Ngege (Fish Gill Respiration in Lake Victoria)",
        "title_en": "Fish Gill Aquatic Respiration Diagram",
        "topic_id": "aquatic_biology_kisumu",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 380" class="w-full h-auto rounded-2xl shadow-inner bg-gradient-to-b from-cyan-100 via-blue-50 to-teal-100 font-sans">
  <!-- Lake Victoria Waves -->
  <path d="M0 50 Q 80 30 160 50 T 320 50 T 480 50 T 640 50 L 640 0 L 0 0 Z" fill="#BAE6FD" opacity="0.5"/>
  <text x="320" y="30" font-size="12" font-weight="bold" fill="#0369A1" text-anchor="middle">Ziwa Victoria (Kisumu) • Upumuaji wa Samaki Ngege (Tilapia)</text>

  <!-- Fish Body Outline -->
  <path d="M80 190 C 120 100 350 80 480 190 C 350 300 120 280 80 190 Z" fill="#93C5FD" stroke="#1D4ED8" stroke-width="4"/>
  <!-- Fish Tail -->
  <path d="M480 190 L 580 120 L 550 190 L 580 260 Z" fill="#60A5FA" stroke="#1D4ED8" stroke-width="3"/>
  <!-- Fish Eye -->
  <circle cx="140" cy="160" r="14" fill="#FFFFFF" stroke="#1E3A8A" stroke-width="2"/>
  <circle cx="140" cy="160" r="7" fill="#0F172A"/>

  <!-- Open Mouth with Water Inflow -->
  <path d="M80 180 Q 60 190 80 200" fill="none" stroke="#1D4ED8" stroke-width="5"/>
  <rect x="15" y="130" width="130" height="40" rx="8" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <text x="80" y="148" font-size="10" font-weight="bold" fill="#1E40AF" text-anchor="middle">1. Maji Yanaingia</text>
  <text x="80" y="161" font-size="8.5" fill="#1D4ED8" text-anchor="middle">Maji yenye Oksijeni ➔</text>
  <!-- Inflow Arrows -->
  <path d="M30 190 L 85 190" fill="none" stroke="#2563EB" stroke-width="4" stroke-linecap="round"/>

  <!-- Operculum / Gill Filaments -->
  <path d="M220 130 C 260 160 260 220 220 250" fill="none" stroke="#DC2626" stroke-width="6" stroke-linecap="round"/>
  <!-- Red Gill Arches -->
  <path d="M230 140 C 270 165 270 215 230 240 M 240 150 C 280 170 280 210 240 230" fill="none" stroke="#EF4444" stroke-width="4" stroke-linecap="round"/>
  
  <!-- Gill Label Box -->
  <rect x="180" y="70" width="160" height="45" rx="8" fill="#FEE2E2" stroke="#EF4444" stroke-width="2"/>
  <text x="260" y="88" font-size="11" font-weight="bold" fill="#991B1B" text-anchor="middle">Yavuyavu / Mashavu (Gills)</text>
  <text x="260" y="103" font-size="8.5" fill="#B91C1C" text-anchor="middle">Mishipa ya damu inavuta O₂</text>
  <line x1="260" y1="115" x2="250" y2="145" stroke="#EF4444" stroke-width="2" stroke-dasharray="3,3"/>

  <!-- Outflow of Water + CO2 -->
  <rect x="190" y="280" width="160" height="45" rx="8" fill="#E0F2FE" stroke="#0284C7" stroke-width="2"/>
  <text x="270" y="298" font-size="11" font-weight="bold" fill="#075985" text-anchor="middle">2. Maji Yanaondoka</text>
  <text x="270" y="313" font-size="8.5" fill="#0369A1" text-anchor="middle">Hewa chafu (CO₂) inatoka nje</text>
  <path d="M255 245 L 270 275" fill="none" stroke="#0284C7" stroke-width="3"/>

  <!-- Bloodstream Oxygenation Info -->
  <rect x="390" y="290" width="220" height="65" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="2" opacity="0.95"/>
  <text x="500" y="310" font-size="11" font-weight="bold" fill="#065F46" text-anchor="middle">Mzunguko wa Damu (Bloodstream)</text>
  <text x="500" y="327" font-size="9" fill="#047857" text-anchor="middle">🔴 Damu safi yenye O₂ inaenda mwilini</text>
  <text x="500" y="342" font-size="9" fill="#047857" text-anchor="middle">🔵 Damu yenye CO₂ inatupwa majini</text>
</svg>"""
    },
    "electricity_circuits": {
        "title_sw": "Mchoro wa Saketi ya Umeme (Electric Circuit Diagram)",
        "title_en": "Closed Electrical Circuit Diagram",
        "topic_id": "electricity_circuits",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 380" class="w-full h-auto rounded-2xl shadow-inner bg-slate-900 font-sans">
  <text x="320" y="30" font-size="13" font-weight="bold" fill="#38BDF8" text-anchor="middle">Saketi Kamili ya Umeme (Closed Electrical Circuit - 12V Taa ya Kuvulia)</text>

  <!-- Continuous Copper Wire Rectangle -->
  <rect x="90" y="60" width="460" height="240" rx="20" fill="none" stroke="#F59E0B" stroke-width="6"/>

  <!-- Battery Source (Left) -->
  <rect x="60" y="140" width="60" height="90" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="3"/>
  <rect x="75" y="130" width="30" height="10" rx="3" fill="#EF4444"/>
  <text x="90" y="175" font-size="13" font-weight="bold" fill="#EF4444" text-anchor="middle">+</text>
  <text x="90" y="195" font-size="11" font-weight="bold" fill="#F8FAFC" text-anchor="middle">12V</text>
  <text x="90" y="215" font-size="13" font-weight="bold" fill="#94A3B8" text-anchor="middle">-</text>
  <text x="90" y="250" font-size="10" font-weight="bold" fill="#38BDF8" text-anchor="middle">Betri (Source)</text>

  <!-- Switch (Top) -->
  <circle cx="280" cy="60" r="7" fill="#F59E0B"/>
  <circle cx="360" cy="60" r="7" fill="#F59E0B"/>
  <!-- Closed Switch Blade -->
  <line x1="280" y1="60" x2="360" y2="60" stroke="#10B981" stroke-width="6" stroke-linecap="round"/>
  <text x="320" y="48" font-size="10" font-weight="bold" fill="#10B981" text-anchor="middle">Swichi Imefungwa (Closed Switch)</text>

  <!-- Glowing LED Light Bulb (Right) -->
  <!-- Glowing aura -->
  <circle cx="550" cy="180" r="50" fill="#FDE047" opacity="0.25"/>
  <circle cx="550" cy="180" r="30" fill="#FEF08A" stroke="#EAB308" stroke-width="3"/>
  <!-- Filament -->
  <path d="M540 190 L 545 170 L 555 170 L 560 190" fill="none" stroke="#CA8A04" stroke-width="3"/>
  <!-- Rays -->
  <line x1="550" y1="115" x2="550" y2="135" stroke="#FDE047" stroke-width="3" stroke-linecap="round"/>
  <line x1="595" y1="135" x2="580" y2="150" stroke="#FDE047" stroke-width="3" stroke-linecap="round"/>
  <line x1="615" y1="180" x2="595" y2="180" stroke="#FDE047" stroke-width="3" stroke-linecap="round"/>
  <line x1="595" y1="225" x2="580" y2="210" stroke="#FDE047" stroke-width="3" stroke-linecap="round"/>
  <text x="550" y="250" font-size="10" font-weight="bold" fill="#FEF08A" text-anchor="middle">Taa ya LED (Load)</text>

  <!-- Current Flow Arrows (Bottom & Sides) -->
  <text x="320" y="290" font-size="10" font-weight="bold" fill="#F59E0B" text-anchor="middle">Mkondo wa Umeme Unatiririka (Current Flow) ➔</text>

  <!-- Explanation Banner -->
  <rect x="120" y="320" width="400" height="35" rx="8" fill="#1E293B" stroke="#475569" stroke-width="1"/>
  <text x="320" y="342" font-size="10" fill="#94A3B8" text-anchor="middle">Waya ukikatika mahali popote, saketi inakatika na taa inazimika mara moja!</text>
</svg>"""
    },
    "fractions_math": {
        "title_sw": "Mchoro wa Sehemu za Hesabu (Fractions: 1/4, 1/2, 3/4 & 1 Whole)",
        "title_en": "Fractions Visual Slices Diagram",
        "topic_id": "fractions_math",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 380" class="w-full h-auto rounded-2xl shadow-inner bg-gradient-to-b from-amber-50 to-orange-100 font-sans">
  <text x="320" y="30" font-size="13" font-weight="bold" fill="#78350F" text-anchor="middle">Sehemu za Nambari: Mgawanyo Sawa wa Chapati / Pawpaw</text>

  <!-- Big Round Chapati divided into 4 slices -->
  <g transform="translate(190, 190)">
    <!-- Slice 1 (Top-Left) -->
    <path d="M 0 0 L 0 -110 A 110 110 0 0 0 -110 0 Z" fill="#F59E0B" stroke="#78350F" stroke-width="3"/>
    <text x="-50" y="-45" font-size="16" font-weight="900" fill="#FFFFFF" text-anchor="middle">¼</text>
    <text x="-50" y="-25" font-size="9" font-weight="bold" fill="#78350F" text-anchor="middle">Robo</text>

    <!-- Slice 2 (Top-Right) -->
    <path d="M 0 0 L 110 0 A 110 110 0 0 0 0 -110 Z" fill="#FBBF24" stroke="#78350F" stroke-width="3"/>
    <text x="50" y="-45" font-size="16" font-weight="900" fill="#FFFFFF" text-anchor="middle">¼</text>
    <text x="50" y="-25" font-size="9" font-weight="bold" fill="#78350F" text-anchor="middle">Robo</text>

    <!-- Slice 3 (Bottom-Right) -->
    <path d="M 0 0 L 0 110 A 110 110 0 0 0 110 0 Z" fill="#FCD34D" stroke="#78350F" stroke-width="3"/>
    <text x="50" y="55" font-size="16" font-weight="900" fill="#FFFFFF" text-anchor="middle">¼</text>
    <text x="50" y="75" font-size="9" font-weight="bold" fill="#78350F" text-anchor="middle">Robo</text>

    <!-- Slice 4 (Bottom-Left) -->
    <path d="M 0 0 L -110 0 A 110 110 0 0 0 0 110 Z" fill="#FDE68A" stroke="#78350F" stroke-width="3"/>
    <text x="-50" y="55" font-size="16" font-weight="900" fill="#FFFFFF" text-anchor="middle">¼</text>
    <text x="-50" y="75" font-size="9" font-weight="bold" fill="#78350F" text-anchor="middle">Robo</text>
  </g>

  <!-- Math Legend on Right -->
  <rect x="360" y="75" width="240" height="240" rx="15" fill="#FFFFFF" stroke="#F59E0B" stroke-width="2"/>
  <text x="480" y="105" font-size="12" font-weight="bold" fill="#92400E" text-anchor="middle">Kanuni za Sehemu (Rules):</text>
  
  <text x="380" y="140" font-size="11" font-weight="bold" fill="#B45309">• ¼ = Robo Moja (One Quarter)</text>
  <text x="380" y="175" font-size="11" font-weight="bold" fill="#B45309">• ¼ + ¼ = ²⁄₄ = ½ (Nusu / Half)</text>
  <text x="380" y="210" font-size="11" font-weight="bold" fill="#B45309">• ¼ + ¼ + ¼ = ¾ (Robo Tatu)</text>
  <text x="380" y="245" font-size="11" font-weight="bold" fill="#B45309">• ⁴⁄₄ = 1 Kitu Kizima (Whole)</text>
  <text x="480" y="285" font-size="9" fill="#78350F" text-anchor="middle">Jumla ya vipande 4 sawa = 1 zima</text>
</svg>"""
    },
    "chemistry_reactions": {
        "title_sw": "Mchoro wa Kemia: Mmenyuko wa Asidi na Besi (Acid-Base Reaction)",
        "title_en": "Chemistry Acid-Base Neutralization Diagram",
        "topic_id": "chemistry_reactions",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 380" class="w-full h-auto rounded-2xl shadow-inner bg-gradient-to-b from-purple-50 via-pink-50 to-indigo-50 font-sans">
  <text x="320" y="30" font-size="13" font-weight="bold" fill="#581C87" text-anchor="middle">Kemia: Mmenyuko wa Asidi (Ndimu/Siki) na Besi (Baking Soda / Majivu)</text>

  <!-- Reactant 1: Acid Flask (Left) -->
  <path d="M120 120 L120 160 L70 260 C60 280 80 290 100 290 L180 290 C200 290 220 280 210 260 L160 160 L160 120 Z" fill="#FCE7F3" stroke="#DB2777" stroke-width="3"/>
  <rect x="85" y="220" width="110" height="65" fill="#F472B6" opacity="0.6"/>
  <text x="140" y="255" font-size="11" font-weight="bold" fill="#831843" text-anchor="middle">🧪 ASIDI (Acid)</text>
  <text x="140" y="272" font-size="9" fill="#9D174D" text-anchor="middle">Juisi ya Ndimu / Siki</text>

  <!-- Plus Sign -->
  <text x="245" y="220" font-size="30" font-weight="bold" fill="#7C3AED" text-anchor="middle">+</text>

  <!-- Reactant 2: Base Powder (Middle) -->
  <path d="M300 220 Q350 170 400 220 L410 290 L290 290 Z" fill="#E0E7FF" stroke="#4F46E5" stroke-width="3"/>
  <text x="350" y="255" font-size="11" font-weight="bold" fill="#312E81" text-anchor="middle">🥄 BESI (Base)</text>
  <text x="350" y="272" font-size="9" fill="#3730A3" text-anchor="middle">Baking Soda / Majivu</text>

  <!-- Arrow to Result -->
  <path d="M425 210 L475 210" fill="none" stroke="#7C3AED" stroke-width="4" stroke-linecap="round"/>
  <text x="450" y="195" font-size="10" font-weight="bold" fill="#7C3AED" text-anchor="middle">Mmenyuko ➔</text>

  <!-- Result Box (Right): CO2 Bubbles + Salt Water -->
  <rect x="490" y="130" width="135" height="155" rx="12" fill="#FFFFFF" stroke="#059669" stroke-width="2.5"/>
  <circle cx="530" cy="180" r="10" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5"/>
  <circle cx="560" cy="160" r="14" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5"/>
  <circle cx="585" cy="190" r="8" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5"/>
  <text x="557" y="165" font-size="10" font-weight="bold" fill="#0284C7" text-anchor="middle">CO₂</text>
  
  <text x="557" y="225" font-size="11" font-weight="bold" fill="#065F46" text-anchor="middle">✨ MATOKEO:</text>
  <text x="557" y="242" font-size="9" fill="#047857" text-anchor="middle">1. Gesi ya Viputo (CO₂)</text>
  <text x="557" y="257" font-size="9" fill="#047857" text-anchor="middle">2. Maji & Chumvi Safi</text>

  <!-- Bottom Principle Rule -->
  <rect x="80" y="320" width="480" height="35" rx="10" fill="#4C1D95" opacity="0.95"/>
  <text x="320" y="342" font-size="11" font-weight="bold" fill="#F5F3FF" text-anchor="middle">Asidi + Besi ➔ Chumvi (Salt) + Maji (H₂O) + Gesi ya Kaboni (CO₂)</text>
</svg>"""
    },
    "computer_algorithms": {
        "title_sw": "Mchoro wa Sayansi ya Kompyuta & Algoriti (Computer Algorithms & Logic)",
        "title_en": "Computer Science Algorithm Flowchart",
        "topic_id": "computer_algorithms",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 380" class="w-full h-auto rounded-2xl shadow-inner bg-slate-950 font-sans">
  <text x="320" y="30" font-size="13" font-weight="bold" fill="#38BDF8" text-anchor="middle">Sayansi ya Kompyuta: Algoriti ya Maamuzi (If-Else Decision Logic)</text>

  <!-- Start Node -->
  <rect x="240" y="55" width="160" height="36" rx="18" fill="#10B981" stroke="#059669" stroke-width="2"/>
  <text x="320" y="77" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">🏁 MWANZO (Start)</text>

  <!-- Arrow down -->
  <line x1="320" y1="91" x2="320" y2="120" stroke="#38BDF8" stroke-width="3"/>

  <!-- Decision Diamond: Is Soil Dry? -->
  <polygon points="320,120 420,170 320,220 220,170" fill="#1E293B" stroke="#F59E0B" stroke-width="3"/>
  <text x="320" y="165" font-size="10" font-weight="bold" fill="#FDE047" text-anchor="middle">Je, Udongo Umekauka?</text>
  <text x="320" y="180" font-size="9" fill="#CBD5E1" text-anchor="middle">(Is Soil Dry?)</text>

  <!-- Branch YES (Right) -->
  <line x1="420" y1="170" x2="490" y2="170" stroke="#10B981" stroke-width="3"/>
  <text x="450" y="160" font-size="10" font-weight="bold" fill="#10B981">NDIYO (True)</text>
  <rect x="490" y="145" width="130" height="50" rx="8" fill="#064E3B" stroke="#10B981" stroke-width="2"/>
  <text x="555" y="167" font-size="10" font-weight="bold" fill="#ECFDF5" text-anchor="middle">💧 Fungua Maji</text>
  <text x="555" y="182" font-size="8.5" fill="#A7F3D0" text-anchor="middle">(Turn On Pump)</text>

  <!-- Branch NO (Left) -->
  <line x1="220" y1="170" x2="150" y2="170" stroke="#EF4444" stroke-width="3"/>
  <text x="165" y="160" font-size="10" font-weight="bold" fill="#EF4444">HAPANA (False)</text>
  <rect x="20" y="145" width="130" height="50" rx="8" fill="#450A0A" stroke="#EF4444" stroke-width="2"/>
  <text x="85" y="167" font-size="10" font-weight="bold" fill="#FEF2F2" text-anchor="middle">🛑 Zima Maji</text>
  <text x="85" y="182" font-size="8.5" fill="#FECACA" text-anchor="middle">(Keep Pump Off)</text>

  <!-- Convergence to Loop/End -->
  <path d="M555 195 L555 260 L320 260" fill="none" stroke="#38BDF8" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M85 195 L85 260 L320 260" fill="none" stroke="#38BDF8" stroke-width="2" stroke-dasharray="4,4"/>

  <!-- Process Node: Sleep & Repeat -->
  <rect x="220" y="285" width="200" height="40" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="2"/>
  <text x="320" y="303" font-size="10" font-weight="bold" fill="#38BDF8" text-anchor="middle">⏱️ Subiri Dakika 10 (Loop)</text>
  <text x="320" y="317" font-size="8.5" fill="#94A3B8" text-anchor="middle">Rudia hatua ya ukaguzi</text>

  <!-- Bottom Code Concept -->
  <text x="320" y="355" font-size="10" font-weight="bold" fill="#A855F7" text-anchor="middle">Hivi ndivyo kompyuta, simu, na roboti hufanya maamuzi (Algorithms)!</text>
</svg>"""
    },
    "algebra_math": {
        "title_sw": "Mchoro wa Aljebra: Kusawazisha Mlinganyo (x + 3 = 10 ➔ x = 7)",
        "title_en": "Algebra Balance Scale Diagram",
        "topic_id": "algebra_math",
        "svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 380" class="w-full h-auto rounded-2xl shadow-inner bg-gradient-to-b from-indigo-900 to-slate-950 font-sans">
  <text x="320" y="30" font-size="14" font-weight="bold" fill="#38BDF8" text-anchor="middle">Aljebra: Mizani ya Mlinganyo (x + 3 = 10 ➔ x = 7)</text>

  <!-- Balance Fulcrum -->
  <polygon points="320,180 290,270 350,270" fill="#64748B" stroke="#94A3B8" stroke-width="2"/>
  <rect x="250" y="270" width="140" height="20" rx="6" fill="#334155"/>

  <!-- Balance Beam -->
  <rect x="100" y="170" width="440" height="14" rx="4" fill="#F59E0B" stroke="#B45309" stroke-width="2"/>
  <circle cx="320" cy="177" r="8" fill="#EF4444"/>

  <!-- Left Pan (x + 3) -->
  <line x1="160" y1="184" x2="160" y2="230" stroke="#CBD5E1" stroke-width="2"/>
  <rect x="100" y="230" width="120" height="12" rx="4" fill="#94A3B8"/>
  <!-- Box for x -->
  <rect x="110" y="190" width="40" height="40" rx="8" fill="#8B5CF6" stroke="#C4B5FD" stroke-width="2"/>
  <text x="130" y="215" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">x</text>
  <!-- 3 weights of +1 -->
  <circle cx="165" cy="210" r="10" fill="#10B981" stroke="#ECFDF5" stroke-width="1.5"/>
  <text x="165" y="214" font-size="9" font-weight="bold" fill="#FFFFFF" text-anchor="middle">+1</text>
  <circle cx="190" cy="210" r="10" fill="#10B981" stroke="#ECFDF5" stroke-width="1.5"/>
  <text x="190" y="214" font-size="9" font-weight="bold" fill="#FFFFFF" text-anchor="middle">+1</text>
  <circle cx="178" cy="190" r="10" fill="#10B981" stroke="#ECFDF5" stroke-width="1.5"/>
  <text x="178" y="194" font-size="9" font-weight="bold" fill="#FFFFFF" text-anchor="middle">+1</text>

  <text x="160" y="265" font-size="12" font-weight="bold" fill="#A78BFA" text-anchor="middle">Upande wa Kushoto: x + 3</text>

  <!-- Center Equals Sign -->
  <text x="320" y="140" font-size="28" font-weight="bold" fill="#FDE047" text-anchor="middle">=</text>

  <!-- Right Pan (10 weights) -->
  <line x1="480" y1="184" x2="480" y2="230" stroke="#CBD5E1" stroke-width="2"/>
  <rect x="420" y="230" width="120" height="12" rx="4" fill="#94A3B8"/>
  <g transform="translate(435, 175)">
    <circle cx="15" cy="40" r="9" fill="#10B981"/>
    <circle cx="35" cy="40" r="9" fill="#10B981"/>
    <circle cx="55" cy="40" r="9" fill="#10B981"/>
    <circle cx="75" cy="40" r="9" fill="#10B981"/>
    <circle cx="25" cy="22" r="9" fill="#10B981"/>
    <circle cx="45" cy="22" r="9" fill="#10B981"/>
    <circle cx="65" cy="22" r="9" fill="#10B981"/>
    <circle cx="35" cy="4" r="9" fill="#10B981"/>
    <circle cx="55" cy="4" r="9" fill="#10B981"/>
    <circle cx="45" cy="-12" r="9" fill="#10B981"/>
  </g>
  <text x="480" y="265" font-size="12" font-weight="bold" fill="#34D399" text-anchor="middle">Upande wa Kulia: 10</text>

  <!-- Bottom Equation Box -->
  <rect x="120" y="300" width="400" height="55" rx="12" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
  <text x="320" y="322" font-size="11" font-weight="bold" fill="#E2E8F0" text-anchor="middle">Hatua: Ondoa 3 pande zote mbili ➔ x = 10 - 3</text>
  <text x="320" y="342" font-size="13" font-weight="900" fill="#FACC15" text-anchor="middle">JIBU: x = 7 (Mizani Imetulia Sawasawa!)</text>
</svg>"""
    }
}


def get_diagram_for_topic(query_or_id: str) -> Optional[Dict[str, Any]]:
    """Returns matching responsive SVG science diagram."""
    q = query_or_id.lower()
    if any(k in q for k in ["algebra", "aljebra", "equation", "mlinganyo", "variable", "kigeuzi", "solve for x"]):
        return DIAGRAMS["algebra_math"]
    elif any(k in q for k in ["fraction", "sehemu", "divide", "gawanya", "chapati", "proportion", "math", "hisabati"]):
        return DIAGRAMS["fractions_math"]
    elif any(k in q for k in ["chem", "kemia", "acid", "asidi", "base", "besi", "reaction", "siki", "soda", "lemon", "chumvi"]):
        return DIAGRAMS["chemistry_reactions"]
    elif any(k in q for k in ["comput", "code", "coding", "program", "algorithm", "algoriti", "software", "tech", "teknolojia", "logic", "binary"]):
        return DIAGRAMS["computer_algorithms"]
    elif any(k in q for k in ["electr", "circuit", "umeme", "saketi", "wire", "battery", "betri", "taa", "physics", "fizikia"]):
        return DIAGRAMS["electricity_circuits"]
    elif any(k in q for k in ["fish", "samaki", "ngege", "gill", "shavu", "ziwa", "lake", "respiration", "aquatic"]):
        return DIAGRAMS["aquatic_biology_kisumu"]
    elif any(k in q for k in ["photo", "mmea", "plant", "leaf", "jani", "usanisinuru", "sukuma", "bio", "botany"]):
        return DIAGRAMS["photosynthesis"]
    return None
