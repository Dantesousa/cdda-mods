# AGENTS.md — Dante's CDDA Mod Collection

Collection of 9 Cataclysm: Dark Days Ahead JSON data mods. No build system, no tests, no CI — pure JSON.

## Architecture

```
cdda-mods/
├── antigravity_market/     # Shopping terminal (items, EOCs)
├── atom_eve_powers/        # Superpowers via mutations/spells/EOCs
├── atomic_smartphone/      # Infinite-battery phone (items)
├── dante_starter_gear/     # Central mod: spawns briefcase on game_start
├── exodii_heritage/        # Scenario: Exodii cyborg scout start
├── nanite_tool/            # Omni-tool nanite swarm (items)
├── overmap_teleport_watch/ # UPS-powered teleport watch (items, EOCs)
├── pocket_dimension/       # Persistent instanced 24×24 workshop
└── viltrumite_dna/         # Viltrumite trait tree + martial art (single all_data.json)
```

## Dependency Graph

```
dda (base game)
├── atomic_smartphone
├── antigravity_market
├── overmap_teleport_watch
├── pocket_dimension
├── nanite_tool
│   └── viltrumite_dna        ← depends on nanite_tool
├── exodii_heritage           ← depends only on dda
└── dante_starter_gear
    ├── atomic_smartphone
    ├── antigravity_market
    ├── overmap_teleport_watch
    ├── pocket_dimension
    └── nanite_tool
```

> `dante_starter_gear` does **not** depend on `viltrumite_dna` or `exodii_heritage` (verified in `modinfo.json`).

## CDDA JSON Conventions (easy to get wrong)

- `examine_action.type`: singular `"effect_on_condition"`
- `use_action.type`: plural `"effect_on_conditions"`
- `u_spawn_item` supports `count`, `container`, `use_item_group`, `variant` — NOT `charges` or `sealed`
- `"method": "json"` is obsolete — never use it
- `search_range` is incompatible with `om_terrain_match_type: "EXACT"`
- `city_size` is invalid in `overmap_special`
- `npc_travel_radius` + `npc_travel_filter` are required on dimension travels
- Double spaces after periods in `description` strings (repo convention)

## Mod Structure

Every mod needs `modinfo.json` (type `MOD_INFO`) with `id`, `name`, `dependencies`. Other files named by CDDA type:

- `items.json` — TOOL, ARMOR, BOOK, GENERIC, etc.
- `eocs.json` — effect_on_condition (EOC) entries
- `itemgroups.json` — item_group entries
- `mutations.json` / `spells.json` / `professions.json` / `effects.json` / `scenarios.json` / `overlay_order.json` — as needed

Mapgen files go in `mapgen/` subdirectory.

## Item Group Patterns

- `subtype: "collection"` spawns ALL entries; `distribution` picks one
- `"use_item_group": true` on `u_spawn_item` means the item ID is treated as an item_group reference, not a direct item
- `contents-item` spawns items pre-loaded inside a container

## Pocket Dimension Architecture

A dimension mod requires these file types:

| File | Purpose |
|------|---------|
| `region_settings.json` | Dimension config: default_oter, feature_flag whitelist, no cities/roads |
| `overmap_terrain.json` | `NO_ROTATE` + `SIDEWALK` prevents item spawns; `mondensity: 0` prevents monsters |
| `overmap_location.json` | Links overmap_special to terrain |
| `overmap_special.json` | Flags: `EXTRADIMENSIONAL`, `GLOBALLY_UNIQUE`, `SAFE_AT_WORLDGEN` |
| `mapgen/` | `fill_ter` defines default terrain; 24-character rows |
| `furniture.json` | Portal furniture with `examine_action` → EOC |
| `eocs.json` | Toggle EOC: save origin → teleport → travel to dimension → mapgen → place portal |
| `items.json` | Warp stone item with `use_action` → toggle EOC |

## `viltrumite_dna` Special Case

Single `all_data.json` file (not split by type) — intentional design to avoid CDDA flexbuffer cache conflicts on Experimental builds.

## Cache

CDDA caches parsed JSON in `data/cache/`. After any mod file change, clear the cache:
```bash
rm -rf data/cache/
```

## Git

- Remote: `git@github.com:Dantesousa/cdda-mods.git`
- Push uses deploy key `~/.ssh/github_key` (SSH config: `github.com` → `IdentityFile ~/.ssh/github_key`)
