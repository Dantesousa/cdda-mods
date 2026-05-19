# Dante's CDDA Mod Collection

Personal mod collection for **Cataclysm: Dark Days Ahead**, created by Dante.

All mods work with the latest stable version of CDDA.

---

## 📦 Mods

### 1. Antigravity Market
**ID:** `antigravity_market`

Adds a portable shopping terminal that lets you buy items (food, weapons, ammo) using **FMCNotes** (Free Merchant Certified Notes). Items are delivered instantly.

- Files: `items.json`, `eocs.json`
- Dependencies: `dda`

### 2. Atom Eve Powers
**ID:** `atom_eve_powers`

Adds superpowers inspired by **Atom Eve** (Invincible): energy manipulation, flight, regeneration, and enhanced abilities.

- Files: `mutation.json`, `effects.json`, `eocs.json`, `spells.json`, `professions.json`
- Dependencies: `dda`

### 3. Dante's Gadgets
**ID:** `dante_gadgets`

Collection of high-tech portable devices:
- **Viltrumite Nanite Swarm** — nanite swarm that reconfigures into any tool (UPS-powered)
- **Quantum Teleport Watch** — smartwatch that teleports across the overmap (UPS-powered)
- **Atomic Smartphone** — smartphone with infinite atomic battery, music player, flashlight, and power link

- Files: `items.json`, `eocs.json`
- Dependencies: `dda`

### 4. Dante's Pocket Dimension
**ID:** `pocket_dimension`

Adds a **persistent compact dimension** (24x24) — a fully walled high-tech workshop, accessed via a dimensional warp stone. All area outside the workshop is filled with solid walls, preventing external exploration. Includes warp stone, dimensional storage crystal, and return portal.

- Files: `items.json`, `eocs.json`, `furniture.json`, `region_settings.json`, `overmap_terrain.json`, `overmap_location.json`, `overmap_special.json`, `mapgen/`
- Dependencies: `dda`

### 5. Dante's Starter Gear
**ID:** `dante_starter_gear`

**Central mod of the collection.** Spawns a pre-loaded briefcase at game start containing all items from the other mods: portable gadgets, antigravity terminal, dimensional stone, and storage crystal.

- Files: `items.json`, `itemgroups.json`, `eocs.json`
- Dependencies: `dda`, `dante_gadgets`, `antigravity_market`, `pocket_dimension`

### 6. Viltrumite Heritage
**ID:** `viltrumite_dna`

Adds the **Viltrumite** genetic trait (Invincible), granting super-strength, flight, and adaptive biology that grows stronger after taking damage. Includes Viltrumite martial art and adaptive evolution system.

- Files: `all_data.json`
- Dependencies: `dda`, `dante_gadgets`

### 7. Exodii Heritage
**ID:** `exodii_heritage`

Adds the **Exodii Crash Landing** scenario — start as an Exodii dimensional scout, a full-conversion cyborg from another world who suffered a portal generator failure and crash-landed in New England. Includes scout frame with integrated armor, pre-installed bionics, and Exodii equipment.

- Files: `scenarios.json`, `professions.json`, `mutations.json`, `eocs.json`, `overlay_order.json`
- Dependencies: `dda`

---

## 🔗 Mod Dependencies

```text
dda (base game)
├── dante_gadgets
│   └── viltrumite_dna
├── antigravity_market
├── pocket_dimension
└── exodii_heritage

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
