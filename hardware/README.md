# hardware/

This is where the Altium project lives once it's exported/checked in — schematic (10 hierarchical sheets, see [../docs/schematic-status.md](../docs/schematic-status.md)), PCB layout, library parts, and fab outputs.

Suggested layout once populated:

```
hardware/
  altium/           Altium project (.PrjPcb, .SchDoc x10, .PcbDoc)
  libraries/        Schematic symbols / PCB footprints not from a vendor library
  fab/              Gerbers, drill files, pick-and-place, BOM export per revision
  README.md
```

Until the schematic is further along, treat [../docs/architecture.md](../docs/architecture.md) and [../docs/bom.md](../docs/bom.md) as the source of truth for design intent, and this folder as empty on purpose.
