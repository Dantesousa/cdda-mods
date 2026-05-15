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

### 4. Dante's Starter Gear
**ID:** `dante_starter_gear`

**Mod central da coleção.** Spawna uma maleta pré-carregada (com relógio de teletransporte, smartphone atômico e terminal antigravidade dentro) e uma **pedra dimensional** no abrigo de evacuação no início do jogo.

A pedra dimensional concede acesso a uma **dimensão compacta persistente** (24x24) — uma oficina high-tech totalmente equipada.

- **11 arquivos:** O mod mais complexo da coleção
- Dependências: `dda`, `atomic_smartphone`, `antigravity_market`, `overmap_teleport_watch`

### 5. Overmap Teleport Watch
**ID:** `overmap_teleport_watch`

Adiciona um smartwatch high-tech alimentado por **UPS** capaz de teletransportar o usuário através do overmap. Permite viagens rápidas entre locais explorados.

- Arquivos: `items.json`, `eocs.json`
- Dependências: `dda`

### 6. Viltrumite Heritage
**ID:** `viltrumite_dna`

Adiciona o traço genético **Viltrumita** (Invincible), concedendo super-força, voo e uma biologia adaptativa que fica mais forte após sofrer dano.

- Arquivos: `all_data.json`
- Dependências: `dda`

---

## 🔗 Dependências Entre Mods

```
dda (base game)
├── atomic_smartphone
├── antigravity_market
├── overmap_teleport_watch
└── dante_starter_gear
    ├── atomic_smartphone
    ├── antigravity_market
    └── overmap_teleport_watch
```

> **Nota:** `dante_starter_gear` depende dos outros 3 mods (atomic_smartphone, antigravity_market, overmap_teleport_watch). Para usar todos juntos, ative `dante_starter_gear` que as dependências serão carregadas automaticamente.

---

## 🚀 Como Usar

1. Copie a pasta do(s) mod(s) desejado(s) para `data/mods/` do seu CDDA
2. Ative no launcher ou no menu de mods ao criar um novo mundo
3. Para o **Starter Gear**: crie uma nova partida com o mod ativo — a maleta e a pedra dimensional estarão no abrigo de evacuação

---

## 🛠️ Autor

- **Dante** — [Dantesousa](https://github.com/Dantesousa)
