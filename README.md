# Dante's CDDA Mod Collection

Personal mod collection for **Cataclysm: Dark Days Ahead**, created by Me.

All mods work with the latest experimental builds of CDDA.

---

## 📦 Active Mods

### 1. Antigravity Market
**ID:** `antigravity_market`

Adds a portable shopping terminal that lets you buy items (food, weapons, ammo) using **FMCNotes** (Free Merchant Certified Notes). Items are delivered instantly.

- Files: `items.json`, `eocs.json`
- Dependencies: `dda`

### 2. Dante's Gadgets
**ID:** `dante_gadgets`

Collection of high-tech portable devices:
- **Viltrumite Nanite Swarm** — nanite swarm that reconfigures into any tool (UPS-powered)
- **Quantum Teleport Watch** — smartwatch that teleports across the overmap (UPS-powered)
- **Atomic Smartphone** — smartphone with infinite atomic battery, music player, flashlight, and power link

- Files: `items.json`, `eocs.json`
- Dependencies: `dda`

### 3. Dante's Pocket Dimension
**ID:** `pocket_dimension`

Adds a **persistent compact dimension** (24×24) — a fully walled high-tech workshop, accessed via a dimensional warp stone. All area outside the workshop is filled with solid walls, preventing external exploration. Includes warp stone, dimensional storage crystal, and return portal.

- Files: `items.json`, `eocs.json`, `furniture.json`, `region_settings.json`, `overmap_terrain.json`, `overmap_location.json`, `overmap_special.json`, `mapgen/`
- Dependencies: `dda`

### 4. Dante's Starter Gear
**ID:** `dante_starter_gear`

**Central mod of the collection.** Spawns a pre-loaded briefcase at game start containing all items from the other mods: portable gadgets, antigravity terminal, dimensional stone, and storage crystal.

- Files: `items.json`, `itemgroups.json`, `eocs.json`
- Dependencies: `dda`, `dante_gadgets`, `antigravity_market`, `pocket_dimension`

### 5. Viltrumite Heritage
**ID:** `viltrumite_dna`

Adds the **Viltrumite** genetic trait (Invincible), granting super-strength, flight, and adaptive biology that grows stronger after taking damage. Includes Viltrumite martial art and adaptive evolution system.

- Files: `all_data.json`
- Dependencies: `dda`, `dante_gadgets`

### 6. Exodii Heritage
**ID:** `exodii_heritage`

Adds the **Exodii Crash Landing** scenario — start as an Exodii dimensional scout, a full-conversion cyborg from another world who suffered a portal generator failure and crash-landed in New England. Includes scout frame with integrated armor, pre-installed bionics, and Exodii equipment.

- Files: `scenarios.json`, `professions.json`, `mutations.json`, `eocs.json`, `overlay_order.json`, `exodii_scout_frame.png`, `tile_config.json`
- Dependencies: `dda`

### 7. Arcane Pocket Dimension
**ID:** `arcane_pocket`

Adds a personal **24×24 arcane pocket dimension** accessible via a magical translocation spell (requires Magiclysm). A persistent instanced library dimension with bookshelves full of Magiclysm spellbooks, reading tables, statues, and a return portal.

- Files: `items.json`, `spells.json`, `eocs.json`, `furniture.json`, `itemgroups.json`, `region_settings.json`, `overmap_terrain.json`, `overmap_location.json`, `overmap_special.json`, `mapgen/`
- Dependencies: `dda`, `magiclysm`

### 8. Genius Mutation
**ID:** `genius`

Adds a **hyper-learning mutation line** (Spark → Bright → Brilliant → Transcendent) with instant activated powers: conjure light, food, and blades from thought. The Transcendent menu materializes components and building supplies, summons thought servants and a thought toolbox, and opens a persistent **Mind Palace** dimension to build in.

- Files: `modinfo.json`, `genius.json`, `genius_powers.json`, `genius_dimension.json`, `genius_servants.json`
- Dependencies: `dda`

### 9. Dante Skyship
**ID:** `dante_skyship`

A player-piloted **skyship HQ**: plot a course on the helm console and jump the whole ship — crew, vehicles and all — across the overmap, landing in open fields. Starts with the Skyship Captain scenario.

- Files: `modinfo.json`, `skyship_terrain.json`, `skyship_mapgen.json`, `skyship_eoc.json`, `skyship_talk.json`, `skyship_scenario.json`
- Dependencies: `dda`

### 10. Dan's Weapons
**ID:** `dans_weapons`

Adds new firearms with custom sprites: **AK-102 carbine**, **G36 assault rifle**, **Enfield EM-2** and **FG-42 paratrooper rifle** (converted to 5.56 STANAG), each with wielded overlay sprites.

- Files: `genius_ak102.json`, `genius_g36.json`, `dans_em2.json`, `genius_fg42.json`, `tile_config.json`, sprites
- Dependencies: `dda`

---

## 📦 Archived Mods

### Atom Eve Powers
**ID:** `atom_eve_powers`

Superpowers inspired by **Atom Eve** (Invincible): energy manipulation, flight, regeneration, and enhanced abilities. **Not actively maintained.**

- Location: `archive/atom_eve_powers/`
- Dependencies: `dda`

---

## 🔗 Mod Dependencies

```text
dda (base game)
├── dante_gadgets
│   └── viltrumite_dna
├── antigravity_market
├── pocket_dimension
├── exodii_heritage
├── arcane_pocket (requires magiclysm)
├── genius
├── dans_weapons
└── dante_skyship

dante_starter_gear (central mod)
├── dante_gadgets
├── antigravity_market
└── pocket_dimension
```

> **Note:** Enable `dante_starter_gear` to start with all collection items — dependencies will be loaded automatically.

---

## 🚀 How to Use

1. Copy the desired mod folder(s) to your CDDA `data/mods/` directory
2. Enable them in the launcher or mod menu when creating a new world
3. For **Starter Gear**: create a new game with the mod active — the briefcase and items will be in the evac shelter

---

## 🛠️ Author

- **Dante** — [Dantesousa](https://github.com/Dantesousa)
