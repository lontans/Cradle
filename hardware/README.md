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

**Not the same thing as [`../docs/Altium/`](../docs/Altium/):** that folder holds periodic, lightweight text/CSV exports (Protel netlist, BOM) pulled from Altium and re-exported often, purely as input to the analysis tooling in [`../tools/`](../tools/) (see [../docs/workflow-cheatsheet.md](../docs/workflow-cheatsheet.md)). This folder is meant for the actual Altium project (binary/proprietary files, checked in once schematic work is further along, updated far less often). The two exist in parallel on purpose — `docs/Altium/` is real and actively used well before this folder will be.
