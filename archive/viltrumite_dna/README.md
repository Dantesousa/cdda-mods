# Viltrumite Heritage (Viltrumite DNA)

A [Cataclysm: Dark Days Ahead](https://cataclysmdda.org/) mod that adds the **Viltrumite** race from *Invincible* (Robert Kirkman / Image Comics) as a playable mutation path with adaptive evolution.

**Tested on:** CDDA Experimental `2026-05-11-1115` (`c35ba76-dirty`)  
**Mod ID:** `viltrumite_dna`  
**Dependencies:** `dda`

---

## File Structure

```
viltrumite_dna/
  ├── modinfo.json         # Mod metadata & dependencies
  ├── all_data.json        # ALL mod data (single JSON file)
  └── README.md            # This file
```

All mod data lives in a **single `all_data.json`** to avoid flexbuffer cache conflicts that commonly occur with split JSON files in CDDA Experimental.

---

## Features

### 1. Viltrumite Heritage — Base Trait

**ID:** `TRAIT_VILTRUMITE_BASE`  
**Cost:** 10 points | **Starting trait:** Yes | **Purifiable:** No

#### Attribute Bonuses

| Attribute          | Bonus   |
|--------------------|---------|
| Strength           | **+10** |
| Dexterity          | **+5**  |
| Perception         | **+3**  |
| Speed              | **+25** |
| Stamina Regen      | **+5**  |

#### Regeneration & Healing

| Mechanic           | Multiplier |
|--------------------|-----------|
| HP Regen (sleeping)| **9.0×**  |
| HP Regen (awake)   | **3.0×**  |
| Mending Modifier   | **+2**    |

#### Native Armor (all body parts)

| Type   | Protection |
|--------|-----------|
| Bash   | **25**    |
| Cut    | **35**    |
| Bullet | **45**    |
| Stab   | **35**    |

#### Incoming Damage Reduction

| Type   | Reduction |
|--------|----------|
| Bullet | **-50%** |
| Stab   | **-30%** |
| Bash   | **-20%** |

#### Flags

`NO_DISEASE` · `UNARMED_BONUS` · `HEAT_IMMUNE` · `COLD_IMMUNE` · `BLEED_IMMUNE`

**Temperature immunity:** `CLIMATE_CONTROL_HEAT` +1000, `CLIMATE_CONTROL_CHILL` +1000 — complete environmental immunity.

---

### 2. Viltrumite Warrior — Evolved Trait

**ID:** `TRAIT_VILTRUMITE_EVOLVED_1`  
**Cost:** 0 points | **Purifiable:** No  
**Replaces:** `TRAIT_VILTRUMITE_BASE`  
**Unlock:** Adaptive Stress System at **500 stress**

#### Attribute Bonuses

| Attribute          | Bonus   |
|--------------------|---------|
| Strength           | **+15** |
| Dexterity          | **+7**  |
| Perception         | **+4**  |
| Speed              | **+35** |
| Stamina Regen      | **+10** |

#### Regeneration & Healing

| Mechanic           | Multiplier |
|--------------------|-----------|
| HP Regen (sleeping)| **19.0×** |
| HP Regen (awake)   | **8.0×**  |
| Mending Modifier   | **+5**    |

#### Native Armor (all body parts)

| Type   | Protection |
|--------|-----------|
| Bash   | **30**    |
| Cut    | **45**    |
| Bullet | **60**    |
| Stab   | **45**    |

#### Incoming Damage Reduction

| Type   | Reduction |
|--------|----------|
| Bullet | **-70%** |
| Stab   | **-45%** |
| Bash   | **-30%** |
| Cut    | **-15%** |

#### Flags

`NO_DISEASE` · `UNARMED_BONUS` · `HEAT_IMMUNE` · `COLD_IMMUNE` · `BLEED_IMMUNE`

Inherits full temperature immunity from base trait (`CLIMATE_CONTROL` +1000 both).

---

### 3. Adaptive Stress System

The Viltrumite DNA evolves through conflict. A stress counter tracks cumulative damage taken.

| Threshold | Effect |
|-----------|--------|
| **Every hit** | +5 stress added to `u_viltrumite_stress` |
| **250 stress** | Hint message: *"You feel your Viltrumite blood pulsing..."* |
| **500+ stress** | **Evolution triggered:** Replaces base trait with `TRAIT_VILTRUMITE_EVOLVED_1`, resets stress to 0 |

**Mechanics:**
- Stress is tracked per-character via `u_viltrumite_stress` variable
- Triggered via `EOC` with `eoc_type: EVENT` + `required_event: character_takes_damage`
- No manual control — pure adaptive progression
- Encourages aggressive play: the more you fight, the stronger you become

#### Viltrumite Style — Automatic Learning

Upon taking the **first hit** while holding `TRAIT_VILTRUMITE_BASE` without the martial art learned, an EOC fallback teaches `style_viltrumite` automatically:

> *"Your Viltrumite instincts guide your fists. You adopt the Viltrumite fighting style."*

This supplements the `initial_ma_styles` field on the base trait and the `autolearn` at Unarmed 6.

---

### 4. Viltrumite Flight — Active Mutation

**ID:** `MUT_VILTRUMITE_FLIGHT_ACTIVE`

Toggleable flight ability for free Z-level movement.

| Property | Value |
|----------|-------|
| Activation | Mutations menu (`p` key) — toggles on/off |
| Effect | `eff_viltrumite_flight` (permanent duration) |
| Movement Flags | `LEVITATION` + `CLIMB_FLYING` — full vertical mobility |
| Speed Bonus | **+150** while flying |
| Safety | `FEATHER_FALL` — no fall damage when toggling off mid-air |
| Messages | Contextual on/off messages via single EOC toggle |

**Toggle EOC** (`EOC_VILTRUMITE_FLIGHT_TOGGLE`):
- Checks `u_viltrumite_flight_active` variable
- **If 0:** Activates flight, applies effect, sets variable to 1
- **If 1:** Deactivates flight, removes effect, sets variable to 0

---

### 5. Viltrumite Super Punch — Active Mutation

**ID:** `MUT_VILTRUMITE_SUPER_PUNCH`

A charged, devastating attack that destroys terrain and devastates enemies.

| Property | Value |
|----------|-------|
| Activation | Mutations menu (`p` key) — uses `EOC_GENERIC_SPELL_MUTATION` |
| Prep Time | **0.5 seconds** |
| Stamina Cost | **300** |
| Damage | **80–400** bash (random, increments of 8) |
| Bash Scaling | **3.0×** — destroys walls, furniture, vehicles |
| Range | Melee (1 tile) |
| Targets | Hostile, ground |
| Spell Flags | `SOMATIC` · `NO_EXPLOSION_SFX` · `RANDOM_DAMAGE` |

**Shockwave** (`viltrumite_punch_boom`):

| Property | Value |
|----------|-------|
| Type | Secondary spell (auto-cast, no extra cost) |
| Damage | **30–120** bash (random) |
| AoE | **1–2** tile radius |
| Targets | Hostile, ground |
| Flags | `RANDOM_DAMAGE` · `IGNORE_WALLS` |
| Cost | 0 stamina, 0 casting time |

The shockwave propagates through walls, making this effective against tightly packed enemies in buildings.

---

### 6. Viltrumite Style — Martial Art

**ID:** `style_viltrumite`

A custom unarmed martial art built for raw, overwhelming force. Scales directly with Strength.

#### Learning Paths

| Method | Condition |
|--------|-----------|
| Starting trait | `initial_ma_styles: [style_viltrumite]` on `TRAIT_VILTRUMITE_BASE` |
| First hit (EOC) | Fallback: teaches style if missing on damage taken |
| Autolearn | Unarmed skill **≥ 6** |

#### Properties

| Property | Value |
|----------|-------|
| `force_unarmed` | `true` (disables weapons) |
| `arm_block` | 8 |
| `leg_block` | 6 |
| Priority | 1 |

#### Static Buffs (always active)

| Buff | Effect |
|------|--------|
| **Viltrumite Stance** | +5 flat hit bonus · +1.5 bash damage per STR · Block reduces 50% of STR damage |
| **Overwhelming Force** | **+50%** bash damage (multiplicative) |

#### On-get-hit Buff

| Buff | Effect |
|------|--------|
| **Viltrumite Fury** | **+30%** bash damage per stack (max 3 stacks) · Duration: 5 turns |

Getting hit fuels your damage output. At 3 stacks, you gain +90% bonus bash damage.

#### Techniques

| Technique | ID | Weight | Damage | Special Effects |
|-----------|----|--------|--------|-----------------|
| Viltrumite Strike | `tec_viltrumite_strike` | 2 | **1.8×** | — |
| Heavy Blow | `tec_viltrumite_heavy_blow` | 2 | **2.0×** | Knockback 2 tiles · Stun 1 turn |
| Devastating Blow | `tec_viltrumite_devastating` | 3 | **2.5×** | Critical only · Armor pierce: STR × 0.5 bash |
| Stunning Blow | `tec_viltrumite_stun` | 1 | **1.5×** | Stun 2 turns · Knockdown 1 turn |

**Weighting:** Higher values = more likely to be selected. Devastating Blow (weight 3) is the most frequent technique.

#### Example Damage Calculation (Base Trait)

```
Strength: 8 (base) + 10 (trait) = 18 STR
Base punch: ~18 damage
Viltrumite Stance: 18 × 1.5 = +27 flat damage
Overwhelming Force: ×1.50 multiplier
Expected: (18 + 27) × 1.50 ≈ 67 average damage
With Viltrumite Strike (1.8×): (18 + 27) × 1.80 ≈ 81 damage
With Devastating Blow (2.5×, crit): (18 + 27) × 2.50 ≈ 112 damage + 9 armor pierce
With max Fury (3 stacks): (18 + 27) × (1.50 + 0.90) ≈ 108 damage
```

---

### 7. Character Creation — Background (Hobby)

| Field | Value |
|-------|-------|
| **ID** | `bg_viltrumite_dna` |
| **Type** | Hobby (background) |
| **Cost** | **15 points** |
| **Tab** | Hobbies |

#### Included Traits & Mutations

| ID | Name |
|----|------|
| `TRAIT_VILTRUMITE_BASE` | Viltrumite Heritage |
| `MUT_VILTRUMITE_FLIGHT_ACTIVE` | Viltrumite Flight |
| `MUT_VILTRUMITE_SUPER_PUNCH` | Viltrumite Super Punch |

The hobby also grants the `initial_ma_styles` field on the base trait, giving you Viltrumite Style from the start.

---

## Technical Notes

### Cache Issues

CDDA caches parsed JSON in `data/cache/`. If you modify any file in this mod, you **must clear the cache**:

```bash
rm -rf data/cache/mods/viltrumite_dna/
```

Or clear the entire JSON cache:

```bash
rm -rf data/cache/
```

### Validated JSON Fields

This mod was built against a strict Experimental build. All fields below are **confirmed working**:

- `incoming_damage_mod` with `"type"` key (not `"damage_type"`)
- `REGEN_HP` / `REGEN_HP_AWAKE` with `"multiply"` (multiplicative to base regeneration)
- `CLIMATE_CONTROL_HEAT` / `CLIMATE_CONTROL_CHILL` with `"add"`
- `u_add_effect` / `u_lose_effect` for permanent effect management in EOCs
- `"condition": { "math": [...] }` for variable-checking EOCs
- `"eoc_type": "EVENT"` + `"required_event"` (replaces deprecated `"trigger"`)
- `EOC_GENERIC_SPELL_MUTATION` with custom variables (`prep_time`, `spell_to_cast`, messages)
- `"damage_increment"` with `"RANDOM_DAMAGE"` flag for variable-damage spells

---

## Balance Notes

| Aspect | Detail |
|--------|--------|
| Base trait cost | **10 points** — powerful but costly |
| Hobby cost | **15 points** — trait + both active mutations |
| Super Punch stamina | **300** — powerful but not spammable |
| Evolution threshold | **500 stress** (~100 hits taken) |
| Regeneration | Powerful but not instant — still requires combat management |
| Bullet resistance | Base -50%, Evolved -70% — strong but not invulnerable |
| Temperature immunity | Complete — works in all biomes and seasons |

---

## Changelog

### `2026-05-12` — Bullet resistance overhaul, bleed immunity, hit bonus fix

- **Base trait** bullet damage reduction increased from **-30% to -50%** and evolved from **-60% to -70%**
- **Base trait** stab reduction increased from **-20% to -30%**
- Added `BLEED_IMMUNE` flag to both traits
- Added **+5 flat hit bonus** to Viltrumite Stance (`buff_viltrumite_stance`)
- Fixed all stat table values in README to match actual JSON data
- Native armor values updated: Base (25/35/45/35), Evolved (30/45/60/45)
- Added `damage_increment: 8` clarification to Super Punch damage formula
- Documented technique weightings for clarity

### `2026-05-11` — Initial release

- Base and evolved trait trees
- Adaptive Stress System with EOC event triggers
- Viltrumite Flight toggle mutation
- Viltrumite Super Punch with shockwave
- Viltrumite Style martial art with 4 techniques
- Hobby background for character creation
- Single-file architecture to avoid flexbuffer cache issues

---

## Future Plans

- [ ] Viltrumite hero costumes (Mark Grayson / Omni-Man inspired)
- [ ] Additional evolution tiers (conquest-level Viltrumites)
- [ ] More martial art techniques
- [ ] Custom scenarios (Viltrumite scout crash-landing, etc.)

---

## Credits & Legal

- **Inspired by:** *Invincible* by Robert Kirkman, Cory Walker, and Ryan Ottley (Image Comics)
- **This is a fan mod** — not affiliated with or endorsed by the copyright holders
- **Free to use and modify** for personal and non-commercial purposes

---

*"Look at what they need to mimic a fraction of our power."*
