# Dante's CDDA Mod Collection

Coleção de mods pessoais para **Cataclysm: Dark Days Ahead**, criados por Dante.

Todos os mods funcionam com a versão estável mais recente do CDDA.

---

## 📦 Mods

### 1. Antigravity Market
**ID:** `antigravity_market`

Adiciona um terminal de compras portátil que permite comprar itens (comida, armas, munição) usando **FMCNotes** (Free Merchant Certified Notes). Os itens são entregues instantaneamente.

- Arquivos: `items.json`, `eocs.json`
- Dependências: `dda`

### 2. Atom Eve Powers
**ID:** `atom_eve_powers`

Adiciona superpoderes inspirados na **Atom Eve** (Invincible): manipulação de energia, voo, regeneração e habilidades aprimoradas.

- Arquivos: `mutation.json`, `effects.json`, `eocs.json`, `spells.json`, `professions.json`
- Dependências: `dda`

### 3. Atomic Smartphone
**ID:** `atomic_smartphone`

Adiciona um smartphone com bateria **atômica (infinita)**, similar ao antigo celular atômico do jogo. Nunca mais se preocupe com bateria.

- Arquivos: `items.json`
- Dependências: `dda`

### 4. Dante's Pocket Dimension
**ID:** `pocket_dimension`

Adiciona uma **dimensão compacta persistente** (24x24) — uma oficina high-tech totalmente equipada, acessada via uma pedra dimensional. Inclui warp stone, cristal de armazenamento dimensional e portal de retorno.

- Arquivos: `items.json`, `eocs.json`, `furniture.json`, `region_settings.json`, `overmap_terrain.json`, `overmap_location.json`, `overmap_special.json`, `mapgen/`
- Dependências: `dda`

### 5. Dante's Starter Gear
**ID:** `dante_starter_gear`

**Mod central da coleção.** Spawna uma maleta pré-carregada no início do jogo contendo todos os itens dos outros mods: relógio de teletransporte, smartphone atômico, terminal antigravidade e nanite swarm — além da pedra dimensional e do cristal de armazenamento da pocket dimension.

- Arquivos: `items.json`, `itemgroups.json`, `eocs.json`
- Dependências: `dda`, `atomic_smartphone`, `antigravity_market`, `overmap_teleport_watch`, `pocket_dimension`, `nanite_tool`

### 6. Nanite Tool
**ID:** `nanite_tool`

Adiciona um enxame de nanites programáveis que se reconfiguram em qualquer ferramenta necessária — de um martelo simples a uma bigorna de precisão. Requer bateria (UPS) para operar.

- Arquivos: `items.json`
- Dependências: `dda`

### 7. Overmap Teleport Watch
**ID:** `overmap_teleport_watch`

Adiciona um smartwatch high-tech alimentado por **UPS** capaz de teletransportar o usuário através do overmap. Permite viagens rápidas entre locais explorados.

- Arquivos: `items.json`, `eocs.json`
- Dependências: `dda`

### 8. Viltrumite Heritage
**ID:** `viltrumite_dna`

Adiciona o traço genético **Viltrumita** (Invincible), concedendo super-força, voo e uma biologia adaptativa que fica mais forte após sofrer dano. Inclui arte marcial Viltrumita e sistema de evolução adaptativa.

- Arquivos: `all_data.json`
- Dependências: `dda`, `nanite_tool`

---

## 🔗 Dependências Entre Mods

```
dda (base game)
├── atomic_smartphone
├── antigravity_market
├── overmap_teleport_watch
├── pocket_dimension
├── nanite_tool
│   └── viltrumite_dna
└── dante_starter_gear
    ├── atomic_smartphone
    ├── antigravity_market
    ├── overmap_teleport_watch
    ├── pocket_dimension
    └── nanite_tool
```

> **Nota:** Ative `dante_starter_gear` para começar com todos os itens da coleção — as dependências serão carregadas automaticamente.

---

## 🚀 Como Usar

1. Copie a pasta do(s) mod(s) desejado(s) para `data/mods/` do seu CDDA
2. Ative no launcher ou no menu de mods ao criar um novo mundo
3. Para o **Starter Gear**: crie uma nova partida com o mod ativo — a maleta e os itens estarão no abrigo de evacuação

---

## 🛠️ Autor

- **Dante** — [Dantesousa](https://github.com/Dantesousa)
