# firmware/

Bring-up and software work for Cradle: bootloader/kernel config, RKNN NPU runtime, Whisper wake-word/STT pipeline, and general Linux bring-up over the UART debug header before WiFi/SSH is available.

Not started as of 2026-07-05 — hardware bring-up (schematic, PCB) comes first. See [../docs/schematic-status.md](../docs/schematic-status.md) for hardware readiness and [LOG.md](LOG.md) for the firmware-specific running log once work begins.

Planned targets (see [../docs/architecture.md](../docs/architecture.md#software-target)):
- Mainline-adjacent Linux with real community support
- NPU inference via RKNN toolkit (6 TOPS)
- Whisper tiny/small for local speech-to-text
- Always-on wake word detection
- Cloud offload for heavy reasoning
- SSH over WiFi as the primary dev interface once the network stack is up
