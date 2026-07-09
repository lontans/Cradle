# Standard parts (staged stock, not yet functionally placed)

Designators the user holds/copy-pastes around the Altium canvas as generic stock — not yet assigned a specific circuit role. Maintained by hand; the BOM/netlist can't distinguish these from functionally-specific parts on their own (see `cradle_sidecar/co-design-workflow.md`, Layer 0.5 — several of these share exact part numbers with designators that *are* functionally placed, e.g. `C11` and `C84`/`C85` are the identical 10pF/0402/C0G part).

**Discipline this depends on:** no more than one instance of a given "standard part" designator left floating/unplaced in Altium at a time. If that discipline slips, this list goes stale and any gap analysis built on it (see below) will misreport.

| Designator | Part | Value/Description |
|---|---|---|
| C8 | CL05A105KP5NNNC | 1uF X5R 0402 |
| C9 | JLC_C2012X5R1A476MTJ00E | 47uF X5R 0805 |
| C10 | GRM155R61E104KA87D | 0.1uF X5R 0402 |
| C11 | JLC_10pF_0402CG100J500NT | 10pF C0G 0402 |
| C12 | JLC_CL10A106KP8NNNC | 10uF X5R 0603 |
| C13 | JLC_1210B225K500NT | 2.2uF X7R 1210 |
| C80 | JLC_30pF_0402CG300J500NT | 30pF C0G 0402 |
| C83 | JLC_22uF_0603_C1608X5R1A226MT000E | 22uF X5R 0603 |
| L2 | JLC_WPN252012ER47MT | 0.47uH, 1008 |
| R25 | JLC_30K_CR0402FF3002G | 30kOhm 0402 |
| R26 | TNPW040210K0DEED | 10kOhm 0402 |
| R27 | JLC_0_OHM_0402_RC0402JR-070RL | 0Ohm 0402 |
| R28 | JLC_100_OHM_CR0402JF0101G | 100Ohm 0402 |
| LED3 | JLC_XL-0603QYGC | Green LED 0603 |
| L9 | SLS3D16S2R2NTT | 2.2uH, 1A, 60mOhm DCR, 4x4mm shielded |
| C88 | CL10A475KP8NNNC | 4.7uF X5R 0603 |

**How this should get used:** when cross-referencing a component card's pin table against the real netlist (e.g. "which AP6275S pins still need wiring"), any net whose only members are designators on this list should be treated as *not yet functionally connected* — it's staged stock sitting on a net, not a real circuit connection, even though it technically isn't "missing" from the netlist's point of view.
