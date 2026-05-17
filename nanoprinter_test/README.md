# Nanoprinter Test Mod

Mod de teste para mecânica de Nanoprinter + Console interface no CDDA.

## Funcionalidades

### Nanoprinter
- **Item deployable** que vira um appliance quando usado no chão
- Conecta automaticamente à **power grid** quando adjacente a outros appliances
- Consome energia para operar
- Sintetiza itens básicos a partir de matéria-prima

### Console Interface
- **f_nanoprinter_console** - Interface de controle com menu EOC
- Verifica se o Nanoprinter está conectado à energia
- Menu com 4 opções de crafting:
  1. **Bandages** (1 plastic chunk → 2 bandages)
  2. **Water Bottle** (1 plastic chunk → 1 water_clean + bottle)
  3. **Ration Pack** (2 organic chunks → 1 ration)
  4. **Extension Cable** (2 metal chunks → 1 extension_cable)

### Matéria-Prima
- `plastic_chunk` - Para itens sintéticos
- `metal_chunk` - Para componentes eletrônicos/cabos
- `organic_chunk` - Para comida/organicos

## Como Usar

### No Pocket Dimension
1. Entre na sua dimensão de bolso com o `dante_warp_stone`
2. O Nanoprinter e Console já estarão colocados no mapa (posição NN e C)
3. Conecte um gerador ou bateria à power grid:
   - Use `portable_generator` + gasolina
   - Ou `battery_car` + `jumper_cable`
4. Examine o Console (`f_nanoprinter_console`)
5. Selecione o item que quer fabricar
6. Se tiver matéria-prima suficiente, o item é criado!

### Em Outro Lugar
1. Deploy o `nanoprinter` no chão
2. Coloque o `f_nanoprinter_console` adjacente
3. Conecte à energia
4. Use o console

## Arquivos do Mod

```
nanoprinter_test/
├── modinfo.json      # Metadata e dependências
├── items.json        # Nanoprinter item + chunks de matéria-prima
├── furniture.json    # f_nanoprinter (appliance) + f_nanoprinter_console (UI)
└── eocs.json         # Lógica de interface e crafting
```

## Dependências
- `dda` (base game)

## Integração com Outros Mods

### Pocket Dimension
- O mapa 24x24 agora inclui Nanoprinter + Console
- Posição: canto superior direito (substitui o `f_console` vanilla)

### Dante's Starter Gear
- Briefcase agora spawn com:
  - 1x `nanoprinter`
  - 5x `plastic_chunk`
  - 5x `metal_chunk`
  - 5x `organic_chunk`

## JSON Fields Usados

### Appliance
```json
{
  "type": "furniture",
  "examine_action": { "type": "appliance_convert" },
  "flags": [ "APPLIANCE", "ENABLED_DRAINS_EPOWER" ],
  "crafting_pseudo_item": "nanoprinter"
}
```

### Console UI
```json
{
  "type": "furniture",
  "examine_action": { "type": "effect_on_condition" },
  "condition": { "u_has_powered_appliance": "f_nanoprinter" }
}
```

### Crafting Menu
```json
{
  "run_eoc_selector": [ "EOC_1", "EOC_2", ... ],
  "names": [ "Opção 1", "Opção 2", ... ],
  "keys": [ "1", "2", ... ],
  "descriptions": [ "Desc 1", "Desc 2", ... ]
}
```

## Próximos Passos (Ideias)

- [ ] Adicionar mais receitas (ferramentas, componentes)
- [ ] Sistema de upgrade para receitas avançadas
- [ ] Consumir energia da grid (atualmente só verifica se tem power)
- [ ] Som/feedback visual diferente por tipo de item
- [ ] Interface com sub-menus para categorias de itens
- [ ] Recipe de matéria-prima (converter lixo em chunks)

## Notas Técnicas

- Usa `u_has_powered_appliance` para verificar conexão à energia
- `u_consume_item` remove os chunks do inventário
- `u_spawn_item` cria os itens fabricados
- `u_make_sound` adiciona feedback sonoro ("soft whirring")
- Mensagens com `type: "good"` ou `"bad"` para cores diferentes

## Testando

1. Inicie o jogo com os mods ativados
2. Pegue a briefcase inicial
3. Vá para o pocket dimension
4. Conecte energia ao Nanoprinter
5. Teste cada receita do console
